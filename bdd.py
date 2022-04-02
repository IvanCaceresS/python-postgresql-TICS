from tkinter import *
import psycopg2


def consulta1():
    ventana_nueva1 = Toplevel()
    ventana_nueva1.geometry("400x50")
    ventana_nueva1.title("CONSULTA 1")

    conexion = psycopg2.connect(dbname="proyecto", user="postgres", password="admin", host="localhost", port="5432")
    cursor = conexion.cursor()
    query = ''' SELECT count(c.*) FROM cliente as c, piscina as p, arriendo as a WHERE c.rut = a.rut_cliente and p.id = a.id_piscina and p.tipo='profesional' and p.nombre_sede='Sede NEMO' '''
    cursor.execute(query)
    row = cursor.fetchone()
    listbox=Listbox(ventana_nueva1,width=5,height=1)
    listbox.place(x=160, y=17)
    for x in row:
        listbox.insert(END, x)
    label1 = Label(ventana_nueva1, text='Cuantos clientes arrendaron piscinas profesionales en la Sede Nemo')
    label1.place(x=10,y=0)
    
    conexion.commit()
    conexion.close()

def botonconsulta3():
    ventana_nueva1 = Toplevel()
    ventana_nueva1.geometry("400x200")
    ventana_nueva1.title("CONSULTA 3")
    button31 = Button(ventana_nueva1, text="Encargado 1", command=lambda:consulta3('12.345.678-9',ventana_nueva1))
    button31.place(x=0, y=0)
    button32 = Button(ventana_nueva1, text="Encargado 2", command=lambda:consulta3('9.999.999-9',ventana_nueva1))
    button32.place(x=100, y=0)
    button33 = Button(ventana_nueva1, text="Encargado 3", command=lambda:consulta3('8.998.979-3',ventana_nueva1))
    button33.place(x=200, y=0)

def consulta2():
    ventana_nueva1 = Toplevel()
    ventana_nueva1.geometry("320x100")
    ventana_nueva1.title("CONSULTA 2")
    conexion = psycopg2.connect(dbname="proyecto", user="postgres", password="admin", host="localhost", port="5432")
    cursor = conexion.cursor()
    query = ''' select s.nombre,sum(a.hora_final-a.hora_inicio)/count(a.*) as horas_arrendadas_promedio from arriendo as a, piscina as p, sede as s where p.id=a.id_piscina and p.nombre_sede=s.nombre group by 1 '''
    cursor.execute(query)
    row = cursor.fetchall()
    listbox=Listbox(ventana_nueva1,width=25,height=3)
    listbox.place(x=100, y=30)
    for x in row:
        listbox.insert(END, x)
    label1 = Label(ventana_nueva1, text='Cantidad promedio de horas arrendadas en cada sede')
    label1.place(x=10,y=10)
    conexion.commit()
    conexion.close()

def consulta3(rut,ventana_nueva1):
    conexion = psycopg2.connect(dbname="proyecto", user="postgres", password="admin", host="localhost", port="5432")
    cursor = conexion.cursor()
    if rut == '12.345.678-9':
        label1 = Label(ventana_nueva1, text='Todos los datos de los clientes que han sido atendidos por el encargado 1 ')
        label1.place(x=0,y=30)
        query = ''' select distinct c.nombre,c.rut,c.telefono,c.edad from cliente as c, arriendo as a, encargado as e where c.rut=a.rut_cliente and a.rut_encargado='12.345.678-9' '''
    elif rut == '9.999.999-9':
        label1 = Label(ventana_nueva1, text='Todos los datos de los clientes que han sido atendidos por el encargado 2 ')
        label1.place(x=0,y=30)
        query = ''' select distinct c.nombre,c.rut,c.telefono,c.edad from cliente as c, arriendo as a, encargado as e where c.rut=a.rut_cliente and a.rut_encargado='9.999.999-9' '''
    elif rut == '8.998.979-3':
        label1 = Label(ventana_nueva1, text='Todos los datos de los clientes que han sido atendidos por el encargado 3 ')
        label1.place(x=0,y=30)
        query = ''' select distinct c.nombre,c.rut,c.telefono,c.edad from cliente as c, arriendo as a, encargado as e where c.rut=a.rut_cliente and a.rut_encargado='8.998.979-3' '''
    
    cursor.execute(query)
    row = cursor.fetchall()
    listbox=Listbox(ventana_nueva1,width=50,height=10)
    listbox.place(x=0, y=60)
    for x in row:
        listbox.insert(END, str('-----------------------'))
        listbox.insert(END, str('Nombre ')+ x[0])
        listbox.insert(END, str('Rut ')+ x[1])
        listbox.insert(END, str('Teléfono ')+ x[2])
    

    conexion.commit()
    conexion.close()

def botonconsulta4():

    ventana_nueva1 = Toplevel()
    ventana_nueva1.geometry("300x150")
    ventana_nueva1.title("CONSULTA 4")
    label = Label(ventana_nueva1, text='Rut cliente (con puntos y guion)')
    label.place(x=60, y=50)
    entry_rut = Entry(ventana_nueva1)
    entry_rut.place(x=80, y=30)
    button = Button(ventana_nueva1, text="Sede nemo", command=lambda:consulta4(entry_rut.get(),'Sede NEMO',ventana_nueva1))
    button.place(x=0, y=0)
    button = Button(ventana_nueva1, text="Sede dory", command=lambda:consulta4(entry_rut.get(),'Sede DORY',ventana_nueva1))
    button.place(x=100, y=0)
    button = Button(ventana_nueva1, text="Sede marlin", command=lambda:consulta4(entry_rut.get(),'Sede MARLIN',ventana_nueva1))
    button.place(x=200, y=0)

def consulta4(rut,sede,ventana_nueva1):
    conexion = psycopg2.connect(dbname="proyecto", user="postgres", password="admin", host="localhost", port="5432")
    cursor = conexion.cursor()
    query = ''' select count(p.*) from piscina as p, cliente as c, arriendo as a where c.rut=a.rut_cliente and a.id_piscina=p.id and p.nombre_sede ilike(%s) and c.rut= (%s) '''
    cursor.execute(query,(sede,rut))
    row = cursor.fetchone()
    listbox=Listbox(ventana_nueva1,width=5,height=1)
    listbox.place(x=120, y=100)
    listbox.insert(END,str(row[0]))
    label1 = Label(ventana_nueva1, text='Cuantas piscinas ha arrendado '+str(rut))
    label1.place(x=60,y=80)
    conexion.commit()
    conexion.close()

def consulta5(n,ventana_nueva1):
    conexion = psycopg2.connect(dbname="proyecto", user="postgres", password="admin", host="localhost", port="5432")
    cursor = conexion.cursor()
    if n == 0:
        query = ''' select p.id, s.nombre from piscina as p, sede as s where p.estado='no necesita mantencion' and p.nombre_sede=s.nombre '''
        label1 = Label(ventana_nueva1, text='Piscinas que no necesitan mantencion')
        label1.place(x=50,y=40)
    else:
        query = ''' select p.id, s.nombre from piscina as p, sede as s where p.estado='necesita mantencion' and p.nombre_sede=s.nombre '''
        label2 = Label(ventana_nueva1, text='Piscinas que si necesitan mantencion')
        label2.place(x=50,y=40)
    cursor.execute(query)
    row = cursor.fetchall()
    listbox=Listbox(ventana_nueva1,width=20,height=10)
    listbox.place(x=80,y=60)
    for x in row:
        listbox.insert(END, x)
    conexion.commit()
    conexion.close()

def botonconsulta5():
    ventana_nueva1 = Toplevel()
    ventana_nueva1.geometry("300x200")
    ventana_nueva1.title("CONSULTA 5")
    button = Button(ventana_nueva1, text="no necesita mantencion", command=lambda:consulta5(0,ventana_nueva1))
    button.place(x=0,y=0)
    button = Button(ventana_nueva1, text="necesita mantencion", command=lambda:consulta5(1,ventana_nueva1))
    button.place(x=160,y=0)

def consulta6():
    ventana_nueva1 = Toplevel()
    ventana_nueva1.geometry("300x200")
    ventana_nueva1.title("CONSULTA 6")
    conexion = psycopg2.connect(dbname="proyecto", user="postgres", password="admin", host="localhost", port="5432")
    cursor = conexion.cursor()
    query = ''' select a.*,p.precio_por_hora,(a.hora_final-a.hora_inicio) as cant_horas, (extract(hour from a.hora_final-a.hora_inicio)*p.precio_por_hora + sc.tarifa)as precio_total from Servicio_de_Comida as sc, arriendo as a, piscina as p where a.id_piscina=p.id and sc.nombre=a.nombre_servicio order by 2 '''
    cursor.execute(query)
    row = cursor.fetchall()
    label2 = Label(ventana_nueva1, text='Todos los arriendos y sus datos')
    label2.place(x=40,y=10)
    listbox=Listbox(ventana_nueva1,width=40,height=10)
    listbox.place(x=40,y=30)
    for x in row:
        listbox.insert(END, "------------")
        listbox.insert(END, "Rut Cliente: " + x[0])
        listbox.insert(END, "ID Piscina: " + x[1])
        listbox.insert(END, "Rut Encargado: " + x[2])
        listbox.insert(END, "Servicio de comida: " + x[3])
        listbox.insert(END, "Hora Inicio: " + str(x[4]))
        listbox.insert(END, "Hora Final: " + str(x[5]))
        listbox.insert(END, "Cant. de personas: " + str(x[6]))
        listbox.insert(END, "Fecha: " + str(x[7]))
        listbox.insert(END, "Precio por hora: " + str(x[8]))
        listbox.insert(END, "Cant. Horas: " + str(x[9]))
        listbox.insert(END, "Precio total: " + str(x[10]))
    conexion.commit()
    conexion.close()

def botonconsulta7():

    ventana_nueva1 = Toplevel()
    ventana_nueva1.geometry("370x150")
    ventana_nueva1.title("CONSULTA 7")
    label = Label(ventana_nueva1, text='Fecha inicio (DD-MM-AA)')
    label.place(x=0, y=0)
    entry_f1 = Entry(ventana_nueva1)
    entry_f1.place(x=160, y=0)
    label = Label(ventana_nueva1, text='Fecha final (DD-MM-AA)')
    label.place(x=0, y=20)
    entry_f2 = Entry(ventana_nueva1)
    entry_f2.place(x=160, y=20)
    button = Button(ventana_nueva1, text="Buscar", command=lambda:consulta7(entry_f1.get(),entry_f2.get(),ventana_nueva1))
    button.place(x=160, y=40)

def consulta7(finicio,ftermino,ventana_nueva1):
    conexion = psycopg2.connect(dbname="proyecto", user="postgres", password="admin", host="localhost", port="5432")
    cursor = conexion.cursor()
    query = ''' select sede.nombre as SEDE, sum(extract(hour from a.hora_final-a.hora_inicio)*p.precio_por_hora + sc.tarifa) as DINERO_DE_ARRIENDOS from Servicio_de_Comida as sc, sede, arriendo as a, piscina as p where a.id_piscina=p.id and p.nombre_sede=sede.nombre and sc.nombre=a.nombre_servicio and a.fecha between %s and %s group by 1 '''
    cursor.execute(query,(finicio,ftermino))
    row = cursor.fetchall()
    listbox=Listbox(ventana_nueva1,width=30,height=5)
    listbox.place(x=80,y=90)
    for x in row:
        listbox.insert(END, x)
    label2 = Label(ventana_nueva1, text='Dinero de arriendos de cada sede entre el '+ str(finicio) + ' y el ' + str(ftermino))
    label2.place(x=0,y=70)
    conexion.commit()
    conexion.close()

def consulta8():
    ventana_nueva1 = Toplevel()
    ventana_nueva1.geometry("220x230")
    ventana_nueva1.title("CONSULTA 8")
    conexion = psycopg2.connect(dbname="proyecto", user="postgres", password="admin", host="localhost", port="5432")
    cursor = conexion.cursor()
    query = ''' (select p.id as Id_Piscina, s.nombre as SEDE, count(a.*) as ARRIENDOS from sede as s, piscina as p, arriendo as a where p.nombre_sede=s.nombre and s.nombre='Sede NEMO' and p.id=a.id_piscina group by 1,2 order by 3 desc limit 1)
                union
                (select p.id as Id_Piscina, s.nombre as SEDE, count(a.*) as ARRIENDOS from sede as s, piscina as p, arriendo as a where p.nombre_sede=s.nombre and s.nombre='Sede DORY' and p.id=a.id_piscina group by 1,2 order by 3 desc limit 1)
                union
                (select p.id as Id_Piscina, s.nombre as SEDE, count(a.*) as ARRIENDOS from sede as s, piscina as p, arriendo as a where p.nombre_sede=s.nombre and s.nombre='Sede MARLIN' and p.id=a.id_piscina group by 1,2 order by 3 desc limit 1) '''
    cursor.execute(query)
    row = cursor.fetchall()
    label2 = Label(ventana_nueva1, text='Piscina más arrendada en cada Sede')
    label2.place(x=0,y=10)
    listbox=Listbox(ventana_nueva1,width=30,height=12)
    listbox.place(x=0,y=30)
    for x in row:
        listbox.insert(END,'----------------')
        listbox.insert(END, x[1])
        listbox.insert(END,'Piscina mas arrendada: ' + x[0])
        listbox.insert(END,'Cantidad de veces arrendada: ' + str(x[2]))

    conexion.commit()
    conexion.close()

def consulta9():
    ventana_nueva1 = Toplevel()
    ventana_nueva1.geometry("300x50")
    ventana_nueva1.title("CONSULTA 9")
    conexion = psycopg2.connect(dbname="proyecto", user="postgres", password="admin", host="localhost", port="5432")
    cursor = conexion.cursor()
    query = ''' select m.nombre, count(a.*) from Servicio_de_Comida as m, arriendo as a where a.nombre_servicio=m.nombre group by 1 order by 2 desc limit 1 '''
    cursor.execute(query)
    row = cursor.fetchall()
    listbox=Listbox(ventana_nueva1,width=30,height=1)
    listbox.place(x=50,y=20)
    label2 = Label(ventana_nueva1, text='Menú más pedido al arrendar')
    label2.place(x=60,y=0)
    for x in row:
        listbox.insert(END, x[0] + " pedido " + str(x[1]) + " veces")


    conexion.commit()
    conexion.close()

def consulta10():
    ventana_nueva1 = Toplevel()
    ventana_nueva1.geometry("220x180")
    ventana_nueva1.title("CONSULTA 10")
    conexion = psycopg2.connect(dbname="proyecto", user="postgres", password="admin", host="localhost", port="5432")
    cursor = conexion.cursor()
    query = ''' select total.nombre as sede, sum(total.sum) as total_sueldos from ((select s.nombre, sum(ce.salario) from Contrato_encargado as ce, sede as s where ce.nombre_sede=s.nombre group by 1)
                union
                (select s.nombre, sum(cp.salario) from Contrato_personal as cp, sede as s where cp.nombre_sede=s.nombre group by 1)
                union
                (select s.nombre, sum(cs.salario) from Contrato_salvavidas as cs, sede as s where cs.nombre_sede=s.nombre group by 1)) as total group by 1 '''
    cursor.execute(query)
    row = cursor.fetchall()
    listbox=Listbox(ventana_nueva1,width=25,height=9)
    listbox.place(x=30,y=20)
    label2 = Label(ventana_nueva1, text='Dinero total de sueldos en cada sede')
    label2.place(x=15,y=0)
    for x in row:
        listbox.insert(END, "----------------------")
        listbox.insert(END, str(x[0]))
        listbox.insert(END, "Dinero total: " + str(x[1]))
    conexion.commit()
    conexion.close()

def clientes():
    ventana_nueva1 = Toplevel()
    ventana_nueva1.geometry("400x400")
    ventana_nueva1.title("Manejo de Clientes")
    mostrar_cliente(ventana_nueva1)

        #NAME INPUT
    label = Label(ventana_nueva1, text='Rut cliente')
    label.grid(row=1, column=1)

    entry_rut = Entry(ventana_nueva1)
    entry_rut.grid(row=1,column=2)

    #NAME INPUT
    label = Label(ventana_nueva1, text='Nombre cliente')
    label.grid(row=2, column=1)

    entry_name = Entry(ventana_nueva1)
    entry_name.grid(row=2,column=2)
    #BOTON ACTUALIZAR
    button = Button(ventana_nueva1, text="Actualizar", command=lambda:mostrar_cliente(ventana_nueva1))
    button.grid(row=5, column=4, sticky=W+E)

    #NAME INPUT
    label = Label(ventana_nueva1, text='Telefono cliente')
    label.grid(row=3, column=1)

    entry_tel = Entry(ventana_nueva1)
    entry_tel.grid(row=3,column=2)

    #NAME INPUT
    label = Label(ventana_nueva1, text='Edad cliente')
    label.grid(row=4, column=1)

    entry_edad = Entry(ventana_nueva1)
    entry_edad.grid(row=4,column=2)

    #BOTON AÑADIR
    button = Button(ventana_nueva1, text="Añadir", command=lambda:guardar_cliente(entry_rut.get(), entry_name.get(), entry_tel.get(), entry_edad.get()))
    button.grid(row=5, column=2, sticky=W+E)

    
    #RUT INPUT
    label = Label(ventana_nueva1, text='Rut cliente')
    label.grid(row=3, column=3)

    entry_rute = Entry(ventana_nueva1)
    entry_rute.grid(row=4,column=3)

    #BOTON ELIMINAR
    button = Button(ventana_nueva1, text="Eliminar", command=lambda:eliminar_cliente(entry_rute.get()))
    button.grid(row=5, column=3, sticky=W+E)

def mostrar_cliente(ventana_nueva1):
    conexion = psycopg2.connect(dbname="proyecto", user="postgres", password="admin", host="localhost", port="5432")
    cursor = conexion.cursor()
    query = ''' SELECT * FROM cliente '''
    cursor.execute(query)
    row = cursor.fetchall()
    listbox=Listbox(ventana_nueva1,width=50,height=10)
    listbox.place(x=0,y=110)
    for x in row:
        listbox.insert(END, str('-----------------------'))
        listbox.insert(END, str('Rut: ')+ x[0])
        listbox.insert(END, str('Nombre: ')+ x[1])
        listbox.insert(END, str('Teléfono: ')+ x[2])

    conexion.commit()
    conexion.close()

def guardar_cliente(rut, nombre, telefono, edad):
    conexion = psycopg2.connect(dbname="proyecto", user="postgres", password="admin", host="localhost", port="5432")
    cursor = conexion.cursor()
    query = '''INSERT INTO cliente values('%s','%s','%s','%s')''' %(rut,nombre,telefono,edad)
    cursor.execute(query)
    conexion.commit()
    conexion.close()

def eliminar_cliente(rut):
    conexion = psycopg2.connect(dbname="proyecto", user="postgres", password="admin", host="localhost", port="5432")
    cursor = conexion.cursor()
    query = ''' DELETE FROM cliente WHERE rut = '%s' ''' %(rut)
    cursor.execute(query)
    conexion.commit()
    conexion.close()

def piscinas():
    ventana_nueva1 = Toplevel()
    ventana_nueva1.geometry("400x400")
    ventana_nueva1.title("Manejo de Piscinas")
    mostrar_piscinas(ventana_nueva1)

        #NAME INPUT
    label = Label(ventana_nueva1, text='Id')
    label.grid(row=1, column=1)

    entry_id = Entry(ventana_nueva1)
    entry_id.grid(row=1,column=2)

    #NAME INPUT
    label = Label(ventana_nueva1, text='Tipo')
    label.grid(row=2, column=1)

    entry_tipo = Entry(ventana_nueva1)
    entry_tipo.grid(row=2,column=2)
    #BOTON ACTUALIZAR
    button = Button(ventana_nueva1, text="Actualizar", command=lambda:mostrar_piscinas(ventana_nueva1))
    button.grid(row=7, column=4, sticky=W+E)

    #NAME INPUT
    label = Label(ventana_nueva1, text='Temperatura')
    label.grid(row=3, column=1)

    entry_temp = Entry(ventana_nueva1)
    entry_temp.grid(row=3,column=2)

    #NAME INPUT
    label = Label(ventana_nueva1, text='Profundidad')
    label.grid(row=4, column=1)

    entry_prof = Entry(ventana_nueva1)
    entry_prof.grid(row=4,column=2)

    #NAME INPUT
    label = Label(ventana_nueva1, text='Precio')
    label.grid(row=5, column=1)

    entry_precio = Entry(ventana_nueva1)
    entry_precio.grid(row=5,column=2)

    #NAME INPUT
    label = Label(ventana_nueva1, text='Sede')
    label.grid(row=6, column=1)

    entry_sede = Entry(ventana_nueva1)
    entry_sede.grid(row=6,column=2)

    #BOTON AÑADIR
    button = Button(ventana_nueva1, text="Añadir", command=lambda:guardar_piscinas(entry_id.get(), entry_tipo.get(), entry_temp.get(), entry_prof.get(), entry_precio.get(), entry_sede.get()))
    button.grid(row=7, column=2, sticky=W+E)

    
    #RUT INPUT
    label = Label(ventana_nueva1, text='Id Piscina')
    label.grid(row=5, column=3)

    entry_rute = Entry(ventana_nueva1)
    entry_rute.grid(row=6,column=3)

    #BOTON ELIMINAR
    button = Button(ventana_nueva1, text="Eliminar", command=lambda:eliminar_piscinas(entry_rute.get()))
    button.grid(row=7, column=3, sticky=W+E)

def mostrar_piscinas(ventana_nueva1):
    conexion = psycopg2.connect(dbname="proyecto", user="postgres", password="admin", host="localhost", port="5432")
    cursor = conexion.cursor()
    query = ''' SELECT * FROM piscina '''
    cursor.execute(query)
    row = cursor.fetchall()
    listbox=Listbox(ventana_nueva1,width=50,height=10)
    listbox.place(x=0,y=180)
    for x in row:
        listbox.insert(END, str('-----------------------'))
        listbox.insert(END, str('Ubicacion: ')+ x[9])
        listbox.insert(END, str('Id: ')+ x[0])
        listbox.insert(END, str('Tipo: ')+ x[1])
        listbox.insert(END, str('Temperatura: ')+ x[2])
        listbox.insert(END, str('Profundidad(mt): ')+ str(x[3]))
        listbox.insert(END, str('Precio por hora: ')+ str(x[5]))

    conexion.commit()
    conexion.close()

def guardar_piscinas(id, tipo, temperatura, profundidad,precio,sede):
    conexion = psycopg2.connect(dbname="proyecto", user="postgres", password="admin", host="localhost", port="5432")
    cursor = conexion.cursor()
    query = '''INSERT INTO piscina values('%s','%s','%s','%s',30,%s,'no necesita mantencion',200,0,'%s')''' %(id,tipo,temperatura,profundidad,precio,sede)
    cursor.execute(query)
    conexion.commit()
    conexion.close()

def eliminar_piscinas(id):
    conexion = psycopg2.connect(dbname="proyecto", user="postgres", password="admin", host="localhost", port="5432")
    cursor = conexion.cursor()
    query = ''' DELETE FROM piscina WHERE id = '%s' ''' %(id)
    cursor.execute(query)
    conexion.commit()
    conexion.close()

def comidas():
    ventana_nueva1 = Toplevel()
    ventana_nueva1.geometry("400x400")
    ventana_nueva1.title("Manejo de Servicios de comida")
    mostrar_comidas(ventana_nueva1)

        #NAME INPUT
    label = Label(ventana_nueva1, text='Nombre')
    label.grid(row=1, column=1)

    entry_nombre = Entry(ventana_nueva1)
    entry_nombre.grid(row=1,column=2)

    #NAME INPUT
    label = Label(ventana_nueva1, text='Porciones')
    label.grid(row=2, column=1)

    entry_por = Entry(ventana_nueva1)
    entry_por.grid(row=2,column=2)
    #BOTON ACTUALIZAR
    button = Button(ventana_nueva1, text="Actualizar", command=lambda:mostrar_comidas(ventana_nueva1))
    button.grid(row=8, column=4, sticky=W+E)

    #NAME INPUT
    label = Label(ventana_nueva1, text='Tarifa')
    label.grid(row=3, column=1)

    entry_tar = Entry(ventana_nueva1)
    entry_tar.grid(row=3,column=2)

    #NAME INPUT
    label = Label(ventana_nueva1, text='Plato Principal')
    label.grid(row=4, column=1)

    entry_pp = Entry(ventana_nueva1)
    entry_pp.grid(row=4,column=2)

    #NAME INPUT
    label = Label(ventana_nueva1, text='Plato Fondo')
    label.grid(row=5, column=1)

    entry_pf = Entry(ventana_nueva1)
    entry_pf.grid(row=5,column=2)

    #NAME INPUT
    label = Label(ventana_nueva1, text='Postre')
    label.grid(row=6, column=1)

    entry_po = Entry(ventana_nueva1)
    entry_po.grid(row=6,column=2)

    #NAME INPUT
    label = Label(ventana_nueva1, text='Bebestible')
    label.grid(row=7, column=1)

    entry_be = Entry(ventana_nueva1)
    entry_be.grid(row=7,column=2)

    #BOTON AÑADIR
    button = Button(ventana_nueva1, text="Añadir", command=lambda:guardar_comidas(entry_nombre.get(), entry_por.get(), entry_tar.get(), entry_pp.get(), entry_pf.get(), entry_po.get(), entry_be.get()))
    button.grid(row=8, column=2, sticky=W+E)

    #NAME INPUT
    label = Label(ventana_nueva1, text='Nombre')
    label.grid(row=6, column=3)

    entry_nom = Entry(ventana_nueva1)
    entry_nom.grid(row=7,column=3)

    #BOTON ELIMINAR
    button = Button(ventana_nueva1, text="Eliminar", command=lambda:eliminar_comidas(entry_nom.get()))
    button.grid(row=8, column=3, sticky=W+E)

def mostrar_comidas(ventana_nueva1):
    conexion = psycopg2.connect(dbname="proyecto", user="postgres", password="admin", host="localhost", port="5432")
    cursor = conexion.cursor()
    query = ''' SELECT * FROM servicio_de_comida '''
    cursor.execute(query)
    row = cursor.fetchall()
    listbox=Listbox(ventana_nueva1,width=50,height=10)
    listbox.place(x=0,y=180)
    for x in row:
        listbox.insert(END, str('-----------------------'))
        listbox.insert(END, str('Nombre: ')+ str(x[0]))
        listbox.insert(END, str('Porciones: ')+ str(x[1]))
        listbox.insert(END, str('Tarifa: ')+ str(x[2]))
        listbox.insert(END, str('Plato principal: ')+ str(x[3]))
        listbox.insert(END, str('Plato fondo: ')+ str(x[4]))
        listbox.insert(END, str('Poste: ')+ str(x[5]))
        listbox.insert(END, str('Bebestible: ')+ str(x[6]))

    conexion.commit()
    conexion.close()

def guardar_comidas(nombre, porciones, tarifa, platoppal,platofondo,postre,bebestible):
    conexion = psycopg2.connect(dbname="proyecto", user="postgres", password="admin", host="localhost", port="5432")
    cursor = conexion.cursor()
    query = '''INSERT INTO servicio_de_comida values('%s',%s,%s,'%s','%s','%s','%s')''' %(nombre,porciones,tarifa,platoppal,platofondo,postre,bebestible)
    cursor.execute(query)
    conexion.commit()
    conexion.close()

def eliminar_comidas(id):
    conexion = psycopg2.connect(dbname="proyecto", user="postgres", password="admin", host="localhost", port="5432")
    cursor = conexion.cursor()
    query = ''' DELETE FROM servicio_de_comida WHERE nombre = '%s' ''' %(id)
    cursor.execute(query)
    conexion.commit()
    conexion.close()

def arriendos():
    ventana_nueva1 = Toplevel()
    ventana_nueva1.geometry("400x400")
    ventana_nueva1.title("Manejo de Arriendos")
    mostrar_arriendos(ventana_nueva1)
    #RUT CLIENTE, ID PISCINA, RUT ENCARGADO, NOMBRE MENU DE COMIDA, HORA INICIO, HORA FIN, CANTIDAD PERSONAS, FECHA
        #NAME INPUT
    label = Label(ventana_nueva1, text='Rut Cliente')
    label.grid(row=1, column=1)

    entry_rutC = Entry(ventana_nueva1)
    entry_rutC.grid(row=1,column=2)

    #NAME INPUT
    label = Label(ventana_nueva1, text='Id Piscina')
    label.grid(row=2, column=1)

    entry_pis = Entry(ventana_nueva1)
    entry_pis.grid(row=2,column=2)
    #BOTON ACTUALIZAR
    button = Button(ventana_nueva1, text="Actualizar", command=lambda:mostrar_arriendos(ventana_nueva1))
    button.grid(row=9, column=4, sticky=W+E)

    #NAME INPUT
    label = Label(ventana_nueva1, text='Rut Encargado')
    label.grid(row=3, column=1)

    entry_rutE = Entry(ventana_nueva1)
    entry_rutE.grid(row=3,column=2)

    #NAME INPUT
    label = Label(ventana_nueva1, text='Nombre servicio de comida')
    label.grid(row=4, column=1)

    entry_comida = Entry(ventana_nueva1)
    entry_comida.grid(row=4,column=2)

    #NAME INPUT
    label = Label(ventana_nueva1, text='Hora Inicio')
    label.grid(row=5, column=1)

    entry_hinicio = Entry(ventana_nueva1)
    entry_hinicio.grid(row=5,column=2)

    #NAME INPUT
    label = Label(ventana_nueva1, text='Hora Fin')
    label.grid(row=6, column=1)

    entry_hfin = Entry(ventana_nueva1)
    entry_hfin.grid(row=6,column=2)

    #NAME INPUT
    label = Label(ventana_nueva1, text='Cant. personas')
    label.grid(row=7, column=1)

    entry_cant = Entry(ventana_nueva1)
    entry_cant.grid(row=7,column=2)

      #NAME INPUT
    label = Label(ventana_nueva1, text='Fecha')
    label.grid(row=8, column=1)

    entry_fecha = Entry(ventana_nueva1)
    entry_fecha.grid(row=8,column=2)

    #BOTON AÑADIR
    button = Button(ventana_nueva1, text="Añadir", command=lambda:guardar_arriendos(entry_rutC.get(), entry_pis.get(), entry_rutE.get(), entry_comida.get(), entry_hinicio.get(), entry_hfin.get(), entry_cant.get(),entry_fecha.get()))
    button.grid(row=9, column=2, sticky=W+E)

def mostrar_arriendos(ventana_nueva1):
    conexion = psycopg2.connect(dbname="proyecto", user="postgres", password="admin", host="localhost", port="5432")
    cursor = conexion.cursor()
    query = ''' SELECT * FROM arriendo '''
    cursor.execute(query)
    row = cursor.fetchall()
    listbox=Listbox(ventana_nueva1,width=50,height=10)
    listbox.place(x=0,y=200)
    for x in row:
        listbox.insert(END, str('-----------------------'))
        listbox.insert(END, str('Rut Cliente: ')+ str(x[0]))
        listbox.insert(END, str('Id Piscina: ')+ str(x[1]))
        listbox.insert(END, str('Rut Encargado: ')+ str(x[2]))
        listbox.insert(END, str('Nombre servicio comida: ')+ str(x[3]))
        listbox.insert(END, str('Hora Inicio: ')+ str(x[4]))
        listbox.insert(END, str('Hora fin: ')+ str(x[5]))
        listbox.insert(END, str('Cantidad de personas: ')+ str(x[6]))
        listbox.insert(END, str('Fecha: ')+ str(x[7]))

    conexion.commit()
    conexion.close()

def guardar_arriendos(rutcliente, idpiscina, rutencargado, comida,hinicio,hfin,cant,fecha):
    conexion = psycopg2.connect(dbname="proyecto", user="postgres", password="admin", host="localhost", port="5432")
    cursor = conexion.cursor()
    query = ''' INSERT INTO arriendo values('%s','%s','%s','%s','%s','%s',%s,'%s') ''' %(rutcliente,idpiscina,rutencargado,comida,hinicio,hfin,cant,fecha)
    cursor.execute(query)
    conexion.commit()
    conexion.close()



root = Tk()
root.title('Aplicacion Bases de datos')

#Canvas
canvas = Canvas(root, height=200, width=500)
canvas.pack()
frame = Frame()
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)


#BOTON MOSTRAR
#button = Button(frame, text="Mostrar", command=lambda:mostrar_clientes())
#button.grid(row=6, column=2, sticky=W+E)

#BOTON Manejo de Clientes
button = Button(frame, text="Clientes", command=lambda:clientes())
button.place(x=0, y=60)

#BOTON Manejo de Piscinas
button = Button(frame, text="Piscinas", command=lambda:piscinas())
button.place(x=60, y=60)

#BOTON Manejo de Arriendo
button = Button(frame, text="Arriendos", command=lambda:arriendos())
button.place(x=250, y=60)

#BOTON Manejo de Menus
button = Button(frame, text="Servicios de comida", command=lambda:comidas())
button.place(x=120, y=60)

#BOTON CONSULTA 1
button = Button(frame, text="Consulta 1", command=lambda:consulta1())
button.place(x=0, y=0)

#BOTON CONSULTA 2
button = Button(frame, text="Consulta 2", command=lambda:consulta2())
button.place(x=70, y=0)

#BOTON CONSULTA 3
button = Button(frame, text="Consulta 3", command=lambda:botonconsulta3())
button.place(x=140, y=0)

#BOTON CONSULTA 4
button = Button(frame, text="Consulta 4", command=lambda:botonconsulta4())
button.place(x=210, y=0)

#BOTON CONSULTA 5
button = Button(frame, text="Consulta 5", command=lambda:botonconsulta5())
button.place(x=280, y=0)

#BOTON CONSULTA 6
button = Button(frame, text="Consulta 6", command=lambda:consulta6())
button.place(x=0, y=25)

#BOTON CONSULTA 7
button = Button(frame, text="Consulta 7", command=lambda:botonconsulta7())
button.place(x=70, y=25)

#BOTON CONSULTA 8
button = Button(frame, text="Consulta 8", command=lambda:consulta8())
button.place(x=140, y=25)

#BOTON CONSULTA 9
button = Button(frame, text="Consulta 9", command=lambda:consulta9())
button.place(x=210, y=25)

#BOTON CONSULTA 10
button = Button(frame, text="Consulta 10", command=lambda:consulta10())
button.place(x=280, y=25)

root.mainloop()