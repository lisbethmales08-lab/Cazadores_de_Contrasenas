import tkinter as tk
from tkinter import messagebox

from cazadores_de_contrasenas import JuegoCazador


class CazadorGUI:
    def __init__(self, master):
        self.master = master
        master.title("Cazadores de Contraseñas")

        self.juego = JuegoCazador()

        self.frame = tk.Frame(master, padx=10, pady=10)
        self.frame.pack()

        tk.Label(self.frame, text="Longitud (mínimo 8):").grid(row=0, column=0, sticky="w")
        self.entrada_longitud = tk.Entry(self.frame, width=10)
        self.entrada_longitud.grid(row=0, column=1, sticky="w")

        self.boton_jugar = tk.Button(self.frame, text="Jugar ronda", command=self.jugar_ronda)
        self.boton_jugar.grid(row=0, column=2, padx=5)

        tk.Label(self.frame, text="Contraseña generada:").grid(row=1, column=0, sticky="w", pady=(10, 0))
        self.label_contrasena = tk.Label(self.frame, text="-", fg="blue")
        self.label_contrasena.grid(row=1, column=1, columnspan=2, sticky="w", pady=(10, 0))

        tk.Label(self.frame, text="Resultado:").grid(row=2, column=0, sticky="w")
        self.label_resultado = tk.Label(self.frame, text="-", wraplength=400, justify="left")
        self.label_resultado.grid(row=2, column=1, columnspan=2, sticky="w")

        tk.Label(self.frame, text="Puntos acumulados:").grid(row=3, column=0, sticky="w", pady=(10, 0))
        self.label_puntos = tk.Label(self.frame, text="0", fg="green")
        self.label_puntos.grid(row=3, column=1, sticky="w", pady=(10, 0))

        self.boton_reset = tk.Button(self.frame, text="Reiniciar puntos", command=self.reiniciar)
        self.boton_reset.grid(row=4, column=0, pady=(10, 0))

        self.boton_salir = tk.Button(self.frame, text="Salir", command=master.quit)
        self.boton_salir.grid(row=4, column=2, pady=(10, 0))

    def jugar_ronda(self):
        texto = self.entrada_longitud.get().strip()
        if not texto.isdigit():
            messagebox.showerror("Error", "Ingrese un número entero válido para la longitud.")
            return

        longitud = int(texto)
        resultado = self.juego.jugar_ronda_con_longitud(longitud)

        if "error" in resultado:
            messagebox.showerror("Error", resultado["error"])
            return

        self.label_contrasena.config(text=resultado["contrasena"])
        self.label_resultado.config(text=resultado["mensaje"])
        self.label_puntos.config(text=str(resultado["puntos_acumulados"]))

    def reiniciar(self):
        self.juego = JuegoCazador()
        self.label_contrasena.config(text="-")
        self.label_resultado.config(text="-")
        self.label_puntos.config(text="0")


def main():
    root = tk.Tk()
    app = CazadorGUI(root)
    root.resizable(False, False)
    root.mainloop()


if __name__ == "__main__":
    main()
