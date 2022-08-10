from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
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
muestra = canvas.read_sql("SELECT ")

pdf = canvas.Canvas("form.pdf", pagesize=A4)
pdf.setLineWidth(.3)
pdf.setFont('Helvetica', 14)

pdf.drawString(300,750,'COPARMEX')
pdf.drawString(30,735,'RICARDOGEEK.COM')
pdf.drawString(500,750,"27/10/2016")
pdf.line(480,747,580,747)

pdf.drawString(275,725,'ESTIMADO:')
pdf.drawString(500,725,"<NOMBRE>")
pdf.line(378,723,580,723)

pdf.drawString(30,703,'ETIQUETA:')
pdf.line(120,700,580,700)
pdf.drawString(120,703,"<ASUNTO DE LA CARTA GENERICO>")

pdf.save()