"""
Assignment 2-A
==============

Wrap Assignment 1-A in function `poem()` that satisfies the doctest:

>>> from pathlib import Path
>>> poem() == Path('data/poem-en.txt').read_text()
True
"""

def poem():
    main_data = [[' ', 'farmer sowing his corn'],
                 ['kept', 'cock that crowed in the morn'],
                 ['waked', 'priest all shaven and shorn'],
                 ['married', 'man all tattered and torn'],
                 ['kissed', 'maiden all forlorn'],
                 ['milked', 'cow with the crumpled horn'],
                 ['tossed', 'dog'],
                 ['worried', 'cat'],
                 ['killed', 'rat'],
                 ['ate', 'malt'],
                 ['lay in', 'house that Jack built.']]
    couplet = ''; message = ''; ent = '\n'

    for i in range(len(main_data)):
        if i >= 2 :
            message = (F'{message}\nThis is the {main_data[-i - 1][1]},\n{couplet}')
            couplet = 'That ' + main_data[-i - 1][0] + ' the ' + main_data[-i - 1][1] + ',\n' + couplet
        else:
            message = (F'{message}This is the {main_data[-i - 1][1]}\n{couplet}{ent*(i==0)}')
            couplet = 'That ' + main_data[-i - 1][0] + ' the ' + main_data[-i - 1][1] + '\n' + couplet
    return message

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    
