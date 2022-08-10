from tkinter import *
import mariadb

#Conexión-BDD
try: 
    conexion = mariadb.connect(
        user="ventana",
        password="123",
        host="127.0.0.1",
        port=3306,
        database="prueba"
    )
    
    cursor = conexion.cursor()
    
except mariadb.Error as error:
    print(f"Error en la conexión: {error}")


def funcionagregar():
    def _on_frame_configure(self, event=None):
        ventana.configure(scrollregion=ventana.bbox("all"))
    
    def registro():
            area = txt33.get()
            noma = txt34.get()
            tel3 = txt35.get()
            ext1 = txt36.get()
            cor3 = txt37.get()
            fk_idempresa2 = txt38.get()
            
            try:
                cursor.execute("INSERT INTO contactos_area (area, nombre_persona, tel, ext, correo, id_empresa) VALUES (?,?,?,?,?,?)", (area, noma, tel3, ext1, cor3, fk_idempresa2))
                conexion.commit()
            except mariadb.Error as error_registro: 
                print(f"Error en el registro: {error_registro}")
            
    #Creación de la Ventana
    ventana = Tk()
    ventana.title("Agregar - Contactos Área")
    ventana.geometry("300x240")
    ventana.resizable(0,0)

    lblTitulo4 = Label(ventana, text="Contactos Área", bg="orange", fg="black")
    lblTitulo4.place(x=0, y=5, width=310, height=20)
    #--------------------------------------------
    lbl33 = Label(ventana, text="Area:")
    lbl33.place(x=5, y=30)
    txt33 = Entry(ventana)
    txt33.place(x=75, y=30, width=220, height=20)
    #--------------------------------------------
    lbl34 = Label(ventana, text="Nombre P.:")
    lbl34.place(x=5, y=60)
    txt34 = Entry(ventana)
    txt34.place(x=75, y=60, width=220, height=20)
    #--------------------------------------------
    lbl35 = Label(ventana, text="Teléfono:")
    lbl35.place(x=5, y=90)
    txt35 = Entry(ventana)
    txt35.place(x=75, y=90, width=220, height=20)
    #--------------------------------------------
    lbl36 = Label(ventana, text="Ext.:")
    lbl36.place(x=5, y=120)
    txt36 = Entry(ventana)
    txt36.place(x=75, y=120, width=220, height=20)
    #--------------------------------------------
    lbl37 = Label(ventana, text="Correo:")
    lbl37.place(x=5, y=150)
    txt37 = Entry(ventana)
    txt37.place(x=75, y=150, width=220, height=20)
    #--------------------------------------------
    lbl38 = Label(ventana, text="id_empresa:")
    lbl38.place(x=5, y=180)
    txt38 = Entry(ventana)
    txt38.place(x=75, y=180, width=80, height=20)
    #--------------------------------------------
    btnAgregar = Button(ventana, text="Agregar", bg="green", fg="white", command=registro)
    btnAgregar.place(x=130, y=210)
    ventana.mainloop()
#funcionagregar()