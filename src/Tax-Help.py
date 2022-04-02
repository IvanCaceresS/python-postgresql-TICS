from tkinter import *
import psycopg2
import customtkinter

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")
root = customtkinter.CTk()
root.title("Tax-help")
root.wm_maxsize()

def Eliminar_tabla(anio):
    conn = psycopg2.connect(
        dbname="postgres", 
        user="postgres", 
        password="admin", 
        host="localhost",
        port="5432"
        )
    cursor = conn.cursor()
    query = ''' delete from impuestos where anio like(%s)''' %("'"+str(anio)+"%'")
    cursor.execute(query)
    conn.commit()
    conn.close()

def AgregarEnBase(anio,d1,d2,d3,d4,d5,d6,d7,d8,h1,h2,h3,h4,h5,h6,h7,h8,f1,f2,f3,f4,f5,f6,f7,f8,c1,c2,c3,c4,c5,c6,c7,c8,gp,pr):
    conn = psycopg2.connect(
        dbname="postgres", 
        user="postgres", 
        password="admin", 
        host="localhost",
        port="5432"
        )
    cursor = conn.cursor()

    query = ''' INSERT INTO impuestos values (%s,%s,%s,%s,%s,%s,%s)''' %("'"+str(anio)+".1'",d1,h1,f1,c1,gp,pr)
    cursor.execute(query)
    query = ''' INSERT INTO impuestos values (%s,%s,%s,%s,%s,%s,%s)''' %("'"+str(anio)+".2'",d2,h2,f2,c2,gp,pr)
    cursor.execute(query)
    query = ''' INSERT INTO impuestos values (%s,%s,%s,%s,%s,%s,%s)''' %("'"+str(anio)+".3'",d3,h3,f3,c3,gp,pr)
    cursor.execute(query)
    query = ''' INSERT INTO impuestos values (%s,%s,%s,%s,%s,%s,%s)''' %("'"+str(anio)+".4'",d4,h4,f4,c4,gp,pr)
    cursor.execute(query)
    query = ''' INSERT INTO impuestos values (%s,%s,%s,%s,%s,%s,%s)''' %("'"+str(anio)+".5'",d5,h5,f5,c5,gp,pr)
    cursor.execute(query)
    query = ''' INSERT INTO impuestos values (%s,%s,%s,%s,%s,%s,%s)''' %("'"+str(anio)+".6'",d6,h6,f6,c6,gp,pr)
    cursor.execute(query)
    query = ''' INSERT INTO impuestos values (%s,%s,%s,%s,%s,%s,%s)''' %("'"+str(anio)+".7'",d7,h7,f7,c7,gp,pr)
    cursor.execute(query)
    query = ''' INSERT INTO impuestos values (%s,%s,%s,%s,%s,%s,%s)''' %("'"+str(anio)+".8'",d8,h8,f8,c8,gp,pr)
    cursor.execute(query)
    conn.commit()
    conn.close()

def Agregar(admin):
    if (admin!="admin"):
        admintext.set("Contraseña incorrecta.")
        return
    else:
        admintext.set("")
        ventana_nueva1 = Toplevel()
        ventana_nueva1.geometry("910x400")
        ventana_nueva1.title("Agregar tabla")
   
        label = Label(ventana_nueva1, text = 'Año')
        label.grid(row=0, column=0)
        

        entryAño = Entry(ventana_nueva1)
        entryAño.grid(row=1,column=0)

        label_desde1 = Label(ventana_nueva1, text = 'DESDE')
        label_desde1.grid(row=0, column=3)

        desde1 = Entry(ventana_nueva1)
        desde1.grid(row=1,column=3)
        label_desde1.config(fg="black", font=('Input Mono',10,'bold'), bg="#9B9B9B")

        desde2 = Entry(ventana_nueva1)
        desde2.grid(row=2,column=3)

        desde3 = Entry(ventana_nueva1)
        desde3.grid(row=3,column=3)

        desde4 = Entry(ventana_nueva1)
        desde4.grid(row=4,column=3)

        desde5 = Entry(ventana_nueva1)
        desde5.grid(row=5,column=3)

        desde6 = Entry(ventana_nueva1)
        desde6.grid(row=6,column=3)

        desde7 = Entry(ventana_nueva1)
        desde7.grid(row=7,column=3)

        desde8 = Entry(ventana_nueva1)
        desde8.grid(row=8,column=3)

        label_hasta1 = Label(ventana_nueva1, text = 'HASTA')
        label_hasta1.grid(row=0, column=4)
        

        hasta1 = Entry(ventana_nueva1)
        hasta1.grid(row=1,column=4)
        label_hasta1.config(fg="black", font=('Input Mono',10,'bold'), bg="#9B9B9B")

        hasta2 = Entry(ventana_nueva1)
        hasta2.grid(row=2,column=4)

        hasta3 = Entry(ventana_nueva1)
        hasta3.grid(row=3,column=4)

        hasta4 = Entry(ventana_nueva1)
        hasta4.grid(row=4,column=4)

        hasta5 = Entry(ventana_nueva1)
        hasta5.grid(row=5,column=4)

        hasta6 = Entry(ventana_nueva1)
        hasta6.grid(row=6,column=4)

        hasta7 = Entry(ventana_nueva1)
        hasta7.grid(row=7,column=4)

        hasta8 = Entry(ventana_nueva1)
        hasta8.grid(row=8,column=4)

        label = Label(ventana_nueva1, text = 'FACTOR')
        label.grid(row=0, column=5)

        factor1 = Entry(ventana_nueva1)
        factor1.grid(row=1,column=5)

        factor2 = Entry(ventana_nueva1)
        factor2.grid(row=2,column=5)

        factor3 = Entry(ventana_nueva1)
        factor3.grid(row=3,column=5)

        factor4 = Entry(ventana_nueva1)
        factor4.grid(row=4,column=5)

        factor5 = Entry(ventana_nueva1)
        factor5.grid(row=5,column=5)

        factor6 = Entry(ventana_nueva1)
        factor6.grid(row=6,column=5)

        factor7 = Entry(ventana_nueva1)
        factor7.grid(row=7,column=5)

        factor8 = Entry(ventana_nueva1)
        factor8.grid(row=8,column=5)

        label = Label(ventana_nueva1, text = 'CANTIDAD A REBAJAR')
        label.grid(row=0, column=6)

        cant1 = Entry(ventana_nueva1)
        cant1.grid(row=1,column=6)

        cant2 = Entry(ventana_nueva1)
        cant2.grid(row=2,column=6)

        cant3 = Entry(ventana_nueva1)
        cant3.grid(row=3,column=6)

        cant4 = Entry(ventana_nueva1)
        cant4.grid(row=4,column=6)

        cant5 = Entry(ventana_nueva1)
        cant5.grid(row=5,column=6)

        cant6 = Entry(ventana_nueva1)
        cant6.grid(row=6,column=6)

        cant7 = Entry(ventana_nueva1)
        cant7.grid(row=7,column=6)

        cant8 = Entry(ventana_nueva1)
        cant8.grid(row=8,column=6)

        label = Label(ventana_nueva1, text = 'GASTOS PRESUNTOS')
        label.grid(row=0, column=7)

        gastosp = Entry(ventana_nueva1)
        gastosp.grid(row=1,column=7)

        label = Label(ventana_nueva1, text = 'PORCENTAJE DE RETENCION')
        label.grid(row=0, column=8)

        porcreten = Entry(ventana_nueva1)
        porcreten.grid(row=1,column=8)

        button=customtkinter.CTkButton(ventana_nueva1, text="AGREGAR", command=lambda:AgregarEnBase(entryAño.get(),desde1.get(),desde2.get(),desde3.get(),desde4.get(),desde5.get(),desde6.get(),desde7.get(),desde8.get(),
        hasta1.get(),hasta2.get(),hasta3.get(),hasta4.get(),hasta5.get(),hasta6.get(),hasta7.get(),hasta8.get(),factor1.get(),factor2.get(),factor3.get(),factor4.get(),factor5.get(),factor6.get(),factor7.get(),factor8.get(),
        cant1.get(),cant2.get(),cant3.get(),cant4.get(),cant5.get(),cant6.get(),cant7.get(),cant8.get(),gastosp.get(),porcreten.get()))

        button.grid(row=9, column=3)


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

    ventana_nueva2 = Toplevel()
    ventana_nueva2.geometry("400x400")
    ventana_nueva2.title("RESULTADO")

    if ret-impto_global >=0:
        label = Label(ventana_nueva2, text = 'TIENES UNA DEVOLUCION DE $' + str(ret-impto_global))
        label.grid(row=2, column=2)
        label.config(bg="#900C3F",fg="white",font=('Input Mono',8,'bold'))
    elif ret-impto_global <=0:
        label = Label(ventana_nueva2, text = 'TIENES QUE PAGAR $' + str(-(ret-impto_global)) + ' DE IMPUESTOS')
        label.grid(row=2, column=2)
        label.config(bg="#900C3F",fg="white",font=('Input Mono',8,'bold'))
    

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

    label_enero.config(fg="white")
    label_febrero.config(fg="white")
    label_marzo.config(fg="white")
    label_abril.config(fg="white")
    label_mayo.config(fg="white")
    label_junio.config(fg="white")
    label_julio.config(fg="white")
    label_agosto.config(fg="white")
    label_septiembre.config(fg="white")
    label_octubre.config(fg="white")
    label_noviembre.config(fg="white")
    label_diciembre.config(fg="white")

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

    actualizar_datos(suma,row)
    actualizar_retencion_meses(enero, febrero, marzo, abril, mayo, junio, julio, agosto, septiembre, octubre, noviembre, diciembre,row)
    conn.commit()
    conn.close()

    

#Canvas
canvas = Canvas(root, height=500, width=600)
canvas.pack()
canvas['bg'] = '#900C3F'

frame = Frame()
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
frame['bg'] = '#900C3F'
root['bg'] = '#900C3F'


texto_variable = StringVar()
label = Label(frame, textvariable = texto_variable)
label.grid(row=14, column=1)
label.config(bg="#900C3F",fg="white",font=('Input Mono',8,'bold'))

retencion_enero_variable = DoubleVar()
label = Label(frame, textvariable = retencion_enero_variable)
label.grid(row=1, column=2)
label.config(bg="#900C3F",fg="white",font=('Input Mono',8,'bold'))

retencion_febrero_variable = DoubleVar()
label = Label(frame, textvariable = retencion_febrero_variable)
label.grid(row=2, column=2)
label.config(bg="#900C3F",fg="white",font=('Input Mono',8,'bold'))

retencion_marzo_variable = DoubleVar()
label = Label(frame, textvariable = retencion_marzo_variable)
label.grid(row=3, column=2)
label.config(bg="#900C3F",fg="white",font=('Input Mono',8,'bold'))

retencion_abril_variable = DoubleVar()
label = Label(frame, textvariable = retencion_abril_variable)
label.grid(row=4, column=2)
label.config(bg="#900C3F",fg="white",font=('Input Mono',8,'bold'))

retencion_mayo_variable = DoubleVar()
label = Label(frame, textvariable = retencion_mayo_variable)
label.grid(row=5, column=2)
label.config(bg="#900C3F",fg="white",font=('Input Mono',8,'bold'))

retencion_junio_variable = DoubleVar()
label = Label(frame, textvariable = retencion_junio_variable)
label.grid(row=6, column=2)
label.config(bg="#900C3F",fg="white",font=('Input Mono',8,'bold'))

retencion_julio_variable = DoubleVar()
label = Label(frame, textvariable = retencion_julio_variable)
label.grid(row=7, column=2)
label.config(bg="#900C3F",fg="white",font=('Input Mono',8,'bold'))

retencion_agosto_variable = DoubleVar()
label = Label(frame, textvariable = retencion_agosto_variable)
label.grid(row=8, column=2)
label.config(bg="#900C3F",fg="white",font=('Input Mono',8,'bold'))

retencion_septiembre_variable = DoubleVar()
label = Label(frame, textvariable = retencion_septiembre_variable)
label.grid(row=9, column=2)
label.config(bg="#900C3F",fg="white",font=('Input Mono',8,'bold'))

retencion_octubre_variable = DoubleVar()
label = Label(frame, textvariable = retencion_octubre_variable)
label.grid(row=10, column=2)
label.config(bg="#900C3F",fg="white",font=('Input Mono',8,'bold'))

retencion_noviembre_variable = DoubleVar()
label = Label(frame, textvariable = retencion_noviembre_variable)
label.grid(row=11, column=2)
label.config(bg="#900C3F",fg="white",font=('Input Mono',8,'bold'))

retencion_diciembre_variable = DoubleVar()
label = Label(frame, textvariable = retencion_diciembre_variable)
label.grid(row=12, column=2)
label.config(bg="#900C3F",fg="white",font=('Input Mono',8,'bold'))

retenido = DoubleVar()
label = Label(frame, textvariable = retenido)
label.grid(row=13, column=2)
label.config(bg="#900C3F",fg="white",font=('Input Mono',8,'bold'))

text_variable2 = DoubleVar()
label = Label(frame, textvariable = text_variable2)
label.grid(row=13, column=1)
label.config(bg="#900C3F",fg="white",font=('Input Mono',8,'bold'))


#img = Tk.PhotoImage(file="a.jpg")
#lbl_img = Tk.Label(root, image = img)
#lbl_img.pack()

label_0 = Label(frame, text = 'Honorarios Brutos')
label_0.grid(row=0, column=1)
label_0.config(fg="white",font=('Input Mono',10,'bold'), bg="#900C3F")

label_1 = Label(frame, text = 'Impuestos Retenidos')
label_1.grid(row=0, column=2)

label_1.config(fg="white",font=('Input Mono',10,'bold'), bg="#900C3F")

label_enero = Label(frame, text = 'Enero')
label_enero.grid(row=1, column=0)
label_enero.config(fg="white",font=('Input Mono',8,'bold'), bg="#900C3F")

entry_ener = Entry(frame)
entry_ener.grid(row=1,column=1)
entry_ener.insert(0,"0")

label_febrero = Label(frame, text = 'Febrero')
label_febrero.grid(row=2, column=0)
label_febrero.config(fg="white",font=('Input Mono',8,'bold'), bg="#900C3F")

entry_feb = Entry(frame)
entry_feb.grid(row=2,column=1)
entry_feb.insert(0,"0")

label_marzo = Label(frame, text = 'Marzo')
label_marzo.grid(row=3, column=0)
label_marzo.config(fg="white",font=('Input Mono',8,'bold'), bg="#900C3F")

entry_mar = Entry(frame)
entry_mar.grid(row=3,column=1)
entry_mar.insert(0,"0")

label_abril = Label(frame, text = 'Abril')
label_abril.grid(row=4, column=0)
label_abril.config(fg="white",font=('Input Mono',8,'bold'), bg="#900C3F")

entry_abr = Entry(frame)
entry_abr.grid(row=4,column=1)
entry_abr.insert(0,"0")

label_mayo = Label(frame, text = 'Mayo')
label_mayo.grid(row=5, column=0)
label_mayo.config(fg="white",font=('Input Mono',8,'bold'), bg="#900C3F")

entry_may = Entry(frame)
entry_may.grid(row=5,column=1)
entry_may.insert(0,"0")

label_junio = Label(frame, text = 'Junio')
label_junio.grid(row=6, column=0)
label_junio.config(fg="white",font=('Input Mono',8,'bold'), bg="#900C3F")

entry_jun = Entry(frame)
entry_jun.grid(row=6,column=1)
entry_jun.insert(0,"0")

label_julio = Label(frame, text = 'Julio')
label_julio.grid(row=7, column=0)
label_julio.config(fg="white",font=('Input Mono',8,'bold'), bg="#900C3F")

entry_jul = Entry(frame)
entry_jul.grid(row=7,column=1)
entry_jul.insert(0,"0")

label_agosto = Label(frame, text = 'Agosto')
label_agosto.grid(row=8, column=0)
label_agosto.config(fg="white",font=('Input Mono',8,'bold'), bg="#900C3F")

entry_ago = Entry(frame)
entry_ago.grid(row=8,column=1)
entry_ago.insert(0,"0")

label_septiembre = Label(frame, text = 'Septiembre')
label_septiembre.grid(row=9, column=0)
label_septiembre.config(fg="white",font=('Input Mono',8,'bold'), bg="#900C3F")

entry_sep = Entry(frame)
entry_sep.grid(row=9,column=1)
entry_sep.insert(0,"0")

label_octubre = Label(frame, text = 'Octubre')
label_octubre.grid(row=10, column=0)
label_octubre.config(fg="white",font=('Input Mono',8,'bold'), bg="#900C3F")

entry_oct = Entry(frame)
entry_oct.grid(row=10,column=1)
entry_oct.insert(0,"0")

label_noviembre = Label(frame, text = 'Noviembre')
label_noviembre.grid(row=11, column=0)
label_noviembre.config(fg="white",font=('Input Mono',8,'bold'), bg="#900C3F")

entry_nov = Entry(frame)
entry_nov.grid(row=11,column=1)
entry_nov.insert(0,"0")

label_diciembre = Label(frame, text = 'Diciembre')
label_diciembre.grid(row=12, column=0)
label_diciembre.config(fg="white",font=('Input Mono',8,'bold'), bg="#900C3F")

entry_dic = Entry(frame)
entry_dic.grid(row=12,column=1)
entry_dic.insert(0,"0")

label = Label(frame, text = 'Año')
label.grid(row=14, column=0)
label.config(fg="black",font=('Input Mono',10,'bold'), bg="#900C3F")

entry_anio = Entry(frame)
entry_anio.grid(row=15,column=0)

label = Label(frame, text = 'Anual ->')
label.grid(row=13, column=0)
label.config(fg="black",font=('Input Mono',10,'bold'), bg="#900C3F")

gastos_presuntos = StringVar()
label = Label(frame, textvariable = gastos_presuntos)
label.grid(row=16, column=0)
label.config(bg="#900C3F",fg="white",font=('Input Mono',8,'bold'))

impuesto_global = StringVar()
label = Label(frame, textvariable = impuesto_global)
label.grid(row=17, column=0)
label.config(bg="#900C3F",fg="white",font=('Input Mono',8,'bold'))

devolucion = StringVar()
label = Label(frame, textvariable = devolucion)
label.grid(row=18, column=0)
label.config(bg="#900C3F",fg="white",font=('Input Mono',8,'bold'))

button = Button(frame, text = 'CALCULAR',bg='#34495E',border = (1, 1, 1, 1),activebackground='#85929E',fg="white",font=('Anonymous Pro',8,'bold'),command=lambda:calcular(entry_ener.get(), entry_feb.get(), entry_mar.get(), entry_abr.get(), entry_may.get(), entry_jun.get() , entry_jul.get(), entry_ago.get(), entry_sep.get(), entry_oct.get(), entry_nov.get(), entry_dic.get(), entry_anio.get())) 
button.grid(row=16, column=1)

label_admin = Label(frame, text = 'Admin')
label_admin.grid(row=14, column=2)
label.config(bg="#900C3F",fg="white",font=('Input Mono',8,'bold'))

admin = Entry(frame)
admin.grid(row=15,column=2)

button = Button(frame, text = 'INGRESAR',bg='#34495E',border = (1, 1, 1, 1),activebackground='#85929E',fg="white",font=('Anonymous Pro',8,'bold'),command=lambda:Agregar(admin.get())) 
button.grid(row=16, column=2)

admintext = StringVar()
label = Label(frame, textvariable = admintext)
label.grid(row=17, column=2)
label.config(bg="#900C3F",fg="white",font=('Input Mono',8,'bold'))

root.mainloop()