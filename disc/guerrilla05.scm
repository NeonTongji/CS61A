(define (cddr s)
    (cdr (cdr s)))

(define (cadr s)
    (car (cdr s)))

(define (caddr s)
    (car (cddr s)))

(define (sum-every-other lst)
  (cond ((null? lst) 0)
        ((null? (cdr lst)) (car lst)) 
	(else (+ (car lst)
	      (sum-every-other (cddr lst)))))
)

(define (append s1 s2)
  (cond ((null? s1) s2)
  	((null? s2) s1)
	(else (cons (car s1) (append (cdr s1) s2))))
)

(define (reverse s)
  (if (null? s)
    s
    (append (reverse (cdr s)) (list (car s))))
)


(define (reverse-without-append s)
  (define (add-last s v)
    (cond ((null? s) (list v))
	  (else (cons (car s) (add-last (cdr s) v)))))
  (if (null? s)
    s
    (add-last (reverse-without-append (cdr s)) (car s)))
)

(define (map fn lst)
  (if (null? lst)
    nil
    (cons (fn (car lst)) (map fn (cdr lst))))
)

(define (add-to-all v lst)
  (map (lambda (i) (cons v i)) lst))

(define (sublists lst)
  (if (null? lst)
    (list lst)
    (append (sublists (cdr lst))
	    (add-to-all (car lst) (sublists (cdr lst))) ))
)

(define (sixty-ones s)
  (cond ((< (length s) 2) 0)
	((and (= (car s) 6) 
	      (= (cadr s) 1)) 
	         (+ 1 
		    (sixty-ones (cddr s))))
	(else (sixty-ones (cdr s))))
)

(define (no-elevens n)
  (define (six-at-first s)
    (if (= (car s) 6)
      #t
      #f))
  (cond ((<= n 0) nil)
	((= n 1) '((6) (1)))
	(else (append (add-to-all 6 (no-elevens (- n 1)))
		      (add-to-all 1 (filter six-at-first (no-elevens (- n 1)))))))
)


