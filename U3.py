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
                f"precio: ${self.precio:,} Pesos")

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
                f"Número de puertas:{self.no_puertas}\n"
                f"Metros cúbicos: {self.metros_cubicos} metros cúbicos\n"
                f"Capacidad en pies cúbicos:{self.pies_capacidad} pies cúbicos\n"
                f"Tipo de gama: {self.tipo_gama()}")

class Microondas(Electrodomestico, Gama):
    def __init__(self,id, marca, modelo, precio, potencia, consumo_energia, medidas):
        Electrodomestico.__init__(self, id, marca, modelo, precio )
        self.potencia = potencia
        self.consumo_energia = consumo_energia
        self.medidas = medidas
    def __str__(self):
        return (f"{Electrodomestico.__str__(self)}\n"
                f"Potencia: {self.potencia} W\n"
                f"Consumo De Energia: {self.consumo_energia} W\n"
                f"Medidas (Ancho, Alto, Profundiad): {self.medidas}\n"
                f"Tipo de gama: {self.tipo_gama()}")
    def tipo_gama(self):
        if self.potencia < 1000:
            return "Baja"
        elif self.potencia <=1500:
            return "Media"
        else:
            return "Alta"
            
while True:
    try:
        print(f"\n1. Instanciar\n2. Desplegar\n3. Salir")
        opcion = int(input("\nIngresa la opción: "))
        if opcion == 1:
            lavadora = Lavadora("8MWTW2224WJM", "Whirlpool", "8MWTW2224WJM", 13999, 22, 15 ,12)
            refrigerador = Refrigerador("RF22A4010S9/EM","Samsung","RF22A4010S9/EM",30000,3,0.623,22)
            microondas = Microondas ("MH1596DIR","LG","NeoChef",4700,1200,1350,"54x32.2x43.3")
            print("\nSe instanciaron los objetos")
        elif opcion == 2:
            print(f"\n\n{lavadora}")
            print(f"\n\n{refrigerador}")
            print(f"\n\n{microondas}")
        elif opcion == 3:
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 3.")
        
    except ValueError as error_valor:
        print("Error: Debe ingresar un número entero.")
        print("Detalle del error:", error_valor)
        print("Intente de nuevo.\n")
    
    except NameError as error_nombre:
        print("Error: Intentaste acceder a un electrodoméstico que aún no ha sido creado.")
        print("Detalle del error:", error_nombre)
        print("Intente de nuevo.\n")
        
    except KeyboardInterrupt as interrupcion:
        print("\nPrograma interrumpido por el usuario.")
    
    except Exception as error_general:
        print("Ha ocurrido un error inesperado.")
        print("Detalle del error:", error_general)
        print("Intente de nuevo.\n")
