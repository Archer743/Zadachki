from random_word import RandomWords
from termcolor import colored
from os import system

system("color")


class Hangman:
    def __init__(self):
        self.r = RandomWords()
        
        self.cur_word = self.r.get_random_word(hasDictionaryDef="true", includePartOfSpeech="noun", minCorpusCount=1, maxCorpusCount=10, minDictionaryCount=1, maxDictionaryCount=10, minLength=5, maxLength=10)
        
        self.attempts = 6
        self.letters_guessed = []

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



if __name__ == "__main__":
    game = Hangman()
    print(game)
    game.draw_person()
    print(game.word_by_guessed_letters())