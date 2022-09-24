
import math

class Punto:

    def __init__(self, valor_x=None, valor_y=None):
        if valor_x is None or valor_y is None:
            self.valor_x = 0
            self.valor_y = 0

        else:
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

    def vector(self,punto):
        self.vector = "("+str(int(punto.__str__()[1])-self.valor_x)+","+str(int(punto.__str__()[3])-self.valor_y)+")"
        return self.vector

    def distancia(self,punto):
        self.distancia = "{:.3f}".format(math.sqrt(((int(punto.__str__()[1])-self.valor_x)**2)+((int(punto.__str__()[3])-self.valor_y)**2)))
        return self.distancia

class Rectangulo():

    def __init__(self, punto1, punto2):
        self.vector = punto1.vector(punto2)
         
    def base(self):
        self.base = abs(int(self.vector[1]))
        return self.base

    def altura(self):
        self.altura = abs(int(self.vector[3]))
        return self.altura

    def area(self):
        self.area = self.base()*self.altura()
        return self.area

### Experimentacion ###

# Creacion e impresión de puntos.

A = Punto(2,3)
B = Punto(5,5)
C = Punto(-3,-1)
D = Punto(0,0)

print(A)
print(B)
print(C)
print(D) 

# Consultar cuadrantes A, C y D.

Cuadrante_A = print(A.cuadrante())
Cuadrante_C = print(C.cuadrante())
Cuadrante_D = print(D.cuadrante())

# # Consultar vectores AB y BA.

AB = print(A.vector(B))
BA = print(B.vector(A))


# # Consulta la distancia entre los puntos A - B y B - A.

Distancia_A_B = print(A.distancia(B))
Distancia_B_A = print(B.distancia(A))


# Determina cual de los tres puntos (A,B,C) se encuentra mas lejos del origen (D).
# Ya que me da str object error establezo las variables que necesito de nuevo (corregir).
# Creo una lista para sacar el valor maximo.




# Crea un rectangulo

rectangulo = Rectangulo(A,B)

r_base = print(rectangulo.base())
r_altura = print(rectangulo.altura())
r_area = print(rectangulo.area())

















    




















