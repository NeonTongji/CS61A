; Lab 13: Final Review - Optional Questions

; Q6
(define (nodots s)
  (cond 
    ((null? s) nil)
    ((not (pair? s)) (list s))
    ((pair? (car s))
	 (cons (nodots (car s)) (nodots (cdr s))))
    (else (cons (car s) (nodots (cdr s)))))
)

; Q7
(define (has-cycle? s)
  (define (pair-tracker seen-so-far curr)
    (cond ((null? curr) #f)
          ((contains? seen-so-far curr) #t)
          (else (pair-tracker (cons curr seen-so-far) (cdr-stream curr))))
    )
  (pair-tracker nil s)
)

(define (contains? lst s)
  (cond ((or (null? lst) (null? s)) #f)
	((eq? (car lst) s) #t)
	(else (contains? (cdr lst) s))))


; Q8
(define-macro (switch expr cases)
  (cons 'cond (map (lambda (c) `(,(append `(eq? ,expr) `(',(car c))) ,(car (cdr c)))) cases))
)
