import matplotlib.pyplot as plt
# import prepara_banco as pb

# pb.select(data) = [ a, b, c ,d ]

x = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai']
y = [30, 17, 13, 16, 17]

plt.ylabel ('temperaruta')
plt.xlabel('Mês')
plt.plot(x,y)

plt.show()
