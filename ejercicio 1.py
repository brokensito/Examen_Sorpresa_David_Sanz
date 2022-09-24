
import math

class Punto:

    def __init__(self, valor_x, valor_y):

        self.valor_x = valor_x
        self.valor_y = valor_y

    def __str__(self):
        return f"("+str(self.valor_x)+","+str(self.valor_y)+")"

    def cuadrante(self):
        
        if self.valor_x==0 and self.valor_y!=0:
            self.cuadrante = print("Esta situado sobre el eje Y")
        
        elif self.valor_x!=0 and self.valor_y==0:
            self.cuadrante = print("Esta situado sobre el eje X")

        elif self.valor_x==0 and self.valor_y==0:
            self.cuadrante = print("Esta situado sobre el origen")

        elif self.valor_x>0 and self.valor_y>0:
            self.cuadrante = print("Esta en el PRIMER cuadrante ")

        elif self.valor_x<0 and self.valor_y>0:
            self.cuadrante = print("Esta en el SEGUNDO cuadrante ")

        elif self.valor_x<0 and self.valor_y<0:
            self.cuadrante = print("Esta en el TERCER cuadrante ")

        elif self.valor_x>0 and self.valor_y<0:
            self.cuadrante = print("Esta en el CUARTO cuadrante ")


    def vector(self,nuevo_x, nuevo_y):
        self.vector = print(f"("+str(nuevo_x-self.valor_x)+","+str(nuevo_y-self.valor_y)+")")

    
    def distancia(self,nuevo_x,nuevo_y):
        self.distancia = print("{:.3f}".format(math.sqrt(((nuevo_x-self.valor_x)**2)+((nuevo_y-self.valor_y)**2))))
            

class Rectangulo():

    def __init__(self, punto_i, punto_f):

        self.punto_i = punto_i
        self.punto_f = punto_f

    


        
A = Punto(2,3)
B = Punto(5,5)
C = Punto(-3,-1)
D = Punto(0,0)

Cuadrante_A = A.cuadrante()
Cuadrante_B = B.cuadrante()
Cuadrante_D = D.cuadrante()


print(A)
print(B)
print(C)
print(D)

AB = A.vector(5,5)
BA = B.vector(2,3)









    




















