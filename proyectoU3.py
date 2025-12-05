"""Módulo de gestión de electrodomésticos.

Este módulo proporciona una estructura jerárquica de clases para gestionar
diferentes tipos de electrodomésticos, cada uno con capacidad de autodefinir
su nivel de gama (baja, media, alta) basándose en sus especificaciones técnicas.
"""

from abc import ABC, abstractmethod

class Gama(ABC):
    """Clase abstracta que define la interfaz para determinar el nivel de gama.
    
    Esta clase abstracta actúa como interfaz que deben heredar todas las subclases
    de electrodomésticos, obligándolas a implementar el método tipo_gama().
    """
    
    @abstractmethod
    def tipo_gama(self):
        """Determina el nivel de gama del electrodoméstico.
        
        Returns:
            str: El nivel de gama ("Baja", "Media" o "Alta") basado en las especificaciones técnicas del electrodoméstico.
        """
        pass

class Electrodomestico():
    """Clase principal que define las propiedades básicas de un electrodoméstico.
    
    Esta es la clase base de la que heredarán todos los tipos de electrodomésticos.
    Contiene los atributos comunes a todos: id, marca, modelo y precio.
    """
    
    def __init__(self, id, marca, modelo, precio):
        """Inicializa un electrodoméstico con sus propiedades básicas.
        
        Args:
            id (str): Identificador único del electrodoméstico.
            marca (str): Marca fabricante del electrodoméstico.
            modelo (str): Modelo del electrodoméstico.
            precio (float): Precio del electrodoméstico en pesos.
        """
        self.id = id       
        self.marca = marca
        self.modelo = modelo
        self.precio = precio
    
    def __str__(self):
        """Retorna una representación en string del electrodoméstico.
        
        Returns:
            str: Información formateada del electrodoméstico con su ID, marca, modelo y precio.
        """
        return (f"ID: {self.id}\n"
                f"Marca: {self.marca}\n"
                f"modelo: {self.modelo}\n"
                f"precio: ${self.precio:,} Pesos")
    
class Lavadora(Electrodomestico, Gama):
    """Representa una lavadora automática.
    
    Hereda propiedades de Electrodomestico y la capacidad de determinar su gama
    mediante la interfaz Gama. Incluye características específicas como capacidad
    de carga, consumo de agua y número de ciclos de lavado.
    """

    def __init__(self, id, marca, modelo, precio, capacidad_carga, consumo_agua, ciclos_lavado):
        """Inicializa una lavadora con sus propiedades básicas y específicas.
        
        Args:
            id (str): Identificador único de la lavadora.
            marca (str): Marca fabricante de la lavadora.
            modelo (str): Modelo de la lavadora.
            precio (float): Precio de la lavadora en pesos.
            capacidad_carga (float): Capacidad de carga en kilogramos.
            consumo_agua (float): Consumo de agua por ciclo en litros.
            ciclos_lavado (int): Número de ciclos de lavado disponibles.
        """
        Electrodomestico.__init__(self, id, marca, modelo, precio)
        self.capacidad_carga = capacidad_carga
        self.consumo_agua = consumo_agua
        self.ciclos_lavado = ciclos_lavado
    
    def __str__(self):
        """Retorna una representación en string de la lavadora.
        
        Returns:
            str: Información completa de la lavadora incluyendo propiedades básicas, capacidad de carga, consumo de agua, ciclos de lavado y tipo de gama.
        """
        return (f"{Electrodomestico.__str__(self)}\n"
                f"Capacidad De Carga: {self.capacidad_carga} kg\n"
                f"Consumo De Agua: {self.consumo_agua} Litros\n"
                f"Ciclos De Lavado: {self.ciclos_lavado}\n"
                f"Tipo de gama: {self.tipo_gama()}")
    
    def tipo_gama(self):
        """Determina el nivel de gama de la lavadora.
        
        Clasifica la lavadora como Baja, Media o Alta según su capacidad de carga
        y número de ciclos de lavado.
        
        Returns:
            str: "Baja" si capacidad<=10kg y ciclos<=3,
                "Media" si capacidad<=15kg o ciclos<=3,
                "Alta" en caso contrario.
        """
        if self.capacidad_carga <=10 and self.ciclos_lavado <=3:
            return "Baja"
        elif self.capacidad_carga <=15 or self.ciclos_lavado <=3:
            return "Media"
        else:
            return "Alta"

class Refrigerador(Electrodomestico, Gama):
    """Representa un refrigerador.
    
    Hereda propiedades de Electrodomestico y la capacidad de determinar su gama.
    Incluye características específicas como número de puertas, capacidad en metros
    cúbicos y pies cúbicos.
    """
    
    def __init__(self, id, marca, modelo, precio, no_puertas, metros_cubicos, pies_capacidad):
        """Inicializa un refrigerador con sus propiedades básicas y específicas.
        
        Args:
            id (str): Identificador único del refrigerador.
            marca (str): Marca fabricante del refrigerador.
            modelo (str): Modelo del refrigerador.
            precio (float): Precio del refrigerador en pesos.
            no_puertas (int): Número de puertas del refrigerador.
            metros_cubicos (float): Capacidad en metros cúbicos.
            pies_capacidad (float): Capacidad en pies cúbicos.
        """
        Electrodomestico.__init__(self, id, marca, modelo, precio)
        self.no_puertas = no_puertas
        self.metros_cubicos = metros_cubicos
        self.pies_capacidad = pies_capacidad
    
    def tipo_gama(self):
        """Determina el nivel de gama del refrigerador.
        
        Clasifica el refrigerador como Baja, Media o Alta según el número de puertas
        y la capacidad en metros cúbicos.
        
        Returns:
            str: "Baja" si 1 puerta y <=10m³,
                "Media" si 2 puertas y <=13m³,
                "Alta" en caso contrario.
        """
        if self.no_puertas == 1 and self.metros_cubicos <= 10:
            return "Baja"
        elif self.no_puertas == 2 and self.metros_cubicos <= 13:
            return "Media"
        else:
            return "Alta"
    
    def __str__(self):
        """Retorna una representación en string del refrigerador.
        
        Returns:
            str: Información completa del refrigerador incluyendo propiedades básicas, número de puertas, capacidad en metros y pies cúbicos, y tipo de gama.
        """
        return (f"{Electrodomestico.__str__(self)}\n"
                f"Número de puertas:{self.no_puertas}\n"
                f"Metros cúbicos: {self.metros_cubicos} metros cúbicos\n"
                f"Capacidad en pies cúbicos:{self.pies_capacidad} pies cúbicos\n"
                f"Tipo de gama: {self.tipo_gama()}")

class Microondas(Electrodomestico, Gama):
    """Representa un microondas.
    
    Hereda propiedades de Electrodomestico y la capacidad de determinar su gama.
    Incluye características específicas como potencia, consumo de energía y medidas.
    """
    
    def __init__(self, id, marca, modelo, precio, potencia, consumo_energia, medidas):
        """Inicializa un microondas con sus propiedades básicas y específicas.
        
        Args:
            id (str): Identificador único del microondas.
            marca (str): Marca fabricante del microondas.
            modelo (str): Modelo del microondas.
            precio (float): Precio del microondas en pesos.
            potencia (float): Potencia del microondas en watts.
            consumo_energia (float): Consumo de energía en watts.
            medidas (str): Medidas del microondas (Ancho, Alto, Profundidad).
        """
        Electrodomestico.__init__(self, id, marca, modelo, precio)
        self.potencia = potencia
        self.consumo_energia = consumo_energia
        self.medidas = medidas
    
    def __str__(self):
        """Retorna una representación en string del microondas.
        
        Returns:
            str: Información completa del microondas incluyendo propiedades básicas, potencia, consumo de energía, medidas y tipo de gama.
        """
        return (f"{Electrodomestico.__str__(self)}\n"
                f"Potencia: {self.potencia} W\n"
                f"Consumo De Energia: {self.consumo_energia} W\n"
                f"Medidas (Ancho, Alto, Profundiad): {self.medidas}\n"
                f"Tipo de gama: {self.tipo_gama()}")
    
    def tipo_gama(self):
        """Determina el nivel de gama del microondas.
        
        Clasifica el microondas como Baja, Media o Alta según su potencia.
        
        Returns:
            str: "Baja" si potencia < 1000W,
                "Media" si potencia <= 1500W,
                "Alta" si potencia > 1500W.
        """
        if self.potencia < 1000:
            return "Baja"
        elif self.potencia <=1500:
            return "Media"
        else:
            return "Alta"

# ============================================================================
# PROGRAMA PRINCIPAL
# ============================================================================
# Este programa implementa un menú interactivo para gestionar electrodomésticos.
# Permite instanciar objetos de diferentes tipos de electrodomésticos y
# visualizar sus propiedades, incluyendo su clasificación automática de gama.
# ============================================================================

while True:
    try:
        print ("--- Menú Principal---")
        print(f"\n1. Instanciar\n2. Desplegar\n3. Salir")
        opcion = int(input("\nIngresa la opción 1, 2 ó 3: "))
        if opcion == 1:
            lavadora = Lavadora("8MWTW2224WJM", "Whirlpool", "8MWTW2224WJM", 13999, 22, 15 ,12)
            refrigerador = Refrigerador("RF22A4010S9/EM", "Samsung", "RF22A4010S9/EM", 30000, 3, 0.623, 22)
            microondas = Microondas ("MH1596DIR", "LG", "NeoChef", 4700, 1200, 1350, "54x32.2x43.3")
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
