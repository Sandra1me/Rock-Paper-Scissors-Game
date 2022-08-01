from tkinter import *
import random


def button_choose(selection):
    options=('Rock','Paper','Scissors')
    user=selection
    computer=random.choice(options)

    userEntry.delete(0, END)
    computerEntry.delete(0, END)

    userEntry.insert(0, "You choose: " +user)
    computerEntry.insert(0, "Computer chooses: " +computer)
    
    resultEntry.delete(0, END)

    if user=='Rock' and computer=='Rock':
        resultEntry.insert(0, "Tie")
    elif user=='Rock' and computer=='Paper':
        resultEntry.insert(0, "The computer wins")
    elif user=='Rock' and computer=='Scissors':
        resultEntry.insert(0, "You win!")
    
    elif user=='Paper' and computer=='Rock':
        resultEntry.insert(0, "You win!")
    elif user=='Paper' and computer=='Paper':
        resultEntry.insert(0, "Tie")
    elif user=='Paper' and computer=='Scissors':
        resultEntry.insert(0, "The computer wins")

    elif user=='Scissors' and computer=='Rock':
        resultEntry.insert(0, "The computer wins")
    elif user=='Scissors' and computer=='Paper':
        resultEntry.insert(0, "You win!")
    elif user=='Scissors' and computer=='Scissors':
        resultEntry.insert(0, "Tie")


def resetAll():
    userEntry.delete(0, END)
    computerEntry.delete(0, END)
    resultEntry.delete(0, END)
    

root=Tk()
root.title("Rock, Paper, Scissors Game!")
root.resizable(0,0)

#Text explaining the game
titleLabel=Label(root,text="ROCK, PAPER, SCISSORS GAME!", bg="#F2EEEB", padx=20, pady=10)
titleLabel.grid(column=0,row=0,columnspan=3)

explainLabel=Label(root,text="Choose your weapon: ", bg="#F2EEEB")
explainLabel.grid(column=0, row=1,columnspan=3)

#Choose buttons
rock=Button(root, text="ROCK", command=lambda: button_choose("Rock"), bg="#D97904")
paper=Button(root, text="PAPER", command=lambda: button_choose("Paper"), bg="#F29F05")
scissors=Button(root, text="SCISSORS", command=lambda: button_choose("Scissors"), bg="#BF5B04")

rock.grid(column=0, row=3, pady=8, padx=2)
paper.grid(column=1, row=3, pady=8, padx=2)
scissors.grid(column=2, row=3, pady=8, padx=2)

#Game messages
userEntry=Entry(root, bg="#F2EEEB", width=30)
computerEntry=Entry(root, bg="#F2EEEB", width=30)

userEntry.grid(column=0, row=4, columnspan=3)
computerEntry.grid(column=0, row=5, columnspan=3)

resultEntry=Entry(root, bg="#F2EEEB", width=30)
resultEntry.grid(column=0, row=6, columnspan=3, pady=10)

#Reset button
resetButton=Button(root, text="Reset", command=resetAll, bg="#D97904", padx=10)
resetButton.grid(row=9, column=0, pady=10)

#Exit button
exitButton=Button(root, text="Exit", command=root.destroy, bg="#D97904", padx=15)
exitButton.grid(row=9, column=2, pady=10)

root.mainloop()