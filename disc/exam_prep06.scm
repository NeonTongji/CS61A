(define (directions n sym)
  (define (search s exp)
    ; Search an expression s for n and return an expression based on exp.
    (cond ((number? s) (if (= n s) exp nil))
	  ((null? s) nil)
	  (else (search-list s exp))))
  (define (search-list s exp)
    ; Search a nested list s for n and return an expression based on exp.
    (let ((first (search (car s) (list 'car exp)))
	  (rest (search (cdr s) (list 'cdr exp))))
	 (if (null? first) rest first)))
  (search (eval sym) sym))

(define (parens s)
  (f s 2))
(define (f s t)
  (cond ((pair? s)(+ t
		     (f (car s) 2)
		     (f (cdr s) 0)))
	((null? s) t)
	(else 0)))

(quote (1 . ((2 . ()) . (3 . ()))). ())
