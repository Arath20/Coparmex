from tkinter import *
from form_agregar import agregar
from form_modificar import modificar
from detalles import details
import mariadb

try: 
    conexion = mariadb.connect(
        user="root",
        password="123",
        host="127.0.0.1",
        port=3306,
        database="prueba"
    )
    
    lbl = Label(text="Conexión exitosa a la base de datos " + conexion.database + ".").pack()
    
    cursor = conexion.cursor()
    
except mariadb.Error as error:
    print(f"Error en la conexión: {error}")
    
#Creación de la Ventana----------------------------------------------------------------------
ventana = Tk()
ventana.title("Coparmex NCG")
ventana.geometry("400x300")
ventana.resizable(0,0)

#Labels--------------------------------------------------------------------------------------
lbltitulo = Label(ventana, text="Afiliciones", font="Calisto", bg="gray", fg="white")
lbltitulo.place(x=0, y=20, width=400, height=30)

#ListBox------------------------------------------------------------------------------------
def CurSelect(evt):
    value=str((mylistbox.get(mylistbox.curselection())))
    print (value)
    
    scrollbar = Scrollbar(mylistbox)
    scrollbar.pack(side = RIGHT, fill = BOTH)
    mylistbox.config(yscrollcommand = scrollbar.set)
    scrollbar.config(command = mylistbox.yview)

listData = cursor.execute("SELECT razon_comercial FROM cliente")
customers = cursor.fetchall()

mylistbox=Listbox(ventana,width=60,height=10)
mylistbox.bind('<<ListboxSelect>>',CurSelect)
mylistbox.place(x=20, y=60, width=360, height=170)

for items in customers:
    mylistbox.insert(END,items)

#Botones-------------------------------------------------------------------------------------
btnAgregar = Button(ventana, text="Agregar", command=agregar)
btnAgregar.place(x=20, y=245, width=80)

btnVisualizar = Button(ventana, text="Ver", command=details)
btnVisualizar.place(x=125, y=245, width=50)

btnModificar = Button(ventana, text="Modificar", command=modificar)
btnModificar.place(x=200, y=245, width=80)

btnEliminar = Button(ventana, text="Eliminar")
btnEliminar.place(x=300, y=245, width=80)



#Final---------------------------------------------------------------------------------------
ventana.mainloop()