/**
 * @name Flask Security Issues
 * @description Detects common Flask security vulnerabilities
 * @kind problem
 * @problem.severity error
 * @precision high
 * @tags security
 *       flask
 *       python
 */

import python
import semmle.python.web.flask.Flask
import semmle.python.security.dataflow.CommandInjection
import semmle.python.security.dataflow.SqlInjection
import semmle.python.security.dataflow.UrlRedirect
import semmle.python.security.dataflow.Xss

/**
 * Detects Flask applications with debug mode enabled in production
 */
class FlaskDebugMode extends Flask::FlaskApp {
  FlaskDebugMode() {
    exists(Flask::FlaskApp app |
      app.getARunCall().getKeywordArgument("debug").getValue().(NameConstant).getId() = "True" and
      // Check if this is likely production code (not in test files)
      not app.getLocation().getFile().getBaseName().matches("%test%")
    )
  }

  override string getMessage() {
    result = "Flask application is running in debug mode. This should be disabled in production."
  }
}

/**
 * Detects missing CSRF protection on forms
 */
class MissingCsrfProtection extends Flask::FlaskRoute {
  MissingCsrfProtection() {
    // Check if route handles POST/PUT/PATCH requests
    this.getHttpMethod().toLowerCase() in ["post", "put", "patch"] and
    // Check if CSRF token is not validated
    not exists(Flask::FlaskRequest request |
      request.getMethodCall("form").getAKeywordArgument("csrf_token") or
      request.getMethodCall("headers").getAKeywordArgument("X-CSRF-Token") or
      // Check for Flask-WTF CSRF protection
      exists(Call call |
        call.getFunc().(Attribute).getName() = "validate_on_submit" and
        call.getFunc().getBase().(Name).getId().matches("form") or
        call.getFunc().(Name).getId() = "csrf.exempt"
      )
    )
  }

  override string getMessage() {
    result = "Route handles state-changing requests but does not validate CSRF tokens. Consider using Flask-WTF for automatic CSRF protection."
  }
}

/**
 * Detects insecure secret key usage
 */
class InsecureSecretKey extends Flask::FlaskApp {
  InsecureSecretKey() {
    exists(Flask::FlaskApp app |
      app.getASecretKeyAssignment().getValue().(StrConstant).getText().length() < 32 or
      app.getASecretKeyAssignment().getValue().(StrConstant).getText() = "your-secret-key-here"
    )
  }

  override string getMessage() {
    result = "Flask secret key is too short or uses default value. Use a secure random key of at least 32 characters."
  }
}

/**
 * Detects unsafe file uploads without validation
 */
class UnsafeFileUpload extends Flask::FlaskRoute {
  UnsafeFileUpload() {
    exists(Flask::FlaskRequest request |
      request.getMethodCall("files") and
      not exists(Expr validation |
        validation.getLocation().getFile() = this.getLocation().getFile() and
        (validation.(Call).getFunc().(Name).getId().matches("%validat%") or
         validation.(Call).getFunc().(Name).getId().matches("%check%") or
         validation.(Call).getFunc().(Name).getId().matches("%sanitize%") or
         // Check for file extension validation
         exists(Expr ext |
           ext.(Call).getFunc().(Attribute).getName() = "endswith" and
           ext.getAnArgument().(StrConstant).getText().matches("%.jpg") or
           ext.getAnArgument().(StrConstant).getText().matches("%.png")
         ) or
         // Check for mimetype validation
         exists(Expr mime |
           mime.(Call).getFunc().(Attribute).getName() = "startswith" and
           mime.getAnArgument().(StrConstant).getText().matches("image/")
         ))
      )
    )
  }

  override string getMessage() {
    result = "File upload detected without proper validation. Implement file type, size, and content validation to prevent malicious uploads."
  }
}

/**
 * Detects potential command injection in Flask routes
 */
class FlaskCommandInjection extends CommandInjection::Configuration {
  FlaskCommandInjection() { this = "FlaskCommandInjection" }

  override predicate isSource(DataFlow::Node source) {
    exists(Flask::FlaskRequest request |
      source.asExpr() = request.getARequestExpr()
    )
  }

  override predicate isSink(DataFlow::Node sink) {
    exists(Call call |
      call.getFunc().(Name).getId() in ["system", "popen", "call", "run", "subprocess.call", "subprocess.run", "os.system", "os.popen"] or
      call.getFunc().(Attribute).getName() in ["call", "run", "system", "popen"] and
      sink.asExpr() = call.getAnArg()
    )
  }

  override string getMessage() {
    result = "Potential command injection vulnerability in Flask route."
  }
}

/**
 * Detects SQL injection vulnerabilities in Flask applications
 */
class FlaskSqlInjection extends SqlInjection::Configuration {
  FlaskSqlInjection() { this = "FlaskSqlInjection" }

  override predicate isSource(DataFlow::Node source) {
    exists(Flask::FlaskRequest request |
      source.asExpr() = request.getARequestExpr()
    )
  }

  override predicate isSink(DataFlow::Node sink) {
    exists(Call call |
      call.getFunc().(Name).getId() in ["execute", "executemany", "executescript", "cursor.execute", "connection.execute"] or
      call.getFunc().(Attribute).getName() in ["execute", "executemany", "executescript"] and
      sink.asExpr() = call.getAnArg()
    )
  }

  override string getMessage() {
    result = "Potential SQL injection vulnerability in Flask route."
  }
}

// Combined select statement to report all findings
from Locatable l, string message
where
  exists(FlaskDebugMode f | l = f and message = f.getMessage()) or
  exists(MissingCsrfProtection m | l = m and message = m.getMessage()) or
  exists(InsecureSecretKey i | l = i and message = i.getMessage()) or
  exists(UnsafeFileUpload u | l = u and message = u.getMessage()) or
  exists(FlaskCommandInjection c | l = c and message = c.getMessage()) or
  exists(FlaskSqlInjection s | l = s and message = s.getMessage())
select l, message