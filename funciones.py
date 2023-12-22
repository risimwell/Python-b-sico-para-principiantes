from random import randrange, seed 

def verificar_si_puedes_conducir():
    
    edad = int(input("Le gustaria conducir ingrese su edad por favor  "))
    nombre = input("Le gustaria conducir ingrese su Nombre por favor  ")

    if edad >= 18: 
        print(nombre,"Usted puede conducir: y su edad es  ", edad)

    else:
        print(nombre,"Lo sentimos no puedes conducir tu edad es ", edad, "Te faltan ", 18-edad,"años aun")

verificar_si_puedes_conducir()


frase_alura = [' Digitales', 'y ', 'Negocios ', 'de ', 'Tecnología ', 'Cursos ']

notas_pruebas = []
seed(3)

for notas_matematicas in range(8):
    notas_pruebas.append(randrange(0,11))

print(notas_pruebas)

carros = (
    ('Jetta Variant','Motor 4.0 Turbo',2003,False,
     ('Llantas de aleación', 'Cerraduras eléctricas', 'Piloto automático')
    ),('Passat','Motor Diesel',1991,True,('Central multimedia', 'Techo panoramico', 'Frenos ABS'))
)