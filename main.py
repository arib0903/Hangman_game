import random
import HangmanLives
import WordList
import os


def clear():
    os.system("cls")


def runGame():
    chosen_word = random.choice(WordList.word_list)

    stages = HangmanLives.stages



    print(HangmanLives.logo)
    # print(f'Pssst, the solution is {chosen_word}.')

    display = []
    wrongLetters = []
    for x in chosen_word:
        display.insert(0, "_")

    gameEnd = False  # initiates a starting point for the game to end
    # Set 'lives' to equal 6.
    lives = 6
    while (not gameEnd):  # will run until gameEnd = True

        guess = input("Guess a letter: ").lower()
        clear()  # Clears the game board for a better user experience
        if guess in display:
            print(f"You have already used {guess}")

        if guess in wrongLetters:
            print(f"You have already used {guess}")
            lives+=1

        for letters in range(len(chosen_word)):
            if guess == chosen_word[letters]:
                display[letters] = guess




        if guess not in chosen_word:
            wrongLetters.append(guess)
            lives -= 1

            if lives == 0:
                gameEnd = True
                print("You Lost")

        if '_' not in display:
            gameEnd = True
            print(f"\n You Win, with {lives} lives left")

        print(f"Wrong Letters Chosen: {wrongLetters}")
        print(f"\n{lives} lives left")
        print(stages[lives])
        print(f"{' '.join(display)}")



runGame()
