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
      request.getMethodCall("headers").getAKeywordArgument("X-CSRF-Token")
    )
  }

  override string getMessage() {
    result = "Route handles state-changing requests but does not validate CSRF tokens."
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
        validation.(Call).getFunc().(Name).getId().matches("%validat%")
      )
    )
  }

  override string getMessage() {
    result = "File upload detected without proper validation. Implement file type, size, and content validation."
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
      call.getFunc().(Name).getId() in ["system", "popen", "call", "run"] and
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
      call.getFunc().(Name).getId().matches("%sql%") and
      sink.asExpr() = call.getAnArg()
    )
  }

  override string getMessage() {
    result = "Potential SQL injection vulnerability in Flask route."
  }
}

// Select statements to report the findings
from FlaskDebugMode f
select f, f.getMessage()

from MissingCsrfProtection m
select m, m.getMessage()

from InsecureSecretKey i
select i, i.getMessage()

from UnsafeFileUpload u
select u, u.getMessage()

from FlaskCommandInjection::Configuration c
select c, c.getMessage()

from FlaskSqlInjection::Configuration s
select s, s.getMessage()