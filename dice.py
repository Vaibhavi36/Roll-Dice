import tkinter
import random

#main Window ,resize ,Title
root =tkinter.Tk()
root.geometry('600x600')
root.title('Roll Dice')

#label to display dice
label = tkinter.Label(root, text='', font=('Helvetica', 260))

#functions activated by button
def roll_dice():
    #unicode character strings for dice
    dice = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
    label.configure(text=f'{random.choice(dice)} {random.choice(dice)}')
    label.pack()
    
#button
button = tkinter.Button(root, text='Roll dice', foreground='green', command=roll_dice)

#pack a widget in the parent widget
button.pack()

#call the mainloop of Tk
#keep the window open
root.mainloop()
