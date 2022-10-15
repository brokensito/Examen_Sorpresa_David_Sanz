
import math

class Punto:

    def __init__(self, valor_x=0, valor_y=0):
        self.valor_x = valor_x
        self.valor_y = valor_y
    
    def punto(self):
        return (self.valor_x,self.valor_y)
        
    def str(self):
        return f"("+str(Punto(self.valor_x,self.valor_y).punto()[0])+","+str(Punto(self.valor_x,self.valor_y).punto()[1])+")"

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

    def vector(self,punto2):
        self.vector = (punto2.punto()[0]-self.valor_x,punto2.punto()[1]-self.valor_y)
        return self.vector

    def distancia(self,punto2):
        self.distancia = math.sqrt(((punto2.punto()[0]-self.valor_x)**2)+((punto2.punto()[1]-self.valor_y)**2))
        return self.distancia

class Rectangulo():

    def __init__(self, punto1, punto2):
        self.vector = punto1.vector(punto2)
         
    def base(self):
        self.base = abs(self.vector[0])
        return self.base

    def altura(self):
        self.altura = abs(self.vector[1])
        return self.altura

    def area(self):
        self.area = self.base()*self.altura()
        return self.area

### Experimentacion ###

# Creacion e impresión de puntos.

# A = Punto(2,3)
# B = Punto(5,5)
# C = Punto(-3,-1)
# D = Punto()

# print(A.str())
# print(B.str())
# print(C.str())
# print(D.str()) 

# Consultar cuadrantes A, C y D.

# Cuadrante_A = A.cuadrante()
# Cuadrante_C = C.cuadrante()
# Cuadrante_D = D.cuadrante()

# print(Cuadrante_A)
# print(Cuadrante_C)
# print(Cuadrante_D)

# Consultar vectores AB y BA.

# AB = A.vector(B)
# BA = B.vector(A)

# print(AB)
# print(BA)


## Consulta la distancia entre los puntos A - B y B - A.

# Distancia_A_B = A.distancia(B)
# Distancia_B_A = B.distancia(A)

# print(Distancia_A_B)
# print(Distancia_B_A)


# Determina cual de los tres puntos (A,B,C) se encuentra mas lejos del origen (D).
# valores = []
# Distancia_A_D = valores.append(A.distancia(D))
# Distancia_B_D = valores.append(B.distancia(D))
# Distancia_C_D = valores.append(C.distancia(D))
# print("El punto que se encuentra a mayor distancia del origen es el B, con una distancia de:"+str(valores(max)))


# Crea un rectangulo

# rectangulo = Rectangulo(A,B)

# r_base = print(rectangulo.base())
# r_altura = print(rectangulo.altura())
# r_area = print(rectangulo.area())



        


