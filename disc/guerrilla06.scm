(define (merge s1 s2)
  (if (< (car s1) (car s2)) 
    (cons-stream (car s1) (merge (cdr-stream s1) s2)) 
    (cons-stream (car s2) (merge s1 (cdr-stream s2)))))

; Returns a new Stream where each new value is the result of calling
; fn on the value in the stream
(define (map-stream s fn)
  (if (null? s) s
    (cons-stream (fn (car s)) (map-stream (cdr-stream s) fn))))

; Returns a new Stream containing all values in the stream s that
; satisfy the predicate fn
(define (filter-stream s fn)
  (cond ((null? s) s)
	((fn (car s)) (cons-stream (car s) (filter-stream
					     (cdr-stream s) fn)))
	(else (filter-stream (cdr-stream s) fn))))

; Returns True if n contains the digit 2. False otherwise
(define (contains-two n)
  (cond ((= n 0) #f)
	((= (remainder n 10) 2) #t)
	(else (contains-two (quotient n 10)))))

; Returns the factorial n
(define (factorial n)
  (if (= n 0) 1 (* n (factorial (- n 1)))))

; Returns a stream of factorials
(define (factorial-stream)
  (define (helper n)
    (cons-stream (factorial n) (helper (+ n 1))))
  (helper 1))

(define (half-twos-factorial)
  (map-stream (filter-stream (factorial-stream) contains-two) (lambda (x) (/ x 2))))

; Multiplies x by y
(define (mult x y)
  (define (mult-sofar product y)
    (if (= y 0) product (mult-sofar (+ x product) (- y 1))))
  (mult-sofar 0 y))

; Returns a list of pairs, the ith pair has item as its car and the
; ith element of lst as its cdr
(define (add-to-all item lst)
  (define (add-item-sofar lst-added lst)
    (if (null? lst) lst-added
      (add-item-sofar (append lst-added (list (cons item (car lst)))) (cdr lst))))
  (add-item-sofar nil lst)
)

(define (sum-satisfied-k lst f k)
  (define (sum-so-far sum lst n)
    (if (or (null? lst) (= n k)) sum
      (sum-so-far (+ sum (car lst)) (cdr lst) (+ n 1))))
  (sum-so-far 0 (filter f lst) 0))

(define (remove-range lst i j)
  (define (helper lst-prev index lst)
    (cond
      ((or (null?) (> index j)) (append lst-prev lst))
      ((< index i) (helper (append lst-prev (list (car lst))) (+ index 1) (cdr lst)))
      (else (helper lst-prev (+ index 1) (cdr lst)))))
  (helper nil 0 lst))

(define-macro (when condition . exprs)
  (list 'if condition (cons 'begin exprs) ''okay))


(define-macro (when2 condition . exprs)
  `(if ,condition ,(cons 'begin exprs) 'okay))

(define (fact n)
  (define (fact-sofar result k)
    (if (< n k) result (fact-sofar (* result k) (+ k 1))))
  (fact-sofar 1 1))

(define-macro (while initial-bindings condition updates return)
  (define helper-vars (map (lambda (x) (car x)) initial-bindings)) 
  (define initial-vals (map (lambda (x) (car (cdr x))) initial-bindings))
  (list 'begin 
    (list 'define (cons 'helper helper-vars)
      `(if ,condition
	 ,(cons 'helper updates)
	 ,return))
    (cons 'helper initial-vals)))



