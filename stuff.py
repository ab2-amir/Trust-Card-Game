import numpy as np
from tkinter import *
import tkinter.font as font
from PIL import ImageTk, Image

scoreJ1 = 0
scoreJ2 = 0
winJ1 = False
winJ2 = False

max_points = 100

mat = [[(1, 1), (0, 5), (0, 10)],
       [(5, 0), (-5, -5), (-5, -10)],
       [(10, 0), (-10, -5), (-10, -10)]]

mat2 = [[(2, 2), (0, 10), (0, 20)],
       [(10, 0), (-10, -10), (-10, -20)],
       [(20, 0), (-20, -10), (-20, -20)]]

strat1 = ["COOPERE", "TRAHIR", "MASTERCLASS"]
strat2 = ["COOPERE", "TRAHIR", "MASTERCLASS"]


def max_col(mat):
    i = 0
    max = ()
    list_max = []

    while (i < len(mat[0])):
        j = 0
        list_col = []

        while (j < len(mat)):
            list_col.append(mat[j][i][0])
            j += 1
        max = (np.argmax(list_col), i)
        list_max.append(max)
        i += 1

    return list_col, list_max


def max_row(mat):
    i = 0
    max = ()
    list_max = []
    while (i < len(mat)):
        j = 0
        list_row = []

        while (j < len(mat[0])):
            list_row.append(mat[i][j][1])
            j += 1
        max = (i, np.argmax(list_row))
        list_max.append(max)
        i += 1

    return list_row, list_max


def nash(mat5):
    liste1, max1 = max_col(mat5)
    liste2, max2 = max_row(mat5)

    x1 = 0
    nash = []
    while (x1 < (len(max1))):
        x2 = 0
        while (x2 < (len(max2))):
            if (max1[x1] == max2[x2]):
                # print("L'équilibre de NASH est:", max1[x1], ",", max2[x2])
                nash.append(max1[x1])
            x2 += 1
        x1 += 1
    return nash


def removeOldLabel(gainsValuePlayer1, gainsValuePlayer2):
    gainsValuePlayer1.destroy()
    gainsValuePlayer2.destroy()


def maj_Score(app, index_carteJ1, index_carteJ2, mat):
    global scoreJ1
    global scoreJ2
    global winJ1
    global winJ2

    myFont = font.Font(family='Helvetica', size=15, weight='bold')


    gains = mat[index_carteJ1][index_carteJ2]
    print("Les gains des cartes choisie sont: ", gains)
    scoreJ1 += gains[0]
    scoreJ2 += gains[1]
    print("Scors J1: ", scoreJ1, "Score J2: ", scoreJ2)


    #valeur de gains ou de perte
    if(gains[0] >= 0):
        gainsValuePlayer1 = Label(
            app, text="+"+str(gains[0]), background="green", fg="white")
        gainsValuePlayer1.place(x='80', y='160')
        gainsValuePlayer1['font'] = myFont
    else:
        gainsValuePlayer1 = Label(
            app, text=gains[0], background="green", fg="white")
        gainsValuePlayer1.place(x='80', y='160')
        gainsValuePlayer1['font'] = myFont  

    if (gains[1] >= 0):
        gainsValuePlayer2 = Label(
            app, text="+"+str(gains[1]), background="green", fg="white")
        gainsValuePlayer2.place(x='900', y='160')
        gainsValuePlayer2['font'] = myFont
    else:
        gainsValuePlayer2 = Label(
            app, text=gains[1], background="green", fg="white")
        gainsValuePlayer2.place(x='900', y='160')
        gainsValuePlayer2['font'] = myFont

    #call function to remove old label to draw new one on it
    #replace "gains"
    app.after(1500, lambda: removeOldLabel(
        gainsValuePlayer1, gainsValuePlayer2))

    if(scoreJ1 >= max_points and scoreJ2 < max_points):
        winJ1 = True
        print("======> FIN DE LA PARTIE\n======> J1 a gagné")
    elif (scoreJ2 >= max_points and scoreJ1 < max_points):
        winJ2 = True
        print("======> FIN DE LA PARTIE\n======> J2 a gagné")
    elif (scoreJ1 >= max_points and scoreJ2 >= max_points):
        winJ1 = True
        winJ2 = True
    
    return scoreJ1, scoreJ2, winJ1, winJ2


def game_over_window(event, app, winJ1, winJ2):
    go = Tk()
    go.title("Game Over")

    go.minsize(1000, 700)
    go.maxsize(1000, 700)

    if(winJ1 and not winJ2):
        go.configure(bg="gold")

        Title = Label(go, text="The winner is Player 1", font=(
            "Helvitica Bold", 35), background="gold", fg="black")
        Title.place(x='300', y='200')

        textScoreP1 = "Score Player 1: "+str(scoreJ1)
        scoreP1 = Label(go, text=textScoreP1, font=(
            "Helvitica Bold", 20), background="gold", fg="black")
        scoreP1.place(x='370', y='350')

        textScoreP2 = "Score Player 2: "+str(scoreJ2)
        scoreP2 = Label(go, text=textScoreP2, font=(
            "Helvitica Bold", 20), background="gold", fg="black")
        scoreP2.place(x='370', y='400')

        
    elif(winJ2 and not winJ1):
        go.configure(bg="gold")

        Title = Label(go, text="The winner is Player 2", font=(
            "Helvitica Bold", 35), background="gold", fg="black")
        Title.place(x='300', y='200')

        textScoreP1 = "Score Player 1: "+str(scoreJ1)
        scoreP1 = Label(go, text=textScoreP1, font=(
            "Helvitica Bold", 20), background="gold", fg="black")
        scoreP1.place(x='370', y='350')

        textScoreP2 = "Score Player 2: "+str(scoreJ2)
        scoreP2 = Label(go, text=textScoreP2, font=(
            "Helvitica Bold", 20), background="gold", fg="black")
        scoreP2.place(x='370', y='400')
    else:
        go.configure(bg="gray")

        Title = Label(go, text="No winner.. Equality", font=(
            "Helvitica Bold", 35), background="gray", fg="black")
        Title.place(x='300', y='200')

        textScoreP1 = "Score Player 1: "+str(scoreJ1)
        scoreP1 = Label(go, text=textScoreP1, font=(
            "Helvitica Bold", 20), background="gray", fg="black")
        scoreP1.place(x='370', y='350')

        textScoreP2 = "Score Player 2: "+str(scoreJ2)
        scoreP2 = Label(go, text=textScoreP2, font=(
            "Helvitica Bold", 20), background="gray", fg="black")
        scoreP2.place(x='370', y='400')

    app.destroy()


def border(app, keys, cpt, selectedKeyP1, selectedKeyP2):
 
    if(keys=="q1"):
        
        selectedKeyP1.place(x='200', y='465')
        selectedKeyP2.place(x='200', y='540')

    elif (keys=="q2"):
      
        selectedKeyP1.place(x='200', y='465')
        selectedKeyP2.place(x='420', y='540')
    elif (keys=="q3"):

        selectedKeyP1.place(x='200', y='465')
        selectedKeyP2.place(x='655', y='540')
    elif (keys=="s1"):
    
        selectedKeyP1.place(x='420', y='465')
        selectedKeyP2.place(x='200', y='540')
    elif (keys=="s2"):
        selectedKeyP1.place(x='420', y='465')
        selectedKeyP2.place(x='420', y='540')
    elif (keys=="s3"):
        selectedKeyP1.place(x='420', y='465')
        selectedKeyP2.place(x='655', y='540')
    elif (keys=="d1"):
        selectedKeyP1.place(x='655', y='465')
        selectedKeyP2.place(x='200', y='540')
    elif (keys=="d2"):
        selectedKeyP1.place(x='655', y='465')
        selectedKeyP2.place(x='420', y='540')
    elif (keys=="d3"):
        selectedKeyP1.place(x='655', y='465')
        selectedKeyP2.place(x='655', y='540')


def openGameMatrix(card_number):  
    global strat1
    global strat2
    myFont = font.Font(family='Helvetica', size=15, weight='bold')
  
    gmatrix = Toplevel()
    gmatrix.title("Game Matrix")

    gmatrix.minsize(1000, 700)
    gmatrix.maxsize(1000, 700)
    gmatrix.configure(bg='green')

    Title = Label(gmatrix, text="Game Matrix", font=(
        "Helvitica Bold", 35), background="green", fg="white")
    Title.pack(anchor=N)

    matrix = "ressources/mat"+str(card_number)+".png"
    matrixImage = Image.open(matrix)
    resized_matrixImage = matrixImage.resize((600,150), Image.ANTIALIAS)
    converted_resized_matrixImage = ImageTk.PhotoImage(resized_matrixImage, master=gmatrix)

    matrixLabel = Label(master=gmatrix, image= converted_resized_matrixImage, width=600, height=150)

    matrixLabel.place(x='200', y='150')

    result = nash(mat)

    ENtxt = Label(gmatrix, text="L'équilibre de NASH:", background="green", fg="white")
    ENtxt.place(x='200', y='330')
    ENtxt['font'] = myFont

    ENash1 = Label(gmatrix, text="("+str(strat1[result[0][0]])+", "+str(strat2[result[0][1]])+")", background="green", fg="white")
    ENash1.place(x='220', y='380')
    ENash1['font'] = myFont

    ENash2 = Label(gmatrix, text="("+str(strat1[result[1][0]])+", "+str(strat1[result[1][1]])+")", background="green", fg="white")
    ENash2.place(x='220', y='410')
    ENash2['font'] = myFont

    for i in range(len(result)):
        print("res", result)
        print("L'équilibre de NASH est:(", strat1[result[i][0]], ", ", strat2[result[i][1]], ")")


    gmatrix.mainloop()


# result = nash(mat)

# for i in range(len(result)):
#     print("L'équilibre de NASH est:(", strat1[result[i][0]], ", ", strat2[result[i][1]], ")")

# list_cartes = ["Carte Coopère", "Carte Trahir", "Carte MasterClass"]
# win = False

# while(not win):
#     print("\nChoisir le numéro de la carte: \n1-Carte Coopère\n2-Carte Trahir\n3-Carte MasterClass\n")
#     num = ""
#     num = str(input("Saisissez votre réponse pour J1 et J2 simultanémant:  "))

#     if(num == "11" or num == "22" or num == "33" or num == "12" or num == "21" or num == "13" or num == "31" or num == "23" or num == "32"):
#         index_carteJ1 = int(num[0])-1
#         index_carteJ2 = int(num[1])-1
#         carteJ1 = (list_cartes[index_carteJ1])
#         carteJ2 = (list_cartes[index_carteJ2])
#         print("carte J1", carteJ1)
#         print("carte J2", carteJ2)

#         maj_Score(index_carteJ1, index_carteJ2, mat)
#         if(scoreJ1 >= max_points or scoreJ2 >= max_points):
#             if (scoreJ1 >= max_points):
#                 print("======> FIN DE LA PARTIE\n======> J1 a gagné")
#             else:
#                 print("======> FIN DE LA PARTIE\n======> J2 a gagné")
#             win = True

