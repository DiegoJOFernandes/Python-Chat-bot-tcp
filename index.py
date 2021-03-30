#importar as bibliotecas
import tkinter
from tkinter import *
from tkinter import messagebox


#criar nossa janela 
jan = Tk()
jan.title("APS- Bate Papo Unip")
jan.geometry("600x300")
jan.configure(background="white")
jan.resizable(width=False, height=False)
jan.attributes("-alpha", 1.0)

#jan.iconbitmap(default="#")

#---------- carregar imagens 
logo = PhotoImage(file="interface/fixture/et.png")


#--- Widgets ------------
LeftFrame = Frame(jan,width=200, height=300,bg="white", relief="raise")
LeftFrame.pack(side=LEFT)

RightFrame = Frame(jan, width=395, height=300,bg="white", relief="raise")
RightFrame.pack(side=RIGHT)

# ----------Logo label ---------
LogoLabel = Label(LeftFrame, image=logo, bg="white")
LogoLabel.place(x=70,y=100)


# --------------------- User

UserLabel = Label(RightFrame, text="Username:", font=("Century Gothic", 16), bg="white",fg="black")
UserLabel.place(x=5,y=102)

UserEntry= Entry(RightFrame,width=28)
UserEntry.place(x=140,y=110)

## 
PassLabel = Label(RightFrame, text="Password:", font=("Century Gothic", 16), bg="white", fg="black")
PassLabel.place(x=5,y=152)

PassEntry = Entry(RightFrame, width=28, show="*")
PassEntry.place(x=140,y=160)

#botoes
LoginButton = Button(RightFrame, text="Login", width=30)
LoginButton.place(x=100, y=225)

BackButton = Button(RightFrame, text="Voltar", width=30)

def Register():
    #removendo widgets de login

    RegisterButton.place(x=100, y=225)
    BackButton.place(x=100, y=260)
    #inserindo widgets

    NomeLabel = Label(RightFrame, text="Nome:", font=("Century Gothic", 16), bg="white", fg="black")
    NomeLabel.place(x=5,y=5)

    NomeEntry = Entry(RightFrame, width=28)
    NomeEntry.place(x=140, y=16)

    EmailLabel = Label(RightFrame, text="E-mail:", font=("Century Gothic", 16), bg="white",fg="black")
    EmailLabel.place(x=5,y=55)

    EmailEntry= Entry(RightFrame,width=28)
    EmailEntry.place(x=140,y=66)



RegisterButton = Button(RightFrame,text="Register", width=30, command=Register)
RegisterButton.place(x=100, y=260)

# def login_user():
    


jan.mainloop()#significa que as propriedades da Jan acabou