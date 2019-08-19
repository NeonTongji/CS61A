(define (reverse lst)
  (define (f l r)
    (if (null? l)
      r
      (f (cdr l) (cons (car l) r))))
  (f lst nil)
)

(define (power b n)
  (define (f p k)
    (if (= n k)
      p
      (f (* p b) (+ k 1))))
  (f 1 0)
)

;Write a tail-recursive function that finds the length of the hailstone sequence that
;starts with n.
(define (hailstone n)
  (define (f k i)
    (if (= k 1)
      i
      (if (even? k)
        (f (/ k 2) (+ i 1))
        (f (+ (* k 3) 1) (+ i 1)))))
  (f n 1)
)

