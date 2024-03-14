import random
word_list = ["apple", "beautiful", "potato"]
lives = 6
chosen_word = random.choice(word_list).lower()
print(chosen_word)
display = ['_' if letter != ' ' else ' ' for letter in chosen_word]

hangman_stages = [
    """
    --------
    |      |
    |      O
    |     \\|/
    |      |
    |     / \\
    -
    """,
    """
    --------
    |      |
    |      O
    |     \\|/
    |      |
    |     / 
    -
    """,
    """
    --------
    |      |
    |      O
    |     \\|/
    |      |
    |      
    -
    """,
    """
    --------
    |      |
    |      O
    |     \\|
    |      |
    |     
    -
    """,
    """
    --------
    |      |
    |      O
    |      |
    |      |
    |     
    -
    """,
    """
    --------
    |      |
    |      O
    |      
    |      
    |     
    -
    """,
    """
    --------
    |      |
    |      
    |      
    |      
    |     
    -
    """
]

current_stage = 0
game_over = False
while not game_over:
    guessed_letter = input("Guess a letter: ").lower()
    if guessed_letter in chosen_word:
        for position in range(len(chosen_word)):
            if chosen_word[position] == guessed_letter:
                display[position] = guessed_letter
    else:
        lives -= 1
        print(hangman_stages[current_stage])
        current_stage += 1
        if lives == 0:
            game_over = True
            print("You lose!! The word was:", chosen_word)
    
    if '_' not in display:
        game_over = True
        print("Congratulations! You've guessed the word correctly.")
    
    print(' '.join(display))
