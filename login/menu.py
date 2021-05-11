from tkinter import *
#import server
# import chat


  # import chatconnec as chatclient
  # import server as servidor

menu = Tk()

menu.title('Teste')
menu.geometry('700x300')
menu.configure(background='white')
menu.resizable(width=False, height=False)


class OpcoesMenu:
 
  def __init__(self,master):
    myframe = Frame(master)
    myframe.pack()

    # server = server.OpenServer()

    def openChat():
      newWindowChat = Tk()
      newWindowChat.title('janelaChata')
      a = chat.NewChat(newWindowChat)

    self.chat = Button(master, text= 'Chat', width=18, command=openChat)
    self.chat.place(x=100, y=90)

    self.insertdata = Button(master, text='Inserir dados', width= 18)
    self.insertdata.place(x=100, y=180)

    self.manipulateData = Button(master, text= 'Gerenciar dados', width=18)
    self.manipulateData.place(x=350, y=90)

    self.generateGraphics = Button(master, text= 'Gerar Gráficos', width=18)
    self.generateGraphics.place(x=350, y=180)

    self.labelServer = Label(master, text='Conectado ao servidor', font=('Century Gothic', 9), fg='black')

    menu.mainloop()

  # newWindow.pack()
  # samplewindow.pack()

  
m = OpcoesMenu(menu)

