import random

top_of_range = input('Type a number : ')

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <=0:
        print('Please type a number larger than 0')
        quit()
else:
    print('Please type a digit')
    quit()


random_number = random.randint(0,top_of_range) # absolute upper bound\
guesses = 0 

while True:
    guesses += 1
    num = input('Start guessing your number')
    if num.isdigit():
       num = int(num)

    else:
        print('Please type a digit')
        continue

    if num == random_number:
        print('You guessed the right number')
        break

    elif num > random_number:
        print('You were above the number')
    else:
        print('You were below the number')
        
print('You got it in',guesses,'guesses')