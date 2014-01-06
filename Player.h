//Player.h
//Created by Craig Gleckman
#ifndef PLAYER_H
#define PLAYER_H

#include "Card.h"
#include <vector>
#include <string>

class Player
{
public:
	Player();
	~Player();
	int getPlayerNum();
	void setPlayerNum(const int playerNum);
	string getName();
	void setName(string name);
	int getPalaceCount();
	Card getPalaceCard(int pos);
	void setPalaceCard(Card card);
	int getTopOfPalaceCount();
	Card getTopOfPalaceCard(int pos);
	vector<Card> getTopOfPalace();
	void setTopOfPalace(const Card CARD);
	vector<Card> getHand();
	void setHand(vector<Card> &cards);
	int getHandCount();
	Card getHandCard(int pos);
	Card getHighestHandCard();
	void setHandCard(Card card);
	void removeHandCard(int pos);
	void DisplayHand();
	
	
private:
	int playerNum;
	string name;
	vector<Card> palace; 
	vector<Card> topOfPalace;
	vector <Card>hand;
};


#endif