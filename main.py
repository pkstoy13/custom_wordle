import random 
from words import word_list

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

Resources Used:
https://www.index.dev/blog/python-string-comparison-methods
https://dictionaryapi.dev/
https://fastapi.tiangolo.com/#opinions
https://www.freecodecamp.org/news/how-to-build-a-wordle-clone-using-python-and-rich/
'''
NUMBER_OF_GUESSES = 6

def word_picker():
    chosen_word = random.randint(1, len(word_list))
    return word_list[chosen_word]

def check_guess(user_guess, word_to_guess):
    #user_guess = input().lower()
    word = ["_"] * len(word_to_guess)
    color = ["⬛"] * len(word_to_guess)

    for i in range(len(user_guess)):
        if user_guess[i] == word_to_guess[i]:
            word[i] = user_guess[i]
            color[i] = "🟩"
        elif user_guess[i] in word_to_guess:
            word[i] = "?"
            color[i] = "🟧"
        else:
            word[i] = "X"
    print(word)
    print(color)
    return user_guess




def game():
    chosen_word = word_picker()
    guess_count = 0
    end_of_game = False
    blank_word = "_" * len(chosen_word)
    #constructed_word = ["_"] * len(chosen_word)
    print("Welcome to Wordle: You get 6 chances to guess this word", blank_word)
    while not end_of_game:
        user_guess = check_guess(input().lower(), chosen_word)
        print("Number of guesses left: ", (NUMBER_OF_GUESSES - guess_count))
        if user_guess == "xxx":
            print("manual override")
            end_of_game = True
        if user_guess == chosen_word: 
            print("correct")
            end_of_game = True
        if user_guess != chosen_word and guess_count == 6:
            print("incorrect, you ran out of guesses")
            end_of_game = True
        guess_count += 1    

def main():
    game()

main()

