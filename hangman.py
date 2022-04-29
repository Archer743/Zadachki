from random_word import RandomWords
from termcolor import colored
from os import system

system("color")


class Hangman:
    def __init__(self):
        self.r = RandomWords()
        
        self.cur_word = rand_word if (rand_word := self.r.get_random_word(hasDictionaryDef="true", includePartOfSpeech="noun", minCorpusCount=1, maxCorpusCount=10, minDictionaryCount=1, maxDictionaryCount=10, minLength=5, maxLength=10)) != None else "banana"
        self.letters_guessed = []
        self.letters_failed = []
        
        self.attempts = 6
        self.guessed = False

    def __str__(self):
        return f"Current word: {self.cur_word}"

    def draw_person(self):
        head = ["()", "green"]
        l_arm, r_arm = ["/", "green"], ["\\", "green"]
        body = ["||", "green"]
        l_leg, r_leg = ["/", "green"], ["\\", "green"]

        if self.attempts == 5:
            l_leg[1] = "red"
        elif self.attempts == 4:
            l_leg[1], r_leg[1] = "red", "red"
        elif self.attempts == 3:
            l_leg[1], r_leg[1] = "red", "red"
            l_arm[1] = "red"
        elif self.attempts == 2:
            l_leg[1], r_leg[1] = "red", "red"
            l_arm[1], r_arm[1] = "red", "red"
        elif self.attempts == 1:
            l_leg[1], r_leg[1] = "red", "red"
            l_arm[1], r_arm[1] = "red", "red"
            body[1] = "red"
        elif self.attempts == 0:
            l_leg[1], r_leg[1] = "red", "red"
            l_arm[1], r_arm[1] = "red", "red"
            body[1] = "red"
            head[1] = "red"
        
        head = colored(text=head[0], color=head[1])
        l_arm, r_arm = colored(text=l_arm[0], color=l_arm[1]), colored(text=r_arm[0], color=r_arm[1])
        body = colored(text=body[0], color=body[1])
        l_leg, r_leg = colored(text=l_leg[0], color=l_leg[1]), colored(text=r_leg[0], color=r_leg[1])
        print(f"  {head}\n {l_arm}{body}{r_arm}\n  {l_leg}{r_leg}")
    
    def word_by_guessed_letters(self):
        result = ""
        for letter in self.cur_word:
            if letter in self.letters_guessed: result += f" {letter} "
            else: result += " _ "
        
        return result
    
    def start_game(self):
        print(colored(text="Let's play Hangman!", color="magenta"))
        self.draw_person()
        print(self.word_by_guessed_letters())
        
        while True:
            if self.attempts == 0:
                print(colored(text="You lost!", color="red"))
                print(colored(text=f"Word: {self.cur_word}", color="magenta"))
                break
            elif ("_" not in self.word_by_guessed_letters()):
                print(colored(text="You win!", color="green"))
                print(colored(text=f"Word: {self.cur_word}", color="magenta"))
                break


            letter = input(colored(text="Enter a letter: ", color="yellow"))


            if letter.lower() == "exit":
                print(colored(text=f"Word: {self.cur_word}", color="magenta"))
                break
            elif letter == self.cur_word:
                print(colored(text="You win!", color="green"))
                print(colored(text=f"Word: {self.cur_word}", color="magenta"))
                break


            if letter not in self.letters_guessed:
                if letter in self.cur_word:
                    self.letters_guessed.append(letter)
                    print(colored(text="Correct!", color="green"))
                    print(self.word_by_guessed_letters())
                    self.draw_person()
                elif letter in self.letters_failed:
                    print(colored(text="Already failed! Continue!", color="red"))
                else:
                    self.attempts -= 1
                    self.letters_failed.append(letter)
                    self.draw_person()
                    if self.attempts != 0: print(colored(text="Incorrect! Try again!", color="red"))
            else:
                print(colored(text="Already quessed! Continue!", color="green"))


if __name__ == "__main__":
    game = Hangman()
    game.start_game()