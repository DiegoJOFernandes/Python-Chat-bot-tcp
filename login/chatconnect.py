
import threading
import socket
import DataBaser
from tkinter import *

class ChatConnect:

    janelaChat = Tk()
    janelaChat.geometry("700x300")
    janelaChat.configure(background="white")

    labelEnterServer = Label(janelaChat, text="Conenctar ao server:", font=("Century Gothic", 12), bg="white", fg="black")
    labelEnterServer.place(x=120,y=110)

    InsertServer = Entry(janelaChat,width=28)
    InsertServer.place(x=300,y=112)



    def EnterRoom():
      nickname = "Cliente"

      nameConnection = InsertServer.get()

      client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      client.connect((nameConnection, 55555))

      def receive():
        while True:
            try:
                # Receive Message From Server
                # If 'NICK' Send Nickname
                message = client.recv(1024).decode("ascii")
                if message == "NICK":
                    client.send(nickname.encode("ascii"))
                else:
                    print(message)
            except:
                # Close Connection When Error
                print("Ocorreu um erro!")
                client.close()
                break

    Room = Button(janelaChat, text="Entrar na Sala", command=EnterRoom)
    Room.place(x=300,y=150)


    janelaChat.mainloop()
