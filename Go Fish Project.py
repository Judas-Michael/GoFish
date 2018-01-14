def main():

	answer = "Y"

	while (answer != "N"):

		answer = input("Wanna play 'Go Fish'? (Y or N) ")
		if answer == "Y":
			print("Cool!")
			print("Draw 5 Cards.")
			myCards = drawCards(5) #adds 5 cards to hand
			opponentCards = drawCards(5) #gets 5 cards to add to hand
			print(myCards) #This is to check function
			print (opponentCards) #checks function 
	
		if answer == "N":
			print("Oh.... ok")
		else:
			answer = "Y"
			print("That's not an answer!")
		
		
def drawCards(x):	
	cards = []
	while x > 0:
		cards.append(random.randint(1,13))
		x = x-1
	return cards

def cardDeck():
	deck = []
	cards = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
	type = ["Spades", "Hearts", "Diamonds", "Clubs"]
	for c in cards:
		for t in type:
		deck.append[c,t]
	return deck
	
def matchesMade():
	for x in cards:
		cardnum = cards[x]
		
		
		
# TO DO -- Subtract Deck from 42 each drawCards
#TO DO -- WHY DONT FUNCTIONS WORK????
#TO DO -- check for matches in hands
#TO DO -- add points when matches occur