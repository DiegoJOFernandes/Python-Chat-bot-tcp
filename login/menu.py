from tkinter import *

menu = Tk()

menu.title("Teste")
menu.geometry("700x300")
menu.configure(background="white")
menu.resizable(width=False, height=False)

chat = Button(menu, text= "Chat", width=18)
chat.place(x=100, y=90)
insertdata = Button(menu, text="Inserir dados", width= 18)
insertdata.place(x=100, y=180)
manipulateData = Button(menu, text= "Gerenciar dados", width=18)
manipulateData.place(x=350, y=90)
generateGraphics = Button(menu, text= "Gerar Gráficos", width=18)
generateGraphics.place(x=350, y=180)



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

menu.mainloop()

