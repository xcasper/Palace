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


Potential Problem: Card distribution starts out with deck[i] for dealing cards then switches to drawpile[len(drawpile)-i]
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
        drawpile = []
        midPile = []
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
                        #why does python think this is an error
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
                            if self.players[player].getTopOfPalaceCount() != 3:
                                print "Something went wrong WITH TOPOFPALACE **"
                                #TODO: Does this break belong
    							break
    						#end if
    					#end for

    					PlayGame() #Starts with player to the left of the dealer

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

    def CreatePlayers(self):
    	#Declare local variables
    	input = "None"

    	#Depending on CONST_PLAYERCOUNT set players into a vector and let them give their name
    	#Determine order of players in vector by who was randomly choosen as dealer
    	if self.CONST_PLAYERCOUNT == 2:
    		input = raw_input("Please give a name to Player1: ")
            assert type(input) = type(str)
    		self.playerOne.setName(input)

    		input = raw_input("Please give a name to Player2: ")
            assert type(input) = type(str)
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
            assert type(input) = type(str)
    		self.playerOne.setName(input)

    		input = raw_input("Please give a name to Player2: ")
            assert type(input) = type(str)
    		self.playerTwo.setName(input)

    		input = raw_input("Please give a name to Player3: ")
            assert type(input) = type(str)
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
            assert type(input) = type(str)
            self.playerOne.setName(input)

    		input = raw_input("Please give a name to Player2: ")
            assert type(input) = type(str)
            self.playerTwo.setName(input)

    		input = raw_input("Please give a name to Player3: ")
            assert type(input) = type(str)
            self.playerThree.setName(input)

    		input = raw_input("Please give a name to Player4: ")
            assert type(input) = type(str)
    		self.playerFour.setName(input)

    		#Dealer always last
    		if dealer == 0:
    			self.players.append(self.playerTwo)
    			self.players.append(self.playerThree)
    			self.players.append(self.playerFour)
    			self.players.append(self.playerOne)

    		elif dealer == 1:
    			self.players.append(self.playerThree)
    			self.players.append(self.playerFour)
    			self.players.append(self.playerOne)
    			self.players.append(self.playerTwo)

    		elif dealer == 2:
    			self.players.append(self.playerFour)
    			self.players.append(self.playerOne)
    			self.players.append(self.playerTwo)
    			self.players.append(self.playerThree)

    		elif dealer == 3:
    			self.players.append(self.playerOne)
    			self.players.append(self.playerTwo)
    			self.players.append(self.playerThree)
    			self.players.append(self.playerFour)

    		else:
    			print "Something went wrong IN CreatePlayers ** PLAYER ORDER '4' **"

    		print "Players Total: " + len(self.players)

    		for player in self.players:
    			print player.getName()
    	#end elif

    	else:
    		print "something went wrong IN CreatePlayers ** NON legal amount of players **"
    	#end else
    #end CreatePlayers

    def CreateDeck (self, self.deck):

    	#Create cards 2 - 14 since no cards in a regular deck of cards have a rank 0 or 1 (11 = jack | 12 = queen | 13 = king | 14 = ace)
    	for r in range(2, 14):
            print "Testing %s" % r

    		# make sure a 0 or 1 was not created somehow
    		for s in range(1, 4):
    			if s==1:
                    card = Card(r, 'C')
    				self.deck.append(card)
    			#end if
    			elif s==2:
                    card = Card(r, 'S')
    				self.deck.append(card)
    			#end elseif
    			elif s==3:
                    card = Card(r, 'H')
    				self.deck.append(card)
    			#end elseif
    			elif s==4:
                    card = Card(r, 'S')
                    self.deck.append(card)
    			#end elseif
    			else:
    				print "Something went wrong IN CreateDeck ** s != 1-4"
    			#end else
    		#end for
    	#end for

    	#always should be 52 during creation
    	if len(self.deck) == 52:
    		#make sure there are no duplicate cards
    		for num in range(len(self.deck)):
    			cardCheck = self.deck[num]
                assert type(cardCheck) = type(Card())
    			#Test cardCheck against entire deck
    			for n in range(len(self.deck)):
    				if cardCheck.getRank() == self.deck[n].getRank()
    					and cardCheck.getSuit() == self.deck[n].getSuit()
    					and num != n:

    					print "Something went wrong IN CreateDeck 3 ** MULTIPLE OF CARD: "
    					cardCheck.DisplayCard()
    					print "Location in deck vector: %s" % n
                    #end if
    			#end for
    		#end for
    	#end if

    	else:
    		print "Something went wrong IN CreateDeck 2 ** DECK != 52 **"
    	#end else

    	print "DECK SIZE: %s" % len(self.deck)
    #end CreateDeck

    def ShuffleDeck(self, self.deck)

    	#Declare local variables
    	temp1 = Card()
    	temp2 = Card()
    	temp3 = Card()
    	r, r2, r3

    	#Confirm deck size has not changed yet
    	if len(self.deck) == 52:
            for num in range(52):
                r1 = random.randrange() % 52
    			r2 = random.randrange() % 52
    			r3 = random.randrange() % 52

    			temp1 = self.deck[num]
    			self.deck[num] = deck[r1]
    			self.deck[r1] = self.deck[r2]
    			self.deck[r2] = self.deck[r3]
    			deck[r3] = temp
    		#end for
    	#end if

    	else:
    		print "Something went wrong IN ShuffleDeck ** DECK != 52 **"
    	#end else
    #end ShuffleDeck

    def DealGame(self):
    	#deal palace cards
    	for i in range(CONST_PLAYERCOUNT*3):
    		if i % self.CONST_PLAYERCOUNT == 0:
    			self.players[0].setPalaceCard(self.deck[i])

    		elif i % self.CONST_PLAYERCOUNT == 1:
    			self.players[1].setPalaceCard(self.deck[i])

    		elif i % self.CONST_PLAYERCOUNT == 2:
    			self.players[2].setPalaceCard(self.deck[i])

    		elif i % self.CONST_PLAYERCOUNT == 3:
    			self.players[3].setPalaceCard(self.deck[i])
    	#end for

    	#erase cards used for Palace cards
    	for r in range(self.CONST_PLAYERCOUNT*3):
            self.deck.pop(0)

    	#output player hands for testing
        #TODO: Remove after testing/conversion to graphics
    	for i in range(self.CONST_PLAYERCOUNT):
    		print "Player ", n, "'s palace: "

            for p in range(self.players[i].getPalaceCount()):
                print "Card ", p, " = ", self.players[n].getPalaceCard(p).DisplayCard()

    	#deal initial 6 cards
    	for i in range(self.CONST_PLAYERCOUNT*6):
    		if i % CONST_PLAYERCOUNT == 0:
    			self.players[0].setHandCard(self.deck[i])

    		elif i % CONST_PLAYERCOUNT == 1:
    			self.players[1].setHandCard(self.deck[i])

    		elif i % CONST_PLAYERCOUNT == 2:
    			self.players[2].setHandCard(self.deck[i])

    		elif i % CONST_PLAYERCOUNT == 3:
    			self.players[3].setHandCard(self.deck[i])

    	#erase cards used for initial deal
        for r in range(self.CONST_PLAYERCOUNT*6):
            self.deck.pop(0)

        #move remaining cards to drawpile
    	self.drawPile = self.deck
    	self.deck = []
    #end DealGame

    def ChooseTopOfPalace(self):
    	cardChoice = 0
        counter = 0

        while True:
    		while counter < 3:
    			print "%s Please choose number corresponding to the card you would like to be ontop of your palace: " % self.players[self.turn].getName()
    			print "Current Cards: "

    			for i in range(self.players[self.turn].getHandCount()):
    				print i, ". "
                    self.players[self.turn].getHandCard(i).DisplayCard()

    			cardChoice = raw_input("Choose TopOfPalace Card ", counter, ": ")

    			if cardChoice < 0 or cardChoice >= self.players[self.turn].getHandCount():
    				print "INVALID OPTION"
                    #so that it has the user retry adding a topofpalace card
    				counter--

    			elif cardChoice >= 0 and cardChoice < self.players[self.turn].getHandCount():
    				self.players[self.turn].setTopOfPalace(self.players[self.turn].getHandCard(cardChoice))
    				self.players[self.turn].removeHandCard(cardChoice)
                #increment counter
    			counter++

            #reset to 0 so that it starts fresh for each player
    		counter = 0
            #increment the global turn variable
    		IncrementTurn()

            #test to break the outer while loop
            if turn == 0:
                break

    	print "****** PRINTING TOP OF PALACE CARDS FOR EACH PLAYER:******"
        #TODO: maybe adjust to get actual player object instead of length of players array
    	for p in range(len(self.players)):
    		print "Top Of Palace Cards for Player " , p, ":"
    		print "Card 1:"
    		self.players[p].getTopOfPalaceCard(0).DisplayCard()

    		print "Card 2:"
    		self.players[p].getTopOfPalaceCard(1).DisplayCard()

    		print "Card 3:"
    		self.players[p].getTopOfPalaceCard(2).DisplayCard()

    def PlayGame(self):
        print "!!!!!!!!Current turn: %s" % turn

    	while !gameover:
    		print self.players[self.turn].getName() << " It's you're turn!"
    		if self.players[self.turn].getHandCount() == 0 and len(self.drawPile == 0):
    			if self.players[self.turn].getTopOfPalaceCount() != 0:
                    #may need to be adjusted to make topofpalace its own thing instead of being assigned to hand
                    #this is because of how graphics will display everything -- not sure yet
    				self.players[self.turn].setHand(self.players[self.turn].getTopOfPalace())

    			elif self.players[self.turn].getPalaceCount() != 0:
    				PlayFromPalace()
                else:
                    print "Potential Issue in PlayGame -- No cards to play?"
            #end if
    		PlayCard()

        	#check drawPile size here to a unneeded function calls
    		if len(self.drawPile) != 0):
    			DrawCards(turn)


    		if(self.players[self.turn].getHandCount() == 0 and self.players[self.turn].getTopOfPalaceCount() == 0 and self.players[self.turn].getPalaceCount() == 0 and len(self.drawPile == 0)):
    			print "A winner has been decided! Congradulations Player %s" self.players[self.turn].getName()
    			gameover = True
    		else:
    			IncrementTurn()
        #end while loop
    	if gameover:

    		print "Thank you for playing Palace Card Game"

    	else:
    		print "WTF WHY AM I RUNNING.. THIS IS BS.. I QUIT LIFE"
    #end PlayGame

    def DrawCards(self):
        if len(self.drawPile) != 0:
            #TODO: convert forloop to python
            for(int i=0 i<3-players[turn].getHandCount() i++):
                self.players[self.turn].setHandCard(self.drawPile[len(self.drawPile) - 1])

                #TODO: possibly incase in whileloop incase multiple cards are drawn of same rank
    			if self.drawPile[len(self.drawPile) - 1].getRank() == self.midPile.back().getRank()):
    				print "You drew a card with the same rank as what was just played, it has been played for you! You draw again."  # may need to adjust and give option
                    #todo: still need?
    				if(len(self.drawPile) != 0:
                        print ""

                #needs testing to make sure card removed properly
    			self.drawPile.pop()


    	elif len(self.drawPile) == 0:
    		print "DrawPile is Empty!"

    	else:
    		print "Something went wrong IN DrawCard"

    #end DrawCards

    def PickUpMidPile(self):
        self.players[self.turn].setHand(self.midPile)
    	midPile = []
        #make sure midpile cleared
    	if len(self.midPile) != 0:
            print "Error in PickUpMidPile"

    #end PickUpMidPile

    def PlayCard(self):
        #TODO:May move functionality to playGame and make PlayCard simply add card to midPile
    	cardChoice
    	turnOver = False

    	while !turnOver:
    		self.players[self.turn].DisplayHand()
    		cardChoice = raw_input("Choose a card to Play")

    		while cardChoice < 0 or cardChoice >= self.players[self.turn].getHandCount():
                cardChoice = raw_input("Please enter a valid choice: ")

    		if isPlayable(self.players[self.turn].getHandCard(cardChoice)):
    			playersCard = Card()
    			self.midPile.append(self.players[self.turn].getHandCard(cardChoice))
    			playersCard = self.players[self.turn].getHandCard(cardChoice)
    			self.players[self.turn].removeHandCard(cardChoice)

    			if isWildCard(playersCard):
    				PlayWildCard(playersCard)

    			elif CheckMultiple(playersCard):
    				playMultiple(playersCard)

    			else:
    				print "Next players turn!"
                    turnOver = True
            # end if
    		else:
    			print "You have selected a card that is unable to be played, please choose again"

    #end PlayCard

#maybe can be adjusted to just return the # of the current turn instead of the entire player?
Player def CurrentTurn(self):

	return self.players[self.turn]


def IncrementTurn(self):

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


