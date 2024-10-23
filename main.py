import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import json

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Organizador de Tareas")
        self.root.geometry("800x600")
        
        # Datos
        self.tareas = []
        self.cargar_tareas()
        
        # Variables
        self.var_titulo = tk.StringVar()
        self.var_prioridad = tk.StringVar(value="Normal")
        self.var_categoria = tk.StringVar(value="Personal")
        
        self.crear_interfaz()
        
    def crear_interfaz(self):
        # Marco principal
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Formulario de entrada
        ttk.Label(main_frame, text="Nueva Tarea").grid(row=0, column=0, columnspan=2, pady=5)
        
        ttk.Label(main_frame, text="Título:").grid(row=1, column=0, sticky=tk.W)
        ttk.Entry(main_frame, textvariable=self.var_titulo, width=40).grid(row=1, column=1, pady=2)
        
        ttk.Label(main_frame, text="Prioridad:").grid(row=2, column=0, sticky=tk.W)
        ttk.Combobox(main_frame, textvariable=self.var_prioridad, 
                     values=["Alta", "Normal", "Baja"]).grid(row=2, column=1, pady=2)
        
        ttk.Label(main_frame, text="Categoría:").grid(row=3, column=0, sticky=tk.W)
        ttk.Combobox(main_frame, textvariable=self.var_categoria,
                     values=["Personal", "Trabajo", "Estudio", "Hogar"]).grid(row=3, column=1, pady=2)
        
        ttk.Button(main_frame, text="Agregar Tarea", command=self.agregar_tarea).grid(row=4, column=0, columnspan=2, pady=10)
        
        # Lista de tareas
        self.tree = ttk.Treeview(main_frame, columns=("Título", "Fecha", "Prioridad", "Categoría", "Estado"),
                                show="headings", height=15)
        
        self.tree.heading("Título", text="Título")
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Prioridad", text="Prioridad")
        self.tree.heading("Categoría", text="Categoría")
        self.tree.heading("Estado", text="Estado")
        
        self.tree.grid(row=5, column=0, columnspan=2, pady=10)
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(main_frame, orient=tk.VERTICAL, command=self.tree.yview)
        scrollbar.grid(row=5, column=2, sticky=(tk.N, tk.S))
        self.tree.configure(yscrollcommand=scrollbar.set)
        
        # Botones de acción
        ttk.Button(main_frame, text="Marcar Completada", 
                  command=self.marcar_completada).grid(row=6, column=0, pady=5)
        ttk.Button(main_frame, text="Eliminar Tarea",
                  command=self.eliminar_tarea).grid(row=6, column=1, pady=5)
        
        self.actualizar_lista()
        
    def agregar_tarea(self):
        titulo = self.var_titulo.get().strip()
        if not titulo:
            messagebox.showwarning("Error", "El título no puede estar vacío")
            return
            
        tarea = {
            "titulo": titulo,
            "fecha": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "prioridad": self.var_prioridad.get(),
            "categoria": self.var_categoria.get(),
            "estado": "Pendiente"
        }
        
        self.tareas.append(tarea)
        self.guardar_tareas()
        self.actualizar_lista()
        self.var_titulo.set("")
        
    def actualizar_lista(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
            
        for tarea in self.tareas:
            self.tree.insert("", tk.END, values=(
                tarea["titulo"],
                tarea["fecha"],
                tarea["prioridad"],
                tarea["categoria"],
                tarea["estado"]
            ))
            
    def marcar_completada(self):
        seleccion = self.tree.selection()
        if not seleccion:
            messagebox.showwarning("Error", "Por favor, selecciona una tarea")
            return
            
        item = seleccion[0]
        index = self.tree.index(item)
        self.tareas[index]["estado"] = "Completada"
        self.guardar_tareas()
        self.actualizar_lista()
        
    def eliminar_tarea(self):
        seleccion = self.tree.selection()
        if not seleccion:
            messagebox.showwarning("Error", "Por favor, selecciona una tarea")
            return
            
        if messagebox.askyesno("Confirmar", "¿Estás seguro de eliminar esta tarea?"):
            item = seleccion[0]
            index = self.tree.index(item)
            del self.tareas[index]
            self.guardar_tareas()
            self.actualizar_lista()
            
    def guardar_tareas(self):
        with open("tareas.json", "w") as f:
            json.dump(self.tareas, f)
            
    def cargar_tareas(self):
        try:
            with open("tareas.json", "r") as f:
                self.tareas = json.load(f)
        except FileNotFoundError:
            self.tareas = []

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
