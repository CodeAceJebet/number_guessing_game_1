import random

number = random.randint(1,100)

for attempt in range(5):
    guess=int(input('Guess the number :D'))
    if guess > number:
        print('Too high!')
    elif guess < number:
        print('Too low!')
    else:
        print('Just perfect!')
