
(define-macro (make-lambda expr)
  `(lambda () ,expr))

(define-macro (or-macro expr1 expr2)
  `(let ((v1 ,expr1))
     (if v1 v1 ,expr2)))

(define (range-stream start end)
  (if (>= start end)
    nil
    (cons-stream start (range-stream (+ start 1) end))))

(define (naturals n)
  (cons-stream n (naturals (+ n 1))))

(define (slice s start end)
  (define (helper s i)
    (cond ((or (null? s) (>= i end)) nil)
	((< i start) (helper (cdr-stream s) (+ i 1)))
	(else (cons (car s) (helper (cdr-stream s) (+ i 1))))))
  (helper s 0))

(define (combine-with f xs ys)
  (if (or (null? xs) (null? ys))
    nil
    (cons-stream
      (f (car xs) (car ys))
      (combine-with f (cdr-stream xs) (cdr-stream ys)))))

(define factorials
   (cons-stream 1 (combine-with * (naturals 1) factorials)))

(define fibs
  (cons-stream 0 (cons-stream 1 (combine-with + fibs (cdr-stream fibs)))))

(define (exp x)
   (define (power x n) (cons-stream (expt x n) (power x (+ n 1))))
   (define ex (combine-with / (power x 0)  factorials))
   (cons-stream 1 (combine-with + (cdr-stream ex) (exp x))))

(define (replicate x n)
  (if (= n 0) nil
    (cons x (replicate x (- n 1)))))

(define-macro (repeat-n expr n)
  (cons 'begin (replicate expr n)))

(define-macro (prune-expr expr)
  (define (no-other s) (if (<= (length s) 1) s (cons (car s) (no-other (cdr (cdr s))))))
  (cons (car expr) (no-other (cdr expr)))
)

(define-macro (make-stream first second)
  `(cons ,first (make-lambda ,second)))

(define (cdr-stream-lambda stream)
  ((cdr stream)))
