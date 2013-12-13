//Card.h
//Created by Craig Gleckman
#ifndef CARD_H
#define CARD_H

#include <iostream>
using namespace std;

class Card
{
public:
	Card();
	Card(int rank, char suit);
	~Card();
	int getRank();
	char getSuit();
	void setRank(int rank);
	void setSuit(char suit);
	void DisplayCard();
private:
	int rank;
	char suit;
};
#endif
