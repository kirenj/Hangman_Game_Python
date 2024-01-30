import random
from hangman_words import word_list
from hangman_art import stages
from hangman_art import logo


print(logo)
chosen_word = random.choice(word_list)
chosen_word_length = int(len(chosen_word))
#print(chosen_word)

display = []

for j in chosen_word:
  display += '_'


lives_left = 6
turns = True
word_length = 0


while turns == True:
  guess = input("Guess a letter: ").lower()
 
  word_count = 0
  word_length += 1
  
  
  if guess in display:
    print(f"You have already entered '{guess}'. Guess again")
  
  for i in chosen_word:    
    if guess == i:
      word_count += 1
      display[word_count-1] = guess      
      if '_' not in display:
        print("You Win")
        turns = False       
    else:      
      word_count += 1
        
  if guess not in chosen_word:
    print(f"'{guess}' is not in the word. Try again")
    lives_left -= 1
      
  
  #print(lives_left)
  print(''.join(display))
  print(stages[lives_left])
  if lives_left == 0:
    turns = False


if '_' in display and lives_left == 0:
  print("You Lose")
  print(f"The correct word was '{chosen_word}'")

    
  
  