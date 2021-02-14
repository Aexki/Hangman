import os
from generate import getword
from hangman_art import stages,logo

x=[]
lc=0

def game(lc):
    #generating a word randomly
    word=getword()
    mistake=0

    while(mistake<=7):
        os.system('cls')
        if mistake==0:
            print(logo)
        print(stages[(6-mistake)])
        
        #check whether mistake has become 0 or not
        if mistake==6:
            print('The word was {}.'.format(word.upper()))
            print('\nYou Lost!!!\nHangman Died :(\n')
            break
        
        #check whether the player has won or not
        if all(item in x for item in word):
            print('The word was {}.'.format(word.upper()))
            print('\nCongratulations!!\nYou have won and saved Hangman :)\n')
            break
        
        for i in word:
            if i in x:
                print(i.upper()+' ',end='')
            else:
                print('_ ',end='')
        print(' (It has {} characters)'.format(len(word)))
        
        if lc==0:
            pass
        else:
            if lc.lower() not in word:
                print('\nYou have guessed wrong. {} is not present in the word.'.format(lc.upper()))
            else:
                print('\nYou have guessed correct. {} is present in the word.'.format(lc.upper()))
                
        
        inp=input('\nEnter a character: ')
        x.append(inp.lower())
        lc=inp
        
        if inp.lower() not in word:
            mistake+=1

game(lc)

while(True):
    m=input('Do you want to play again?(y/n) : ')
    if m=='y':
        lc=0
        x=[]
        game(lc)
    elif m=='n':
        print('\nThanks for playing. Goodbye..\n')
        break  
    else:
        print('Enter y or n only.')  
    



