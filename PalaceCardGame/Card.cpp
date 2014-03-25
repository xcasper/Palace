//Card.cpp
//Created by Craig Gleckman

#include "Card.h"
//CSHD
Card::Card()
{
	rank = 0;
	suit = 'N';
}

Card::Card(int rank, char suit)
{
	this->rank = rank;
	this->suit = suit;
}

Card::~Card()
{
}

int Card::getRank()
{
	return rank;
}

char Card::getSuit()
{
	return suit;
}

void Card::setRank(int rank)
{
	this->rank = rank; 
}

void Card::setSuit(char suit)
{
	this->suit = suit;
}

void Card::DisplayCard()
{
	cout << getRank() << " " << getSuit() << endl;
}
