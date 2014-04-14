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
from random import randrange
from Card import Card
from Player import Player

class PalaceGame(object):

    def __init__(self):
        #Initialize all variables
    	self.turn = 0
    	self.gameover = False

    	self.numPlayers = 0
        self.CONST_PLAYERCOUNT = 0
        self.dealer = 0

        self.players = []
        self.deck = []
        self.drawpile = []
        self.midPile = []
        self.deadPile = []

        self.playerOne = Player()
        #playerOne.setName("Craig")
        assert type(self.playerOne) == type(Player())
        self.playerTwo = Player()
        self.playerThree = Player()
        self.playerFour = Player()

        print "Name: %s" % self.playerOne.getName()

    	self.setupGame()

    def setupGame(self):

        #get player count
        #numPlayers not being set
    	self.numPlayers = int(raw_input("How many players? (Enter 2-4):"))
        print "NumPlayers 1: ", (self.numPlayers < 2) or (self.numPlayers > 4)

    	#check valid num players
        #For some reason does not accept 2-4 as valid?
       	while (self.numPlayers < 2) or (self.numPlayers > 4):
            print "NumPlayers 2: ", (self.numPlayers < 2) or (self.numPlayers > 4)
            self.numPlayers = int(raw_input("Please enter a valid number of Players (2-4):"))

    	#save numPlayers to const variable so it doesnt ever get modified
    	self.CONST_PLAYERCOUNT = self.numPlayers

    	#set dealer
    	r = randrange(self.CONST_PLAYERCOUNT)
        #TODO: Ask Charlie: How do i do the range? Confused | tried without 0 as well
        self.dealer = r

        #Confirm valid player amount
    	if self.CONST_PLAYERCOUNT >= 2 and self.CONST_PLAYERCOUNT <= 4:
            print "Palace Card Game Loading..."
            #Allows each player to pick a name
            self.CreatePlayers()

            #Make sure that players array (setup in CreatePlayers) worked
            if len(self.players) == self.CONST_PLAYERCOUNT:
                print "CreatePlayers ran successfully"
                self.CreateDeck() #forms the 52 card deck

    			#Make sure deck was created properly (52 cards)
                if len(self.deck) == 52:
                    print "CreateDeck ran successfully"
                    self.ShuffleDeck() #randomizes the deck (when created it is created in rank and suit order)

                    #Recheck deck size to make sure shuffle did not mess anything up
                    if len(self.deck) == 52:
                        #why does python think this is an error
                        #print "ShuffleDeck ran successfully"
                        self.DealGame() #Gives each player 3 palace cards and then 6 cards to start with

                        #Make sure each player has 6 cards in his/her hand at start
                        for player in range(len(self.players)):
                            if self.players[player].getHandCount() != 6:
                                print "Something went wrong WITH DealGame **"
                                #TODO: does this break belong?
                                break
    				        #end if
    					 #end for

                        self.ChooseTopOfPalace() #Asks each player which 3 cards from their hand they would like to use for the OnTopOfPalace cards

    					#Make sure each player has 3 cards left after choosing top of palace
                        for player in range(len(self.players)):
                            if self.players[player].getTopOfPalaceCount() != 3:
                                print "Something went wrong WITH TOPOFPALACE **"
                                #TODO: Does this break belong?
                                break
    						#end if
    					#end for

                        self.PlayGame() #Starts with player to the left of the dealer

    					#Gameover should be true after playgame is finished
                        if gameover == False:
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
            input = str(raw_input("Please give a name to Player1: "))
            #why does this throw an assert error when I give my name?
            #assert type(input) == type(str)
            self.playerOne.setName(input)

            input = str(raw_input("Please give a name to Player2: "))
            #assert type(input) == type(str())
            print "Input 2: ", type(input), type(str())
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

            print "Players Total: ", len(self.players)
            for player in range(len(self.players)):
            	print self.players[player].getName()
            #end if

    	elif self.CONST_PLAYERCOUNT == 3:
            input = str(raw_input("Please give a name to Player1: "))
            print "Input: ", type(input)
            #assert type(input) == type(str())
            self.playerOne.setName(input)

            input = str(raw_input("Please give a name to Player2: "))
            assert type(input) == type(str())
            self.playerTwo.setName(input)

            input = str(raw_input("Please give a name to Player3: "))
            assert type(input) == type(str())
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
            assert type(input) == type(str)
            self.playerOne.setName(input)

            input = raw_input("Please give a name to Player2: ")
            assert type(input) == type(str)
            self.playerTwo.setName(input)

            input = raw_input("Please give a name to Player3: ")
            assert type(input) == type(str)
            self.playerThree.setName(input)

            input = raw_input("Please give a name to Player4: ")
            assert type(input) == type(str)
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

    def CreateDeck(self):
    	#Create cards 2 - 14 since no cards in a regular deck of cards have a rank 0 or 1 (11 = jack | 12 = queen | 13 = king | 14 = ace)
    	for r in range(2, 15):
            print "Create Deck R:", r
            for s in range(1, 5):
                print "Create Deck S:", s
                if s==1:
                    card = Card(r, 'C')
                    print "test r/s: ", card.getRank(), card.getSuit()
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
                    card = Card(r, 'D')
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
                assert type(cardCheck) == type(Card())
    			#Test cardCheck against entire deck
                for n in range(len(self.deck)):
                    if cardCheck.getRank() == self.deck[n].getRank() and cardCheck.getSuit() == self.deck[n].getSuit() and num != n:
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

    def ShuffleDeck(self):

    	#Declare local variables
    	tempCard = Card()
    	r1 = 0.00
        r2 = 0.00
        r3 = 0.00

    	#Confirm deck size has not changed yet
    	if len(self.deck) == 52:
            for num in range(52):
                #r = randrange(self.CONST_PLAYERCOUNT)
                r1 = randrange(0, 52)
                print "R1:", r1
                r2 = randrange(0, 52)
                print "R1:", r2
                r3 = randrange(0, 52)
                print "R1:", r3

                tempCard = self.deck[num]
                self.deck[num] = self.deck[r1]
                self.deck[r1] = self.deck[r2]
                self.deck[r2] = self.deck[r3]
                self.deck[r3] = tempCard
    		#end for
    	#end if

    	else:
    		print "Something went wrong IN ShuffleDeck ** DECK != 52 **"
    	#end else
    #end ShuffleDeck

    def DealGame(self):
    	#deal palace cards
    	for i in range(self.CONST_PLAYERCOUNT*3):
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
    	for n in range(self.CONST_PLAYERCOUNT):
            print "Player ", n, "'s palace: "

            for p in range(self.players[n].getPalaceCount()):
                print "Card ", p, " = ", self.players[n].getPalaceCard(p).DisplayCard()

    	#deal initial 6 cards
    	for i in range(self.CONST_PLAYERCOUNT*6):
    		if i % self.CONST_PLAYERCOUNT == 0:
    			self.players[0].setHandCard(self.deck[i])

    		elif i % self.CONST_PLAYERCOUNT == 1:
    			self.players[1].setHandCard(self.deck[i])

    		elif i % self.CONST_PLAYERCOUNT == 2:
    			self.players[2].setHandCard(self.deck[i])

    		elif i % self.CONST_PLAYERCOUNT == 3:
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
                print "Current Cards: "
                print "%s Please choose number corresponding to the card you would like to be ontop of your palace: " % self.players[self.turn].getName()

                for i in range(self.players[self.turn].getHandCount()):
                    print i, ". "
                    self.players[self.turn].getHandCard(i).DisplayCard()

                cardChoice = int(raw_input("Choose TopOfPalace Card: "))
                print "CardChoice 1: ", (cardChoice < 2), (cardChoice >= self.players[self.turn].getHandCount())
                print "CardChoice 2: ", (cardChoice < 2) or (cardChoice >= self.players[self.turn].getHandCount())
                if (cardChoice < 0) or (cardChoice >= self.players[self.turn].getHandCount()):
                    print "INVALID OPTION"
                    #so that it has the user retry adding a topofpalace card
                    counter -= 1

                elif cardChoice >= 0 and cardChoice < self.players[self.turn].getHandCount():
                    self.players[self.turn].setTopOfPalace(self.players[self.turn].getHandCard(cardChoice))
                    self.players[self.turn].removeHandCard(cardChoice)
                    #increment counter
                    counter += 1

            #reset to 0 so that it starts fresh for each player
            counter = 0
            #increment the global turn variable
            self.IncrementTurn()

            #test to break the outer while loop
            if self.turn == 0:
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
        print "!!!!!!!!Current turn: %s" % self.turn

    	while self.gameover == False:
    		print self.players[self.turn].getName(), "It's you're turn!"
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
    		self.PlayCard()

        	#check drawPile size here to a unneeded function calls
    		if len(self.drawPile) != 0:
    			self.DrawCards()


    		if(self.players[self.turn].getHandCount() == 0 and self.players[self.turn].getTopOfPalaceCount() == 0 and self.players[self.turn].getPalaceCount() == 0 and len(self.drawPile == 0)):
    			print "A winner has been decided! Congradulations Player %s" % self.players[self.turn].getName()
    			self.gameover = True
    		else:
    			self.IncrementTurn()
        #end while loop
    	if self.gameover:

    		print "Thank you for playing Palace Card Game"

    	else:
    		print "WTF WHY AM I RUNNING.. THIS IS BS.. I QUIT LIFE"
    #end PlayGame

    def DrawCards(self):
        if len(self.drawPile) != 0:
            #TODO: convert forloop to python
            for i in range(3-self.players[self.turn].getHandCount()):
                self.players[self.turn].setHandCard(self.drawPile[len(self.drawPile) - 1])

                #TODO: possibly encase in whileloop incase multiple cards are drawn of same rank
                if self.drawPile[len(self.drawPile) - 1].getRank() == self.midPile[-1].getRank():
                    print "You drew a card with the same rank as what was just played, it has been played for you! You draw again."  # may need to adjust and give option
                    #todo: still need?

                    if len(self.drawPile) != 0:
                        DrawCards()
                    else:
                        print "Sorry! There are no more cards in the drawPile"

                #needs testing to make sure card removed properly
                if len(self.drawPile) != 0:
                    self.drawPile.pop()

            return 0

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
        playersCard = Card()
        cardChoice = -1
    	turnOver = False

    	while turnOver == False:
            self.players[self.turn].DisplayHand()
            cardChoice = int(raw_input("Choose a card to Play"))

            while cardChoice < 0 or cardChoice >= self.players[self.turn].getHandCount():
                cardChoice = raw_input("Please enter a valid choice: ")

            if self.isPlayable(self.players[self.turn].getHandCard(cardChoice)):
                self.midPile.append(self.players[self.turn].getHandCard(cardChoice))
                playersCard = self.players[self.turn].getHandCard(cardChoice)
                self.players[self.turn].removeHandCard(cardChoice)

                if self.isWildCard(playersCard):
    				self.PlayWildCard(playersCard)

                elif self.CheckMultiple(playersCard):
    				self.playMultiple(playersCard)

                else:
                    print "Next players turn!"
                    turnOver = True
            # end if
            else:
    			print "You have selected a card that is unable to be played, please choose again"

    #end PlayCard

    #TODO: maybe can be adjusted to just return the # of the current turn instead of the entire player?
    def CurrentTurn(self):
        return self.players[self.turn]

    #end CurrentTurn

    def IncrementTurn(self):
    	if self.turn == len(self.players)-1:
    		self.turn = 0

    	elif self.turn == 0 or self.turn == 1 or self.turn == 2:
    		self.turn += 1

    	else:
    		print "Something went wrong IN IncrementTurn"

    #end IncrementTurn

    def CheckMultiple(self, card):
        assert type(card) == type(Card())
    	for i in range(self.players[self.turn].getHandCount()):
    		if card.getRank() == self.players[self.turn].getHandCard(i).getRank():
    			return True

    	return False

    #end CheckMultiple

    def isPlayable(self, card):
        assert type(card) == type(Card())
        if len(self.midPile) == 0:
    		return True

    	elif card.getRank() >= self.midPile[-1].getRank() or self.isWildCard(card):
    		return True

        else:
    		return False

    #end isPlayable


    def isWildCard(self, card):
        assert type(card) == type(Card())
    	if(card.getRank() == 2 or card.getRank() == 10):
    		return True

    	else:
    		return False

    #end isWildCard

    def playMultiple(self, playersCard):

        multiCardPlayInput = 0

    	print "Would you like to play cards of the same rank?"
    	multiCardPlayInput = int(raw_input( "1. Yes, all! \n 2. Yes, but not all! \n 3. No."))

    	while multiCardPlayInput < 1 or multiCardPlayInput > 3:
    	    multiCardPlayInput = int(raw_input( "Please enter a valid choice: "))

    	if multiCardPlayInput == 1:
    		for i in range(self.players[self.turn].getHandCount()):
    			if self.players[self.turn].getHandCard(i).getRank() == playersCard.getRank():
    				self.midPile.append(self.players[self.turn].getHandCard(i))
    				self.players[self.turn].removeHandCard(i)
    	elif multiCardPlayInput == 2:
            while CheckMultiple(playersCard):
                self.players[self.turn].DisplayHand()
                multiCardPlayInput = int(raw_input("Please choose a card with the same rank to play(Type 123 to quit): "))

                if multiCardPlayInput == 123:
    				break

                else:
                    if self.players[self.turn].getHandCard(multiCardPlayInput).getRank() == playersCard.getRank():
    					self.midPile.append(self.players[self.turn].getHandCard(multiCardPlayInput))
    					self.players[self.turn].removeHandCard(multiCardPlayInput)

                    elif self.players[self.turn].getHandCard(multiCardPlayInput).getRank() != playersCard.getRank():
                        print "Please choose a Card with the rank: %s" % playersCard.getRank()

                    else:
    					print "Something went horribly wrong in PlayCard() ** multiCardPlayInput case 2**"

    	elif multiCardPlayInput == 3:
            Quit()

    #end playMultiple

    def PlayWildCard(self, wildCard):
        assert type(wildCard) == type(Card())

    	wildCardChoice = -1

        while self.isWildCard(wildCard):
            if wildCard.getRank() == 2:

                self.midPile.append(wildCard)
                print "You played a 2, please play another card... You may play anything!"
                self.players[self.turn].DisplayHand()
                wildCardChoice = int(raw_input("Choice: "))

                while wildCardChoice < 0 or wildCardChoice >= self.players[self.turn].getHandCount():
    				wildCardChoice = int(raw_input("Please enter a valid choice: "))

                wildCard = self.players[self.turn].getHandCard(wildCardChoice)

                if isWildCard(wildCard):
    				print "You have selected another wild card"
    				self.players[self.turn].removeHandCard(wildCardChoice)

                elif isWildCard(wildCard) == True and wildCard.getRank() >= self.midPild[-1].getRank():
    				self.midPile.append(wildCard)
    				self.players[self.turn].removeHandCard(wildCardChoice)

                else:
                    print "Something went terribly wrong in PlayWildCard ** not additional wild card **"
            elif wildCard.getRank() == 10:
                self.midPile.append(wildCard)

                self.deadPile = self.midPileself
                self.midPile = []

                if len(self.deadPile) != 0 and len(self.midPile) == 0:

                    print "You played a 10, please play another card... You may play anything!"
                    self.players[self.turn].DisplayHand()
                    wildCardChoice = int(raw_input("Choice: "))

                    while wildCardChoice < 0 or wildCardChoice >= self.players[self.turn].getHandCount():
    					wildCardChoice = int(raw_input("Please enter a valid choice: "))

                    wildCard = self.players[self.turn].getHandCard(wildCardChoice)

                    #additional wild card may not be being played?
                    if isWildCard(wildCard):
                        print "You have selected another wild card"
                        #add?: self.midPile.append(wildCard)
                        self.players[self.turn].removeHandCard(wildCardChoice)

                    else:
                        self.midPile.append(wildCard)
                        self.players[self.turn].removeHandCard(wildCardChoice)

                    if self.CheckMultiple(wildCard):
    						self.playMultiple(wildCard)

                else:
    				print "Something went terribly wrong in PlayWildCard ** rank = 10 **"

    #end playWildCard

    def PlayFromPalace(self):
        palaceCardChoice
        playersCard

    	print "You have %s palace cards." % self.players[self.turn].getPalaceCount()
    	print "Please choose one of your remaining palace cards to play"
    	palaceCardChoice = raw_input("Choice: ")

    	while palaceCardChoice < 0 or palaceCardChoice > self.players[self.turn].getPalaceCount():
    		palaceCardChoice = raw_input("Please enter a valid choice: ")

    	if isPlayable(self.players[self.turn].getHandCard(palaceCardChoice)):
            self.midPile.append(self.players[selfturn].getHandCard(palaceCardChoice))
            playersCard = self.players[self.turn].getHandCard(palaceCardChoice)
            players[self.turn].removeHandCard(palaceCardChoice)

            if isWildCard(playersCard):
    			PlayWildCard(playersCard)

            elif CheckMultiple(playersCard):
                playMultiple(playersCard)

            else:
    			print "Next players turn!"

    	elif self.players[self.turn].getHandCard(palaceCardChoice).getRank() < self.midPile[-1].getRank():
            self.players[self.turn].setHand(self.midPile)
            self.midPile = []

    #end PlayFromPalace