const { app, BrowserWindow } = require('electron');
const expressApp = require('./app');
const path = require('path');

let mainWindow;
let server;

function createWindow() {
  // Create the browser window
  mainWindow = new BrowserWindow({
    width: 1200,
    height: 800,
    webPreferences: {
      nodeIntegration: false,
      contextIsolation: true,
    },
    icon: path.join(__dirname, 'static/images/favicon.svg'), // Adjust path if needed
    titleBarStyle: 'hiddenInset', // macOS style
    backgroundColor: '#000000',
  });

  // Start the Express server
  startServer();

  // Load the app after a short delay to ensure server is ready
  setTimeout(() => {
    mainWindow.loadURL('http://localhost:8000');
  }, 1000);

  // Emitted when the window is closed
  mainWindow.on('closed', () => {
    mainWindow = null;
    // Close the server
    if (server) {
      server.close();
    }
  });
}

function startServer() {
  server = expressApp.listen(8000, () => {
    console.log('Server running on port 8000');
  });
}

// This method will be called when Electron has finished initialization
app.whenReady().then(createWindow);

// Quit when all windows are closed
app.on('window-all-closed', () => {
  // On macOS it is common for applications to stay active until explicitly quit
  if (process.platform !== 'darwin') {
    app.quit();
  }
});

app.on('activate', () => {
  // On macOS it's common to re-create a window when dock icon is clicked
  if (BrowserWindow.getAllWindows().length === 0) {
    createWindow();
  }
});

// Security: Prevent new window creation
app.on('web-contents-created', (event, contents) => {
  contents.setWindowOpenHandler(() => {
    return { action: 'deny' };
  });
});
