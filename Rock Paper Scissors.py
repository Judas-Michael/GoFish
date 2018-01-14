import random

def main():

	answer = "Y"

	while (answer != "N"):

		answer = input("Wanna play 'Rock Paper Scissors'? (Y or N) ")
		if answer == "Y":
			print("Cool!")
			choice = input("Rock, Paper, Scissors?")
			comp_choice = choose(choice)
	
		if answer == "N":
			print("Oh.... ok")
		else:
			answer = "Y"
			print("That's not an answer!")
		
		
def choose(choice):
	x = random.randint(1,3)
	if choice == "Rock" and x == 2:
		print("Your opponent chose Paper. You lose!")
	if choice == "Rock" and x == 1:
		print("Your opponent also chose Rock. It's a tie!")
	if choice == "Rock" and x == 3:
		print("Your opponent chose Scissors. You win!")
	if choice == "Scissors" and x == 2:
		print("Your opponent chose Paper. You win!")
	if choice == "Scissors" and x == 1:
		print("Your opponent also chose Rock. You lose!")
	if choice == "Rock" and x == 3:
		print("Your opponent chose Scissors. It's a tie!")
	if choice == "Paper" and x == 2:
		print("Your opponent chose Paper. It's a tie!")
	if choice == "Paper" and x == 1:
		print("Your opponent also chose Rock. You win!")
	if choice =="Paper" and x == 3:
		print("Your opponent chose Scissors. You lose!")
	return null