(define (factorial x)
  (if (= x 0)
    1
    (* x (factorial (- x 1))))
)


(define (fib n)
  (cond
    ((= n 0) 0)
    ((= n 1) 1)
    (else (+ (fib(- n 2)) (fib (- n 1)))))
)

(define (concat a b)
  (cond 
    ((null? a) b)
    ((null? b) a)
    (else (cons (car a) (concat (cdr a) b))))
)

(define (replicate x n)
  (if (= n 0) 
    nil
    (cons x (replicate x (- n 1))))
)

(define (uncompress s)
  (if(or (null? s) (not (pair? (car s))))
    s
    (concat (replicate (car (car s)) (car (cdr (car s)))) (uncompress (cdr s))))
)

(define (map fn lst)
  (if (null? lst)
    nil
    (cons (fn (car lst)) (map fn (cdr lst))))
)

(define (deep-map fn lst)
  (cond
    ((null? lst) nil)
    ((pair? (car lst)) 
      (cons (deep-map fn (car lst)) (deep-map fn (cdr lst))))
    (else
      (cons (fn (car lst)) (deep-map fn (cdr lst)))))
)

(define (make-tree label branches) (cons label branches))

(define (label tree) (car tree))

(define (branches tree) (cdr tree))

(define (tree-sum tree)
  (define (sum-lst lst)
    (if (null? lst)
      0
      (+ (car lst) (sum-lst (cdr lst)))))
  (+ (label tree) (sum-lst (map tree-sum (branches tree))))
)

(define (path-product-tree t)
  (define (product-b label-t b)
    (make-tree (* label-t (label b)) 
	       (map (lambda (b-branch) (product-b (* label-t (label b)) b-branch)) (branches b))))
  (make-tree (label t) (map (lambda (b) (product-b (label t) b)) (branches t)))
)
