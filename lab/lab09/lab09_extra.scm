;; Extra Scheme Questions ;;

; Q8
(define (max a b) (if (> a b) a b))
(define (min a b) (if (> a b) b a))
(define (gcd a b)
	(cond ((= b 0) a)
	  ; (else (and (> a b) (not (eq? (modulo a b) 0))) (gcd b (modulo a b))
	  (else (gcd b (modulo a b))
	  	)
  )
)

;;; Tests
(gcd 24 60)
; expect 12
(gcd 1071 462)
; expect 21

; Q9
(define (split-at lst n)
  
)
