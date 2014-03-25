//PalaceGame.cpp

/* Notes:
First Refactoring: combine if/else statements that were seperated for error testing

Current Objective:

Created by Craig Gleckman
*/

#include "PalaceGame.h"

PalaceGame::PalaceGame()
{
	//Initialize all variables
	turn = 0;
	gameover = false;
        //
	//declare local variables
	int numPlayers;

	//get player count
	cout << "How many players? (Enter 2-4)" << endl;
	cin >> numPlayers;

	//check valid num players
	while(numPlayers < 2 || numPlayers > 4)
	{
		cout << "Please enter a valid number of Players (2-4)" << endl;
		cin >> numPlayers;
	}

	//save numPlayers to const variable so it doesnt ever get modified
	const int PLAYERCOUNT = numPlayers;
	
	//set dealer
	srand(time(NULL));
	int r = rand() % PLAYERCOUNT;
	dealer = r;

	setupGame(PLAYERCOUNT);
}

PalaceGame::~PalaceGame()
{
}

void PalaceGame::setupGame(const int PLAYERCOUNT)
{
	//Confirm valid player amount
	if(PLAYERCOUNT >= 2 && PLAYERCOUNT <= 4)
	{
		cout << "Palace Card Game Loading..." << endl;

		//Allows each player to pick a name
		CreatePlayers(PLAYERCOUNT, players,  dealer);
		
		//Make sure that players array (setup in CreatePlayers) worked
		if(players.size() == PLAYERCOUNT)
		{
			cout << "CreatePlayers ran successfully" << endl;
			CreateDeck(deck); //forms the 52 card deck

			//Make sure deck was created properly (52 cards)
			if(deck.size() == 52)
			{
				cout << "CreateDeck ran successfully" << endl;
				ShuffleDeck(deck); //randomizes the deck (when created it is created in rank and suit order)

				//Recheck deck size to make sure shuffle did not mess anything up
				if(deck.size() == 52)
				{
					cout << "ShuffleDeck ran successfully" << endl;
					DealGame(PLAYERCOUNT); //Gives each player 3 palace cards and then 6 cards to start with
					
					//Make sure each player has 6 cards in his/her hand at start
					for(int i=0; i<PLAYERCOUNT; i++)
					{
						if(players[i].getHandCount() != 6)
						{
							cout << "Something went wrong WITH DealGame **" << endl;
							break;
						} //end if
					} //end for
					ChooseTopOfPalace(players); //Asks each player which 3 cards from their hand they would like to use for the OnTopOfPalace cards
					
					//Make sure each player has 3 cards left after choosing top of palace
					for(int i=0; i<PLAYERCOUNT; i++)
					{
						if(players[i].getTopOfPalaceCount() != 3)
						{
							cout << "Something went wrong WITH TOPOFPALACE **" << endl;
							break;
						}//end if
					}//end for
					PlayGame(PLAYERCOUNT); //Starts with player to the left of the dealer

					//Gameover should be true after playgame is finished
					if(!gameover)
					{
						cout << "Something went wrong WITH playGame" << endl;
					}

					else
					{
						cout << "Good-Bye!" << endl;
					}
	
				}//end if
				else
				{
					cout << "Something went wrong WITH ShuffleDeck" << endl;
				}//end else
				
			}//end if
			else
			{
				cout << "Something went wrong WITH CreateDeck" << endl;
			}//end else
		}//end if
		else
		{
			cout << "something went wrong WITH CreatePlayers" << endl;
		}//end else
	}
	else
	{
	cout << "Palace Card Game Loaded Successfully!" << endl;
	}
}//end setupGame

void PalaceGame::CreatePlayers(const int PLAYERCOUNT, vector<Player> &players, const int DEALER)
{
	//Declare local variables
	string input;

	//Depending on PLAYERCOUNT set players into a vector and let them give their name
	//Determine order of players in vector by who was randomly choosen as dealer
	if(PLAYERCOUNT == 2)
	{
		cout << "Please give a name to Player1: " << endl;
		cin >> input;
		playerOne.setName(input);
		cout << "Please give a name to Player2: " << endl;
		cin >> input;
		playerTwo.setName(input);

		//Dealer always last
		if(dealer == 0)
		{
			players.push_back(playerTwo);
			players.push_back(playerOne);
		}
	
		else if(dealer == 1)
		{
			players.push_back(playerOne);
			players.push_back(playerTwo);
		}
		else
		{
			cout << "Something went wrong IN CreatePlayers ** PLAYER ORDER '2' **" << endl;
		}

		cout << "Players Total: " << players.size() << endl;
		for(int i=0; i<players.size(); i++)
		{
			cout << players[i].getName() << endl;
		}
	}//end if

	else if(PLAYERCOUNT == 3)
	{
		cout << "Please give a name to Player1: " << endl;
		cin >> input;
		playerOne.setName(input);
		cout << "Please give a name to Player2: " << endl;
		cin >> input;
		playerTwo.setName(input);
		cout << "Please give a name to Player3: " << endl;
		cin >> input;
		playerThree.setName(input);
		
		//Dealer always last
		if(dealer == 0)
		{
			players.push_back(playerTwo);
			players.push_back(playerThree);
			players.push_back(playerOne);
		}
		
		else if(dealer == 1)
		{
			players.push_back(playerThree);
			players.push_back(playerOne);
			players.push_back(playerTwo);
		}
		
		else if(dealer == 2)
		{
			players.push_back(playerOne);
			players.push_back(playerTwo);
			players.push_back(playerThree);
		}
		else
		{
			cout << "Something went wrong IN CreatePlayers ** PLAYER ORDER '3' **" << endl;
		}
		
		cout << "Players Total: " << players.size() << endl;
		for(int i=0; i<players.size(); i++)
		{
			cout << players[i].getName() << endl;
		}
	}//end elseif

	else if(PLAYERCOUNT == 4)
	{
		cout << "Please give a name to Player1: " << endl;
		cin >> input;
		playerOne.setName(input);
		cout << "Please give a name to Player2: " << endl;
		cin >> input;
		playerTwo.setName(input);
		cout << "Please give a name to Player3: " << endl;
		cin >> input;
		playerThree.setName(input);
		cout << "Please give a name to Player4: " << endl;
		cin >> input;
		playerFour.setName(input);

		//Dealer always last
		if(dealer == 0)
		{
			players.push_back(playerTwo);
			players.push_back(playerThree);
			players.push_back(playerFour);
			players.push_back(playerOne);
		}
		
		else if(dealer == 1)
		{
			players.push_back(playerThree);
			players.push_back(playerFour);
			players.push_back(playerOne);
			players.push_back(playerTwo);
		}

		else if(dealer == 2)
		{
			players.push_back(playerFour);
			players.push_back(playerOne);
			players.push_back(playerTwo);
			players.push_back(playerThree);
		}
	
		else if(dealer == 3)
		{
			players.push_back(playerOne);
			players.push_back(playerTwo);
			players.push_back(playerThree);
			players.push_back(playerFour);
		}
		else
		{
			cout << "Something went wrong IN CreatePlayers ** PLAYER ORDER '4' **" << endl; 
		}
		
		cout << "Players Total: " << players.size() << endl;
		for(int i=0; i<players.size(); i++)
		{
			cout << players[i].getName() << endl;
		}
	}//end elseif

	else
	{
		cout << "something went wrong IN CreatePlayers ** NON legal amount of players **" << endl;
	}//end else
}//end CreatePlayers

void PalaceGame::CreateDeck(vector<Card> &deck)
{
	//Create cards 2 - 14 since no cards in a regular deck of cards have a rank 0 or 1 (11 = jack | 12 = queen | 13 = king | 14 = ace)
	for(int r=2; r<15; r++)
	{
		// make sure a 0 or 1 was not created somehow
		if(r == 0 || r == 1)
		{
			cout << "ERROR IN CREATE DECK **CREATION LOOP**" << endl;
		}
		//create suits 1 - 4 (1 = Club | 2 = Spade | 3 = heart | 4 = diamonds)
		for(int s=1; s<=4; s++)
		{
			if(s==1)
			{
				Card card(r, 'C');
				deck.push_back(card);
			}//end if
			else if(s==2)
			{
				Card card(r, 'S');
				deck.push_back(card);
			}//end elseif
			else if(s==3)
			{
				Card card(r, 'H');
				deck.push_back(card);
			}//end elseif
			else if(s==4)
			{
				Card card(r, 'D');
				deck.push_back(card);
			}//end elseif
			else
			{
				cout << "Something went wrong IN CreateDeck ** s != 1-4" << endl;
			}//end else
		}//end for
	}//end for

	//always should be 52 during creation
	if(deck.size() == 52)
	{
		//make sure there are no duplicate cards
		for(int i=0; i<deck.size(); i++)
		{
			Card cardCheck = deck[i];
			//Test cardCheck against entire deck
			for(int j=0; j<deck.size(); j++)
			{
				if(cardCheck.getRank() == deck[j].getRank() 
					&& cardCheck.getSuit() == deck[j].getSuit()
					&& i != j)
				{
					cout << "Something went wrong IN CreateDeck 3 ** MULTIPLE OF CARD: ";
					cardCheck.DisplayCard();
					cout << endl;
					cout << "Location in deck vector: " << j << "**" << endl;
				}//end if
			}//end for
		}//end for
	}//end if

	else
	{
		cout << "Something went wrong IN CreateDeck 2 ** DECK != 52 **" << endl;
	}//end else

	cout << "DECK SIZE: " << deck.size() << endl;
}//end CreateDeck

void PalaceGame::ShuffleDeck(vector<Card> &deck)
{
	//Declare local variables
	srand(time(NULL));
	Card temp;
	Card temp2;
	Card temp3;
	int r, r2, r3;
	
	//Confirm deck size has not changed yet
	if(deck.size() == 52)
	{
		for(int i = 0; i < 52; i++)
		{
			r = rand() % 52;
			r2 = rand() % 52;
			r3 = rand() % 52;

			temp = deck[i];
			deck[i] = deck[r];
			deck[r] = deck[r2];
			deck[r2] = deck[r3];
			deck[r3] = temp;
			
		}//end for	
	}//end if
	
	else
	{
		cout << "Something went wrong IN ShuffleDeck ** DECK != 52 **" << endl;
	}//end else	
}//end ShuffleDeck

void PalaceGame::DealGame(const int PLAYERCOUNT)
{
	//deal palace
	for(int i=0; i<PLAYERCOUNT*3; i++)
	{
		if(i%PLAYERCOUNT==0)
		{
			players[0].setPalaceCard(deck[i]);
		}
		else if(i%PLAYERCOUNT==1)
		{
			players[1].setPalaceCard(deck[i]);
		}
		else if(i%PLAYERCOUNT==2)
		{
			players[2].setPalaceCard(deck[i]);
		}
		else if(i%PLAYERCOUNT==3)
		{
			players[3].setPalaceCard(deck[i]);
		}
	}//end for

	//erase cards used for Palace
	for(int r=0; r<PLAYERCOUNT*3; r++)
	{
		deck.erase(deck.begin());
	}

	//check player hands
	for(int i=0; i<PLAYERCOUNT; i++)
	{
		cout << "Player " << i << "'s palace: " << endl;
		for(int j=0; j<players[i].getPalaceCount(); j++)
		{
			cout << "Card " << j << " = ";
			players[i].getPalaceCard(j).DisplayCard();
			cout << endl;
		}
	}

	//deal initial 6 cards
	for(int i=0; i<PLAYERCOUNT*6; i++)
	{
		if(i%PLAYERCOUNT==0)
		{
			players[0].setHandCard(deck[i]);
		}
		else if(i%PLAYERCOUNT==1)
		{
			players[1].setHandCard(deck[i]);
		}
		else if(i%PLAYERCOUNT==2)
		{
			players[2].setHandCard(deck[i]);
		}
		else if(i%PLAYERCOUNT==3)
		{
			players[3].setHandCard(deck[i]);
		}
	}

	//erase cards used for initial deal
	for(int r=0; r<PLAYERCOUNT*6; r++)
	{
		deck.erase(deck.begin());
	}

	drawPile = deck;
	deck.clear();
}//end DealGame

void PalaceGame::ChooseTopOfPalace(vector<Player> &players)
{
	int cardChoice, counter = 0;
	do
	{
		while(counter < 3)
		{
			cout << players[turn].getName() << " Please choose number corresponding to the card you would like to be ontop of your palace: " << endl;
			cout << "Current Cards: " << endl;
		
			for(int i=0; i < players[turn].getHandCount(); i++)
			{
				cout << i << ". ";
				players[turn].getHandCard(i).DisplayCard();
				cout << endl;
			}
			
			cout << "Choose TopOfPalace Card " << counter << ": ";
			cin >> cardChoice;
			cout << endl;
			if(cardChoice < 0 || cardChoice >= players[turn].getHandCount())
			{
				cout << "INVALID OPTION" << endl;
				counter--;
			}
			else if(cardChoice >= 0 && cardChoice < players[turn].getHandCount())
			{
				players[turn].setTopOfPalace(players[turn].getHandCard(cardChoice));
				players[turn].removeHandCard(cardChoice);
			}
			counter++;
		}
		counter = 0;
		IncrementTurn();
	}while(turn != 0);
	
	cout << "****** PRINTING TOP OF PALACE CARDS FOR EACH PLAYER:******" << endl;
	for(int y=0; y<players.size(); y++)
	{
		cout << "Player " << y << ":" << endl;
		cout << "Card 1:"; 
		players[y].getTopOfPalaceCard(0).DisplayCard();
		cout<< endl;

		cout << "Card 2:"; 
		players[y].getTopOfPalaceCard(1).DisplayCard(); 
		cout<< endl;

		cout << "Card 3:";
		players[y].getTopOfPalaceCard(2).DisplayCard();
		cout<< endl << endl;
	}
}

void PalaceGame::PlayGame(const int PLAYERCOUNT)
{
	cout << "!!!!!!!!Current turn: " << turn << endl;
	while(!gameover)
	{
		cout << players[turn].getName() << " It's you're turn!" << endl;
		if(players[turn].getHandCount() == 0 && drawPile.size() == 0)
		{
			if(players[turn].getTopOfPalaceCount() != 0)
			{
				players[turn].setHand(players[turn].getTopOfPalace());		
			}

			else if(players[turn].getPalaceCount() != 0)
			{
				PlayFromPalace();
			}
		}
		PlayCard();
		//check drawPile size here to avoid unneeded function calls
		if(drawPile.size() != 0)
		{
			DrawCards(turn);
		}

		if(players[turn].getHandCount() == 0 && players[turn].getTopOfPalaceCount() == 0 && players[turn].getPalaceCount() == 0)
		{
			cout << "A winner has been decided! Congradulations Player " << players[turn].getName() << endl;
			gameover = true;
		}
		else
		{
			IncrementTurn();
		}
	}
	if(gameover)
	{
		cout << "Thank you for playing Palace Card Game" << endl;
	}
	else
	{
		cout << "WTF WHY AM I RUNNING.. THIS IS BS.. I QUIT LIFE" << endl;
	}
}

void PalaceGame::DrawCards(const int turn)
{

	if(drawPile.size() != 0)
	{
		for(int i=0; i<3-players[turn].getHandCount(); i++)
		{
			players[turn].setHandCard(drawPile.back());

			if(drawPile.back().getRank() == midPile.back().getRank())
			{
				cout << "You drew a card with the same rank as what was just played, it has been played for you! You draw again." << endl; // may need to adjust and give option
				
				if(drawPile.size() != 0)
				{

				}
			
			}
			drawPile.erase(drawPile.end()-1);
		}
	}
	else if(drawPile.size() == 0)
	{
		cout << "DrawPile is Empty!" << endl;
	}
	else
	{
		cout << "Something went wrong IN DrawCard" << endl;
	}
}

void PalaceGame::PickUpMidPile()
{
	players[turn].setHand(midPile);
	midPile.clear();
	if(midPile.size() != 0)
	{
		cout << "Error in PickUpMidPile" << endl;
	}
}

void PalaceGame::PlayCard()
{
	//May move functionality to playGame and make PlayCard simply add card to midPile
	int cardChoice;
	bool turnover = false;

	while(turnover == false)
	{
		players[turn].DisplayHand();
		cin >> cardChoice;

		while(cardChoice < 0 || cardChoice >= players[turn].getHandCount())
		{
			cout << "Please enter a valid choice: " << endl;
			cin >> cardChoice;
		}

		if(isPlayable(players[turn].getHandCard(cardChoice)))
		{
			Card playersCard;
			midPile.push_back(players[turn].getHandCard(cardChoice));
			playersCard = players[turn].getHandCard(cardChoice);
			players[turn].removeHandCard(cardChoice);
			turnover = true;

			if(isWildCard(playersCard))
			{
				PlayWildCard(playersCard);
			}
			else if(CheckMultiple(playersCard))
			{
				playMultiple(playersCard);
			}// end if
			else
			{
				cout << "Next players turn!" << endl;
			}
		}
		else
		{
			cout << "You have selected a card that is unable to be played, please choose again" << endl;
		}	
	}
}

Player PalaceGame::CurrentTurn()
{
	return players[turn];
}

void PalaceGame::IncrementTurn()
{
	if(turn == players.size()-1)
	{
		turn = 0;
	}
	else if(turn == 0 || turn == 1 || turn == 2)
	{
		turn++;
	}
	else
	{
		cout << "Something went wrong IN IncrementTurn" << endl;
	}
}

bool PalaceGame::CheckMultiple(Card &card)
{
	for(int i=0; i<players[turn].getHandCount(); i++)
	{
		if(card.getRank() == players[turn].getHandCard(i).getRank())
		{
			return true;
		}
	}

	return false;
}

bool PalaceGame::isPlayable(Card &card)
{
	if(midPile.size() == 0)
	{
		return true;
	}
	else if(card.getRank() >= midPile.back().getRank() 
		|| isWildCard(card))
	{
		return true;
	}
	else
	{
		return false;
	}
}

bool PalaceGame::isWildCard(Card &card)
{
	if(card.getRank() == 2 || card.getRank() == 10)
	{
		return true;
	}
	else
	{
		return false;
	}
}

void PalaceGame::playMultiple(Card &playersCard)
{
	int multiCardPlayInput;

	cout << "Would you like to play cards of the same rank?" << endl;
	cout << "1. Yes, all! \n" 
		<< "2. Yes, but not all! \n" 
		<< "3. No." << endl;
	cin >> multiCardPlayInput;

	while(multiCardPlayInput < 1 || multiCardPlayInput > 3)
	{
		cout << "Please enter a valid choice: " << endl;
		cin >> multiCardPlayInput;
	}

	switch(multiCardPlayInput)
	{
	case 1:
		for(int i=0; i<players[turn].getHandCount(); i++)
		{
			if(players[turn].getHandCard(i).getRank() == playersCard.getRank())
			{
				midPile.push_back(players[turn].getHandCard(i));
				players[turn].removeHandCard(i);
			}
		}
		break;
	case 2:
		while(CheckMultiple(playersCard))
		{
			cout << "Please choose a card with the same rank to play(Type 123 to quit): " << endl;
			players[turn].DisplayHand();
			cin >> multiCardPlayInput;
			if(multiCardPlayInput == 123)
			{ 
				break;
			}
			else
			{
				if(players[turn].getHandCard(multiCardPlayInput).getRank() == playersCard.getRank())
				{
					midPile.push_back(players[turn].getHandCard(multiCardPlayInput));
					players[turn].removeHandCard(multiCardPlayInput);
				}
				else if(players[turn].getHandCard(multiCardPlayInput).getRank() != playersCard.getRank())
				{
					cout << "Please choose a Card with the rank: " << playersCard.getRank() << endl;
				}
				else
				{
					cout << "Something went horribly wrong in PlayCard() ** multiCardPlayInput case 2**" << endl;
				}
			}
		}
		break;
	case 3: 
		break;
	}// end switch
}

void PalaceGame::PlayWildCard(Card &wildCard)
{
	int wildCardChoice;
	do
	{

		if(wildCard.getRank() == 2)
		{
			midPile.push_back(wildCard);
			
			cout << "You played a 2, please play another card... You may play anything!" << endl;
			players[turn].DisplayHand();
			cin >> wildCardChoice;
		
			while(wildCardChoice < 0 || wildCardChoice >= players[turn].getHandCount())
			{
				cout << "Please enter a valid choice: " << endl;
				cin >> wildCardChoice;
			}
			wildCard = players[turn].getHandCard(wildCardChoice);

			if(isWildCard(wildCard))
			{
				cout << "You have selected another wild card" << endl;
				players[turn].removeHandCard(wildCardChoice);
			}
			else if(!isWildCard(wildCard) && wildCard.getRank() >= midPile.back().getRank())
			{
				midPile.push_back(wildCard);
				players[turn].removeHandCard(wildCardChoice);
			}
			else
			{
				cout << "Something went terribly wrong in PlayWildCard ** not additional wild card **" << endl;
			}	
		}
		
		else if(wildCard.getRank() == 10)
		{
			midPile.push_back(wildCard);

			deadPile = midPile;
			midPile.clear();

			if(deadPile.size() != 0 && midPile.size() == 0)
			{			
				cout << "You played a 10, please play another card... You may play anything!" << endl;
				players[turn].DisplayHand();
				cin >> wildCardChoice;
		
				while(wildCardChoice < 0 || wildCardChoice >= players[turn].getHandCount())
				{
					cout << "Please enter a valid choice: " << endl;
					cin >> wildCardChoice;
				}

				wildCard = players[turn].getHandCard(wildCardChoice);

				if(isWildCard(wildCard))
				{
					cout << "You have selected another wild card" << endl;
					players[turn].removeHandCard(wildCardChoice);
				}
				else
				{
					midPile.push_back(wildCard);
					players[turn].removeHandCard(wildCardChoice);

					if(CheckMultiple(wildCard))
					{
						playMultiple(wildCard);
					}
				}

			}
			else
			{
				cout << "Something went terribly wrong in PlayWildCard ** rank = 10 **" << endl;
			}
		}
	}while(isWildCard(wildCard));
}

void PalaceGame::PlayFromPalace()
{
	int palaceCardChoice;
	cout << "You have " << players[turn].getPalaceCount() << " palace cards." << endl;
	cout << "Please choose one of your remaining palace cards to play" << endl;
	cin >> palaceCardChoice;

	while(palaceCardChoice < 0 || palaceCardChoice  > players[turn].getPalaceCount())
	{
		cout << "Please enter a valid choice: " << endl;
		cin >> palaceCardChoice;
	}
	
	if(isPlayable(players[turn].getHandCard(palaceCardChoice)))
	{
		Card playersCard;
		midPile.push_back(players[turn].getHandCard(palaceCardChoice));
		playersCard = players[turn].getHandCard(palaceCardChoice);
		players[turn].removeHandCard(palaceCardChoice);

		if(isWildCard(playersCard))
		{
			PlayWildCard(playersCard);
		}
		else if(CheckMultiple(playersCard))
		{
			playMultiple(playersCard);
		}// end if
		else
		{
			cout << "Next players turn!" << endl;
		}
	}

	else if(players[turn].getHandCard(palaceCardChoice).getRank() < midPile.back().getRank())
	{
		PickUpMidPile();
	}

	PlayCard();

}
