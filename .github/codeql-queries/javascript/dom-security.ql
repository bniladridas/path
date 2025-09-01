/**
 * @name DOM-based XSS Vulnerabilities
 * @description Detects potential DOM-based cross-site scripting vulnerabilities
 * @kind problem
 * @problem.severity error
 * @precision high
 * @tags security
 *       dom-xss
 *       javascript
 */

import javascript

/**
 * Detects unsafe use of innerHTML with user input
 */
class UnsafeInnerHTML extends DOM::ElementDefinition {
  UnsafeInnerHTML() {
    exists(DOM::PropertyWrite write |
      write.getPropertyName() = "innerHTML" and
      write.getRhs().(Expr).mayHaveStringValue(_) and
      // Check if the value comes from user input
      exists(DataFlow::Node source |
        source = DOM::locationSource() or
        source = DOM::userInput() or
        source.(Expr).getStringValue().matches("%" + DOM::userInput().toString() + "%")
      )
    )
  }

  override string getMessage() {
    result = "Unsafe use of innerHTML with potential user input. Use textContent or sanitize the input."
  }
}

/**
 * Detects unsafe use of document.write
 */
class UnsafeDocumentWrite extends CallExpr {
  UnsafeDocumentWrite() {
    this.getCallee().(GlobalVarRef).getName() = "document" and
    this.getCallee().(PropAccess).getPropertyName() = "write" and
    // Check if arguments contain user input
    exists(Expr arg |
      arg = this.getAnArgument() and
      arg.mayHaveStringValue(_)
    )
  }

  override string getMessage() {
    result = "Unsafe use of document.write. This can lead to XSS vulnerabilities."
  }
}

/**
 * Detects unsafe use of eval with user input
 */
class UnsafeEval extends CallExpr {
  UnsafeEval() {
    this.getCallee().(GlobalVarRef).getName() = "eval" and
    exists(Expr arg |
      arg = this.getAnArgument() and
      arg.mayHaveStringValue(_)
    )
  }

  override string getMessage() {
    result = "Unsafe use of eval with potential user input. This can lead to code injection."
  }
}

/**
 * Detects missing Content Security Policy
 */
class MissingCSP extends HTML::Document {
  MissingCSP() {
    not exists(HTML::MetaTag meta |
      meta.getAttributeValue("http-equiv") = "Content-Security-Policy" or
      meta.getAttributeValue("name") = "csp"
    )
  }

  override string getMessage() {
    result = "Missing Content Security Policy (CSP) header. Implement CSP to prevent XSS attacks."
  }
}

/**
 * Detects unsafe use of localStorage/sessionStorage
 */
class UnsafeStorage extends CallExpr {
  UnsafeStorage() {
    exists(string method |
      method in ["setItem", "getItem"] and
      this.getCallee().(PropAccess).getPropertyName() = method and
      this.getCallee().getBase().(GlobalVarRef).getName() in ["localStorage", "sessionStorage"]
    )
  }

  override string getMessage() {
    result = "Direct use of localStorage/sessionStorage detected. Consider encrypting sensitive data."
  }
}

/**
 * Detects potential prototype pollution
 */
class PrototypePollution extends Assignment {
  PrototypePollution() {
    exists(Expr lhs |
      lhs = this.getLhs() and
      lhs.(PropAccess).getPropertyName() = "__proto__" or
      lhs.(PropAccess).getPropertyName() = "constructor" or
      lhs.(PropAccess).getPropertyName() = "prototype"
    )
  }

  override string getMessage() {
    result = "Potential prototype pollution vulnerability detected."
  }
}