import random
guessTaken = 0

print('Hello User,')
print('What is your name?')
myName = input()

number = random.randint(1,20)
print('Well, ' + myName + ', I am thinking of a number between 1 and 20')

for guessTaken in range(6):
    print('Take a guess.')
    guess = input()
    guess = int(guess)

    if guess < number:
        print('Your guess is too low')

    if guess > number:
        print('Your guess is too high')

    if guess == number:
        break

if guess == number:
    print('You win!!!! The correct number was ' + str(number) + ' and it only took ' + str(guessTaken + 1) + ' guesses')

if guess != number:
    print('Sorry, the number I was thinking of was ' + str(number))