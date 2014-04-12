#-------------------------------------------------------------------------------
# Name:        Player.py
# Purpose:
#
# Author:      Craig Gleckman
#
# Created:     25/03/2014
# Copyright:   (c) Craig 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#Questions for Charlie:
#   1. How to handle the need to make sure things are cards?
#       a. make hand/palace/topofpalace into own objects
#       b. Put checks in setters (and getters for double checking?)
#       c. ????
#   2. Can I grab the assert if it fails and do something with it? EX: if assert false do something?
from Card import Card

class Player(object):

    def __int__(self):
        #Initialize private variables
        #Create control Card for monitoring
        controlCard = Card()
        controlCard.setRank(999)
        controlCard.setSuit('U')
        CONST_PLAYERNUM = -1337
        name = "NOT SET"
        palace = []
        topOfPalace = []
        #code: type(var) -- will give type of whatever is between ()
        #code: assert type(var) == type(Card())
        hand = []

    def getPlayerNum(self):
        return self.playerNum

    def setPlayerNum(self, playerNum):
        if self.CONST_PLAYERNUM == -1337:
            assert type(playerNum) == type(int)
            self.CONST_PLAYERNUM = playerNum
        else:
            print "Error in setPlayerNum: Attempting to change player number after initial set"

    def getName(self):
        if self.name != "NOT SET":
            return self.name
        else:
            print "Error in getName: Name has not yet been set"

    def setName(self, name):
        if self.name == "NOT SET":
            #add while loop till passes assert
            try:
                assert type(name) == type(str)
            except AssertionError:
                #determine type and if callable turn to string
                print "Assert failed in setName"
            self.name = name
        else:
            print "Error in setName: Name has already been set"

    def getPalaceCount(self):
        print "Palace Count: %s" % (len(self.palace))
        return len(self.palace)

    def getPalaceCard(self, pos):
        assert type(pos) == type(int)
        if type(self.palace[pos]) == type(Card()):
            return self.palace[pos]
        #add further functionality to deal with errors: Convert to Card if possible?
        else:
            print "Error in getPalaceCard: Item stored in palace is not a CARD"

    def setPalaceCard(self, card):
        assert type(card) == type(Card())
        if len(self.palace) > 0 and len(self.palace) < 4:
            self.palace.append(card)
        else:
            print "Error in setPalaceCard: To to many/little amount of cards in Palace"

    def getTopOfPalaceCount(self):
        return len(self.topOfPalace)

    def getTopOfPalaceCard(self, pos):
        assert type(pos) == type(int)
        assert type(self.topOfPalace[pos]) == type(Card())
        return self.topOfPalace[pos]

    def getTopOfPalace(self):
        return self.topOfPalace

    def setTopOfPalace(self, CONST_CARD):
        assert type(CONST_CARD) == type(Card())
        self.topOfPalace.append(CONST_CARD)

    def getHand(self):
        return self.hand

    def setHand(self, cards):
        for card in cards:
            assert type(card) == type(Card())
            self.hand.append(cards)

    def getHandCount(self):
        return len(self.hand)

    def getHandCard(self, pos):
        assert type(pos) == type(int)
        return self.hand[pos]

    #throws error: TypeError: 'list' object is not callable --
    #appears at if Statement
    def getHighestHandCard(self):
        highestCard = self.hand[0]
        print highestCard
        for pos in range(len(self.hand)):
            if self.hand[pos].getRank() > highestCard.getRank():
                highestCard = self.hand(card)
                return highestCard

    def setHandCard(self, card):
        assert type(card) == type(Card())
        self.hand.append(card)

    def removeHandCard(self, pos):
        assert type(pos) == type(int)
        self.hand[pos].DisplayCard()
        if pos == len(self.hand) - 1:
            self.hand.pop()
        #requires testing to make sure pop is done right (may not remove intended card)
        elif pos < len(self.hand) - 1:
            hand.pop(pos)
            print "After Remove Card: %s" % (self.hand[pos].DisplayCard())
        else:
            print "Something went wrong IN removeHandCard ** ERASE DETERMINATION ** "
    #same error as above: TypeError: 'list' object is not callable -- appears at print
    def DisplayHand(self, hand):
        print "Current Hand: "

        for card in self.hand:
            print card.DisplayCard()

