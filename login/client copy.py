class ClientGUI:
	
	import threading
	import socket
	import DataBaser

	from tkinter import *


	janelaChat = Tk()
	janelaChat.geometry("700x350")
	janelaChat.configure(background="white")

	labelEnterServer = Label(janelaChat, text="Conenctar ao server:", font=("Century Gothic", 12), bg="white", fg="black")
	labelEnterServer.place(x=120,y=110)
	InsertServer= Entry(janelaChat,width=28)
	InsertServer.place(x=300,y=112)

	enterRoom = Button(janelaChat, text="Entrar na Sala", command=enterRoom)
	enterRoom.pack()

	def enterRoom():
		nickname = "Cliente"
		server = self.InsertServer.get()
		client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	  	client.connect((server, 55555))
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




	# Connecting To Server
	# 
	# client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	# client.connect((server, 55555))


	# Receiving / Listening Function
	# def nickname(user):
	# 	nickname = user
	# # puxar do BD



	# Listening to Server and Sending Nickname
	# def receive():
	#     while True:
	#         try:
	#             # Receive Message From Server
	#             # If 'NICK' Send Nickname
	#             message = client.recv(1024).decode("ascii")
	#             if message == "NICK":
	#                 client.send(nickname.encode("ascii"))
	#             else:
	#                 print(message)
	#         except:
	#             # Close Connection When Error
	#             print("Ocorreu um erro!")
	#             client.close()
	#             break


	# # Sending Messages To Server
	# def write():
	#     while True:
	#         mensagem = "Client1 -> " + entradaTexto.get()
	#         txt.insert(END, "\n" + mensagem)
	#         entradaTexto.delete(0, END)
	#         message = "{}: {}".format("Meu nome", mensagem)
	#         client.send(message.encode("ascii"))


	# # Starting Threads For Listening And Writing
	# receive_thread = threading.Thread(target=receive)
	# receive_thread.start()

	# write_thread = threading.Thread(target=write)
	# write_thread.start()

	# # txt = Text(janelaChat)
	# # txt.grid(row=0, column=0, columnspan=2)
	# # janelaChat.title("Chat - Data - Client1/Client2")
	# # entradaTexto = Entry(janelaChat, width=70)
	# # enviar = Button(janelaChat, text="Enviar", command=write)
	# # enviar.grid(row=1, column=1)

	# entradaTexto.grid(row=1, column=0)

	janelaChat.mainloop()

	# janelaChat2 = Tk()
	# txt2 = Text(janelaChat2)
	# txt2.grid(row = 0,column = 0, columnspan = 2)

	# janelaChat2.mainloop()
