import random
import time
print("Roll a d6. On a 6 you can say hello and exit the program.")
number = 0
while number != 6:
        enter = input("Press enter to roll the dice.")
        time.sleep(2)
        number = random.randint(1, 6)
        print(number)
        time.sleep(1)


enter = input("Press enter to say hello.")
print('Hello World')