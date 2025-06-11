import random

last_guess = 0
last_result = ''

class GuessingGame:
    def __init__(self, answer = random.randint(1,100)):
        self.answer_number = answer
        self.last_guess = 0
        self.last_result = ''

    def guess(self, user_guess):
        self.guessed_num = user_guess
        if self.guessed_num > self.answer_number:
            self.last_guess = self.guessed_num
            self.last_result = "high"
            return print(self.last_result)
        elif self.guessed_num < self.answer_number:
            self.last_guess = self.guessed_num
            self.last_result = "low"
            return print(self.last_result)
        else:
            self.last_result = "correct"
            return print(self.last_result)
    
    def solved(self):
        if self.last_result == "correct":
            return print(True)
        else:
            return print(False)
        
game = GuessingGame(10)

game.solved()

game.guess(5)
game.guess(20)
game.solved()

game.guess(10)
game.solved()