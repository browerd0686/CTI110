# Rock, Paper, Scissors Excercise
# July 17, 2019
# CTI-110 P5HW2 - Rock, Paper, Scissors Game
# Darrius Brower
#
# Create a program where a random number from 1 to 3 is generated.
# 1 is rock, 2 is paper, 3 is scissor. Don't show the computer's choice yet.
# User should enter their choice on the keyboard.
# Winners are awarded by rock beats scissors, paper beats rock, and scissors beats paper.
# If both players select same thing then game must continue until a winner is declared.
#
import random

def generateRandomNumber():
        randomNumber = random.randint(1, 3)
        return randomNumber

def getComputerChoice(randomNumber):
        if randomNumber == 1:
                computerChoice = 'rock'
        elif randomNumber == 2:
                computerChoice = 'paper'
        elif randomNumber == 3:
                computerChoice = 'scissors'
        return computerChoice

def getUserChoice():
        userChoice = input('Please enter your choice: ')
        return userChoice

def determineWinner(computerChoice, userChoice):
        rockMessage = 'The rock beats the scissors'
        scissorsMessage = 'The scissors beats the paper'
        paperMessage = 'The paper beats rock'
        winner = 'no winner'
        if computerChoice == 'rock' and userChoice == 'scissors':
                winner = 'Computer'
                message = rockMessage
        elif computerChoice == 'scissors' and userChoice == 'rock':
                winner = 'You'
                message = rockMessage
        if computerChoice == 'scissors' and userChoice == 'paper':
                winner = 'Computer'
                message = scissorsMessage
        elif computerChoice == 'paper' and userChoice == 'scissors':
                winner = 'You'
                message = scissorsMessage
        if computerChoice == 'paper' and userChoice == 'rock':
                winner = 'Computer'
                message = paperMessage
        elif computerChoice == 'rock' and userChoice == 'scissors':
                winner = 'You'
                message = paperMessage
        return winner, message

def startAgain():
        randomNumber = generateRandomNumber()
        computerChoice = getComputerChoice(randomNumber)
        userChoice = getUserChoice()
        print('The computer chose', computerChoice)
        winner, message = determineWinner(computerChoice, userChoice)
        if winner != 'no winner':
                print(winner, 'won(', message, ')' )
        while winner == 'no winner':

def main():
        randomNumber = generateRandomNumber()
        computerChoice = getComputerChoice(randomNumber)
        userChoice = getUserChoice()
        print('The computer chose', computerChoice)
        winner, message = determineWinner(computerChoice, userChoice)
        if winner != 'no winner':
                print(winner, 'won(', message, ')' )
        while winner == 'no winner':
                print('\nYou both chose the same')
                winner = startAgain()     
main()


    

