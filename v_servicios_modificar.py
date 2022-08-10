from cgitb import text
from tkinter import *
import mariadb
from tkinter import ttk

#Conexión-BDD
try: 
    conexion = mariadb.connect(
        user="root",
        password="123",
        host="127.0.0.1",
        port=3306,
        database="prueba"
    )
    
    cursor = conexion.cursor()
    
except mariadb.Error as error:
    print(f"Error en la conexión: {error}")

#Función Datos-ComboBox
def combo(self):
    slist = cursor.fetchall()
    self.supplier.configure(values=slist)
    
def serviciosM():
    #Creación de la Ventana
    ventana = Tk()
    ventana.title("Modificar - Servicios")
    ventana.geometry("300x280")
    ventana.resizable(0,0)
    #Servicios
    lblTitulo = Label(ventana, text="Servicios", bg="orange", fg="black")
    lblTitulo.place(x=0, y=10, width=310, height=20)
    #ComboBox---------------------------------------------------------------------------
    curs = conexion.cursor()
    curs.execute('select servicio from servicios;')
    results = curs.fetchall()
    curs.close()
    results_for_combobox = [result[0] for result in results]
    combo = ttk.Combobox(ventana, state="readonly", values=results_for_combobox)
    combo.place(x=5, y=40, width=150)
    #-------------------------------------------
    lblFecha = Label(ventana, text="Fecha:")
    lblFecha.place(x=165, y=40)
    txt1 = Entry(ventana)
    txt1.place(x=205, y=40, width=90)
    #-------------------------------------------
    lblDescripcion = Label(ventana, text="Descripción")
    lblDescripcion.place(x=120, y=70)
    txt2 = Text(ventana)
    txt2.place(x=5, y=90, width=288, height=120)
    #--------------------------------------------
    lbl1 = Label(ventana, text="id_servicio:")
    lbl1.place(x=5, y=215)
    txt3 = Entry(ventana)
    txt3.place(x=70, y=215, width=50)
    #--------------------------------------------
    lbl2 = Label(ventana, text="id_empresa:")
    lbl2.place(x=170, y=215)
    txt4 = Entry(ventana)
    txt4.place(x=245, y=215, width=50)
    #Boton---------------------------------------
    btnGuardar = Button(ventana, text="Guardar", bg="green", fg="white")
    btnGuardar.place(x=110, y=250, width=80)
    ventana.mainloop()
#serviciosM()

