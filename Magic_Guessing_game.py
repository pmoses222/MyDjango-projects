import random

num = random.randint(1,11)

for num_tries in range(1,7):
    pick_num=input('Choose a number: ')

    if int(pick_num) < num:
        print('its too low')
    elif int(pick_num) > num:
        print('its too high')
    else:
        break      

if int(pick_num) == num:
    print('Yeah! you got it right')

else:
    print('Game Over')   
