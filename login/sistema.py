# importar as bibliotecas
from tkinter import *
from tkinter import messagebox
import DataBaser
from menu import *


class Systema:

    # import menu

    # criar nossa janela
    jan = Tk()
    jan.title("APS- Bate Papo Unip")
    jan.geometry("700x300")
    jan.configure(background="white")
    jan.resizable(width=False, height=False)
    jan.attributes("-alpha", 0.7)
    jan.wait_visibility(jan)

    # jan.iconbitmap(default="#")

    # ---------- carregar imagens
    # logo = PhotoImage(file="login/fixture/cypress.png")

    # --- Widgets ------------
    LeftFrame = Frame(jan, width=200, height=300, bg="white", relief="raise")
    LeftFrame.pack(side=LEFT)

    RightFrame = Frame(jan, width=395, height=300, bg="white", relief="raise")
    RightFrame.pack(side=RIGHT)

    # ----------Logo label ---------
    # LogoLabel = Label(LeftFrame, image=logo, bg="white")
    # LogoLabel.place(x=-50,y=-15)

    # --------------------- User

    UserLabel = Label(
        RightFrame,
        text="Username:",
        font=("Century Gothic", 16),
        bg="white",
        fg="black",
    )
    UserLabel.place(x=5, y=102)

    UserEntry = Entry(RightFrame, width=28)
    UserEntry.place(x=140, y=110)

    ##
    PassLabel = Label(
        RightFrame,
        text="Password:",
        font=("Century Gothic", 16),
        bg="white",
        fg="black",
    )
    PassLabel.place(x=5, y=152)

    PassEntry = Entry(RightFrame, width=28, show="*")
    PassEntry.place(x=140, y=160)

    def login_user():
        DataBaser.cursor.execute(
            """
    SELECT * FROM Users
    WHERE (user = ? AND password = ?)
    """,
            (user, password),
        )
        print("")
        VerifyLogin = DataBaser.cursor.fetchone
        try:
            if user in VerifyLogin and password in VerifyLogin:
                messagebox.showinfo(
                    title="Autentication", message="Confirmado! Seja Bem-vindo!"
                )
        except:
            messagebox.showerror(
                title="Autentication", message="Usuário ou senha incorreta!"
            )

    # botoes
    LoginButton = Button(RightFrame, text="Login", width=20, command=login_user)
    LoginButton.place(x=100, y=225)

    def Register():
        # removendo widgets de login
        LoginButton.place(x=5000)
        RegisterButton.place(x=5000)

        # inserindo widgets no cadastro
        NomeLabel = Label(
            RightFrame,
            text="Nome:",
            font=("Century Gothic", 16),
            bg="white",
            fg="black",
        )
        NomeLabel.place(x=5, y=5)
        NomeEntry = Entry(RightFrame, width=28)
        NomeEntry.place(x=140, y=16)
        EmailLabel = Label(
            RightFrame,
            text="E-mail:",
            font=("Century Gothic", 16),
            bg="white",
            fg="black",
        )
        EmailLabel.place(x=5, y=55)
        EmailEntry = Entry(RightFrame, width=28)
        EmailEntry.place(x=140, y=66)

        def RegisterToDataBase():
            name = NomeEntry.get()
            email = EmailEntry.get()
            user = UserEntry.get()
            password = PassEntry.get()

            if name == "" and email == "" and user == "" and password == "":
                messagebox.showerror(
                    title="Preenchimento dos dados", message="Preencha todos os campos!"
                )
            else:
                DataBaser.cursor.execute(
                    """ 
        INSERT INTO Users(name,email,user,password) VALUES(?,?,?,?)
        """,
                    (name, email, user, password),
                )
                DataBaser.conn.commit()
                messagebox.showinfo(
                    title="Status cadastro", message="Cadastro realizado com sucesso!"
                )

        Register = Button(
            RightFrame, text="Salvar", width=20, command=RegisterToDataBase
        )
        Register.place(x=100, y=225)

        def BackToLogin():
            NomeLabel.place(x=5000)
            NomeEntry.place(x=5000)
            EmailLabel.place(x=5000)
            EmailEntry.place(x=5000)
            Register.place(x=5000)

            LoginButton.place(x=100)
            RegisterButton.place(x=100)
            Back.place(x=5000)

        Back = Button(RightFrame, text="Voltar", width=20, command=BackToLogin)
        Back.place(x=100, y=260)

    RegisterButton = Button(RightFrame, text="Cadastre-se", width=20, command=Register)
    RegisterButton.place(x=100, y=260)

    # def ListData():

    # def login_user():

    jan.mainloop()  # significa que as propriedades da Jan acabou
