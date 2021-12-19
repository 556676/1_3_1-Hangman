import random
import turtle as trtl

wn = trtl.Screen()
wn.addshape("hang5.gif")
wn.addshape("hang6.gif")
wn.addshape("hang7.gif")
wn.addshape("hang8.gif")
wn.addshape("hang9.gif")
wn.addshape("hang10.gif")
wn.addshape("hang11.gif")


#list of words used in game
word_list = ["escape", "cat", "ball", "hangman", "mango", "python", "melon"]

#retrieves word from list
def get_word(word_list):
    word = random.choice(word_list)
    return word.upper()

#Start game
def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("Let's play Hangman")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        wn.bgcolor("salmon")
        guess = input("guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("you already tried", guess, "!")
            elif guess not in word:
                print(guess, "isn't in the word :(")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Nice one,", guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already tried ", guess, "!")
            elif guess != word:
                print(guess, " Is not the word :(")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("invalid input")
        display_hangman(tries)
        print(word_completion)
        print("\n")
    if guessed:
        print("Good Job, you guessed the word!")
        wn.bgcolor("green")
    else:
        print("I'm sorry, but you ran out of tries. The word was " + word + ". Maybe next time!")
        wn.bgcolor("red")



#Function used to  display images of hangman
def display_hangman(tries):
    if tries == 6:
        wn.bgpic("hang5.gif")
    elif tries == 5:
        wn.bgpic("hang6.gif")
    elif tries == 4:
        wn.bgpic("hang7.gif")
    elif tries == 3:
        wn.bgpic("hang8.gif")
    elif tries == 2:
        wn.bgpic("hang9.gif")
    elif tries == 1:
        wn.bgpic("hang10.gif")
    elif tries == 0:
        wn.bgpic("hang11.gif")


def main():
    word = get_word(word_list)
    play(word)
    while input("Again? (Y/N) ").upper() == "Y":
        word = get_word(word_list)
        play(word)

if __name__ == "__main__":
    main()

wn.mainloop()
