from tkinter import *

janelaChat = Tk()
# janelaChat.geometry("700x350")
def send():
  mensagem = "Client1 -> "+entradaTexto.get()
  txt.insert(END, "\n"+mensagem)
  if(entradaTexto.get() == "Oi"):
    txt.insert(END, "\n"+"Bot -> Hello")
  entradaTexto.delete(0, END)

txt = Text(janelaChat)
txt.grid(row = 0,column = 0, columnspan = 2)
janelaChat.title("Chat - Data - Client1/Client2")
entradaTexto = Entry(janelaChat, width = 70)
enviar = Button(janelaChat, text = "Enviar", command = send)
enviar.grid(row = 1, column = 1)

entradaTexto.grid(row = 1, column = 0)

janelaChat.mainloop()

# janelaChat2 = Tk()
# txt2 = Text(janelaChat2)
# txt2.grid(row = 0,column = 0, columnspan = 2)

# janelaChat2.mainloop()


