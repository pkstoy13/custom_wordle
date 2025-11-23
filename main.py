import random 

'''
Wordle Clone in Python
Requirements:
-At the start of each day, a new word is picked, that can range from size 5 to size 10
-The user gets 6 guesses to guess the word
-If they get a letter right, in the wrong order, let them know
-If the letter is right, and in the right order, let them know a different way
-keep track of the guess number that they're on
-if they run out of guesses, they fail for the day, at the end, reveal the correct word
-allow users to type a prompt, give them feedback after each guess

Things needed to learn:
-How to give users an input prompt in python
-how to pick between a random word each time
-

'''
NUMBER_OF_GUESSES = 6

def word_picker():
    word_list = {1: "ethereal", 2: "colorful", 3:"obelisk", 4:"willow", 5:"astro", 6:"pink"}
    chosen_word = random.randint(1, len(word_list))
    return word_list[chosen_word]


def game():
    chosen_word = word_picker()
    blank_word = "_" * len(chosen_word)
    user_guesses = 0
    print("Welcome to Wordle: You get 6 chances to guess this word", blank_word)
    user_guess = ""
    while user_guess != chosen_word and user_guesses < NUMBER_OF_GUESSES:
        #print("Try Again")
        user_guess = input()
        if user_guess == "xxx":
            return
        user_guesses += 1
        print("Number of guesses left: ", (NUMBER_OF_GUESSES - user_guesses))
    if user_guess == chosen_word:
        print("You guessed the right word! That being: ", chosen_word)
    else: print("You failed to guess the correct word, try again")
    

def main():
    game()

main()

