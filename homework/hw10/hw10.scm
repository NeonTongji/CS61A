
(define (accumulate combiner start n term)
  (if (< n 1) start
    (combiner (term n) (accumulate combiner start (- n 1) term)))
)

(define (accumulate-tail combiner start n term)
  (if (< n 1) start
      (accumulate-tail combiner (combiner start (term n)) (- n 1) term))
)

(define (partial-sums stream)
  (define (helper start stream)
    (if (null? stream) nil
	(cons-stream (+ (car stream) start) (helper (+ (car stream) start) (cdr-stream stream)))))
  (helper 0 stream)
)

(define (rle s)
  (define (helper num run stream)
    (cond ((null? stream) (cons-stream (list num run) nil))
	  ((= (car stream) num) (helper num (+ 1 run) (cdr-stream stream)))
	  (else (cons-stream (list num run) (helper (car stream) 0 stream)))))
  (if (null? s) nil (helper (car s) 0 s))
)
