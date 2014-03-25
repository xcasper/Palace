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
from card import Card

class Player(object):

    def Player(self):
        #Initialize private variables
        #Create control Card for monitoring
        controlCard = Card()
        controlCard.setRank(999)
        controlCard.setSuit('U')
        playerNum = -1337
        name = "NOT SET"
        palace =[]
        topOfPalace = []
        hand = []

    ''' KEEP UNTIL I know i dont need to revert palace and topOfPalace to arrays
    #Initialize palace and topOfPalace arrays
    #ial cards are all control cards for monitoring
    palace[0].push_back(controlCard)
    palace[1] = controlCard
    palace[2] = controlCard
    topOfPalace[0] = controlCard
    topOfPalace[1] = controlCard
    topOfPalace[2] = controlCard'''

    def getPlayerNum():
        return playerNum


    def setPlayerNum(CONST_PLAYERNUM):
        self.playerNum = CONST_PLAYERNUM


    def getName():
        return name


    def setName(name):
        self.name = name


    def getPalaceCount():
        print "Palace Count: %s" % (len(palace))
        return len(palace)

    def getPalaceCard(pos):
        return palace[pos]

    def setPalaceCard(card):
        if(palace.size() > 3):
            print "SOMEHOW IM TO HIGH"
        else:
            palace.append(card)

    def getTopOfPalaceCount():
        return len(topOfPalace)

    def getTopOfPalaceCard(pos):
        return topOfPalace[pos]


    def getTopOfPalace():
        return topOfPalace


    def setTopOfPalace(CONST_CARD):
        topOfPalace.push_back(CONST_CARD)


    def getHand():
        return hand


    def setHand(cards):
        hand = cards


getHandCount()

return hand.size()


Card getHandCard( pos)

return hand[pos]


Card getHighestHandCard()

Card highestCard = hand[0]
for( i=1 i<=hand.size() i++)

if(hand[i].getRank() > highestCard.getRank())

highestCard = hand[i]


return highestCard


void setHandCard(Card card)

hand.push_back(card)


void removeHandCard( pos)


hand[pos].DisplayCard()
cout << endl
if(pos == hand.size()-1)

hand.pop_back()
hand[pos-1].DisplayCard()
cout << endl

else if(pos < hand.size()-1)

hand.erase(hand.begin()+pos)
cout << "After Remove Card: "
hand[pos].DisplayCard()
cout << endl

else

cout << "Something went wrong IN removeHandCard ** ERASE DETERMINATION ** " << endl



void DisplayHand()

cout << "Current Hand: " << endl

for( i=0 i<hand.size() i++)

cout << i << ". " << hand[i].getRank()
<< " " << hand[i].getSuit() << endl

