
import random
guess = random.randint(1,10)
no_guesses = 0
guess_limit =3

print("You have 3 guesses to win a prize")
print("Guess a number between 1 and 10")

while no_guesses < guess_limit:
    guess_number = int(input("Guess: "))
    no_guesses += 1
    if guess_number == guess:
        print("YOu won")
        break
else:
    print("Game over")
      
     
print("Hello branching manually")        