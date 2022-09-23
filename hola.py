




class Punto:

    def __init__(self, valor_x, valor_y):

        self.valor_x = valor_x
        self.valor_y = valor_y

    def __str__(self):
        return f"("+str(self.valor_x)+","+str(self.valor_y)+")"

    def cuadrante(self, valor_x, valor_y):
        
        if valor_x==0 and valor_y!=0:
            self.cuadrante = print("Esta situado sobre el eje Y")
        
        elif valor_x!=0 and valor_y==0:
            self.cuadrante = print("Esta situado sobre el eje X")

        elif valor_x==0 and valor_y==0:
            self.cuadrante = print("Esta situado sobre el origen")

        else:
            pass
            # self.cuadrante = print("No se puede situar el cuadrante")


    # def vector(self,valor_x, valor_y):
        # self.vector = print(f"El resultado del vector es ("+[Punto(20,40[1])-valor_x]+","+[Punto(20,40[0])-valor_y]+")"



punto = Punto(10,20)

punto2 = Punto(20,40)

# def vector (punto, punto2):

    # print(f"(" + str(punto2.valor_x-punto.valor_x) + "," + str(punto2.valor_y-punto.valor_y)+")")

# vector(punto,punto2)



    




















