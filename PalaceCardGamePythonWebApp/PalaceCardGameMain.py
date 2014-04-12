#-------------------------------------------------------------------------------
# Name:         PalaceCardGameMain.py
#
# Purpose:      Main Method file for Palace Card Game
#               Starts the game
# Author:       Craig Gleckman
#
# Created:      25/03/2014
# Copyright:    (c) Craig 2014
# Licence:      <your licence>
#-------------------------------------------------------------------------------
import PalaceGame

def main():
    PalaceGame.PalaceGame()
    raw_input("Press Enter To Close Window")
    return 0;

if __name__ == '__main__':
    main()
