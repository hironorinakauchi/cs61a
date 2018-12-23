 (define (foo n) 
  (cond (< n 10) 
    (if (= n 1) (n)) 
  (else (n + 1))))

(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  'YOUR-CODE-HERE
  (car(cdr s))
)

(define (caddr s)
  'YOUR-CODE-HERE
  (car(cdr(cdr s)))
)

(define (square x) (* x x))

(define (pow b n)
  'YOUR-CODE-HERE
  (define (helper r b n)
    (cond ((= n 0) r)
      ( (= (modulo n 2) 1) (helper (* r b) (square b) (quotient n 2)))
      (else (helper r (square b) (quotient n 2)))
      )
    )
  (helper 1 b n)
  )

(define (ordered? s)
  'YOUR-CODE-HERE
  (define (helper next_num pre_num)
    (cond ((null? next_num) #t)
          ((<= (car pre_num) (car next_num)) (helper (cdr next_num) next_num))
          (else #f)
        )
      )
  (helper (cdr s) s)
)

(define (no-repeats s)
  'YOUR-CODE-HERE
  ; (define (helper s next_s)
  ;   (cond ((null? next_s) (helper (cdr s) (cdr s)) )
  ;         ((null? s) s)
  ;         ((not (= (car s) (car next_s))) (cons (car s) (helper s (cdr next_s))))
  ;           (else (cons (car s) (helper s (cdr next_s))))
  ;       )
  ;     )
  ; (helper s (cdr s))
  (cond ((null? s) s)
    (else (cons (car s) (no-repeats(remove (car s) (cdr s)))))
    )
  )

(define (remove item lst)
  (cond ((null? lst) ())
       ((= (car lst) item) (remove item (cdr lst)))
        (else (cons (car lst) (remove item (cdr lst))))
          )
        )

(define (nodots s)
  (define (dot s)
  (and (pair? s) (not (or (pair? (cdr s)) (null?(cdr s))))))
  (cond ((null? s) s)
    ((dot s) (list (nodots (car s)) (cdr s)))
    ((pair? s) (cons (nodots (car s)) (nodots (cdr s))))
    (else s)
)
  )

; Sets as sorted lists

(define (empty? s) (null? s))

(define (contains? s v)
    (cond ((empty? s) false)
          ; 'YOUR-CODE-HERE
          ((= (car s) v) True)
          (else (contains? (cdr s) v)) ; replace this line
          )
        )

; Equivalent Python code, for your reference:
;
; def empty(s):
;     return len(s) == 0
;
; def contains(s, v):
;     if empty(s):
;         return False
;     elif s.first > v:
;         return False
;     elif s.first == v:
;         return True
;     else:
;         return contains(s.rest, v)
(define (add s v)
    (cond ((empty? s) (list v))
          ; 'YOUR-CODE-HERE
          ((contains? s v) s)
          ((< v (car s)) (cons v s))
          (else (cons (car s) (add (cdr s) v))) ; replace this line
          ))
(define (intersect s t)
    (cond ((or (empty? s) (empty? t)) nil)
          ; 'YOUR-CODE-HERE
          ((= (car s) (car t)) (cons (car s) (intersect (cdr s) (cdr t))))
          ((< (car s) (car t)) (intersect (cdr s) t))
          (else (intersect s (cdr t))) ; replace this line
          ))

; Equivalent Python code, for your reference:
;
; def intersect(set1, set2):
;     if empty(set1) or empty(set2):
;         return Link.empty
;     else:
;         e1, e2 = set1.first, set2.first
;         if e1 == e2:
;             return Link(e1, intersect(set1.rest, set2.rest))
;         elif e1 < e2:
;             return intersect(set1.rest, set2)
;         elif e2 < e1:
;             return intersect(set1, set2.rest)

(define (union s t)
    (cond ((empty? s) t)
          ((empty? t) s)
          ; 'YOUR-CODE-HERE
          ((not(contains? s (car t))) (union (add s (car t)) t))
          (else (union s (cdr t))) ; replace this line
          ))

; A data abstraction for binary trees where nil represents the empty tree
(define (tree label left right) (list label left right))
(define (label t) (car t))
(define (left t) (cadr t))
(define (right t) (caddr t))
(define (empty? s) (null? s))
(define (leaf label) (tree label nil nil))
(define (in? t v)
    (cond ((empty? t) false)
          ; 'YOUR-CODE-HERE
          ((= (label t) v) True)
          ((< (label t) v) (in? (right t) v))
          (else (in? (left t) v))
          ))

; Equivalent Python code, for your reference:
;
; def contains(s, v):
;     if s.is_empty:
;         return False
;     elif s.label == v:
;         return True
;     elif s.label < v:
;         return contains(s.right, v)
;     elif s.label > v:
;         return contains(s.left, v)
(define (as-list t)
    ; 'YOUR-CODE-HERE
    (if (empty? t) nil 
      (append (append (as-list (left t)) (list (label t))) (as-list (right t)))))
