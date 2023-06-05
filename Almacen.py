import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class AlmacendeBebidas:

    def __init__(self):
        self.bebidas = []
        self.ventana = tk.Tk()
        self.ventana.title("Almacenamiento de Bebidas")

        self.notebook = ttk.Notebook(self.ventana)
        self.notebook.pack(fill='both', expand=True)

        self.pag1 = ttk.Frame(self.notebook)
        self.notebook.add(self.pag1, text="Alta de Bebidas")
        
        self.pag2 = ttk.Frame(self.notebook)
        self.notebook.add(self.pag2, text="Baja de Bebidas")
        
        self.pag3 = ttk.Frame(self.notebook)
        self.notebook.add(self.pag3, text="Consulta de Bebidas")
        
        self.pag4 = ttk.Frame(self.notebook)
        self.notebook.add(self.pag4, text="Actualización de Bebidas")

        self.pag5 = ttk.Frame(self.notebook)
        self.notebook.add(self.pag5, text="Precio Promedio Bebidas")

        self.pag6 = ttk.Frame(self.notebook)
        self.notebook.add(self.pag6, text="Cantidad de Bebidas Marca")

        self.pag7 = ttk.Frame(self.notebook)
        self.notebook.add(self.pag7, text="Cantidad de Bebidas Clasificación")

        self.IDEt = tk.Label(self.pag1, text="ID:")
        self.IDEn = tk.Entry(self.pag1)
        self.NombreEt = tk.Label(self.pag1, text="Nombre:")
        self.NombreEn = tk.Entry(self.pag1)
        self.ClasificacionEt = tk.Label(self.pag1, text="Clasificación:")
        self.ClasificacionEn = tk.Entry(self.pag1)
        self.MarcaEt = tk.Label(self.pag1, text="Marca:")
        self.MarcaEn = tk.Entry(self.pag1)
        self.PrecioEt = tk.Label(self.pag1, text="Precio:")
        self.PrecioEn = tk.Entry(self.pag1)
        self.Agregar = tk.Button(self.pag1, text="Agregar", command=self.Alta_Bebidas)
    
        self.IDEt.grid(row=0, column=0)
        self.IDEn.grid(row=0, column=1)
        self.NombreEt.grid(row=1, column=0)
        self.NombreEn.grid(row=1, column=1)
        self.ClasificacionEt.grid(row=2, column=0)
        self.ClasificacionEn.grid(row=2, column=1)
        self.MarcaEt.grid(row=3, column=0)
        self.MarcaEn.grid(row=3, column=1)
        self.PrecioEt.grid(row=4, column=0)
        self.PrecioEn.grid(row=4, column=1)
        self.Agregar.grid(row=5, column=0)
        
        self.BetID = tk.Label(self.pag2, text="ID:")
        self.BenID = tk.Entry(self.pag2)
        self.Baja = tk.Button(self.pag2, text="Eliminar", command = self.Baja_Bebida)
        self.BetID.grid(row=0, column=0)
        self.BenID.grid(row=0, column=1)
        self.Baja.grid(row=1, column=0)

        self.AetID = tk.Label(self.pag3, text="ID:")
        self.AenID = tk.Entry(self.pag3)
        self.AetNombre = tk.Label(self.pag3, text="Nombre:")
        self.AenNombre = tk.Entry(self.pag3)
        self.AetClasificacion = tk.Label(self.pag3, text="Clasificación:")
        self.AenClasificacion = tk.Entry(self.pag3)
        self.AetMarca = tk.Label(self.pag3, text="Marca:")
        self.AenMarca = tk.Entry(self.pag3)
        self.AetPrecio = tk.Label(self.pag3, text="Precio:")
        self.AenPrecio = tk.Entry(self.pag3)
        self.Actualizar = tk.Button(self.pag3, text="Actualizar", command=self.Actualizar_Bebida)
        
        self.AetID.grid(row=0, column=0)
        self.AenID.grid(row=0, column=1)
        self.AetNombre.grid(row=1, column=0)
        self.AenNombre.grid(row=1, column=1)
        self.AetClasificacion.grid(row=2, column=0)
        self.AenClasificacion.grid(row=2, column=1)
        self.AetMarca.grid(row=3, column=0)
        self.AenMarca.grid(row=3, column=1)
        self.AetPrecio.grid(row=4, column=0)
        self.AenPrecio.grid(row=4, column=1)
        self.Actualizar.grid(row=5, column=0)

        self.Mostrar = tk.Button(self.pag4, text="Mostrar todas", command=self.Consultar_Bebidas)
        self.Mostrar.pack()
        
        self.Preciopromedio = tk.Button(self.pag5, text="Calcular", command=self.Precio_Promedio)
        self.Preciopromedio.pack()
        
        self.CetMarca = tk.Label(self.pag6, text="Marca:")
        self.CenMarca = tk.Entry(self.pag6)
        self.calcularpormarca = tk.Button(self.pag6, text="Clacular", command =self.Cantidad_Marca)
        self.CetMarca.grid(row=0, column=0)
        self.CenMarca.grid(row=0, column=1)
        self.calcularpormarca.grid(row=1, column=0)

        self.CetClasif = tk.Label(self.pag7, text="Clasificación:")
        self.CenClasif = tk.Entry(self.pag7)
        self.calcularporclasificacion = tk.Button(self.pag7, text="Calcular", command=self.Cantidad_Clasificacion)

        self.CetClasif.grid(row=0, column=0)
        self.CenClasif.grid(row=0, column=1)
        self.calcularporclasificacion.grid(row=1, column=0)

        self.notebook.pack()
        self.ventana.mainloop()

    def Alta_Bebidas(self):
        id = int(self.IDEn.get())
        nombre = self.NombreEn.get()
        clasificacion = self.ClasificacionEn.get()
        marca = self.MarcaEn.get()
        precio = float(self.PrecioEn.get())
        bebida = {'id': id, 'nombre': nombre, 'clasificacion': clasificacion, 'marca': marca, 'precio': precio}
        self.bebidas.append(bebida)
        self.IDEn.delete(0, tk.END)
        self.NombreEn.delete(0, tk.END)
        self.ClasificacionEn.delete(0, tk.END)
        self.MarcaEn.delete(0, tk.END)
        self.PrecioEn.delete(0, tk.END)

        messagebox.showinfo("Agregada", "La bebida ya se agrego")


    def Baja_Bebida(self):
        id = int(self.BenID.get())

        for bebida in self.bebidas:
            if bebida['id'] == id:
                self.bebidas.remove(bebida)
                messagebox.showinfo("Eliminado", "La bebida ya se elimino")
                return

    def Actualizar_Bebida(self):
        id = int(self.AenID.get())
        nombre = self.AenNombre.get()
        clasificacion = self.AenClasificacion.get()
        marca = self.AenMarca.get()
        precio = float(self.AenPrecio.get())


        for bebida in self.bebidas:
            if bebida['id'] == id:
                bebida['nombre'] = nombre
                bebida['clasificacion'] = clasificacion
                bebida['marca'] = marca
                bebida['precio'] = precio
                messagebox.showinfo("Actualizado", "Los campos se actualizaron correctamente")

    
    def Consultar_Bebidas(self):
        if self.bebidas:
            bebidas_str = ""
            for bebida in self.bebidas:
                bebidas_str += f"ID: {bebida['id']}, Nombre: {bebida['nombre']}, Clasificación: {bebida['clasificacion']}, Marca: {bebida['marca']}, Precio: {bebida['precio']}\n"
            messagebox.showinfo("Bebidas", bebidas_str)
        else:
            messagebox.showwarning("Advertencia", "No hay nada")

    
    def Precio_Promedio(self):

    def Cantidad_Marca(self):

    def Cantidad_Clasificacion(self):

        



            
ventana = AlmacendeBebidas()
