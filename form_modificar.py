from tkinter import *
from tkinter import ttk
from v_servicios import servicios
from v_areas import funcionagregar
from v_areas_modificar import areasM
from v_servicios_modificar import serviciosM
import mariadb

try: 
    conexion = mariadb.connect(
        user="ventana",
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
color_fondo = "#b8abab"

def modificar():
    ventana = Tk()
    ventana.title("Modificar")
    ventana.geometry("1270x625")
    ventana.config(bg=color_fondo)
    #my_ima = PhotoImage(file='coparmex.png')
    #Etiqueta = Label (ventana, image=my_ima).place(x=420, y=360)
    ventana.resizable(0,0)



    #Datos de la Empresa-------------------------------------------------------------------------
    lblTitulo1 = Label(ventana, text="Datos de la Empresa", bg="orange", fg="black")
    lblTitulo1.place(x=0, y=5, width=1270, height=20)
    #------------------------------------------
    lbl1 = Label(ventana, text="Dirección:")
    lbl1.place(x=1, y=30)
    lbl1.config(bg=color_fondo)
    txt1 = Entry(ventana)
    txt1.place(x=70, y=30, width=180, height=20)
    txt1.config(border=3)
    #------------------------------------------
    lbl2 = Label(ventana, text="Col.:")
    lbl2.place(x=265, y=30)
    lbl2.config(bg=color_fondo)
    txt2 = Entry(ventana)
    txt2.place(x=315, y=30, width=120, height=20)
    txt2.config(border=3)
    #------------------------------------------
    lbl3 = Label(ventana, text="CP:")
    lbl3.place(x=440, y=30)
    lbl3.config(bg=color_fondo)
    txt3 = Entry(ventana)
    txt3.place(x=470, y=30, width=100, height=20)
    txt3.config(border=3)
    #------------------------------------------
    lbl4 = Label(ventana, text="Entre Calles:")
    lbl4.place(x=575, y=30)
    lbl4.config(bg=color_fondo)
    txt4 = Entry(ventana)
    txt4.place(x=650, y=30, width=285, height=20)
    txt4.config(border=3)
    #------------------------------------------
    lbl5 = Label(ventana, text="Teléfono:")
    lbl5.place(x=945, y=30)
    lbl5.config(bg=color_fondo)
    txt5 = Entry(ventana)
    txt5.place(x=1005, y=30, width=100, height=20)
    txt5.config(border=3)
    #------------------------------------------
    lbl6 = Label(ventana, text="Fax:")
    lbl6.place(x=1120, y=30)
    lbl6.config(bg=color_fondo)
    txt6 = Entry(ventana)
    txt6.place(x=1160, y=30, width=100, height=20)
    txt6.config(border=3)
    #------------------------------------------
    lbl7 = Label(ventana, text="Correo:")
    lbl7.place(x=1, y=60)
    lbl7.config(bg=color_fondo)
    txt7 = Entry(ventana)
    txt7.place(x=70, y=60, width=180, height=20)
    txt7.config(border=3)
    #-----------------------------------------
    lbl8 = Label(ventana, text="Pag-Web:")
    lbl8.place(x=255, y=60)
    lbl8.config(bg=color_fondo)
    txt8 = Entry(ventana)
    txt8.place(x=315, y=60, width=255, height=20)
    txt8.config(border=3)
    #------------------------------------------
    lbl9 = Label(ventana, text="Aniversario:")
    lbl9.place(x=575, y=60)
    lbl9.config(bg=color_fondo)
    txt9 = Entry(ventana)
    txt9.place(x=650, y=60, width=80, height=20)
    txt9.config(border=3)
    #------------------------------------------
    lbl10 = Label(ventana, text="Tipo Emp:")
    lbl10.place(x=735, y=60)
    lbl10.config(bg=color_fondo)
    txt10 = Entry(ventana)
    txt10.place(x=800, y=60, width=135, height=20)
    txt10.config(border=3)
    #------------------------------------------
    lbl11 = Label(ventana, text="Tamaño Emp:")
    lbl11.place(x=945, y=60)
    lbl11.config(bg=color_fondo)
    txt11 = Entry(ventana)
    txt11.place(x=1025, y=60, width=235, height=20)
    txt11.config(border=3)
    #------------------------------------------
    lbl12 = Label(ventana, text="Reg-Pat.:")
    lbl12.place(x=5, y=90)
    lbl12.config(bg=color_fondo)
    txt12 = Entry(ventana)
    txt12.place(x=70, y=90, width=180, height=20)
    txt12.config(border=3)
    #------------------------------------------
    lbl13 = Label(ventana, text="Empleos:")
    lbl13.place(x=255, y=90)
    lbl13.config(bg=color_fondo)
    txt13 = Entry(ventana)
    txt13.place(x=315, y=90, width=255, height=20)
    txt13.config(border=3)
    #------------------------------------------
    lbl14 = Label(ventana, text="Sexo:")
    lbl14.place(x=590, y=90)
    lbl14.config(bg=color_fondo)
    txt14 = Entry(ventana)
    txt14.place(x=650, y=90, width=80, height=20)
    txt14.config(border=3)
    #------------------------------------------
    lbl15 = Label(ventana, text="Prod/Serv:")
    lbl15.place(x=735, y=90)
    lbl15.config(bg=color_fondo)
    txt15 = Entry(ventana)
    txt15.place(x=800, y=90, width=460, height=20)
    txt15.config(border=3)
    #-------------------------------------------------Datos Fiscales----------------------------------------------------------------------
    lblTitulo2 = Label(ventana, text="Datos Fiscales", bg="orange", fg="black")
    lblTitulo2.place(x=0, y=120, width=1270, height=20)
    #-------------------------------------------
    lbl16 = Label(ventana, text="R-Social:")
    lbl16.place(x=1, y=150)
    lbl16.config(bg=color_fondo)
    txt16 = Entry(ventana)
    txt16.place(x=70, y=150, width=180, height=20)
    txt16.config(border=3)
    #-------------------------------------------
    lbl17 = Label(ventana, text="R-Comercial:")
    lbl17.place(x=255, y=150)
    lbl17.config(bg=color_fondo)
    txt17 = Entry(ventana)
    txt17.place(x=335, y=150, width=170, height=20)
    txt17.config(border=3)
    #-------------------------------------------
    lbl18 = Label(ventana, text="Dirección:")
    lbl18.place(x=510, y=150)
    lbl18.config(bg=color_fondo)
    txt18 = Entry(ventana)
    txt18.place(x=570, y=150, width=160, height=20)
    txt18.config(border=3)
    #-------------------------------------------
    lbl19 = Label(ventana, text="Col.:")
    lbl19.place(x=735, y=150)
    lbl19.config(bg=color_fondo)
    txt19 = Entry(ventana)
    txt19.place(x=765, y=150, width=180, height=20)
    txt19.config(border=3)
    #--------------------------------------------
    lbl20 = Label(ventana, text="CP:")
    lbl20.place(x=950, y=150)
    lbl20.config(bg=color_fondo)
    txt20 = Entry(ventana)
    txt20.place(x=975, y=150, width=80, height=20)
    txt20.config(border=3)
    #--------------------------------------------
    lbl21 = Label(ventana, text="R.F.C:")
    lbl21.place(x=1060, y=150)
    lbl21.config(bg=color_fondo)
    txt21= Entry(ventana)
    txt21.place(x=1100, y=150, width=160, height=20)
    txt21.config(border=3)
    #--------------------------------------------
    lbl22 = Label(ventana, text="Municipio:")
    lbl22.place(x=1, y=180)
    lbl22.config(bg=color_fondo)
    txt22 = Entry(ventana)
    txt22.place(x=70, y=180, width=180, height=20)
    txt22.config(border=3)
    #--------------------------------------------
    lbl23 = Label(ventana, text="Estado:")
    lbl23.place(x=270, y=180)
    lbl23.config(bg=color_fondo)
    txt23 = Entry(ventana)
    txt23.place(x=335, y=180, width=170, height=20)
    txt23.config(border=3)
    #--------------------------------------------
    lbl24 = Label(ventana, text="id_empresa:")
    lbl24.place(x=510, y=180)
    lbl24.config(bg=color_fondo)
    txt24 = Entry(ventana)
    txt24.place(x=580, y=180, width=80, height=20)
    txt24.config(border=3)
    #-------------------------------------------------Socios----------------------------------------------------------------------
    lblTitulo3 = Label(ventana, text="Datos del Socio", bg="orange", fg="black")
    lblTitulo3.place(x=0, y=210, width=1270, height=20)
    #--------------------------------------------
    lbl25 = Label(ventana, text="Nombre:")
    lbl25.place(x=1, y=240)
    lbl25.config(bg=color_fondo)
    txt25 = Entry(ventana)
    txt25.place(x=70, y=240, width=170, height=20)
    txt25.config(border=3)
    #--------------------------------------------
    lbl26 = Label(ventana, text="Apellido P.:")
    lbl26.place(x=245, y=240)
    lbl26.config(bg=color_fondo)
    txt26 = Entry(ventana)
    txt26.place(x=315, y=240, width=120, height=20)
    txt26.config(border=3)
    #--------------------------------------------
    lbl27 = Label(ventana, text="Apellido M.:")
    lbl27.place(x=440, y=240)
    lbl27.config(bg=color_fondo)
    txt27 = Entry(ventana)
    txt27.place(x=515, y=240, width=120, height=20)
    txt27.config(border=3)
    #--------------------------------------------
    lbl28 = Label(ventana, text="Titulo:")
    lbl28.place(x=640, y=240)
    lbl28.config(bg=color_fondo)
    txt28 = Entry(ventana)
    txt28.place(x=685, y=240, width=100, height=20)
    txt28.config(border=3)
    #--------------------------------------------
    lbl29 = Label(ventana, text="Teléfono:")
    lbl29.place(x=787, y=240)
    lbl29.config(bg=color_fondo)
    txt29 = Entry(ventana)
    txt29.place(x=845, y=240, width=100, height=20)
    txt29.config(border=3)
    #--------------------------------------------
    lbl30 = Label(ventana, text="Correo:")
    lbl30.place(x=950, y=240)
    lbl30.config(bg=color_fondo)
    txt30 = Entry(ventana)
    txt30.place(x=996, y=240, width=260, height=20)
    txt30.config(border=3)
    #--------------------------------------------
    lbl31 = Label(ventana, text="Cumple:")
    lbl31.place(x=1, y=270)
    lbl31.config(bg=color_fondo)
    txt31 = Entry(ventana)
    txt31.place(x=70, y=270, width=120, height=20)
    txt31.config(border=3)
    #--------------------------------------------
    lbl32 = Label(ventana, text="id_empresa:")
    lbl32.place(x=195, y=270)
    lbl32.config(bg=color_fondo)
    txt32 = Entry(ventana)
    txt32.place(x=265, y=270, width=65, height=20)
    txt32.config(border=3)
    #-------------------------------------------------Servicios----------------------------------------------------------------------
    lblTitulo4 = Label(ventana, text="Servicios", bg="blue", fg="white")
    lblTitulo4.place(x=5, y=300, width=400, height=20)
    #ListBox-------------------------------------------------------------------------------------
    listbox = Listbox(ventana)
    listbox.place(x=5, y=330, width=330, height=100)
    #Botones-------------------------------------------------------------------------------------
    btnAgregar = Button(ventana, text="Agregar", command=servicios)
    btnAgregar.place(x=342, y=336, width=62)

    btnModificar = Button(ventana, text="Modificar", command=serviciosM)
    btnModificar.place(x=342, y=366)

    btnEliminar = Button(ventana, text="Eliminar")
    btnEliminar.place(x=342, y=396, width=62)
    #-------------------------------------------------Contactos Area----------------------------------------------------------------------
    lblTitulo5 = Label(ventana, text="Areas/Contactos", bg="blue", fg="white")
    lblTitulo5.place(x=435, y=300, width=400, height=20)
    #ListBox-------------------------------------------------------------------------------------
    listbox = Listbox(ventana)
    listbox.place(x=435, y=330, width=330, height=100)
    #Botones-------------------------------------------------------------------------------------
    btnAgregar1 = Button(ventana, text="Agregar", command=funcionagregar)
    btnAgregar1.place(x=772, y=336, width=62)

    btnModificar1 = Button(ventana, text="Modificar", command=areasM)
    btnModificar1.place(x=772, y=366)

    btnEliminar1 = Button(ventana, text="Eliminar")
    btnEliminar1.place(x=772, y=396, width=62)

    #-------------------------------------------------Factura----------------------------------------------------------------------
    lblTitulo6 = Label(ventana, text="Recepción de Factura", bg="orange", fg="black")
    lblTitulo6.place(x=5, y=440, width=400, height=20)
    #--------------------------------------------
    lbl39 = Label(ventana, text="Encargado:")
    lbl39.place(x=1, y=470)
    lbl39.config(bg=color_fondo)
    txt39 = Entry(ventana)
    txt39.place(x=70, y=470, width=180, height=20)
    txt39.config(border=3)
    #--------------------------------------------
    lbl40 = Label(ventana, text="Teléfono:")
    lbl40.place(x=1, y=500)
    lbl40.config(bg=color_fondo)
    txt40 = Entry(ventana)
    txt40.place(x=70, y=500, width=90, height=20)
    txt40.config(border=3)
    #--------------------------------------------
    lbl41 = Label(ventana, text="Ext.:")
    lbl41.place(x=170, y=500)
    lbl41.config(bg=color_fondo)
    txt41 = Entry(ventana)
    txt41.place(x=205, y=500, width=90, height=20)
    txt41.config(border=3)
    #--------------------------------------------
    lbl42 = Label(ventana, text="Correo:")
    lbl42.place(x=1, y=530)
    lbl42.config(bg=color_fondo)
    txt42 = Entry(ventana)
    txt42.place(x=70, y=530, width=335, height=20)
    txt42.config(border=3)
    # #--------------------------------------------
    lbl43 = Label(ventana, text="Días R.F:")
    lbl43.place(x=1, y=560)
    lbl43.config(bg=color_fondo)
    txt43 = Entry(ventana)
    txt43.place(x=70, y=560, width=125, height=20)
    txt43.config(border=3)
    #--------------------------------------------
    lbl44 = Label(ventana, text="Horario:")
    lbl44.place(x=200, y=560)
    lbl44.config(bg=color_fondo)
    txt44 = Entry(ventana)
    txt44.place(x=255, y=560, width=150, height=20)
    txt44.config(border=3)
    #-------------------------------------------
    lbl45 = Label(ventana, text="Días Pago:")
    lbl45.place(x=1, y=590)
    lbl45.config(bg=color_fondo)
    txt45 = Entry(ventana)
    txt45.place(x=70, y=590, width=125, height=20)
    txt45.config(border=3)
    #-------------------------------------------
    lbl46 = Label(ventana, text="Horario:")
    lbl46.place(x=200, y=590)
    lbl46.config(bg=color_fondo)
    txt46 = Entry(ventana)
    txt46.place(x=255, y=590, width=150, height=20)
    txt46.config(border=3)
    # #-------------------------------------------
    lbl47 = Label(ventana, text="id_empresa:")
    lbl47.place(x=260, y=470)
    lbl47.config(bg=color_fondo)
    txt47 = Entry(ventana)
    txt47.place(x=340, y=470, width=65, height=20)
    txt47.config(border=3)

    #-------------------------------------------------Afiliaciones----------------------------------------------------------------------
    lblTitulo7 = Label(ventana, text="Afiliaciones", bg="orange", fg="white")
    lblTitulo7.place(x=858, y=300, width=400, height=20)
    #-------------------------------------------
    lbl52 = Label(ventana, text="Nombre:")
    lbl52.place(x=858, y=330)
    lbl52.config(bg=color_fondo)
    txt52 = Entry(ventana)
    txt52.place(x=925, y=330, width=330, height=20)
    txt52.config(border=3)
    #-------------------------------------------
    lbl53 = Label(ventana, text="Apellido P.:")
    lbl53.place(x=858, y=360)
    lbl53.config(bg=color_fondo)
    txt53 = Entry(ventana)
    txt53.place(x=925, y=360, width=120, height=20)
    txt53.config(border=3)
    #-------------------------------------------
    lbl54 = Label(ventana, text="Apellido M.:")
    lbl54.place(x=1055, y=360)
    lbl54.config(bg=color_fondo)
    txt54 = Entry(ventana)
    txt54.place(x=1130, y=360, width=125, height=20)
    txt54.config(border=3)
    #-------------------------------------------
    lbl55 = Label(ventana, text="Puesto")
    lbl55.place(x=858, y=390)
    lbl55.config(bg=color_fondo)
    txt55 = Entry(ventana)
    txt55.place(x=925, y=390, width=330, height=20)
    txt55.config(border=3)
    #-------------------------------------------------Coparmex----------------------------------------------------------------------
    lblTitulo8 = Label(ventana, text="Coparmex", bg="orange", fg="black")
    lblTitulo8.place(x=435, y=440, width=331, height=20)
    #-------------------------------------------
    lbl56 = Label(ventana, text="Fecha:")
    lbl56.config(bg=color_fondo)
    lbl56.place(x=435, y=470)
    txt56 = Entry(ventana)
    txt56.place(x=500, y=470, width=265, height=20)
    txt56.config(border=3)
    #-------------------------------------------
    lbl57 = Label(ventana, text="Tipo Plan:")
    lbl57.place(x=435, y=500)
    lbl57.config(bg=color_fondo)
    txt57 = Entry(ventana)
    txt57.place(x=500, y=500, width=265, height=20)
    txt57.config(border=3)
    #-------------------------------------------
    lbl58 = Label(ventana, text="id_emp:")
    lbl58.place(x=435, y=530)
    lbl58.config(bg=color_fondo)
    txt58 = Entry(ventana)
    txt58.place(x=500, y=530, width=80, height=20)
    txt58.config(border=3)
    #-------------------------------------------
    lbl59 = Label(ventana, text="id_afiliación:")
    lbl59.place(x=610, y=530)
    lbl59.config(bg=color_fondo)
    txt59 = Entry(ventana)
    txt59.place(x=690, y=530, width=75, height=20)
    txt59.config(border=3)
    #--------------------------------------------
    btnGuardar = Button(ventana, text="Guardar Cambios", bg="green", fg="white")
    btnGuardar.place(x=555, y=570)
    #Final---------------------------------------------------------------------------------------
    ventana.mainloop()
#modificar()