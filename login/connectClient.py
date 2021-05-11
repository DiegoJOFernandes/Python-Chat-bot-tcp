import threading
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.3', 55555))
class StartConnectClient:
		
	def chooseName(name="Teste"):
		nickname = name

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


a = StartConnectClient()