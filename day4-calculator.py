print(''' 
╔═╗┬─┐┌─┐┌─┐  ╔═╗┌─┐┬  ┌─┐┬ ┬┬  ┌─┐┌┬┐┌─┐┬─┐  ╔═╗┬─┐┌─┐┌─┐┬─┐┌─┐┌┬┐
╠═╣├┬┘├┤ ├─┤  ║  ├─┤│  │  │ ││  ├─┤ │ │ │├┬┘  ╠═╝├┬┘│ ││ ┬├┬┘├─┤│││
╩ ╩┴└─└─┘┴ ┴  ╚═╝┴ ┴┴─┘└─┘└─┘┴─┘┴ ┴ ┴ └─┘┴└─  ╩  ┴└─└─┘└─┘┴└─┴ ┴┴ ┴
_____________________
|  _________________  |
| | JO           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
''')

import math


def paint_calculation(height, width, cover):
    area = height * width
    num_of_cans_of_paint = math.ceil(area / cover)
    print(f"You'll need {num_of_cans_of_paint} cans of paint.")


test_height = int(input("Height of wall: "))
test_width = int(input("Width of wall: "))
coverage = 5
paint_calculation(height=test_height, width=test_width, cover=coverage)
