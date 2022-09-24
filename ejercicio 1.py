
import math

class Punto:

    def __init__(self, valor_x, valor_y):

        self.valor_x = valor_x
        self.valor_y = valor_y

    def __str__(self):
        return f"("+str(self.valor_x)+","+str(self.valor_y)+")"

    def cuadrante(self):
        
        if self.valor_x==0 and self.valor_y!=0:
            self.cuadrante = "Esta situado sobre el eje Y"
            return self.cuadrante
        
        elif self.valor_x!=0 and self.valor_y==0:
            self.cuadrante = "Esta situado sobre el eje X"
            return self.cuadrante

        elif self.valor_x==0 and self.valor_y==0:
            self.cuadrante = "Esta situado sobre el ORIGEN"
            return self.cuadrante

        elif self.valor_x>0 and self.valor_y>0:
            self.cuadrante = "Esta en el PRIMER cuadrante "
            return self.cuadrante

        elif self.valor_x<0 and self.valor_y>0:
            self.cuadrante = "Esta en el SEGUNDO cuadrante "
            return self.cuadrante

        elif self.valor_x<0 and self.valor_y<0:
            self.cuadrante = "Esta en el TERCER cuadrante "
            return self.cuadrante

        elif self.valor_x>0 and self.valor_y<0:
            self.cuadrante = "Esta en el CUARTO cuadrante "
            return self.cuadrante


    def vector(self,nuevo_x, nuevo_y):
        self.vector = "("+str(nuevo_x-self.valor_x)+","+str(nuevo_y-self.valor_y)+")"
        return self.vector
        

    
    def distancia(self,nuevo_x,nuevo_y):
        self.distancia = "{:.3f}".format(math.sqrt(((nuevo_x-self.valor_x)**2)+((nuevo_y-self.valor_y)**2)))
        return self.distancia

class Rectangulo():

     def __init__(self, punto1, punto2):
         self.valor1x = punto1.valor_x
         self.valor1y = punto1.valor_y
         self.valor2x = punto2.valor_x
         self.valor2y = punto2.valor_y
         self.diagonal = punto1.vector(self.valor2x,self.valor2y)
    
     def base(self):
         self.base = self.diagonal



    
### Experimentacion


a= (2,3)
b= (5,5)
c = (-3,-1)
d = (0,0)

A = Punto(a[0],a[1])
B = Punto(b[0],b[1])
C = Punto(c[0],c[1])
D = Punto(d[0],d[1])

# print(A)
# print(B)
# print(C)
# print(D) 

Cuadrante_A = print(A.cuadrante())
Cuadrante_B = print(B.cuadrante())
Cuadrante_D = print(D.cuadrante())


# AB = print(A.vector(5,5))











    




















