import threading
import socket

class ConnectClients:
	
	#  def __init__(self, master):
	# 		myFrame = Frame(master)
	# 		myFrame.pack()

			# self.labelEnterServer = Label(myFrame, text="Conenctar ao server:", font=("Century Gothic", 12), bg="white", fg="black")
			# self.labelEnterServer.place(x=120,y=110)
			# self.InsertServer= Entry(myFrame,width=28)
			# self.InsertServer.place(x=300,y=112)
			# enterRoom = Button(myFrame, text="Entrar na Sala", command=enterRoom)
			# enterRoom.pack()
	def chooseName(name):
		nickname = name

#  def startConnection():
# 		# Choosing Nickname
# 		# Connecting To Server
	
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client.connect(('127.0.0.1', 55555))

	# Receiving / Listening Function


	# Listening to Server and Sending Nickname
	def receive():
		
	  while True:
	    try:
	      # Receive Message From Server
	      # If 'NICK' Send Nickname
	    	message = client.recv(1024).decode('ascii')
	    	if message == 'NICK':
	    	    client.send(nickname.encode('ascii'))
	    	else:
	    	    print(message)
	    except:
	      # Close Connection When Error
	      print("Ocorreu um erro!")
	      client.close()
	      break
						
	# Sending Messages To Server
	def write(nickname, entryMessage):
		while True:
		  message = '{}: {}'.format(nickname, entryMessage)
		  client.send(message.encode('ascii'))
			
  
	# Starting Threads For Listening And Writing
	receive_thread = threading.Thread(target=receive)
	receive_thread.start()

	write_thread = threading.Thread(target=write)
	write_thread.start()


