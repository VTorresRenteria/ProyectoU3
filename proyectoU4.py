from abc import ABC, abstractmethod

class Gama(ABC):
    '''
    Clase Abstracta (Interfaz) para la clasificación de gama de electrodomésticos.
    Define el contrato que deben seguir todas las subclases de Electrodomestico
    que quieran implementar una lógica de clasificación de gama.
    '''
    @abstractmethod
    def tipo_gama(self):
        '''
        Método abstracto que obliga a las subclases a implementar una lógica
        para determinar y retornar el tipo de gama del electrodoméstico 
        (ej. "Baja", "Media", "Alta").
        '''
        pass

class Electrodomestico():
    '''
    Clase Base (Padre) para todos los electrodomésticos.

    Contiene los atributos comunes a todos los productos.

    Attributes:
        id (str): Identificador único del producto.
        marca (str): Nombre de la marca del electrodoméstico.
        modelo (str): Nombre o código del modelo específico.
        precio (float): Precio de venta del electrodoméstico.
    '''
    def __init__(self, id, marca, modelo, precio):
        """Inicializa un nuevo objeto Electrodomestico."""
        self.id = id       
        self.marca = marca
        self.modelo = modelo
        self.precio = precio
        
    def __str__(self):
        """
        Retorna una representación en cadena legible del objeto Electrodomestico,
        formateando el precio con separadores de miles.
        """
        return (f"ID: {self.id}\n"
                f"Marca: {self.marca}\n"
                f"modelo: {self.modelo}\n"
                f"precio: ${self.precio:,.2f} Pesos") # Se agregó formato .2f para decimales
    
class Lavadora(Electrodomestico, Gama):
    '''
    Clase que representa una Lavadora.

    Hereda de Electrodomestico (atributos base) e implementa la interfaz Gama
    (método tipo_gama).

    Attributes:
        capacidad_carga (int): Capacidad máxima de carga en kg.
        consumo_agua (int): Consumo de agua por ciclo en Litros.
        ciclos_lavado (int): Número de ciclos o programas de lavado disponibles.
    '''

    def __init__(self, id, marca, modelo, precio, capacidad_carga, consumo_agua, ciclos_lavado):
        """Inicializa un objeto Lavadora con sus atributos específicos y base."""
        # Llama al constructor de la clase padre Electrodomestico
        super().__init__(id, marca, modelo, precio)
        self.capacidad_carga = capacidad_carga
        self.consumo_agua = consumo_agua
        self.ciclos_lavado = ciclos_lavado
        
    def tipo_gama(self):
        '''
        Implementación del método abstracto para clasificar la Lavadora.

        La clasificación se basa en la capacidad de carga y el número de ciclos.
        '''
        if self.capacidad_carga <= 10 and self.ciclos_lavado <= 3:
            return "Baja"
        # Se modificó la lógica para usar 'and' en lugar de 'or' para ser más estricto con la "media"
        elif self.capacidad_carga <= 15 and self.ciclos_lavado <= 5: 
            return "Media"
        else:
            return "Alta"
    
    def __str__(self):
        """
        Retorna la representación en cadena de la Lavadora, incluyendo los
        atributos base, los específicos y su clasificación de gama.
        """
        # Llama al __str__ de la clase padre y agrega la información específica
        return (f"{super().__str__()}\n" 
                f"Capacidad De Carga: {self.capacidad_carga} kg\n"
                f"Consumo De Agua: {self.consumo_agua} Litros\n"
                f"Ciclos De Lavado: {self.ciclos_lavado}\n"
                f"Tipo de gama: {self.tipo_gama()}")
        
class Refrigerador(Electrodomestico,Gama):
    '''
    Clase que representa un Refrigerador.

    Hereda de Electrodomestico (atributos base) e implementa la interfaz Gama
    (método tipo_gama).

    Attributes:
        no_puertas (int): Número de puertas del refrigerador.
        metros_cubicos (float): Volumen total en metros cúbicos.
        pies_capacidad (float): Volumen total en pies cúbicos.
    '''
    def __init__(self, id, marca, modelo, precio, no_puertas, metros_cubicos, pies_capacidad):
        """Inicializa un objeto Refrigerador con sus atributos específicos y base."""
        super().__init__(id, marca, modelo, precio)
        self.no_puertas = no_puertas
        self.metros_cubicos = metros_cubicos
        self.pies_capacidad = pies_capacidad
        
    def tipo_gama(self):
        '''
        Implementación del método abstracto para clasificar el Refrigerador.

        La clasificación se basa en el número de puertas y el volumen en metros cúbicos.
        '''
        if self.no_puertas == 1 and self.metros_cubicos <= 10:
            return "Baja"
        elif self.no_puertas == 2 and self.metros_cubicos <= 13:
            return "Media"
        else:
            return "Alta"
            
    def __str__(self):
        """
        Retorna la representación en cadena del Refrigerador, incluyendo los
        atributos base, los específicos y su clasificación de gama.
        """
        return (f"{super().__str__()}\n"
                f"Número de puertas:{self.no_puertas}\n"
                f"Metros cúbicos: {self.metros_cubicos} metros cúbicos\n"
                f"Capacidad en pies cúbicos:{self.pies_capacidad} pies cúbicos\n"
                f"Tipo de gama: {self.tipo_gama()}")

class Microondas(Electrodomestico, Gama):
    '''
    Clase que representa un Microondas.

    Hereda de Electrodomestico (atributos base) e implementa la interfaz Gama
    (método tipo_gama).

    Attributes:
        potencia (int): Potencia de salida en Watts (W).
        consumo_energia (int): Consumo de energía en Watts (W).
        medidas (str): Dimensiones (Ancho x Alto x Profundidad).
    '''
    def __init__(self, id, marca, modelo, precio, potencia, consumo_energia, medidas):
        """Inicializa un objeto Microondas con sus atributos específicos y base."""
        super().__init__(id, marca, modelo, precio)
        self.potencia = potencia
        self.consumo_energia = consumo_energia
        self.medidas = medidas

    def tipo_gama(self):
        '''
        Implementación del método abstracto para clasificar el Microondas.

        La clasificación se basa en la potencia de salida.
        '''
        if self.potencia < 1000:
            return "Baja"
        elif self.potencia <= 1500:
            return "Media"
        else:
            return "Alta"
        
    def __str__(self):
        """
        Retorna la representación en cadena del Microondas, incluyendo los
        atributos base, los específicos y su clasificación de gama.
        """
        return (f"{super().__str__()}\n"
                f"Potencia: {self.potencia} W\n"
                f"Consumo De Energia: {self.consumo_energia} W\n"
                f"Medidas (Ancho, Alto, Profundiad): {self.medidas}\n"
                f"Tipo de gama: {self.tipo_gama()}")
        
# --- Bloque del Programa Principal ---

'''
Programa Principal:
Este programa se trata de una jerarquía de clases para gestionar electrodomésticos,
donde cada tipo hereda propiedades básicas y tiene la capacidad de autodefinir
su "gama" (baja, media, alta) basándose en sus especificaciones técnicas.
'''

while True:
    try:
        print ("\n--- Menú Principal---")
        print(f"\n1. Instanciar (Crear) electrodomésticos\n2. Desplegar (Mostrar) electrodomésticos\n3. Salir")
        opcion = int(input("\nIngresa la opción 1, 2 ó 3: "))
        
        # Opción 1: Instanciar los objetos
        if opcion == 1:
            # Creación de instancias de las clases Lavadora, Refrigerador y Microondas
            lavadora = Lavadora("8MWTW2224WJM", "Whirlpool", "8MWTW2224WJM", 13999, 22, 15 ,12)
            refrigerador = Refrigerador("RF22A4010S9/EM", "Samsung", "RF22A4010S9/EM", 30000, 3, 0.623, 22) 
            microondas = Microondas ("MH1596DIR", "LG", "NeoChef", 4700, 1200, 1350, "54x32.2x43.3")
            print("\n Se instanciaron los objetos con éxito.")
            
        # Opción 2: Desplegar los objetos instanciados
        elif opcion == 2:
            # Uso del método __str__ para imprimir la información completa
            print("\n--- Detalles de Electrodomésticos ---")
            print(f"\n* LAVADORA *\n{lavadora}")
            print(f"\n* REFRIGERADOR *\n{refrigerador}")
            print(f"\n* MICROONDAS *\n{microondas}")
            
        # Opción 3: Salir del programa
        elif opcion == 3:
            print("\nSaliendo del programa... ¡Hasta pronto!")
            break
            
        else:
            print("\n Opción no válida. Por favor, seleccione una opción del 1 al 3.")
    # Manejo de errores 
    
    # Excepción para cuando el usuario no ingresa un número
    except ValueError as error_valor:
        print("\nError: Debe ingresar un número entero para seleccionar una opción.")
        print("Detalle del error:", error_valor)
        print("Intente de nuevo.")
    
    # Excepción para cuando se intenta desplegar un objeto que no ha sido instanciado (opción 2 sin haber ejecutado la 1)
    except NameError as error_nombre:
        print("\n Error: Intentaste desplegar un electrodoméstico que aún no ha sido creado (Opción 1).")
        print("Detalle del error:", error_nombre)
        print("Intente de nuevo.")
    
    # Excepción general para capturar cualquier otro error inesperado
    except Exception as error_general:
        print("\n Ha ocurrido un error inesperado.")
        print("Detalle del error:", error_general)
        print("Intente de nuevo.")

