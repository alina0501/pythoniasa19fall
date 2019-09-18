main_data = [[' ', 'farmer sowing his corn'],
             ['kept', 'cock that crow\'d in the morn'],
             ['waked', 'priest all shaven and shorn'],
             ['married', 'man all tatter\'d and torn'],
             ['kissed', 'maiden all forlorn'],
             ['milk\'d', 'cow with the crumpled horn'],
             ['tossed', 'dog'],
             ['worried', 'cat'],
             ['killed', 'rat'],
             ['ate', 'malt'],
             ['lay in', 'house that Jack built.']]
couplet = ''

for i in range(len(main_data)):
    if i >= 2:
        F'This is the {main_data[-i-1][1]}, '
        print(couplet)
        couplet = 'That ' + main_data[-i-1][0] + ' the ' + main_data[-i-1][1] + ',\n' + couplet
    else:
        F'This is the {main_data[-i-1][1]} '
        print(couplet)
        couplet = 'That ' + main_data[-i-1][0] + ' the ' + main_data[-i-1][1] + '\n' + couplet
