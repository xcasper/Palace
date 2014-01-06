//PalaceGame.h
//Created by Craig Gleckman
#ifndef PALACEGAME_H
#define PALACEGAME_H

#include "Player.h"
#include <iostream>
#include <ctime>

class PalaceGame
{
public:
	PalaceGame();
	~PalaceGame();
	void setupGame(const int PLAYERCOUNT);
	void CreatePlayers(const int PLAYERCOUNT, vector<Player> &players, const int DEALER);
	void CreateDeck(vector<Card> &);
	void ShuffleDeck(vector<Card> &deck);
	void DealGame(const int PLAYERCOUNT);
	//void OrderOfPlay(const int PLAYERCOUNT);
	void ChooseTopOfPalace(vector<Player> &players);
	void PlayGame(const int PLAYERCOUNT);
	void DrawCards(const int turn);
	void PickUpMidPile();
	void PlayCard();
	Player CurrentTurn();
	void IncrementTurn();
	bool CheckMultiple(Card &card);
	bool isPlayable(Card &card);
	bool isWildCard(Card &card);
	void playMultiple(Card &playersCard);
	void PlayWildCard(Card &wildCard);
	void PlayFromPalace();
private:
	vector<Card> deck, drawPile, midPile, deadPile;
	vector<Player> players;
	Player playerOne;
	Player playerTwo;
	Player playerThree;
	Player playerFour;
	int turn, dealer;
	bool gameover;
};

#endif