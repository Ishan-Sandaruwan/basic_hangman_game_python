#Step 2

import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

gameList = []
for char in chosen_word:
  gameList.append("_")
print(gameList)

guess = input("Guess a letter: ").lower()

#Loop through each position in the chosen_word;
for letter in range(0,len(chosen_word)):
    if chosen_word[letter] == guess:
      gameList[letter] = guess

print(gameList)

#Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
