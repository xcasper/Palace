#-------------------------------------------------------------------------------
# Name:        PalaceGame
# Purpose:     Game Control Module
#
# Author:      Craig
#
# Created:     24/03/2014
# Copyright:   (c) Craig 2014

# Licence:     <your licence>
#-------------------------------------------------------------------------------
'''
Notes:
First Refactoring: combine if/else statements that were seperated for error testing

Current Objective:

Created by Craig Gleckman
'''

import sys
import random

class PalaceGame(object):

    def __init__(self):
        #Initialize all variables
    	turn = 0
    	gameover = false
    	#declare local variables
    	numPlayers = 0
        players = []
        deck = []
        playerOne = Player()
        playerTwo = Player()
        playerThree = Player()
        playerFour = Player()

    	#get player count
    	numPlayers = raw_input("How many players? (Enter 2-4):")

    	#check valid num players
    	while numPlayers < 2 or numPlayers > 4:
    		numPlayers = raw_input("Please enter a valid number of Players (2-4):")

    	#save numPlayers to const variable so it doesnt ever get modified
    	CONST_PLAYERCOUNT = numPlayers

    	#set dealer
    	srand(time(NULL))
    	r = random()
        dealer = r.randrange(CONST_PLAYERCOUNT)

    	setupGame(CONST_PLAYERCOUNT)

def setupGame(self, CONST_PLAYERCOUNT):

	#Confirm valid player amount
	if CONST_PLAYERCOUNT >= 2 and CONST_PLAYERCOUNT <= 4:
	   print "Palace Card Game Loading..."

		#Allows each player to pick a name
		CreatePlayers(CONST_PLAYERCOUNT, self.players,  self.dealer)

		#Make sure that players array (setup in CreatePlayers) worked
		if len(self.players) == CONST_PLAYERCOUNT:
			print "CreatePlayers ran successfully"

			CreateDeck(self.deck) #forms the 52 card deck

			#Make sure deck was created properly (52 cards)
			if len(self.deck) == 52:

				print "CreateDeck ran successfully"
				ShuffleDeck(self.deck) #randomizes the deck (when created it is created in rank and suit order)

				#Recheck deck size to make sure shuffle did not mess anything up
				if len(self.deck) == 52:

					print "ShuffleDeck ran successfully"
					DealGame(CONST_PLAYERCOUNT) #Gives each player 3 palace cards and then 6 cards to start with

					#Make sure each player has 6 cards in his/her hand at start
					for player in self.players:
						if self.players[player].getHandCount() != 6:
							print "Something went wrong WITH DealGame **"
                            #TODO: does this break belong?
							break
						 #end if
					 #end for
					ChooseTopOfPalace(self.players) #Asks each player which 3 cards from their hand they would like to use for the OnTopOfPalace cards

					#Make sure each player has 3 cards left after choosing top of palace
					for player in self.players:
						if self.players[player].getTopOfPalaceCount() != 3
							print "Something went wrong WITH TOPOFPALACE **"
							break
						#end if
					#end for
					PlayGame(CONST_PLAYERCOUNT) #Starts with player to the left of the dealer

					#Gameover should be true after playgame is finished
					if !gameover:
						print "Something went wrong WITH playGame"
					else:
						print "Good-Bye!"

				#end if
				else:
					print "Something went wrong WITH ShuffleDeck"
				#end else

			#end if
            else:
				print "Something went wrong WITH CreateDeck"
			#end else
		#end if
        else:
            print "something went wrong WITH CreatePlayers"
		#end else

	else:
        print "Palace Card Game NOT Loaded Successfully!"

#end setupGame

def CreatePlayers(self)

	#Declare local variables
	input = "None"

	#Depending on CONST_PLAYERCOUNT set players into a vector and let them give their name
	#Determine order of players in vector by who was randomly choosen as dealer
	if self.CONST_PLAYERCOUNT == 2:
		input = raw_input("Please give a name to Player1: ")
		self.playerOne.setName(input)

		input = raw_input("Please give a name to Player2: ")
		self.playerTwo.setName(input)

		#Dealer always last
		if self.dealer == 0:
			self.players.append(self.playerTwo)
			self.players.append(self.playerOne)


		elif self.dealer == 1:
			self.players.append(self.playerOne)
			self.players.append(self.playerTwo)

		else:
			print "Something went wrong IN CreatePlayers ** PLAYER ORDER '2' **"

		print "Players Total: " + len(self.players)
		for player in self.players:
			print self.players[player].getName()
	#end if

	elif self.CONST_PLAYERCOUNT == 3:

		input = raw_input("Please give a name to Player1: ")
		self.playerOne.setName(input)

		input = raw_input("Please give a name to Player2: ")
		self.playerTwo.setName(input)

		input = raw_input("Please give a name to Player3: ")
		self.playerThree.setName(input)

		#Dealer always last
		if self.dealer == 0:
			self.players.append(self.playerTwo)
			self.players.append(self.playerThree)
			self.players.append(self.playerOne)

		elif self.dealer == 1:
			self.players.append(self.playerThree)
			self.players.append(self.playerOne)
			self.players.append(self.playerTwo)

		elif self.dealer == 2:
			self.players.append(self.playerOne)
			self.players.append(self.playerTwo)
			self.players.append(self.playerThree)

		else:
			print "Something went wrong IN CreatePlayers ** PLAYER ORDER '3' **"

		print "Players Total: " + len(self.players)

		for player in self.players:
			print self.players[player].getName()
	#end elif

	elif self.CONST_PLAYERCOUNT == 4:

		input = raw_input("Please give a name to Player1: ")
        self.playerOne.setName(input)

		input = raw_input("Please give a name to Player2: ")
        self.playerTwo.setName(input)

		input = raw_input("Please give a name to Player3: ")
        self.playerThree.setName(input)

		input = raw_input("Please give a name to Player4: ")
		self.playerFour.setName(input)

		#Dealer always last
		if dealer == 0:
			players.append(self.playerTwo)
			players.append(self.playerThree)
			players.append(self.playerFour)
			players.append(self.playerOne)


		elif dealer == 1:
			players.append(self.playerThree)
			players.append(self.playerFour)
			players.append(self.playerOne)
			players.append(self.playerTwo)

		elif dealer == 2:
			players.append(self.playerFour)
			players.append(self.playerOne)
			players.append(self.playerTwo)
			players.append(self.playerThree)

		elif dealer == 3:
			players.append(self.playerOne)
			players.append(self.playerTwo)
			players.append(self.playerThree)
			players.append(self.playerFour)

		else:
			print "Something went wrong IN CreatePlayers ** PLAYER ORDER '4' **"

		print "Players Total: " + len(self.players)

		for player in self.players:
			print self.players[player].getName()

	#end elif

	else:
		print "something went wrong IN CreatePlayers ** NON legal amount of players **"
	#end else
#end CreatePlayers

def CreateDeck (self.deck):

	#Create cards 2 - 14 since no cards in a regular deck of cards have a rank 0 or 1 (11 = jack | 12 = queen | 13 = king | 14 = ace)
	for(int r=2 r<15 r++)

		# make sure a 0 or 1 was not created somehow
		if(r == 0 || r == 1)

			print "ERROR IN CREATE DECK **CREATION LOOP**"

		#create suits 1 - 4 (1 = Club | 2 = Spade | 3 = heart | 4 = diamonds)
		for(int s=1 s<=4 s++)

			if(s==1)

				Card card(r, 'C')
				deck.push_back(card)
			#end if
			else if(s==2)

				Card card(r, 'S')
				deck.push_back(card)
			#end elseif
			else if(s==3)

				Card card(r, 'H')
				deck.push_back(card)
			#end elseif
			else if(s==4)

				Card card(r, 'D')
				deck.push_back(card)
			#end elseif
			else

				print "Something went wrong IN CreateDeck ** s != 1-4"
			#end else
		#end for
	#end for

	#always should be 52 during creation
	if(deck.size() == 52)

		#make sure there are no duplicate cards
		for(int i=0 i<deck.size() i++)

			Card cardCheck = deck[i]
			#Test cardCheck against entire deck
			for(int j=0 j<deck.size() j++)

				if(cardCheck.getRank() == deck[j].getRank()
					&& cardCheck.getSuit() == deck[j].getSuit()
					&& i != j)

					print "Something went wrong IN CreateDeck 3 ** MULTIPLE OF CARD: "
					cardCheck.DisplayCard()
					print endl
					print "Location in deck vector: " << j << "**"
				#end if
			#end for
		#end for
	#end if

	else

		print "Something went wrong IN CreateDeck 2 ** DECK != 52 **"
	#end else

	print "DECK SIZE: " << deck.size()
#end CreateDeck

def ShuffleDeck(vector<Card> &deck)

	#Declare local variables
	srand(time(NULL))
	Card temp
	Card temp2
	Card temp3
	int r, r2, r3

	#Confirm deck size has not changed yet
	if(deck.size() == 52)

		for(int i = 0 i < 52 i++)

			r = rand() % 52
			r2 = rand() % 52
			r3 = rand() % 52

			temp = deck[i]
			deck[i] = deck[r]
			deck[r] = deck[r2]
			deck[r2] = deck[r3]
			deck[r3] = temp

		#end for
	#end if

	else

		print "Something went wrong IN ShuffleDeck ** DECK != 52 **"
	#end else
#end ShuffleDeck

def DealGame(const int CONST_PLAYERCOUNT)

	#deal palace
	for(int i=0 i<CONST_PLAYERCOUNT*3 i++)

		if(i%CONST_PLAYERCOUNT==0)

			players[0].setPalaceCard(deck[i])

		else if(i%CONST_PLAYERCOUNT==1)

			players[1].setPalaceCard(deck[i])

		else if(i%CONST_PLAYERCOUNT==2)

			players[2].setPalaceCard(deck[i])

		else if(i%CONST_PLAYERCOUNT==3)

			players[3].setPalaceCard(deck[i])

	#end for

	#erase cards used for Palace
	for(int r=0 r<CONST_PLAYERCOUNT*3 r++)

		deck.erase(deck.begin())


	#check player hands
	for(int i=0 i<CONST_PLAYERCOUNT i++)

		print "Player " << i << "'s palace: "
		for(int j=0 j<players[i].getPalaceCount() j++)

			print "Card " << j << " = "
			players[i].getPalaceCard(j).DisplayCard()
			print endl



	#deal initial 6 cards
	for(int i=0 i<CONST_PLAYERCOUNT*6 i++)

		if(i%CONST_PLAYERCOUNT==0)

			players[0].setHandCard(deck[i])

		else if(i%CONST_PLAYERCOUNT==1)

			players[1].setHandCard(deck[i])

		else if(i%CONST_PLAYERCOUNT==2)

			players[2].setHandCard(deck[i])

		else if(i%CONST_PLAYERCOUNT==3)

			players[3].setHandCard(deck[i])



	#erase cards used for initial deal
	for(int r=0 r<CONST_PLAYERCOUNT*6 r++)

		deck.erase(deck.begin())


	drawPile = deck
	deck.clear()
#end DealGame

def ChooseTopOfPalace(vector<Player> &players)

	int cardChoice, counter = 0
	do

		while(counter < 3)

			print players[turn].getName() << " Please choose number corresponding to the card you would like to be ontop of your palace: "
			print "Current Cards: "

			for(int i=0 i < players[turn].getHandCount() i++)

				print i << ". "
				players[turn].getHandCard(i).DisplayCard()
				print endl


			print "Choose TopOfPalace Card " << counter << ": "
			cin >> cardChoice
			print endl
			if(cardChoice < 0 || cardChoice >= players[turn].getHandCount())

				print "INVALID OPTION"
				counter--

			else if(cardChoice >= 0 && cardChoice < players[turn].getHandCount())

				players[turn].setTopOfPalace(players[turn].getHandCard(cardChoice))
				players[turn].removeHandCard(cardChoice)

			counter++

		counter = 0
		IncrementTurn()
	while(turn != 0)

	print "****** PRINTING TOP OF PALACE CARDS FOR EACH PLAYER:******"
	for(int y=0 y<players.size() y++)

		print "Player " << y << ":"
		print "Card 1:"
		players[y].getTopOfPalaceCard(0).DisplayCard()

		print "Card 2:"
		players[y].getTopOfPalaceCard(1).DisplayCard()

		print "Card 3:"
		players[y].getTopOfPalaceCard(2).DisplayCard()



 def PlayGame(const int CONST_PLAYERCOUNT)

	print "!!!!!!!!Current turn: " << turn
	while(!gameover)

		print players[turn].getName() << " It's you're turn!"
		if(players[turn].getHandCount() == 0 && drawPile.size() == 0)

			if(players[turn].getTopOfPalaceCount() != 0)

				players[turn].setHand(players[turn].getTopOfPalace())


			else if(players[turn].getPalaceCount() != 0)

				PlayFromPalace()


		PlayCard()
		#check drawPile size here to a unneeded function calls
		if(drawPile.size() != 0)

			DrawCards(turn)


		if(players[turn].getHandCount() == 0 && players[turn].getTopOfPalaceCount() == 0 && players[turn].getPalaceCount() == 0)

			print "A winner has been decided! Congradulations Player " << players[turn].getName()
			gameover = true

		else

			IncrementTurn()


	if(gameover)

		print "Thank you for playing Palace Card Game"

	else

		print "WTF WHY AM I RUNNING.. THIS IS BS.. I QUIT LIFE"



 def DrawCards(const int turn)


	if(drawPile.size() != 0)

		for(int i=0 i<3-players[turn].getHandCount() i++)

			players[turn].setHandCard(drawPile.back())

			if(drawPile.back().getRank() == midPile.back().getRank())

				print "You drew a card with the same rank as what was just played, it has been played for you! You draw again."  # may need to adjust and give option

				if(drawPile.size() != 0)





			drawPile.erase(drawPile.end()-1)


	else if(drawPile.size() == 0)

		print "DrawPile is Empty!"

	else

		print "Something went wrong IN DrawCard"



 def PickUpMidPile()

	players[turn].setHand(midPile)
	midPile.clear()
	if(midPile.size() != 0)

		print "Error in PickUpMidPile"



 def PlayCard()

	#May move functionality to playGame and make PlayCard simply add card to midPile
	int cardChoice
	bool turnover = false

	while(turnover == false)

		players[turn].DisplayHand()
		cin >> cardChoice

		while(cardChoice < 0 || cardChoice >= players[turn].getHandCount())

			print "Please enter a valid choice: "
			cin >> cardChoice


		if(isPlayable(players[turn].getHandCard(cardChoice)))

			Card playersCard
			midPile.push_back(players[turn].getHandCard(cardChoice))
			playersCard = players[turn].getHandCard(cardChoice)
			players[turn].removeHandCard(cardChoice)
			turnover = true

			if(isWildCard(playersCard))

				PlayWildCard(playersCard)

			else if(CheckMultiple(playersCard))

				playMultiple(playersCard)
			# end if
			else

				print "Next players turn!"


		else

			print "You have selected a card that is unable to be played, please choose again"




Player def CurrentTurn()

	return players[turn]


 def IncrementTurn()

	if(turn == players.size()-1)

		turn = 0

	else if(turn == 0 || turn == 1 || turn == 2)

		turn++

	else

		print "Something went wrong IN IncrementTurn"



bool def CheckMultiple(Card &card)

	for(int i=0 i<players[turn].getHandCount() i++)

		if(card.getRank() == players[turn].getHandCard(i).getRank())

			return true



	return false


bool def isPlayable(Card &card)

	if(midPile.size() == 0)

		return true

	else if(card.getRank() >= midPile.back().getRank()
		|| isWildCard(card))

		return true

	else

		return false



bool def isWildCard(Card &card)

	if(card.getRank() == 2 || card.getRank() == 10)

		return true

	else

		return false



 def playMultiple(Card &playersCard)

	int multiCardPlayInput

	print "Would you like to play cards of the same rank?"
	print "1. Yes, all! \n"
		<< "2. Yes, but not all! \n"
		<< "3. No."
	cin >> multiCardPlayInput

	while(multiCardPlayInput < 1 || multiCardPlayInput > 3)

		print "Please enter a valid choice: "
		cin >> multiCardPlayInput


	switch(multiCardPlayInput)

	case 1:
		for(int i=0 i<players[turn].getHandCount() i++)

			if(players[turn].getHandCard(i).getRank() == playersCard.getRank())

				midPile.push_back(players[turn].getHandCard(i))
				players[turn].removeHandCard(i)


		break
	case 2:
		while(CheckMultiple(playersCard))

			print "Please choose a card with the same rank to play(Type 123 to quit): "
			players[turn].DisplayHand()
			cin >> multiCardPlayInput
			if(multiCardPlayInput == 123)

				break

			else

				if(players[turn].getHandCard(multiCardPlayInput).getRank() == playersCard.getRank())

					midPile.push_back(players[turn].getHandCard(multiCardPlayInput))
					players[turn].removeHandCard(multiCardPlayInput)

				else if(players[turn].getHandCard(multiCardPlayInput).getRank() != playersCard.getRank())

					print "Please choose a Card with the rank: " << playersCard.getRank()

				else

					print "Something went horribly wrong in PlayCard() ** multiCardPlayInput case 2**"



		break
	case 3:
		break
	# end switch


 def PlayWildCard(Card &wildCard)

	int wildCardChoice
	do


		if(wildCard.getRank() == 2)

			midPile.push_back(wildCard)

			print "You played a 2, please play another card... You may play anything!"
			players[turn].DisplayHand()
			cin >> wildCardChoice

			while(wildCardChoice < 0 || wildCardChoice >= players[turn].getHandCount())

				print "Please enter a valid choice: "
				cin >> wildCardChoice

			wildCard = players[turn].getHandCard(wildCardChoice)

			if(isWildCard(wildCard))

				print "You have selected another wild card"
				players[turn].removeHandCard(wildCardChoice)

			else if(!isWildCard(wildCard) && wildCard.getRank() >= midPile.back().getRank())

				midPile.push_back(wildCard)
				players[turn].removeHandCard(wildCardChoice)

			else

				print "Something went terribly wrong in PlayWildCard ** not additional wild card **"



		else if(wildCard.getRank() == 10)

			midPile.push_back(wildCard)

			deadPile = midPile
			midPile.clear()

			if(deadPile.size() != 0 && midPile.size() == 0)

				print "You played a 10, please play another card... You may play anything!"
				players[turn].DisplayHand()
				cin >> wildCardChoice

				while(wildCardChoice < 0 || wildCardChoice >= players[turn].getHandCount())

					print "Please enter a valid choice: "
					cin >> wildCardChoice


				wildCard = players[turn].getHandCard(wildCardChoice)

				if(isWildCard(wildCard))

					print "You have selected another wild card"
					players[turn].removeHandCard(wildCardChoice)

				else

					midPile.push_back(wildCard)
					players[turn].removeHandCard(wildCardChoice)

					if(CheckMultiple(wildCard))

						playMultiple(wildCard)




			else

				print "Something went terribly wrong in PlayWildCard ** rank = 10 **"


	while(isWildCard(wildCard))


 def PlayFromPalace()

	int palaceCardChoice
	print "You have " << players[turn].getPalaceCount() << " palace cards."
	print "Please choose one of your remaining palace cards to play"
	cin >> palaceCardChoice

	while(palaceCardChoice < 0 || palaceCardChoice  > players[turn].getPalaceCount())

		print "Please enter a valid choice: "
		cin >> palaceCardChoice


	if(isPlayable(players[turn].getHandCard(palaceCardChoice)))

		Card playersCard
		midPile.push_back(players[turn].getHandCard(palaceCardChoice))
		playersCard = players[turn].getHandCard(palaceCardChoice)
		players[turn].removeHandCard(palaceCardChoice)

		if(isWildCard(playersCard))

			PlayWildCard(playersCard)

		else if(CheckMultiple(playersCard))

			playMultiple(playersCard)
		# end if
		else

			print "Next players turn!"



	else if(players[turn].getHandCard(palaceCardChoice).getRank() < midPile.back().getRank())

		PickUpMidPile()


	PlayCard()


