from tkinter import *
import chat

  # import chatconnec as chatclient
  # import server as servidor

menu = Tk()

menu.title("Teste")
menu.geometry("700x300")
menu.configure(background="white")
menu.resizable(width=False, height=False)


class OpcoesMenu:
 
  def __init__(self,master):
    myframe = Frame(master)
    myframe.pack()

    def openChat():
      newWindowChat = Tk()
      newWindowChat.title('janelaChata')
      a = chat.NewChat(newWindowChat)

    self.chat = Button(master, text= "Chat", width=18, command=openChat)
    self.chat.place(x=100, y=90)

    self.insertdata = Button(master, text="Inserir dados", width= 18)
    self.insertdata.place(x=100, y=180)

    self.manipulateData = Button(master, text= "Gerenciar dados", width=18)
    self.manipulateData.place(x=350, y=90)

    self.generateGraphics = Button(master, text= "Gerar Gráficos", width=18)
    self.generateGraphics.place(x=350, y=180)

    menu.mainloop()

  # def Open():
  #   top = Toplevel()
  #   top.title("Menu")


  # def Open_window():
  #   new_windows = Tk()
  #   ab = Label(new_windows,text="New label")
  #   ab.pack()


  # newWindow = Button(menu, text="Nova Janela1", width= 30, command=Open)
  # samplewindow = Button(menu, text="Nova 2", width= 30, command=Open_window)

  # newWindow.pack()
  # samplewindow.pack()

  
m = OpcoesMenu(menu)

