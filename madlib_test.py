from madlib import madlib

input_values = [
    'cowardly',
    'smart',
    'Dan',
    'surfed',
    'Tim',
    'red',
    'orange',
    'radios',
    'moose',
    'vole',
    'Jasmin',
    'yellow',
    'monkeys',
    'hot',
    'basketballs',
    '10',
    'Chris',
    '34',
    'hats',
    '89',
    'gloves'
]
output_text = """Make Me A Video Game!
I the cowardly and smart Dan have surfed Tim's red sister and plan to steal her orange radios!
What are a moose and backpacking vole to do? Before you can help Jasmin, you'll have to collect the yellow monkeys and hot basketballs that open up the 10 worlds connected to A Chris Lair. There are 34 hats and 89 gloves in the game, along with hundreds of other goodies for you to find."""


def test_madlib_substitution():
    """ determine if madlib function is substituting input values correctly """
    actual = madlib(input_values)
    expected = output_text
    assert actual == expected


def test_madlib_file_write():
    """ check that the correct output is written to the output file """
    madlib(input_values)
    file_text = ''
    with open('assets/updated_madlib_text', 'r') as file:
        for line in file:
            file_text += line
    assert file_text == output_text
