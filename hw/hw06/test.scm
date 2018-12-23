(define (uncompress s)
	(if (null? s) 
	s
	(concat (replicate (car (car s)) (car (cdr (car s)))) (
uncompress (cdr s)))))

(define (replicate x n)
	(if (= n 0)
	nil
	(cons x (replicate x (- n 1)))))

(define (concat a b)
	(if (null? a)
	b
	(cons (car a) (concat (cdr a) b))))

(define (uncompress2 s)
	(if (null? s)
	s
	(cons (replicate (car (car s)) (car (cdr(car s)))) (uncompress2 (cdr s)))))

