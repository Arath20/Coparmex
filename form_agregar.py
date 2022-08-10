from tkinter import *
import mariadb

#Conexión-BDD
try: 
    conexion = mariadb.connect(
        user="root",
        password="123",
        host="127.0.0.1",
        port=3306,
        database="prueba"
    )
    
except mariadb.Error as error:
    print(f"Error en la conexión: {error}")
cursor = conexion.cursor()

def agregar():
    cursor = conexion.cursor()
    def _on_frame_configure(self, event=None):
        root.configure(scrollregion=root.bbox("all"))

    def registro():
            #Datos De La Empresa
            dir  = txt1.get()
            col  = txt2.get()
            cp   = txt3.get()
            ec   = txt4.get()
            tel1 = txt5.get()
            fax  = txt6.get()
            cor1 = txt7.get()
            pw   = txt8.get()
            ani  = txt9.get()
            tie  = txt10.get()
            tae  = txt11.get()
            rp   = txt12.get()
            sex  = txt13.get()
            te   = txt14.get()
            ps   = txt15.get()
            #Datos Fiscales
            rs  = txt16.get()
            rc  = txt17.get()
            dir = txt18.get()
            col = txt19.get()
            cp  = txt20.get()
            mun = txt21.get()
            est = txt22.get()
            rfc = txt23.get()
            fk_idempresa = txt24.get()
            #Datos del Socio
            nom  = txt25.get()
            app  = txt26.get()
            apm  = txt27.get()
            titu = txt28.get()
            tel2 = txt29.get()
            cor2 = txt30.get()
            cum  = txt31.get()
            fk_idempresa1 = txt32.get()
            #Datos Contactos Area
            area = txt33.get()
            noma = txt34.get()
            tel3 = txt35.get()
            ext1 = txt36.get()
            cor3 = txt37.get()
            fk_idempresa2 = txt38.get()
            #Factura
            ep   = txt39.get()
            tel4 = txt40.get()
            ext2 = txt41.get()
            cor4 = txt42.get()
            drf  = txt43.get()
            hrf  = txt44.get()
            dp   = txt45.get()
            hdp  = txt46.get()
            fk_idempresa3 = txt47.get()
            #Servicios
            fecha = txt48.get()
            des   = txt49.get()
            fk_idservicio = txt50.get()
            fk_idempresa4 = txt51.get()
            #Afiliacion
            nomb   = txt52.get()
            ap_pat = txt53.get()
            ap_mat = txt54.get()
            puest  = txt55.get()
            #Coparmex
            fecha1 = txt56.get()
            t_plan = txt57.get()
            fk_idempresa5   = txt58.get()
            fk_idafiliacion = txt59.get()
            
            try:
                cursor.execute("INSERT INTO empresa (direccion, col, cp, entre_calles, tel, fax, correo, pag_web, aniversario, tipo_empresa, tamaño_empresa, reg_patronal, sexo, total_empleo, p_productos) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (dir, col, cp, ec, tel1, fax, cor1, pw, ani, tie, tae, rp, sex, te, ps))
                cursor.execute("INSERT INTO cliente (razon_social, razon_comercial, direccion, col, cp, municipio, estado, rfc, id_empresa) VALUES (?,?,?,?,?,?,?,?,?)", (rs, rc, dir, col, cp, mun, est, rfc, fk_idempresa))
                cursor.execute("INSERT INTO socios  (nombre, ap_paterno, ap_materno, titulo, telefono, correo, cumpleaños, id_empresa) VALUES (?,?,?,?,?,?,?,?)", (nom, app, apm, titu, tel2, cor2, cum, fk_idempresa1))
                cursor.execute("INSERT INTO contactos_area (area, nombre_persona, tel, ext, correo, id_empresa) VALUES (?,?,?,?,?,?)", (area, noma, tel3, ext1, cor3, fk_idempresa2))
                cursor.execute("INSERT INTO factura (encargado_pagos, tel, ext, correo, dias_rf, horario_rf, dias_pago, horario_dp, id_empresa) VALUES (?,?,?,?,?,?,?,?,?)", (ep, tel4, ext2, cor4, drf, hrf, dp, hdp, fk_idempresa3))
                cursor.execute("INSERT INTO servicio_empresa (fecha, descripcion, id_servicio, id_empresa) VALUES (?,?,?,?)", (fecha, des, fk_idservicio, fk_idempresa4))
                cursor.execute("INSERT INTO afiliacion (nombre, ap_paterno, ap_materno, puesto) VALUES (?,?,?,?)", (nomb, ap_pat, ap_mat, puest))
                cursor.execute("INSERT INTO coparmex (fecha, tipo_plan, id_empresa, id_afiliacion) VALUES(?,?,?,?)", (fecha1, t_plan, fk_idempresa5, fk_idafiliacion))
                conexion.commit()
            except mariadb.Error as error_registro: 
                print(f"Error en el registro: {error_registro}")
        
    root = Tk()
    root.title("Nueva Afiliación")
    root.geometry("942x630")
    root.resizable(0,0)

    #-------------------------------------------------Datos Empresa----------------------------------------------------------------------
    lblTitulo1 = Label(root, text="Datos de la Empresa", bg="blue", fg="white")
    lblTitulo1.place(x=5, y=5, width=300, height=30)
    #------------------------------------------
    lbl1 = Label(root, text="Dirección")
    lbl1.place(x=0, y=40)
    txt1 = Entry(root)
    txt1.place(x=70, y=40, width=235, height=20)
    #------------------------------------------
    lbl2 = Label(root, text="Colonia")
    lbl2.place(x=0, y=65)
    txt2 = Entry(root)
    txt2.place(x=70, y=65, width=100, height=20)
    #------------------------------------------
    lbl3 = Label(root, text="C.Postal")
    lbl3.place(x=170, y=65)
    txt3 = Entry(root)
    txt3.place(x=220, y=65, width=85, height=20)
    #------------------------------------------
    lbl4 = Label(root, text="Entre Calles")
    lbl4.place(x=0, y=90)
    txt4 = Entry(root)
    txt4.place(x=70, y=90, width=235, height=20)
    #------------------------------------------
    lbl5 = Label(root, text="Teléfono")
    lbl5.place(x=0, y=115)
    txt5 = Entry(root)
    txt5.place(x=70, y=115, width=100, height=20)
    #------------------------------------------
    lbl6 = Label(root, text="Fax")
    lbl6.place(x=180, y=115)
    txt6 = Entry(root)
    txt6.place(x=210, y=115, width=95, height=20)
    #------------------------------------------
    lbl7 = Label(root, text="Correo")
    lbl7.place(x=0, y=140)
    txt7 = Entry(root)
    txt7.place(x=70, y=140, width=235, height=20)
    #-----------------------------------------
    lbl8 = Label(root, text="Pag-Web")
    lbl8.place(x=0, y=165)
    txt8 = Entry(root)
    txt8.place(x=70, y=165, width=235, height=20)
    #------------------------------------------
    lbl9 = Label(root, text="Aniversario")
    lbl9.place(x=0, y=190)
    txt9 = Entry(root)
    txt9.place(x=70, y=190, width=235, height=20)
    #------------------------------------------
    lbl10 = Label(root, text="Tipo")
    lbl10.place(x=0, y=215)
    txt10 = Entry(root)
    txt10.place(x=70, y=215, width=100, height=20)
    #-----------------------------------------
    lbl11 = Label(root, text="Tamaño")
    lbl11.place(x=175, y=215)
    txt11 = Entry(root)
    txt11.place(x=230, y=215, width=75, height=20)
    #------------------------------------------
    lbl12 = Label(root, text="Reg-Pat.")
    lbl12.place(x=0, y=240)
    txt12 = Entry(root)
    txt12.place(x=70, y=240, width=235, height=20)
    #------------------------------------------
    lbl13 = Label(root, text="T-Empleos")
    lbl13.place(x=0, y=265)
    txt13 = Entry(root)
    txt13.place(x=70, y=265, width=120, height=20)
    #------------------------------------------
    lbl14 = Label(root, text="Sexo")
    lbl14.place(x=200, y=265)
    txt14 = Entry(root)
    txt14.place(x=240, y=265, width=65, height=20)
    #------------------------------------------
    lbl15 = Label(root, text="Prod/Serv")
    lbl15.place(x=0, y=290)
    txt15 = Entry(root)
    txt15.place(x=70, y=290, width=235, height=20)
    #-------------------------------------------------Datos Fiscales----------------------------------------------------------------------
    lblTitulo2 = Label(root, text="Datos Fiscales", bg="blue", fg="white")
    lblTitulo2.place(x=5, y=320, width=300, height=30)
    #-------------------------------------------
    lbl16 = Label(root, text="R-Social")
    lbl16.place(x=0, y=355)
    txt16 = Entry(root)
    txt16.place(x=70, y=355, width=235, height=20)
    #-------------------------------------------
    lbl17 = Label(root, text="R-Comercial")
    lbl17.place(x=0, y=380)
    txt17 = Entry(root)
    txt17.place(x=70, y=380, width=235, height=20)
    #-------------------------------------------
    lbl18 = Label(root, text="Dirección")
    lbl18.place(x=0, y=405)
    txt18 = Entry(root)
    txt18.place(x=70, y=405, width=235, height=20)
    #-------------------------------------------
    lbl19 = Label(root, text="Colonia")
    lbl19.place(x=0, y=430)
    txt19 = Entry(root)
    txt19.place(x=70, y=430, width=100, height=20)
    #--------------------------------------------
    lbl20 = Label(root, text="CP")
    lbl20.place(x=175, y=430)
    txt20 = Entry(root)
    txt20.place(x=200, y=430, width=105, height=20)
    #--------------------------------------------
    lbl21 = Label(root, text="R.F.C")
    lbl21.place(x=0, y=455)
    txt21= Entry(root)
    txt21.place(x=70, y=455, width=235, height=20)
    #--------------------------------------------
    lbl22 = Label(root, text="Municipio")
    lbl22.place(x=0, y=480)
    txt22 = Entry(root)
    txt22.place(x=70, y=480, width=235, height=20)
    #--------------------------------------------
    lbl23 = Label(root, text="Estado")
    lbl23.place(x=0, y=505)
    txt23 = Entry(root)
    txt23.place(x=70, y=505, width=235, height=20)
    #--------------------------------------------
    lbl24 = Label(root, text="id_empresa")
    lbl24.place(x=0, y=530)
    txt24 = Entry(root)
    txt24.place(x=70, y=530, width=65, height=20)
    #-------------------------------------------------Socios----------------------------------------------------------------------
    lblTitulo3 = Label(root, text="Datos del Socio", bg="blue", fg="white")
    lblTitulo3.place(x=320, y=5, width=300, height=30)
    #--------------------------------------------
    lbl25 = Label(root, text="Nombre")
    lbl25.place(x=320, y=40)
    txt25 = Entry(root)
    txt25.place(x=385, y=40, width=235, height=20)
    #--------------------------------------------
    lbl26 = Label(root, text="Apellido P.")
    lbl26.place(x=320, y=65)
    txt26 = Entry(root)
    txt26.place(x=385, y=65, width=235, height=20)
    #--------------------------------------------
    lbl27 = Label(root, text="Apellido M.")
    lbl27.place(x=320, y=90)
    txt27 = Entry(root)
    txt27.place(x=385, y=90, width=235, height=20)
    #--------------------------------------------
    lbl28 = Label(root, text="Titulo")
    lbl28.place(x=320, y=115)
    txt28 = Entry(root)
    txt28.place(x=385, y=115, width=90, height=20)
    #--------------------------------------------
    lbl29 = Label(root, text="Teléfono")
    lbl29.place(x=480, y=115)
    txt29 = Entry(root)
    txt29.place(x=540, y=115, width=80, height=20)
    #--------------------------------------------
    lbl30 = Label(root, text="Correo")
    lbl30.place(x=320, y=140)
    txt30 = Entry(root)
    txt30.place(x=385, y=140, width=235, height=20)
    #--------------------------------------------
    lbl31 = Label(root, text="Cumple")
    lbl31.place(x=320, y=165)
    txt31 = Entry(root)
    txt31.place(x=385, y=165, width=235, height=20)
    #--------------------------------------------
    lbl32 = Label(root, text="id_empresa")
    lbl32.place(x=320, y=190)
    txt32 = Entry(root)
    txt32.place(x=385, y=190, width=65, height=20)
    #-------------------------------------------------Contactos Area----------------------------------------------------------------------
    lblTitulo4 = Label(root, text="Contactos Área", bg="blue", fg="white")
    lblTitulo4.place(x=320, y=220, width=300, height=30)
    #--------------------------------------------
    lbl33 = Label(root, text="Area")
    lbl33.place(x=320, y=255)
    txt33 = Entry(root)
    txt33.place(x=385, y=255, width=235, height=20)
    #--------------------------------------------
    lbl34 = Label(root, text="Nombre P.")
    lbl34.place(x=320, y=280)
    txt34 = Entry(root)
    txt34.place(x=385, y=280, width=235, height=20)
    #--------------------------------------------
    lbl35 = Label(root, text="Teléfono")
    lbl35.place(x=320, y=305)
    txt35 = Entry(root)
    txt35.place(x=385, y=305, width=100, height=20)
    #--------------------------------------------
    lbl36 = Label(root, text="Ext.")
    lbl36.place(x=500, y=305)
    txt36 = Entry(root)
    txt36.place(x=530, y=305, width=90, height=20)
    #--------------------------------------------
    lbl37 = Label(root, text="Correo")
    lbl37.place(x=320, y=330)
    txt37 = Entry(root)
    txt37.place(x=385, y=330, width=235, height=20)
    #--------------------------------------------
    lbl38 = Label(root, text="id_empresa")
    lbl38.place(x=320, y=355)
    txt38 = Entry(root)
    txt38.place(x=385, y=355, width=65, height=20)
    #-------------------------------------------------Factura----------------------------------------------------------------------
    lblTitulo4 = Label(root, text="Recepción de Factura", bg="blue", fg="white")
    lblTitulo4.place(x=320, y=380, width=300, height=30)
    #--------------------------------------------
    lbl39 = Label(root, text="Encargado")
    lbl39.place(x=320, y=415)
    txt39 = Entry(root)
    txt39.place(x=385, y=415, width=235, height=20)
    #--------------------------------------------
    lbl40 = Label(root, text="Teléfono")
    lbl40.place(x=320, y=440)
    txt40 = Entry(root)
    txt40.place(x=385, y=440, width=90, height=20)
    #--------------------------------------------
    lbl41 = Label(root, text="Ext.")
    lbl41.place(x=500, y=440)
    txt41 = Entry(root)
    txt41.place(x=530, y=440, width=90, height=20)
    #--------------------------------------------
    lbl42 = Label(root, text="Correo")
    lbl42.place(x=320, y=465)
    txt42 = Entry(root)
    txt42.place(x=385, y=465, width=235, height=20)
    #--------------------------------------------
    lbl43 = Label(root, text="Días R.F")
    lbl43.place(x=320, y=490)
    txt43 = Entry(root)
    txt43.place(x=385, y=490, width=90, height=20)
    #--------------------------------------------
    lbl44 = Label(root, text="Horario")
    lbl44.place(x=480, y=490)
    txt44 = Entry(root)
    txt44.place(x=530, y=490, width=90, height=20)
    #-------------------------------------------
    lbl45 = Label(root, text="Días Pago")
    lbl45.place(x=320, y=515)
    txt45 = Entry(root)
    txt45.place(x=385, y=515, width=90, height=20)
    #-------------------------------------------
    lbl46 = Label(root, text="Horario")
    lbl46.place(x=480, y=515)
    txt46 = Entry(root)
    txt46.place(x=530, y=515, width=90, height=20)
    #-------------------------------------------
    lbl47 = Label(root, text="id_empresa")
    lbl47.place(x=320, y=540)
    txt47 = Entry(root)
    txt47.place(x=385, y=540, width=65, height=20)
    #-------------------------------------------------Servicios----------------------------------------------------------------------
    lblTitulo5 = Label(root, text="Servicios", bg="blue", fg="white")
    lblTitulo5.place(x=635, y=5, width=300, height=30)
    #-------------------------------------------
    lbl48 = Label(root, text="Fecha")
    lbl48.place(x=635, y=40)
    txt48 = Entry(root)
    txt48.place(x=700, y=40, width=235, height=20)
    #-------------------------------------------
    lbl49 = Label(root, text="Descripción")
    lbl49.place(x=750, y=62)
    txt49 = Entry(root)
    txt49.place(x=635, y=85, width=300, height=20)
    #-------------------------------------------
    lbl50 = Label(root, text="id_servicio")
    lbl50.place(x=635, y=110)
    txt50 = Entry(root)
    txt50.place(x=700, y=110, width=60, height=20)
    #-------------------------------------------
    lbl51 = Label(root, text="id_empresa")
    lbl51.place(x=800, y=110)
    txt51 = Entry(root)
    txt51.place(x=875, y=110, width=60, height=20)
    #-------------------------------------------------Afiliaciones----------------------------------------------------------------------
    lblTitulo6 = Label(root, text="Afiliaciones", bg="blue", fg="white")
    lblTitulo6.place(x=635, y=140, width=300, height=30)
    #-------------------------------------------
    lbl52 = Label(root, text="Nombre")
    lbl52.place(x=635, y=180)
    txt52 = Entry(root)
    txt52.place(x=700, y=180, width=235, height=20)
    #-------------------------------------------
    lbl53 = Label(root, text="Apellido P.")
    lbl53.place(x=635, y=210)
    txt53 = Entry(root)
    txt53.place(x=700, y=210, width=235, height=20)
    #-------------------------------------------
    lbl54 = Label(root, text="Apellido M.")
    lbl54.place(x=635, y=240)
    txt54 = Entry(root)
    txt54.place(x=700, y=240, width=235, height=20)
    #-------------------------------------------
    lbl55 = Label(root, text="Puesto")
    lbl55.place(x=635, y=270)
    txt55 = Entry(root)
    txt55.place(x=700, y=270, width=235, height=20)
    #-------------------------------------------------Coparmex----------------------------------------------------------------------
    lblTitulo6 = Label(root, text="Coparmex", bg="blue", fg="white")
    lblTitulo6.place(x=635, y=300, width=300, height=30)
    #-------------------------------------------
    lbl56 = Label(root, text="Fecha")
    lbl56.place(x=635, y=335)
    txt56 = Entry(root)
    txt56.place(x=700, y=335, width=235, height=20)
    #-------------------------------------------
    lbl57 = Label(root, text="Tipo Plan")
    lbl57.place(x=635, y=360)
    txt57 = Entry(root)
    txt57.place(x=700, y=360, width=235, height=20)
    #-------------------------------------------
    lbl58 = Label(root, text="id_empresa")
    lbl58.place(x=635, y=385)
    txt58 = Entry(root)
    txt58.place(x=700, y=385, width=60, height=20)
    #-------------------------------------------
    lbl59 = Label(root, text="id_afiliación")
    lbl59.place(x=795, y=385)
    txt59 = Entry(root)
    txt59.place(x=875, y=385, width=60, height=20)
    
    #Boton-Agregar Registro
    btnAgregar = Button(root, text="Registrar", command=registro, bg="green", fg="white")
    btnAgregar.place(x=380, y=580, width=200)
    
    root.mainloop()
#agregar()