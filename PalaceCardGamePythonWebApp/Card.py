#-------------------------------------------------------------------------------
# Name:         Card.py
#
# Purpose:      Allows the creation of a Card via the Card Class.
#               Cards have a rank and suit. Cards created with no params are
#               created with default rank 0 and suit 'N'. The class provides
#               additional functionality such as getting/setting rank and suit.
#               The class also allows you to print out the Cards
#               information(rank/suit)
#
# Author:       Craig Gleckman
#
# Created:      25/03/2014
# Copyright:    (c) Craig 2014
# Licence:      <your licence>
#-------------------------------------------------------------------------------

class Card(object):

    def __init__(self, rank = 0, suit = 'N'):
    	self.rank = rank
    	self.suit = suit

    def getRank(self):
        return self.rank

    def getSuit(self):
        return self.suit

    def setRank(self, rank):
        try:
            int(rank)
        except ValueError:
            print "Rank supplied was not int compatable in setRank in Card"
        if(rank >= 2 or rank >= 14 or rank == 999):
            self.rank = rank
        else:
            print "Invalid Rank was Supplied in setRank in Card"

    def setSuit(self, suit):
        if(len(suit) != 1):
            suit.upper()
            if(suit == "CLUBS"):
                suit = 'C'
            elif(suit == "SPADES"):
                suit = 'S'
            elif(suit == "HEARTS"):
                suit = 'H'
            elif(suit == "DIAMONDS"):
                suit = 'D'
            else:
                print "Invalid Suit was Supplied in setSuit in Card"

        elif(len(suit) == 1 or suit == 'U'):
            self.suit = suit

        else:
            print "Something went seriously wrong in setSuit in Card"

    def DisplayCard(self):
        print "%s%s" % (self.getRank(), self.getSuit())
