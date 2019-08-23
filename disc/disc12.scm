
(define (merge s1 s2)
  (if (< (car s1) (car s2))
    (cons-stream (car s1) (merge (cdr-stream s1) s2))
    (cons-stream (car s2) (merge s1 (cdr-stream s2)))))

(define (cycle start)
  (cons-stream start (cycle (modulo (+ start 2) 5))))

(define-macro (let-macro bindings body)
  (define formals (map (lambda (b) (car b)) bindings))
  (define vals (map (lambda (b) (cadr b)) bindings))
  (cons `(lambda ,formals ,body) vals))

(define (cadr lst) (car (cdr lst)))

(define-macro (zero-cond clauses)
  (cons 'cond (map (lambda (c) `((not (= 0 ,(car c))) ,(cadr c))) clauses)))
