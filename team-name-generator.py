print('Welcome to the..')
print('''
╔╦╗┌─┐┌─┐┌┬┐  ╔╗╔┌─┐┌┬┐┌─┐  ╔═╗┌─┐┌┐┌┌─┐┬─┐┌─┐┌┬┐┌─┐┬─┐
 ║ ├┤ ├─┤│││  ║║║├─┤│││├┤   ║ ╦├┤ │││├┤ ├┬┘├─┤ │ │ │├┬┘
 ╩ └─┘┴ ┴┴ ┴  ╝╚╝┴ ┴┴ ┴└─┘  ╚═╝└─┘┘└┘└─┘┴└─┴ ┴ ┴ └─┘┴└─
 ''')
verb: str = input('What verb best describe your team? ')
noun: str = input('What is one thing that everyone enjoy? ')

team_name: str = 'Here is your new Team Name!'
print(team_name + ' The ' + noun + ' ' + verb + 'ers! ')
print('\n')
