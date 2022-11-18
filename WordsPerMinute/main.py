from tkinter import *
import time
import random


typed_words = []
words_to_type = []
highlight_word = [] 
all_words = []

start = 0
counter = 1
def highlight_text(coun):
    global counter
    try:
        highlight_word[coun].config(bg="#87A2FB")
    except IndexError:
        pass
    highlight_word[coun - 1].config(bg="White")
    counter += 1

def clear_screen(labels):
    for label in labels:
        label.destroy()


def get_text(event):
    your_word = typer.get()
    typed_words.append(your_word)
    typer.delete(0, END)
    highlight_text(counter)

def refill_screen():
    if len(typed_words) % 40 == 0:
            clear_screen(highlight_word)
            fill_screen()

    

def countdown(count):
    global mult
    mult = 1.00
    timer['text'] = count
    if count > 0:
        # call countdown again after 1000ms (1s)
        window.after(1000, countdown, count-1)
        if len(typed_words) >= 60:
            mult += abs(count) * 0.0166
            calculate_words(timer['text'])
            
            

    if timer["text"] == 0:
        calculate_words()
        
        

def calculate_words(time=None):
    x = 0
    for i in range(len(typed_words)):
        all_words.append(words_to_type[i])
    
    for j in range(len(typed_words)):
        if typed_words[j] == all_words[j]:
            x += 1
    if time != None:
        x *= mult
    
    
    calculator = Label (window, text=f"Your wpm is {int(x)}", font=('Helvetica bold', 12))
    calculator.place(x=550, y=600)
    


def fill_screen():
    ycor = 50
    for i in range(6):
        for j in range(1, 11):
            wordi = Label(window, font=('Helvetica bold', 12), text=random.choice(words))
            wordi.config(bg='White')
            wordi.place(x=(j * 70), y=ycor)
            words_to_type.append(wordi['text'])
            highlight_word.append(wordi)
        ycor += 90



window = Tk()
timer = Label(window, font=('Helvetica bold', 26))
timer.place(x=740, y=0)
timer.config(bg='White')

window.configure(bg="White")
typer = Entry(window)
typer.focus()
typer.place(x=350, y=550)

window.bind("<Return>", highlight_text)
window.bind("<Return>", get_text)



file = open("./WordsPerMinute/wpm.txt", "r")

window.title("WPM Counter")
window.geometry("800x625")





words = []
for line in file.readlines():
    words.append(line.strip())



fill_screen()

if counter - 1 == 0:
    highlight_word[0].config(bg='#87A2FB')


countdown(60)
    


window.mainloop()