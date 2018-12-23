test = {
  'name': 'Prologue',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'answer': 'Turns input into tokens',
          'choices': [
            'Turns input into tokens',
            'Tries to beat Superman',
            'Organizes tokens in a data structure',
            'Makes sure that there are no parentheses errors'
          ],
          'hidden': False,
          'locked': False,
          'question': 'What does the lexer do?'
        },
        {
          'answer': 'Organizes tokens in a data structure',
          'choices': [
            'Turns input into tokens',
            'Organizes tokens in a data structure',
            'Evaluates the input'
          ],
          'hidden': False,
          'locked': False,
          'question': 'What does the parser do?'
        },
        {
          'answer': 'Read-Eval-Print-Loop',
          'choices': [
            'Read-Eval-Print-Loop',
            'Really-Enormous-Purple-Llamas',
            'Read-Eval-Parse-Lex'
          ],
          'hidden': False,
          'locked': False,
          'question': 'What does REPL stand for?'
        },
        {
          'answer': 'Four',
          'choices': [
            'One',
            'Two',
            'Three',
            'Four'
          ],
          'hidden': False,
          'locked': False,
          'question': 'How many types of expressions does PyCombinator have?'
        },
        {
          'answer': 'Three',
          'choices': [
            'One',
            'Two',
            'Three',
            'Four'
          ],
          'hidden': False,
          'locked': False,
          'question': 'How many types of values does PyCombinator have?'
        },
        {
          'answer': 'A lambda function is the result of evaluating a lambda expression',
          'choices': [
            'They are the same thing',
            'A lambda expression is the result of evaluating a lambda function',
            'A lambda function is the result of evaluating a lambda expression',
            'A lambda expression is a call to a lambda function'
          ],
          'hidden': False,
          'locked': False,
          'question': 'What is the difference between a lambda expression and a lambda function?'
        },
        {
          'answer': 'A parent environment',
          'choices': [
            'A list of parameters',
            'A body expression',
            'A parent environment',
            'A result value'
          ],
          'hidden': False,
          'locked': False,
          'question': "What information does a lambda function have that a lambda expression doesn't?"
        },
        {
          'answer': 'Literal(1)',
          'choices': [
            'Literal(1)',
            'Number(1)',
            "Name('1')",
            'Name(1)'
          ],
          'hidden': False,
          'locked': False,
          'question': "What will read('1') output?"
        },
        {
          'answer': "Name('x')",
          'choices': [
            'Literal(x)',
            'x',
            'Name(x)',
            "Name('x')"
          ],
          'hidden': False,
          'locked': False,
          'question': "What will read('x') output?"
        },
        {
          'answer': "CallExpr(Name('add'), [Literal(3), Literal(4)])",
          'choices': [
            "CallExpr(Literal('add'), Literal(3), Literal(4))",
            "CallExpr('add', [Literal(3), Literal(4)])",
            "CallExpr(Name('add'), Literal(3), Literal(4))",
            "CallExpr(Name('add'), [Literal(3), Literal(4)])"
          ],
          'hidden': False,
          'locked': False,
          'question': "What will read('add(3, 4)') output?"
        },
        {
          'answer': "CallExpr(CallExpr(Name('f'), []), [])",
          'choices': [
            "CallExpr(CallExpr(Name('f'), []), [])",
            "CallExpr(CallExpr(Name('f'))",
            "CallExpr(Name('f'), [])",
            "CallExpr(Name('f'), [CallExpr(Name('f'), [])])"
          ],
          'hidden': False,
          'locked': False,
          'question': "What will read('f()()') output?"
        }
      ],
      'scored': False,
      'type': 'concept'
    }
  ]
}
