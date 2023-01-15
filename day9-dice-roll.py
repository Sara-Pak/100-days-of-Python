print('''
              _______.
   ______    | .   . |\
  /     /\   |   .   |.\
 /  '  /  \  | .   . |.'|
/_____/. . \ |_______|.'|
\ . . \    /  \ ' .   \'|
 \ . . \  /    \____'__\|
  \_____\/
''')
import random

while True:
    user_input = input('Enter r to roll the dice and any other key to exit ')
    random_num = random.randint(1, 6)
    if(user_input == 'r'):
        print(random_num)
    else:
        print('Thanks for playing!')
        break