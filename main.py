from tkinter import *
import numpy as np
import tkinter.font as font
from PIL import ImageTk, Image
from pynput import keyboard
import stuff
import random

key_cpt = 0
isKeyJ1 = False
isKeyJ2 = False
KeyJ1 = ""
KeyJ2 = ""
scoreJ1 = 0
scoreJ2 = 0
winJ1 = False
winJ2 = False


mat1 = [[(1, 1), (0, 5), (0, 10)],
       [(5, 0), (-5, -5), (-5, -10)],
       [(10, 0), (-10, -5), (-10, -10)]]

mat2 = [[(2, 2), (0, 10), (0, 20)],
        [(10, 0), (-10, -10), (-10, -20)],
        [(20, 0), (-20, -10), (-20, -20)]]

mat3 = [[(3, 3), (0, 20), (0, 30)],
        [(20, 0), (-20, -20), (-20, -30)],
        [(30, 0), (-30, -20), (-30, -30)]]

# generate random card number
card_number_list = [1, 2, 3]   
card_number = random.choice(card_number_list) 

def on_click(label):
   label.after(1000, label.destroy())


def play(event):
    global key_cpt
    global isKeyJ1
    global isKeyJ2
    global KeyJ1
    global KeyJ2
    global mat1
    global mat2
    global mat3
    global scoreJ1
    global scoreJ2
    global winJ1
    global winJ2
    global card_number
    global converted_resized_matrixImage


    if(card_number == 1):
        mat = mat1
    elif(card_number == 2):
        mat = mat2
    else:
        mat = mat3

    cpt = 0


    if((not isKeyJ1) and (event.char == "q" or event.char == "s" or event.char == "d")):
        KeyJ1 = event.char
        isKeyJ1 = True
    elif((not isKeyJ2) and (event.char == "1" or event.char == "2" or event.char == "3")):
        KeyJ2 = event.char
        isKeyJ2 = True
    elif(event.keysym =='Escape'):
        stuff.openGameMatrix(card_number)

    #les deux J ont cliqué sur une de leurs touches
    if(isKeyJ1 and isKeyJ2 and not winJ1 and not winJ2):
        if(KeyJ1 == "q" and KeyJ2 == "1"):
            print("q1")
            scoreJ1, scoreJ2, winJ1, winJ2 = stuff.maj_Score(app, 0, 0, mat)
            update_score(1, scoreJ1)
            update_score(2, scoreJ2)

            if (cpt > 0):
                selectedKeyP1.destroy()
                selectedKeyP2.destroy()
            cpt += 1
            stuff.border(app, "q1", cpt, selectedKeyP1, selectedKeyP2)

        elif (KeyJ1 == "q" and KeyJ2 == "2"):
            print("q2")
            scoreJ1, scoreJ2, winJ1, winJ2 = stuff.maj_Score(app, 0, 1, mat)
            update_score(1, scoreJ1)
            update_score(2, scoreJ2)

            if (cpt > 0):
                selectedKeyP1.destroy()
                selectedKeyP2.destroy()
            cpt += 1
            stuff.border(app, "q2", cpt, selectedKeyP1, selectedKeyP2)
        elif(KeyJ1 == "q" and KeyJ2 == "3"):
            print("q3")
            scoreJ1, scoreJ2, winJ1, winJ2 = stuff.maj_Score(app, 0, 2, mat)
            
            update_score(1, scoreJ1)
            update_score(2, scoreJ2)

            if (cpt > 0):
                selectedKeyP1.destroy()
                selectedKeyP2.destroy()
            cpt += 1
            stuff.border(app, "q3", cpt, selectedKeyP1, selectedKeyP2)
        elif(KeyJ1 == "s" and KeyJ2 == "1"):
            print("s1")
            scoreJ1, scoreJ2, winJ1, winJ2 = stuff.maj_Score(app, 1, 0, mat)

            update_score(1, scoreJ1)
            update_score(2, scoreJ2)

            if (cpt > 0):
                selectedKeyP1.destroy()
                selectedKeyP2.destroy()
            cpt += 1
            stuff.border(app, "s1", cpt, selectedKeyP1, selectedKeyP2)
        elif(KeyJ1 == "s" and KeyJ2 == "2"):
            print("s2")
            scoreJ1, scoreJ2, winJ1, winJ2 = stuff.maj_Score(app, 1, 1, mat)

            update_score(1, scoreJ1)
            update_score(2, scoreJ2)

            if (cpt > 0):
                selectedKeyP1.destroy()
                selectedKeyP2.destroy()
            cpt += 1
            stuff.border(app, "s2", cpt, selectedKeyP1, selectedKeyP2)
        elif(KeyJ1 == "s" and KeyJ2 == "3"):
            print("s3")
            scoreJ1, scoreJ2, winJ1, winJ2 = stuff.maj_Score(app, 1, 2, mat)

            update_score(1, scoreJ1)
            update_score(2, scoreJ2)

            if (cpt > 0):
                selectedKeyP1.destroy()
                selectedKeyP2.destroy()
            cpt += 1
            stuff.border(app, "s3", cpt, selectedKeyP1, selectedKeyP2)
        elif(KeyJ1 == "d" and KeyJ2 == "1"):
            print("d1")
            scoreJ1, scoreJ2, winJ1, winJ2 = stuff.maj_Score(app, 2, 0, mat)
            
            update_score(1, scoreJ1)
            update_score(2, scoreJ2)

            if (cpt > 0):
                selectedKeyP1.destroy()
                selectedKeyP2.destroy()
            cpt += 1
            stuff.border(app, "d1", cpt, selectedKeyP1, selectedKeyP2)
        elif(KeyJ1 == "d" and KeyJ2 == "2"):
            print("d2")
            scoreJ1, scoreJ2, winJ1, winJ2 = stuff.maj_Score(app, 2, 1, mat)

            update_score(1, scoreJ1)
            update_score(2, scoreJ2)

            if (cpt > 0):
                selectedKeyP1.destroy()
                selectedKeyP2.destroy()
            cpt += 1
            stuff.border(app, "d2", cpt, selectedKeyP1, selectedKeyP2)
        elif(KeyJ1 == "d" and KeyJ2 == "3"):
            print("d3")
            scoreJ1, scoreJ2, winJ1, winJ2 = stuff.maj_Score(app, 2, 2, mat)

            update_score(1, scoreJ1)
            update_score(2, scoreJ2)

            if (cpt > 0):
                selectedKeyP1.destroy()
                selectedKeyP2.destroy()
                
            stuff.border(app, "d3", cpt, selectedKeyP1, selectedKeyP2)
            cpt += 1
        isKeyJ1 = False
        isKeyJ2 = False
    if(winJ1 or winJ2):
        stuff.game_over_window(event, app, winJ1, winJ2)



app = Tk()


def update_score(player, score):
    if(player == 1):
        scoreValuePlayer1.config(text=str(score)+"/100")
    else:
        scoreValuePlayer2.config(text=str(score)+"/100")


app.title("Trust Card Game")
app.minsize(1000, 700)
app.maxsize(1000, 700)
app.configure(bg='green')

Title = Label(app, text="Trust Card Game", font=(
    "Helvitica Bold", 35), background="green", fg="white")
Title.pack(anchor=N)

myFont = font.Font(family='Helvetica', size=15, weight='bold')

scoreTextPlayer1 = Label(app, text="Score Player 1",
                         background="green", fg="white")
scoreTextPlayer1.place(x='30', y='100')
scoreTextPlayer1['font'] = myFont

scoreValuePlayer1 = Label(app, text=str(scoreJ1)+"/100", background="green", fg="white")
scoreValuePlayer1.place(x='60', y='130')
scoreValuePlayer1['font'] = myFont


scoreTextPlayer2 = Label(app, text="Score Player 2",
                         background="green", fg="white")
scoreTextPlayer2.place(x='840', y='100')
scoreTextPlayer2['font'] = myFont

scoreValuePlayer2 = Label(app, text=str(scoreJ2)+"/100", background="green", fg="white")
scoreValuePlayer2.place(x='880', y='130')
scoreValuePlayer2['font'] = myFont


card1 = "ressources/"+str(card_number)+"1"+".png"
card1Image = Image.open(card1)
resized_image1 = card1Image.resize((160,250), Image.ANTIALIAS)
converted_image1= ImageTk.PhotoImage(resized_image1)

card1Label = Label(app, image= converted_image1, width=160, height=250, background="green")
card1Label.place(x='200', y='190')

card2 = "ressources/"+str(card_number)+"2"+".png"
card2Image = Image.open(card2)
resized_image2 = card2Image.resize((150,250), Image.ANTIALIAS)
converted_image2= ImageTk.PhotoImage(resized_image2)

card2Label = Label(app, image=converted_image2, width=150,
                   height=250, background="green")
card2Label.place(x='425', y='190')

card3 = "ressources/"+str(card_number)+"3"+".png"
card2Image = Image.open(card3)
resized_image3 = card2Image.resize((150,250), Image.ANTIALIAS)
converted_image3= ImageTk.PhotoImage(resized_image3)

card3Label = Label(app, image=converted_image3, width=150,
                   height=250, background="green")
card3Label.place(x='650', y='190')

Player1Key = Label(app, text="Player1 KeyBind", background="green", fg="white")
Player1Key.place(x='30', y='480')
Player1Key['font'] = myFont

Player2Key = Label(app, text="Player2 KeyBind", background="green", fg="white")
Player2Key.place(x='30', y='550')
Player2Key['font'] = myFont

#Player 1 Keys
Qkey = "ressources/q.png"
QkeyImage = Image.open(Qkey)
resized_Qkey = QkeyImage.resize((50,50), Image.ANTIALIAS)
converted_resized_Qkey= ImageTk.PhotoImage(resized_Qkey)

Q = Label(app, image= converted_resized_Qkey, width=50, height=50, background="green")
Q.place(x='230', y='460')

Skey = "ressources/s.png"
SkeyImage = Image.open(Skey)
resized_Skey = SkeyImage.resize((50,50), Image.ANTIALIAS)
converted_resized_Skey= ImageTk.PhotoImage(resized_Skey)

S = Label(app, image= converted_resized_Skey, width=50, height=50, background="green")
S.place(x='460', y='460')

Dkey = "ressources/d.png"
# print("c: ", c)
DkeyImage = Image.open(Dkey)
resized_Dkey = DkeyImage.resize((50,50), Image.ANTIALIAS)
converted_resized_Dkey= ImageTk.PhotoImage(resized_Dkey)

D = Label(app, image= converted_resized_Dkey, width=50, height=50, background="green")
D.place(x='690', y='460')

#Player 2 keys
num1key = "ressources/1.png"
num1keyImage = Image.open(num1key)
resized_1key = num1keyImage.resize((50,50), Image.ANTIALIAS)
converted_resized_1key= ImageTk.PhotoImage(resized_1key)

num1 = Label(app, image= converted_resized_1key, width=50, height=50, background="green")
num1.place(x='230', y='530')

num2key = "ressources/2.png"
num2keyImage = Image.open(num2key)
resized_2key = num2keyImage.resize((50,50), Image.ANTIALIAS)
converted_resized_2key= ImageTk.PhotoImage(resized_2key)

num2 = Label(app, image= converted_resized_2key, width=50, height=50, background="green")
num2.place(x='460', y='530')

num3key = "ressources/3.png"
num3keyImage = Image.open(num3key)
resized_3key = num3keyImage.resize((50,50), Image.ANTIALIAS)
converted_resized_3key= ImageTk.PhotoImage(resized_3key)

num3 = Label(app, image= converted_resized_3key, width=50, height=50, background="green")
num3.place(x='690', y='530')

#open game matrix window
myFontescapKey = font.Font(family='Helvetica', size=15, weight='bold')

matrixGame = Label(app, text="Press ",
                   background="green", fg="white")
matrixGame['font'] = myFontescapKey
matrixGame.place(x='380', y='650')

escapKey = "ressources/escap.png"
escapKeyImage = Image.open(escapKey)
resized_escapKey = escapKeyImage.resize((50, 50), Image.ANTIALIAS)
converted_resized_escapKey = ImageTk.PhotoImage(resized_escapKey)

escap = Label(app, image=converted_resized_escapKey, width=50, height=50, background="green")
escap.place(x='445', y='640')

matrixGame = Label(app, text="to Open Game Matrix", background="green", fg="white")
matrixGame['font'] = myFontescapKey
matrixGame.place(x='500', y='650')



#draw (*) near to choosed card in border() fct
myFont = font.Font(family='Helvetica', size=40, weight='bold')
selectedKeyP1 = Label(app, text="*", background="green", fg="white")
selectedKeyP1['font'] = myFont

selectedKeyP2 = Label(app, text="*", background="green", fg="white")
selectedKeyP2['font'] = myFont

#draw game matrix table in game matrix window
# matrix = "ressources/mat1.png"
# matrixImage = Image.open(matrix)
# resized_matrixImage = matrixImage.resize((160,250), Image.ANTIALIAS)
# converted_resized_matrixImage = ImageTk.PhotoImage(resized_matrixImage)

# gmatrix.title("Game Matrix")
# gmatrix.minsize(1000, 700)
# gmatrix.maxsize(1000, 700)
# gmatrix.configure(bg='green')


#listen to any key
app.bind('<Any-KeyPress>', play)



app.mainloop()