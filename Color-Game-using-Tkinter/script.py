# importing the modules
import tkinter
import random

# list of possible colours
colours = ['Red', 'Blue', 'Green', 'Pink', 'Black',
           'Yellow', 'Orange', 'White', 'Purple', 'Brown']
# Score of the player, initially zero
score = 0

# the remaining time in the game, initially 30 seconds
timeleft = 30

# function to start the game
def startGame(event):
    if timeleft == 30:
        #starting the countdown timer.
        countdown()

    # calling the function to choose the next colour
    nextColour()

# Function to choose and display the next colour
def nextColour():
    # Using the globally declared variable 'score' and 'timeLeft' variables
    # declared above
    global score
    global timeleft

    # if a game is currently in session
    if timeleft > 0:

        # making the box to write the names of the colour active
        e.focus_set()

        # if the colour typed and colour of the text same
        if e.get().lower() == colours[1].lower():
            score += 1

        # clearing the text entry box
        e.delete(0, tkinter.END)

        random.shuffle(colours)

        # changing the colour to type, by changing the text and the colour
        # to a random colour
        label.config(fg=str(colours[1]), text=str(colours[0]))

        # updating the score
        scoreLabel.config(text="Score: " + str(score))

# Declaring and defining the countdown timer function
def countdown():
    global timeleft

    # if a game is in session
    if timeleft > 0:
        # decrement the timer:
        timeleft -= 1

        # updating the time left Label
        timeLabel.config(text="Time left: "
                              + str(timeleft))

        # calling the function again after 1 second
        timeLabel.after(1000, countdown)

# Main Driver Code

# Creating a GUI window
root = tkinter.Tk()

# setting the title
root.title("COLOR GAME")

# setting the size
root.geometry("375x200")

# adding the instruction label
instructions = tkinter.Label(root, text="Type in the colour"
                                        "of the words, and not the word text!",
                             font=('Helvetica', 12))
instructions.pack()

# adding a score label
scoreLabel = tkinter.Label(root, text="Press enter to start",
                           font=('Helvetica', 12))
scoreLabel.pack()


# adding a time left label
timeLabel = tkinter.Label(root, text="Time left: " +
                                     str(timeleft), font=('Helvetica', 12))

timeLabel.pack()

# adding a Label for displaying the colours
label = tkinter.Label(root, font=('Helvetica', 60))
label.pack()

# Adding a text box for typing in the colours
e = tkinter.Entry(root)

# calling the 'startGame' function when the entry key is pressed
root.bind('<Return>', startGame)
e.pack()

# setting the focus on the entry box
e.focus_set()

# Starting the GUI
root.mainloop()
