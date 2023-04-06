print('Hola. Bienvenido a la app. Contesta las siguientes preguntas \n')
#Poner el aviso de protección de datos personales

#Primer pregunta resultado 0 o 1
print('1. Tienes un salario fijo o la cantidad de dinero que obtienes va cambiando (por ejemplo un comerciante).')
print('Respuesta: \n Si tienes sueldo fijo escribe 1 \n Si tienes sueldo cambiante escribe 0')
fijo = input()
fijo = int(fijo)

#Este va a ser un entero
print('¿Cuanto ganas?(escribe una cantidad sin centavos)')
cantidad = input()
cantidad = int(cantidad)

#print(type(cantidad))

#Saber cuántas deudas tienes
print('¿Tienes deudas (bancarias, personales, etc)?')
print('Respuesta: \n Si \n No')
deuda = input()
#if si = 1 no = 0

#Si no tiene deudas vamos a dejar el valor en 0 y no tenemos que realizar la siguiente pregunta
if deuda == 'no' or deuda == 'No' or deuda == 'NO': #botones para el No 'bonitos'
    deudaMes = 0
    deuda = 0
#Si si tiene deudas necesitamos saber la contidad
else: 
    print('Dinos qué cantidad pagas en deudas cada mes')
    deudaMes = input()
    deudaMes = int(deudaMes)
    deuda = 1

#Es importante saber cuántas deudas tiene que pagar
porcentaje = (deudaMes / cantidad) * 100
print(porcentaje)

#Cuándo piensa retirarse esta persona
#Esto nos ayuda a saber cuánto tiempo tiene para alcanzar sus metas
print('En cuántos años piensas retirarte.')
edad = input()
edad = int(edad)

#Esto nos ayuda a saber cuánta ayuda necesita del presupuesto
print('De uno al cinco, qué tan disciplinado con las finanzas eres.')
dis = input()
dis = int(dis)
#checar que le rango de respuesta esta entre 0-5

#Sabremos si ya tiene ciertos objetivos
print('Quieres utilizar tu dinero para algún objetivo específico. (vacaciones,coche,ect).')
objetivo = input()
if objetivo == 'no' or objetivo == 'No' or objetivo == 'NO': #botones para el No 'bonitos'
    objetivo = 0
else:
    objetivo = 1

#Utilizamos if para saber a qué grupo pertenece cada persona
if (porcentaje <= 15) and (edad >=10) and (dis>=4) and (objetivo ==0):
    f = open('line_item.txt','r')
    contenido = f.readlines()
    print('el mejor presupuesto para ti es el de tipo line item')
elif (porcentaje <= 15) and (edad >=10) and (2>=dis<=3) and (objetivo ==0): 
    f = open('proporcional.txt','r')
    contenido = f.readlines()
    print('el mejor presupuesto para ti es el de tipo proporcional')
elif (15 <= porcentaje <= 40) and (edad >=10) and (dis>=4) and (objetivo ==0):
    f = open('proporcional.txt','r')
    contenido = f.readlines()
    print('el mejor presupuesto para ti es el de tipo proporcional')
elif (porcentaje <= 25) and (edad >=10) and (dis>=3) and (objetivo ==1):
    f = open('pagate_primero.txt','r')
    contenido = f.readlines()
    print('el mejor presupuesto para ti es el de tipo págate primero')
else:
    f = open('zero_sum.txt','r')
    contenido = f.readlines()
    print('el mejor presupuesto para ti es el de tipo zero sum')

print(contenido)
