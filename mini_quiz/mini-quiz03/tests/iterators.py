test = {
  'name': 'iterators',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> class Sad:
          ...     def __init__(self, green):
          ...         self.green = green
          ...     def __next__(self):
          ...         frog = self.green
          ...         if frog > 50:
          ...             raise StopIteration
          ...         self.green += frog
          ...         return frog
          ...     def __iter__(self):
          ...         self.green *= self.green
          ...         return self
          >>> s = Sad(1)
          >>> next(s)
          1
          >>> next(s)
          2
          >>> s.green
          4
          >>> slst = []
          >>> for i in s:
          ...     slst.append(i)
          >>> slst
          d4eb54cf471227a155e1e89626ca8c48
          # locked
          >>> s.green
          8fc6849eb72a236b57a3dd21ff7ff1de
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': True,
      'type': 'wwpp'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> class Such:
          ...     def __init__(self, iteration):
          ...         self.iteration = iteration
          ...     def __next__(self):
          ...         if self.iteration == 0:
          ...             raise StopIteration
          ...         self.iteration //= 2
          ...         return self.iteration
          ...     def __iter__(self):
          ...         while self.iteration < 30:
          ...             yield self.iteration
          ...             self.iteration += 10
          >>> s = Such(16)
          >>> next(s)
          38ed587dc461b5cd621c3f519d1fc50a
          # locked
          >>> next(s)
          99b13d1c0d6879b22a196efd34b4751e
          # locked
          >>> slst = []
          >>> for j in s:
          ...    slst.append(j)
          >>> slst
          1fdbdf6c7fe9aec2c79353a9531ea89b
          # locked
          >>> next(s)
          80c5262c9bae4d6ff1bde8965a5d8dfa
          # locked
          >>> for j in s:
          ...    slst.append(j)
          >>> slst
          ad4b0fc9cb34ab554c38c52981b1f718
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': True,
      'type': 'wwpp'
    }
  ]
}
