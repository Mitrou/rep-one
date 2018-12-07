print ('How many cats do you have?')
numCats = raw_input()
try:
    if int(numCats) >= 4:
        print('That is a lot of cats.')
    elif 0 < int(numCats) < 4:
        print('That is not a lot of cats.')
    elif int(numCats) < 0:
        print('You cant have lesser then zero number of cats.')
except ValueError:
    print('You did not enter a number.')
