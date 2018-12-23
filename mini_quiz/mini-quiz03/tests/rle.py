test = {
  'name': 'rle',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (rle nil)
          f36b5c25c13a4b03b509f3f846ae9d4d
          # locked
          scm> (define foo (cons-stream 6 (cons-stream 6 (cons-stream 6 nil))))
          65ffb5c798995a4e06390225d7e5b0aa
          # locked
          scm> (car (rle foo))
          f482ab849000e38d8fa5d392f29ed893
          # locked
          scm> (cdr-stream (rle foo))
          f36b5c25c13a4b03b509f3f846ae9d4d
          # locked
          scm> (define s (cons-stream 1 (cons-stream 1 (cons-stream 2 nil))))
          bee83b5f9671a34a59d73f9a422696df
          # locked
          scm> (car (rle s))
          96e8ba7b032729d1ca0aba77ba21563c
          # locked
          scm> (car (cdr-stream (rle s)))
          41a9b6008e460256b6aabbd8b421d8d5
          # locked
          scm> (cdr-stream (cdr-stream (rle s)))
          f36b5c25c13a4b03b509f3f846ae9d4d
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (define (long-stream elem repetitions tail)
          ....   (if (= repetitions 0)
          ....       tail
          ....       (cons-stream elem (long-stream elem (- repetitions 1) tail))))
          long-stream
          scm> (define threes (long-stream 3 1000 nil))
          threes
          scm> (define twos (long-stream 2 1000 threes))
          twos
          scm> (define ones (long-stream 1 1000 twos))
          ones
          scm> (define compressed (rle ones))
          compressed
          scm> (car compressed)
          (1 1000)
          scm> (car (cdr-stream compressed))
          (2 1000)
          scm> (car (cdr-stream (cdr-stream compressed)))
          (3 1000)
          scm> (cdr-stream (cdr-stream (cdr-stream compressed)))
          ()
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load 'mini-quiz03)
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
