import random
print('Hi, whats your name player?')
name = raw_input()
sNum = random.randint(1, 20)
print('Well, ' + name + ' I am thinking of a number between 1 and 20')

for aTkn in range(1, 7):
    print('Take a guess.')
    guess = int(raw_input())
    if guess < sNum:
        print('Your guess is too low.')
    elif guess > sNum:
        print('Your guess is too high')
    else:
        break

if guess == sNum:
    print('Good job, ' + name + '! You guessed my number in ' + str(aTkn) + ' attempts')
else:
    print('Nope, ' + name + '! You failed again!')
    print(str(aTkn) + ' is a max attemts in this cruel game!')