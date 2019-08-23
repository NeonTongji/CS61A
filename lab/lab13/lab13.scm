; Lab 13: Final Review

; Q3
(define (compose-all funcs)
  (define (compose-sofar composed funcs)
    (if (null? funcs) composed
      (compose-sofar (lambda (x) ((car funcs) (composed x) )) (cdr funcs))))
  (compose-sofar (lambda (x) (+ x)) funcs)
)
