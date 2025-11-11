import tkinter as tk
from tkinter import ttk, messagebox
import random
import datetime

partidas = []
usados = set()
intentos = 0
numeros_ingresados = []

def generar_numero():
    n = random.randint(1, 100)
    while n in usados:
        n = random.randint(1, 100)
    usados.add(n)
    return n

numero = generar_numero()

def verificar():
    global intentos, numero
    valor = entry.get()
    if not valor.isdigit():
        messagebox.showwarning("Aviso", "Ingrese un número válido.")
        return
    num = int(valor)
    entry.delete(0, tk.END)
    intentos += 1
    numeros_ingresados.append(num)
    mostrar_intentos()
    if num < numero:
        texto.set("El número secreto es más grande 🔼")
    elif num > numero:
        texto.set("El número secreto es más chico 🔽")
    else:
        texto.set("🎯 ¡Adivinaste el número!")
        registrar_partida(True)
        messagebox.showinfo("Ganaste", f"Adivinaste el número en {intentos} intentos.")
        reiniciar()

def mostrar_intentos():
    lista_intentos.delete(0, tk.END)
    for i, n in enumerate(numeros_ingresados, 1):
        lista_intentos.insert(tk.END, f"Intento {i}: {n}")

def registrar_partida(ganada):
    fecha = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
    partidas.append({
        "fecha": fecha,
        "resultado": "Ganada" if ganada else "Perdida",
        "intentos": intentos,
        "numero": numero
    })
    actualizar_historial()

def reiniciar():
    global numero, intentos, numeros_ingresados
    numero = generar_numero()
    intentos = 0
    numeros_ingresados.clear()
    entry.delete(0, tk.END)
    texto.set("Nuevo número generado. ¡Adivina!")
    lista_intentos.delete(0, tk.END)

def actualizar_historial():
    lista.delete(0, tk.END)
    for p in partidas[-8:]:
        lista.insert(tk.END, f"{p['fecha']} - {p['resultado']} ({p['intentos']} intentos)")

ventana = tk.Tk()
ventana.title("Juego de Adivinanza")
ventana.geometry("460x520")
ventana.resizable(False, False)
ventana.config(bg="#dce8ff")

tk.Label(ventana, text="🎯 Juego de Adivinanza", font=("Arial Rounded MT Bold", 20), bg="#dce8ff", fg="#1e3d6b").pack(pady=12)
tk.Label(ventana, text="Adivina un número entre 1 y 100", bg="#dce8ff", fg="#2e2e2e", font=("Arial", 11)).pack()

frame = tk.Frame(ventana, bg="#dce8ff")
frame.pack(pady=15)

entry = ttk.Entry(frame, width=10, justify="center", font=("Arial", 13))
entry.grid(row=0, column=0, padx=6)
ttk.Button(frame, text="Probar", command=verificar).grid(row=0, column=1, padx=6)

texto = tk.StringVar(value="Esperando tu intento...")
tk.Label(ventana, textvariable=texto, bg="#dce8ff", font=("Arial", 13, "bold"), fg="#374a6e").pack(pady=12)

tk.Label(ventana, text="Tus intentos:", bg="#dce8ff", font=("Arial", 10, "bold"), fg="#1f355b").pack()
lista_intentos = tk.Listbox(ventana, width=48, height=6, bg="#f6f8ff", fg="#1e1e1e", font=("Consolas", 10), relief="ridge", borderwidth=2)
lista_intentos.pack(pady=5)

tk.Label(ventana, text="Historial de partidas:", bg="#dce8ff", font=("Arial", 10, "bold"), fg="#1f355b").pack()
lista = tk.Listbox(ventana, width=48, height=6, bg="#f6f8ff", fg="#1e1e1e", font=("Consolas", 10), relief="ridge", borderwidth=2)
lista.pack(pady=5)

ttk.Button(ventana, text="Nuevo Juego", command=reiniciar).pack(pady=15)

ventana.mainloop()
