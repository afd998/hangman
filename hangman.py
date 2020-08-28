import os
import random
import sys

from nltk.corpus import words

stages = [
  "  /|\n   |\n   |\n   |\n -----",
  "  /|\n O |\n   |\n   |\n -----",
  "  /|\n O |\n | |\n   |\n -----",
  "  /|\n O |\n | |\n / |\n -----",
  "  /|\n O |\n | |\n /\|\n -----",
  "  /|\n O |\n-| |\n /\|\n -----",
  "  /|\n O |\n-|-|\n /\|\n -----",
  "  /|\n 🙁|\n-|-|\n /\|\n -----",
  "  /|\n 🥵|\n-|-|\n /\|\n -----",
]

def main():
  #get words
  word_list = words.words()
  word_list_len = len(word_list)
  
  #new game
  while(True): 

    #create state
    word_index = random.randint(0,word_list_len)
    word = word_list[word_index]
    guessed = []
    score = ["_" for char in word]
    curr_stage = 0
    num_stages = len(stages)
    
    #display intro
    clear()
    print("\nWelcome to Hangman")
    input("press enter to begin")
    clear()
    print("-----------------------\n")
    
    #new turn
    while(True):

      #check if game is over
      if(checkendgame(curr_stage, score, num_stages, word)):
        break 
      
      #display state
      print(stages[curr_stage], "\n")
      print(*score)
      print("\nGuessed: ", guessed)

      #take a guess
      guess = input("Guess a letter? (then hit enter)\n")
      

      #process guess
      
      #make sure its a single letter
      if (len(guess) !=1 or guess.isalpha()==False):
        clear()
        print("Please guess a single letter\n")
        #repeat the turn
        continue

      #normalize to lowercase
      guess =guess.lower()
      
      #check if allready guessed
      if guess in guessed:
        clear()
        print("You allready guessed that letter.\n")
        #start turn over
        continue
      guessed.append(guess)

      if guess in word: #hit
        #find the hit indexes
        for hit_index in range (0, len(word)):
            if word[hit_index] == guess:
              #update the score
              score[hit_index] = guess
        clear()
        print("Yep,", guess, ".\n")
      
      else: #miss
        clear()
        print("Nope!\n")
        #update the stage
        curr_stage+=1  






   
def clear(): os.system('clear') #on Linux System


def checkendgame(curr_stage, score, num_stages, word):
  if curr_stage>num_stages-1: #lost
    print("You lost :(")
    print("the word was:", word)
    return endgame()      
  elif "_" not in score: # won
    print("you win!")
    print("the word was:", word)
    return endgame()
  else:
    return 0


def endgame():
  while(True):
    decision= input("want to play again? (type y if YES or n if NO the press enter)")
    if (len(decision) ==1 and decision.isalpha()==True):
      decision = decision.lower()
      if(decision=="y"):
        return 1
      elif (decision=="n"):
        clear()
        sys.exit(0)
      else:
        clear()
        print("Please enter y or n")
        continue
    else:
      clear()
      print("Please enter y or n")
      continue


    

main()
