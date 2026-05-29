import random
import sys


class LongitudInvalidaError(ValueError):
    pass


class DatoNoNumericoError(ValueError):
    pass


class ContrasenaInvalidaError(ValueError):
    pass


class Contrasena:
    MAYUSCULAS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    MINUSCULAS = "abcdefghijklmnopqrstuvwxyz"
    NUMEROS = "0123456789"
    ESPECIALES = "¿¡?=)(/¨*+-%&$#!."
    CARACTERES_PERMITIDOS = MAYUSCULAS + MINUSCULAS + NUMEROS + ESPECIALES

    def __init__(self, longitud: int):
        self.longitud = longitud
        self.valor = self.generar_contrasena(longitud)

    @classmethod
    def validar_longitud(cls, longitud):
        if not isinstance(longitud, int):
            raise DatoNoNumericoError("La longitud debe ser un número entero.")
        if longitud < 8:
            raise LongitudInvalidaError("La longitud mínima es 8 caracteres.")
        if longitud > len(cls.CARACTERES_PERMITIDOS):
            raise LongitudInvalidaError(
                f"La longitud no puede superar {len(cls.CARACTERES_PERMITIDOS)} porque no se permiten caracteres repetidos."
            )

    @classmethod
    def generar_contrasena(cls, longitud: int) -> str:
        cls.validar_longitud(longitud)
        caracteres = random.sample(cls.CARACTERES_PERMITIDOS, longitud)
        random.shuffle(caracteres)
        return "".join(caracteres)

    @classmethod
    def validar_contrasena(cls, contrasena: str) -> bool:
        if len(contrasena) < 8:
            raise ContrasenaInvalidaError("La contraseña debe tener al menos 8 caracteres.")

        if len(set(contrasena)) != len(contrasena):
            raise ContrasenaInvalidaError("La contraseña no puede contener caracteres repetidos.")

        if not any(c in cls.MAYUSCULAS for c in contrasena):
            raise ContrasenaInvalidaError("La contraseña debe incluir al menos una letra mayúscula.")

        if not any(c in cls.MINUSCULAS for c in contrasena):
            raise ContrasenaInvalidaError("La contraseña debe incluir al menos una letra minúscula.")

        if not any(c in cls.NUMEROS for c in contrasena):
            raise ContrasenaInvalidaError("La contraseña debe incluir al menos un número.")

        if not any(c in cls.ESPECIALES for c in contrasena):
            raise ContrasenaInvalidaError(
                "La contraseña debe incluir al menos un carácter especial válido."
            )

        if any(c not in cls.CARACTERES_PERMITIDOS for c in contrasena):
            raise ContrasenaInvalidaError("La contraseña contiene caracteres no permitidos.")

        return True


class Cofre:
    TIPOS_POSITIVOS = [
        ("Común", 10),
        ("Raro", 25),
        ("Legendario", 50),
    ]
    TIPO_MALDITO = ("Maldito", -20)

    @classmethod
    def abrir_cofre(cls, valida: bool):
        if valida:
            tipo, puntos = random.choice(cls.TIPOS_POSITIVOS)
        else:
            tipo, puntos = cls.TIPO_MALDITO
        return tipo, puntos

# Juego principal
class JuegoCazador:
    
    # El constructor inicializa los puntos del jugador a cero.
    def __init__(self):
        self.puntos = 0

# El método solicitar_longitud pide al usuario que ingrese la longitud de la contraseña, valida que sea un número y que cumpla con los requisitos mínimos.
    def solicitar_longitud(self):
        
        # Solicita al usuario que ingrese la longitud de la contraseña y valida que sea un número entero y que cumpla con los requisitos mínimos.
        entrada = input("Ingrese la longitud de la contraseña (mínimo 8): ")
        
        # Valida que la entrada sea un número entero. Si no lo es, lanza una excepción DatoNoNumericoError.
        if not entrada.strip().isdigit():
            raise DatoNoNumericoError("Debe ingresar un número válido.")

        longitud = int(entrada)
        Contrasena.validar_longitud(longitud)
        return longitud

    def jugar_ronda(self):
        try:
            longitud = self.solicitar_longitud()
            contrasena_obj = Contrasena(longitud)
            contrasena = contrasena_obj.valor
            try:
                Contrasena.validar_contrasena(contrasena)
                tipo_cofre, puntos = Cofre.abrir_cofre(True)
                self.puntos += puntos
                print(f"\nContraseña generada: {contrasena}")
                print(f"¡Contraseña válida! Abres un cofre {tipo_cofre} y ganas {puntos} puntos.")
            except ContrasenaInvalidaError as error:
                tipo_cofre, puntos = Cofre.abrir_cofre(False)
                self.puntos += puntos
                print(f"\nContraseña generada: {contrasena}")
                print(f"Contraseña inválida: {error}")
                print(f"Has abierto un cofre {tipo_cofre} y sufres {abs(puntos)} puntos de penalización.")

            print(f"Puntos acumulados: {self.puntos}\n")
        except (DatoNoNumericoError, LongitudInvalidaError) as error:
            print(f"Error: {error}\n")

    def iniciar_juego(self):
        print("Bienvenido al Juego del Cazador de Contraseñas")
        print("Genera contraseñas aleatorias y abre cofres según su calidad.\n")

        while True:
            self.jugar_ronda()
            respuesta = input("¿Deseas continuar jugando? (s/n): ").strip().lower()
            while respuesta not in {"s", "n", "si", "no"}:
                respuesta = input("Por favor ingresa 's' o 'n': ").strip().lower()
            if respuesta in {"n", "no"}:
                print(f"\nJuego terminado. Puntos finales: {self.puntos}")
                break

# Punto de entrada del programa
if __name__ == "__main__":
    try:
        juego = JuegoCazador()
        juego.iniciar_juego()
    except KeyboardInterrupt:
        print("\nJuego interrumpido. ¡Hasta la próxima!")
        sys.exit(0)
