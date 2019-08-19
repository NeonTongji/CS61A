(define (cddr s)
      (cdr (cdr s)))

(define (cadr s)
      (car (cdr s)))

(define (caddr s)
      (car (cddr s)))

(define (contains value lst)
  (cond ((null? lst) #f)
	((= (car lst) value) #t)
        (else (contains value (cdr lst)))))

(define-macro (case value clauses)
  `(cond 
     ((contains ,value ,(car (car clauses))) ,(cadr (car clauses)))
     ((contains ,value ,(car (cadr clauses)))  ,(cadr (cadr clauses)))
     (else ,(cadr (caddr clauses))))
)
