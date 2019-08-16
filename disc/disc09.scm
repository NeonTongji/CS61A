;Tail Recursion

(define (fib n)
  (define (fib-sofar fib-num fib-prev k)
    (if (= n k)
      fib-num
      (fib-sofar (+ fib-num fib-prev) fib-num (+ k 1))))
  (fib-sofar 0 1 0))

(define (sum lst)
  (define (sum-sofar sum_prev lst)
    (if (null? lst) sum_prev
      (sum-sofar (+ sum_prev (car lst)) (cdr lst))))
  (sum-sofar 0 lst))

(define (reverse lst)
  (define (reverse-sofar lst lst-sofar)
    (if (null? lst) lst-sofar
      (reverse-sofar (cdr lst) (cons (car lst) lst-sofar))))
  (reverse-sofar lst nil))

(define (append a b)
  (define (rev-append-tail a b)
    (if (null? a) b
      (rev-append-tail (cdr a) (cons (car a) b))))
  (rev-append-tail (reverse a) b))

(define (insert n lst)
  (define (rev-insert lst rev-lst)
    (cond ((null? lst) (reverse (cons n rev-lst)))
	  ((> (car lst) n) (append (reverse rev-lst) (cons n lst)))
	  (else (rev-insert (cdr lst) (cons (car lst) rev-lst)))))
  (rev-insert lst nil))
