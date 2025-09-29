import matplotlib.pyplot as plt

categorias = ["A", "B", "C", "D", "E" ]
Valores = [5, 10, 15, 20, 25]
Colores = ['green', 'brown', 'red', 'purple', 'orange' ]
plt.bar(categorias, Valores, color=Colores)

plt.xlabel('categorias')
plt.ylabel('valores')
plt.title('grafica de colores')
plt.show()