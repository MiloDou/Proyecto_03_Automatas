import re
import tkinter as tk
from tkinter import messagebox

def aplicar_regex():
    regex = entrada_regex.get()
    texto = entrada_texto.get("1.0", tk.END)

    try:
        patron = re.compile(regex)
    except re.error as e:
        messagebox.showerror("Error", f"Regex inválida:\n{e}")
        return

    coincidencias = patron.findall(texto)

    salida_resultados.delete("1.0", tk.END)
    salida_resultados.insert(tk.END, "Coincidencias:\n")
    for c in coincidencias:
        salida_resultados.insert(tk.END, f"- {c}\n")

    entrada_texto.tag_remove("resaltado", "1.0", tk.END)
    for match in patron.finditer(texto):
        start, end = match.span()
        start_index = f"1.0+{start}c"
        end_index = f"1.0+{end}c"
        entrada_texto.tag_add("resaltado", start_index, end_index)

    entrada_texto.tag_config("resaltado", background="yellow")

ventana = tk.Tk()
ventana.title("Herramienta Regex")

tk.Label(ventana, text="Expresión Regular:").pack()
entrada_regex = tk.Entry(ventana, width=50)
entrada_regex.pack()

##entrada de texto
tk.Label(ventana, text="Texto:").pack()
entrada_texto = tk.Text(ventana, width=60, height=10)
entrada_texto.pack()
tk.Button(ventana, text="Aplicar Regex", command=aplicar_regex).pack(pady=5)

##resultados 
tk.Label(ventana, text="Resultados:").pack()
salida_resultados = tk.Text(ventana, width=60, height=5)
salida_resultados.pack()

ventana.mainloop()
