from abc import ABC, abstractmethod

class Gama(ABC):
    @abstractmethod
    def tipo_gama(self):
        pass

class Electrodomestico():
    def __init__(self, id, marca, modelo, precio):
        self.id = id       
        self.marca = marca
        self.modelo = modelo
        self.precio = precio
    def __str__(self):
        return (f"ID: {self.id}\n"
                f"Marca: {self.marca}\n"
                f"modelo: {self.modelo}\n"
                f"precio: ${self.precio}")

class Lavadora(Electrodomestico, Gama):
    def __init__(self,id, marca, modelo, precio, capacidad_carga, consumo_agua, ciclos_lavado):
        Electrodomestico.__init__(self, id, marca, modelo, precio )
        self.capacidad_carga = capacidad_carga
        self.consumo_agua = consumo_agua
        self.ciclos_lavado = ciclos_lavado
    def __str__(self):
        return (f"{Electrodomestico.__str__(self)}\n"
                f"Capacidad De Carga: {self.capacidad_carga} kg\n"
                f"Consumo De Agua: {self.consumo_agua} Litros\n"
                f"Ciclos De Lavado: {self.ciclos_lavado}\n"
                f"Tipo de gama: {self.tipo_gama()}")
    def tipo_gama(self):
        if self.capacidad_carga <=10 and self.ciclos_lavado <=3:
            return "Baja"
        elif self.capacidad_carga <=15 or self.ciclos_lavado <=3:
            return "Media"
        else:
            return "Alta"



class Refrigerador(Electrodomestico,Gama):
    def __init__(self,id, marca, modelo, precio, no_puertas,metros_cubicos,pies_capacidad):
        Electrodomestico.__init__(self,id,marca,modelo,precio)
        self.no_puertas = no_puertas
        self.metros_cubicos = metros_cubicos
        self.pies_capacidad = pies_capacidad
    def tipo_gama(self):
        if self.no_puertas == 1 and self.metros_cubicos <= 10:
            return "Baja"
        elif self.no_puertas == 2 and self.metros_cubicos <= 13:
            return "Media"
        else:
            return "Alta"
    def __str__(self):
        return (f"{Electrodomestico.__str__(self)}\n"
                f"Número de puertas:{self.no_puertas}"
                f"Metros cúbicos: {self.metros_cubicos}"
                f"Capacidad en pies cúbicos:{self.pies_capacidad}"
                f"Tipo de gama: {self.tipo_gama()}")

class Microondas(Electrodomestico, Gama):
    def __init__(self,id, marca, modelo, precio, potencia, consumo_energia, medidas):
        Electrodomestico.__init__(self, id, marca, modelo, precio )
        self.potencia = potencia
        self.consumo_energia = consumo_energia
        self.medidas = medidas
    def __str__(self):
        return (f"{Electrodomestico.__str__(self)}"
                f"Capacidad De Carga: {self.potencia}\n"
                f"Consumo De Agua: {self.consumo_energia}\n"
                f"Ciclos De Lavado: {self.medidas}\n"
                f"Tipo de gama: {self.tipo_gama()}")
    def tipo_gama(self):
        if self.potencia < 1000:
            return "Baja"
        elif self.potencia <=1500:
            return "Media"
        else:
            return "Alta"
            

try:


    lavadora = Lavadora("1139411095", "LG", "WT18WV6", 13999, 6, 50 ,6)
    print(lavadora)
    refrigerador = Refrigerador("324433","toyota","corolla",4322,2,13,213)
    print(f"\n\n{refrigerador}")
    microondas = Microondas ("122222","yotoya","rocolla",100,1000,322,131)
    print(f"\n\n{microondas}")

except Exception as err:
    print("Ocurrió un error pq usted esun NYE: " + str(err))

































































































































































































































































































































































































































print(":D")
      
































































