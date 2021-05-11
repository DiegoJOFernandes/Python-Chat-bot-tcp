from tkinter import *
import connectClient

# root = Tk()
# root.title("JanelaChata")


class NewChat:
    def __init__(self, master):
		
        myFrame = Frame(master)
        myFrame.grid()

        self.user = "Diego"
        self.user2 = "Lucas"
        self.data = "22/04/2021"

        clientUser = connectClient.StartConnectClient()
        clientUser.chooseName(self.user)

        titleChat = (
            f"Chat - Conversa de {self.user} com {self.user2} - Data {self.data}"
        )
        master.title(titleChat)

        self.txt = Text(master)
        self.txt.grid(row=0, column=0, columnspan=2)

        self.entradaTexto = Entry(master, width=70)
        self.entradaTexto.grid(row=1, column=0)

        def send():
            self.mensagem = self.entradaTexto.get()
            self.txt.insert(END, "\n" + self.mensagem)
            b.write(self.user, self.mensagem)
            entradaTexto.delete(0, END)

        self.enviar = Button(master, text="Enviar", command=send)
        self.enviar.grid(row=1, column=1)

        # janelaChat2 = Tk()
        # txt2 = Text(janelaChat2)
        # txt2.grid(row = 0,column = 0, columnspan = 2)

        # janelaChat2.mainloop()
