class Punto:

    def __init__(self, valor_x=0, valor_y=0):
        self.valor_x = valor_x
        self.valor_y = valor_y
    
    def generador_puntos(self):
        return (self.valor_x,self.valor_y)
        
    def str(self):
        return f"("+str(Punto(self.valor_x,self.valor_y).generador_puntos()[0])+","+str(Punto(self.valor_x,self.valor_y).generador_puntos()[1])+")"








A = Punto(2,3).str()
B = Punto(5,5).str()
C = Punto(-3,-1).str()
D = Punto().str()

print(A)
print(B)
print(C)
print(D)

