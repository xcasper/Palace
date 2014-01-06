//Player.cpp
// Created by Craig Gleckman
#include "Player.h"
#include <iostream>

Player::Player()
{
	//Initialize private variables
	//Create control Card for monitoring
	Card controlCard;
	controlCard.setRank(999);
	controlCard.setSuit('U');

	playerNum = -1337;
	name = "NOT SET";

	palace, topOfPalace, hand;
	
	/* KEEP UNTIL I know i dont need to revert palace and topOfPalace to arrays
	//Initialize palace and topOfPalace arrays
	//Intial cards are all control cards for monitoring
	palace[0].push_back(controlCard);
	palace[1] = controlCard;
	palace[2] = controlCard;
	topOfPalace[0] = controlCard;
	topOfPalace[1] = controlCard;
	topOfPalace[2] = controlCard;*/
}

Player::~Player()
{
}

int Player::getPlayerNum()
{
	return playerNum;
}

void Player::setPlayerNum(const int PLAYERNUM)
{
	this->playerNum = PLAYERNUM;
}

string Player::getName()
{
	return name;
}

void Player::setName(string name)
{
	this->name = name;
}

int Player::getPalaceCount()
{
	cout << "Palace Count: " << palace.size() << endl;
	return palace.size();
}

Card Player::getPalaceCard(int pos)
{
	return palace[pos];
}

void Player::setPalaceCard(Card card)
{
	if(palace.size() > 3)
	{
		cout << "SOMEHOW IM TO HIGH" << endl;
	}
	else
		palace.push_back(card);
}

int Player::getTopOfPalaceCount()
{
	return topOfPalace.size();
}

Card Player::getTopOfPalaceCard(int pos)
{
	return topOfPalace[pos];
}

vector<Card> Player::getTopOfPalace()
{
	return topOfPalace;
}

void Player::setTopOfPalace(const Card CARD)
{
	topOfPalace.push_back(CARD);
}

vector<Card> Player::getHand()
{
	return hand;
}

void Player::setHand(vector<Card> &cards)
{
	hand = cards;
}

int Player::getHandCount()
{
	return hand.size();
}

Card Player::getHandCard(int pos)
{	
	return hand[pos];
}

Card Player::getHighestHandCard()
{
	Card highestCard = hand[0];
	for(int i=1; i<=hand.size(); i++)
	{
		if(hand[i].getRank() > highestCard.getRank())
		{
			highestCard = hand[i];
		}
	}
	return highestCard;
}

void Player::setHandCard(Card card)
{
	hand.push_back(card);
}

void Player::removeHandCard(int pos)
{

	hand[pos].DisplayCard();
	cout << endl;
	if(pos == hand.size()-1)
	{
		hand.pop_back();
		hand[pos-1].DisplayCard();
		cout << endl;
	}
	else if(pos < hand.size()-1)
	{
		hand.erase(hand.begin()+pos);
		cout << "After Remove Card: ";
		hand[pos].DisplayCard(); 
		cout << endl;
	}
	else
	{
		cout << "Something went wrong IN removeHandCard ** ERASE DETERMINATION ** " << endl;
	}
}

void Player::DisplayHand()
{
	cout << "Current Hand: " << endl;

	for(int i=0; i<hand.size(); i++)
	{
		cout << i << ". " << hand[i].getRank() 
			<< " " << hand[i].getSuit() << endl;
	}
}