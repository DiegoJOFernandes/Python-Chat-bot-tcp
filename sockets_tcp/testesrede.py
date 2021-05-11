import socket

#Para obter o endereço IP da máquina atual usando o módulo socket, você pode usar o seguinte truque executando 
print(socket.gethostbyname(socket.gethostname()))

# Você sabe que o nosso computador tem muitas interfaces. Se você quiser saber o endereço IP de todas as interfaces, use a interface estendida:
print(socket.gethostbyname_ex(socket.gethostname()))

print(socket.gethostbyaddr())