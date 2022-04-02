from tkinter import *
import psycopg2
import customtkinter

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")
root = customtkinter.CTk()
root.title("Tax-help")
root.wm_maxsize()

def Agregar():
    ventana_nueva1 = Toplevel()
    ventana_nueva1.geometry("400x50")
    ventana_nueva1.title("Agregar tabla")


def actualizar_datos(suma,row):
    text_variable2.set(suma)
    gp = suma*0.3
    retenido.set(suma*row[0]/100)
    if (gp >= row[1]):
        gastos_presuntos.set("Gastos presuntos: "+str(row[1]))
        gp = row[1]
    else:
        gastos_presuntos.set("Gastos presuntos: "+str(gp)) 
    impto_global = (suma-gp)*row[3]-row[2]
    ret = suma*row[0]/100
    impuesto_global.set("Impuesto global: "+str(impto_global))
    devolucion.set("Devolución: "+str(ret-impto_global))
    #SUMA -> SUMA : 10000000
    #ROW1 -> GASTOS PRESUNTOS :         
    #ROW2 -> CANTIDAD A REBAJAR
    #ROW3 -> FACTOR
    

def actualizar_retencion_meses(enero, febrero, marzo, abril, mayo, junio, julio, agosto, septiembre, octubre, noviembre, diciembre,row):
    retencion_enero_variable.set(float(enero)*row[0]/100)
    retencion_febrero_variable.set(float(febrero)*row[0]/100)
    retencion_marzo_variable.set(float(marzo)*row[0]/100)
    retencion_abril_variable.set(float(abril)*row[0]/100)
    retencion_mayo_variable.set(float(mayo)*row[0]/100)
    retencion_junio_variable.set(float(junio)*row[0]/100)
    retencion_julio_variable.set(float(julio)*row[0]/100)
    retencion_agosto_variable.set(float(agosto)*row[0]/100)
    retencion_septiembre_variable.set(float(septiembre)*row[0]/100)
    retencion_octubre_variable.set(float(octubre)*row[0]/100)
    retencion_noviembre_variable.set(float(noviembre)*row[0]/100)
    retencion_diciembre_variable.set(float(diciembre)*row[0]/100)

def calcular(enero, febrero, marzo, abril, mayo, junio, julio, agosto, septiembre, octubre, noviembre, diciembre, anio):

    label_enero.config(fg="black")
    label_febrero.config(fg="black")
    label_marzo.config(fg="black")
    label_abril.config(fg="black")
    label_mayo.config(fg="black")
    label_junio.config(fg="black")
    label_julio.config(fg="black")
    label_agosto.config(fg="black")
    label_septiembre.config(fg="black")
    label_octubre.config(fg="black")
    label_noviembre.config(fg="black")
    label_diciembre.config(fg="black")

    if anio == "":
        texto_variable.set('CAMPO FALTANTE : Año')
        return
    elif enero== "":
        enero = 0
    elif febrero== "":
        febrero = 0
    elif marzo== "":
        marzo = 0
    elif abril== "":
        abril = 0
    elif mayo== "":
        mayo = 0
    elif junio== "":
        junio = 0
    elif julio== "":
        julio = 0
    elif agosto== "":
        agosto = 0
    elif septiembre== "":
        septiembre = 0
    elif octubre== "":
        octubre = 0
    elif noviembre== "":
        noviembre = 0
    elif diciembre== "":
        diciembre = 0

    #SE COMPRUEBA QUE EL AÑO SEA UN NUMERO
    try:
        int(anio)
    except ValueError:
        texto_variable.set('Año debe ser numero entero. ej:2021')
        return

    #SE COMPRUEBA QUE EL MONTO DE LOS MESES SEAN DE TIPO FLOAT
    error_monto=0
    try:
        float(enero)
    except ValueError:
        texto_variable.set('Los montos deben ser numeros')
        label_enero.config(fg="red")
        error_monto=1
    try:
        float(febrero)
    except ValueError:
        texto_variable.set('Los montos deben ser numeros')
        label_febrero.config(fg="red")
        error_monto=1
    try:
        float(marzo)
    except ValueError:
        texto_variable.set('Los montos deben ser numeros')
        label_marzo.config(fg="red")
        error_monto=1
    try:
        float(abril)
    except ValueError:
        texto_variable.set('Los montos deben ser numeros')
        label_abril.config(fg="red")
        error_monto=1
    try:
        float(mayo)
    except ValueError:
        texto_variable.set('Los montos deben ser numeros')
        label_mayo.config(fg="red")
        error_monto=1
    try:
        float(junio)
    except ValueError:
        texto_variable.set('Los montos deben ser numeros')
        label_junio.config(fg="red")
        error_monto=1
    try:
        float(julio)
    except ValueError:
        texto_variable.set('Los montos deben ser numeros')
        label_julio.config(fg="red")
        error_monto=1
    try:
        float(agosto)
    except ValueError:
        texto_variable.set('Los montos deben ser numeros')
        label_agosto.config(fg="red")
        error_monto=1
    try:
        float(septiembre)
    except ValueError:
        texto_variable.set('Los montos deben ser numeros')
        label_septiembre.config(fg="red")
        error_monto=1
    try:
        float(octubre)
    except ValueError:
        texto_variable.set('Los montos deben ser numeros')
        label_octubre.config(fg="red")
        error_monto=1
    try:
        float(noviembre)
    except ValueError:
        texto_variable.set('Los montos deben ser numeros')
        label_noviembre.config(fg="red")
        error_monto=1
    try:
        float(diciembre)
    except ValueError:
        texto_variable.set('Los montos deben ser numeros')
        label_diciembre.config(fg="red")
        error_monto=1

    if(error_monto == 1):
        return

    #SE VERIFICA QUE LOS MONTOS SEAN NO NEGATIVOS

    conn = psycopg2.connect(
        dbname="postgres", 
        user="postgres", 
        password="admin", 
        host="localhost",
        port="5432"
        )
    suma= float(enero)+float(febrero)+float(marzo)+float(abril)+float(mayo)+float(junio)+float(julio)+float(agosto)+float(septiembre)+float(octubre)+float(noviembre)+float(diciembre)

    cursor = conn.cursor()
    temp = suma*0.7
    query = ''' SELECT DISTINCT i.porcentaje_retencion, i.gastos_presuntos, i.cantidad_a_rebajar, i.factor FROM impuestos AS i WHERE i.anio like(%s) and (%s >= i.desde) and (%s <= i.hasta) '''%("'"+str(anio)+"%'",temp,temp)
    cursor.execute(query)
    row = cursor.fetchone()
    
    if row is None:
        texto_variable.set('No existe este año en la base de datos')
        return
    else:
        texto_variable.set('')

    
    actualizar(suma)
    actualizar_datos(suma,row)
    actualizar_retencion_meses(enero, febrero, marzo, abril, mayo, junio, julio, agosto, septiembre, octubre, noviembre, diciembre,row)

    #print("'"+str(anio)+"%'")
    #print(suma)
    #print(row[0])
    #print(suma*row[0]/100)

    conn.commit()
    conn.close()

#Canvas
canvas = Canvas(root, height=550, width=550)
canvas.pack()

frame = Frame()
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

texto_variable = StringVar()
label = Label(frame, textvariable = texto_variable)
label.grid(row=16, column=1)

retencion_enero_variable = DoubleVar()
label = Label(frame, textvariable = retencion_enero_variable)
label.grid(row=1, column=2)

retencion_febrero_variable = DoubleVar()
label = Label(frame, textvariable = retencion_febrero_variable)
label.grid(row=2, column=2)

retencion_marzo_variable = DoubleVar()
label = Label(frame, textvariable = retencion_marzo_variable)
label.grid(row=3, column=2)

retencion_abril_variable = DoubleVar()
label = Label(frame, textvariable = retencion_abril_variable)
label.grid(row=4, column=2)

retencion_mayo_variable = DoubleVar()
label = Label(frame, textvariable = retencion_mayo_variable)
label.grid(row=5, column=2)

retencion_junio_variable = DoubleVar()
label = Label(frame, textvariable = retencion_junio_variable)
label.grid(row=6, column=2)

retencion_julio_variable = DoubleVar()
label = Label(frame, textvariable = retencion_julio_variable)
label.grid(row=7, column=2)

retencion_agosto_variable = DoubleVar()
label = Label(frame, textvariable = retencion_agosto_variable)
label.grid(row=8, column=2)

retencion_septiembre_variable = DoubleVar()
label = Label(frame, textvariable = retencion_septiembre_variable)
label.grid(row=9, column=2)

retencion_octubre_variable = DoubleVar()
label = Label(frame, textvariable = retencion_octubre_variable)
label.grid(row=10, column=2)

retencion_noviembre_variable = DoubleVar()
label = Label(frame, textvariable = retencion_noviembre_variable)
label.grid(row=11, column=2)

retencion_diciembre_variable = DoubleVar()
label = Label(frame, textvariable = retencion_diciembre_variable)
label.grid(row=12, column=2)

retenido = DoubleVar()
label = Label(frame, textvariable = retenido)
label.grid(row=13, column=2)

text_variable2 = DoubleVar()
label = Label(frame, textvariable = text_variable2)
label.grid(row=13, column=1)

#img = Tk.PhotoImage(file="a.jpg")
#lbl_img = Tk.Label(root, image = img)
#lbl_img.pack()

label = Label(frame, text = 'Honorarios Brutos')
label.grid(row=0, column=1)

label = Label(frame, text = 'Impuestos Retenidos')
label.grid(row=0, column=2)

label_enero = Label(frame, text = 'Enero')
label_enero.grid(row=1, column=0)


entry_ener = Entry(frame)
entry_ener.grid(row=1,column=1)
entry_ener.insert(0,"0")

label_febrero = Label(frame, text = 'Febrero')
label_febrero.grid(row=2, column=0)

entry_feb = Entry(frame)
entry_feb.grid(row=2,column=1)
entry_feb.insert(0,"0")

label_marzo = Label(frame, text = 'Marzo')
label_marzo.grid(row=3, column=0)

entry_mar = Entry(frame)
entry_mar.grid(row=3,column=1)
entry_mar.insert(0,"0")

label_abril = Label(frame, text = 'Abril')
label_abril.grid(row=4, column=0)

entry_abr = Entry(frame)
entry_abr.grid(row=4,column=1)
entry_abr.insert(0,"0")

label_mayo = Label(frame, text = 'Mayo')
label_mayo.grid(row=5, column=0)

entry_may = Entry(frame)
entry_may.grid(row=5,column=1)
entry_may.insert(0,"0")

label_junio = Label(frame, text = 'Junio')
label_junio.grid(row=6, column=0)

entry_jun = Entry(frame)
entry_jun.grid(row=6,column=1)
entry_jun.insert(0,"0")

label_julio = Label(frame, text = 'Julio')
label_julio.grid(row=7, column=0)

entry_jul = Entry(frame)
entry_jul.grid(row=7,column=1)
entry_jul.insert(0,"0")

label_agosto = Label(frame, text = 'Agosto')
label_agosto.grid(row=8, column=0)

entry_ago = Entry(frame)
entry_ago.grid(row=8,column=1)
entry_ago.insert(0,"0")

label_septiembre = Label(frame, text = 'Septiembre')
label_septiembre.grid(row=9, column=0)

entry_sep = Entry(frame)
entry_sep.grid(row=9,column=1)
entry_sep.insert(0,"0")

label_octubre = Label(frame, text = 'Octubre')
label_octubre.grid(row=10, column=0)

entry_oct = Entry(frame)
entry_oct.grid(row=10,column=1)
entry_oct.insert(0,"0")

label_noviembre = Label(frame, text = 'Noviembre')
label_noviembre.grid(row=11, column=0)

entry_nov = Entry(frame)
entry_nov.grid(row=11,column=1)
entry_nov.insert(0,"0")

label_diciembre = Label(frame, text = 'Diciembre')
label_diciembre.grid(row=12, column=0)

entry_dic = Entry(frame)
entry_dic.grid(row=12,column=1)
entry_dic.insert(0,"0")

label = Label(frame, text = 'Año')
label.grid(row=14, column=0)

entry_anio = Entry(frame)
entry_anio.grid(row=15,column=0)

label = Label(frame, text = 'Anual ->')
label.grid(row=13, column=0)

gastos_presuntos = StringVar()
label = Label(frame, textvariable = gastos_presuntos)
label.grid(row=16, column=0)

impuesto_global = StringVar()
label = Label(frame, textvariable = impuesto_global)
label.grid(row=17, column=0)

devolucion = StringVar()
label = Label(frame, textvariable = devolucion)
label.grid(row=18, column=0)

button=customtkinter.CTkButton(frame, text="CALCULAR", command=lambda:calcular(entry_ener.get(), entry_feb.get(), entry_mar.get(), entry_abr.get(), entry_may.get(), entry_jun.get() , entry_jul.get(), entry_ago.get(), entry_sep.get(), entry_oct.get(), entry_nov.get(), entry_dic.get(), entry_anio.get()))
button.grid(relx=0.5, rely=0.5)

label_admin = Label(frame, text = 'Admin')
label_admin.grid(row=18, column=4)

admin = Entry(frame)
admin.grid(row=19,column=4)

button=customtkinter.CTkButton(frame, text="Agregar tabla", command=lambda:Agregar(admin.get()))
button.grid(relx=0.5, rely=0.5)

root.mainloop()