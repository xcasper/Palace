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
from Card import Card

class Player(object):

    def __int__(self):
        #Initialize private variables
        #Create control Card for monitoring
        controlCard = Card()
        controlCard.setRank(999)
        controlCard.setSuit('U')
        playerNum = -1337
        name = "NOT SET"
        palace = []
        topOfPalace = []
        #code: type(var) -- will give type of whatever is between ()
        #code: assert type(var) == type(Card())
        hand = [Card(), Card()]

    def getPlayerNum(self):
        return self.playerNum

    def setPlayerNum(self, CONST_PLAYERNUM):
        self.playerNum = CONST_PLAYERNUM

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getPalaceCount(self):
        print "Palace Count: %s" % (len(self.palace))
        return len(self.palace)

    def getPalaceCard(self, pos):
        return self.palace[pos]

    def setPalaceCard(self, card):
        if len(self.palace) > 3:
            print "SOMEHOW IM TO HIGH"
        else:
            self.palace.append(card)

    def getTopOfPalaceCount(self):
        return len(self.topOfPalace)

    def getTopOfPalaceCard(self, pos):
        return self.topOfPalace[pos]

    def getTopOfPalace(self):
        return self.topOfPalace

    def setTopOfPalace(self, CONST_CARD):
        self.topOfPalace.append(CONST_CARD)

    def getHand(self):
        return self.hand

    def setHand(self, cards):
        self.hand = cards

    def getHandCount(self):
        return len(self.hand)

    def getHandCard(self, pos):
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
        self.hand[pos].DisplayCard()
        if pos == len(self.hand) - 1:
            self.hand.pop()
        #requires testing to make sure pop is done right (may not remove intended card)
        elif pos < len(self.hand) - 1:
            hand.pop(pos)
            print "After Remove Card: %s" % (self.hand(pos))
        else:
            print "Something went wrong IN removeHandCard ** ERASE DETERMINATION ** "
    #same error as above: TypeError: 'list' object is not callable -- appears at print
    def DisplayHand(self, hand):
        print "Current Hand: "
        for card in self.hand:
            print card + ". " + hand(card).getRank()
            + " " + hand(card).getSuit()

