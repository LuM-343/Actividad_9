# Programación Avanzada - Actividad No. 8
# Luis Manuel Velásquez González 1502325

libros=[]

def validar(dato):
    while dato=="":
        print("Dato no válido")
        dato=input("Ingresar de nuevo: ")
    return dato
print("-"*30);print("Biblioteca Digital")

def agregar_libros(*libros_nuevos):
    for libro in libros_nuevos:
        book={
            "titulo":libro,
            "autor":"",
            "genero":"",
            "año":""
        }
        libros.append(book)

def asignar_detalles(titulo, autor, genero, year):
    for libro in libros:
        if libro["titulo"]==titulo:
            libro["autor"]=autor
            libro["genero"]=genero
            libro["año"]=year

def mostrar_biblioteca():
    print("\n Libros Disponibles")
    i=1
    for libro in libros:
        print(f"{i}. Título: {libro["titulo"]} | Autor: {libro["autor"]} | Género: {libro["genero"]} | Año: {libro["año"]}")

def buscar_libro(**filtros):
    print("\nBuscando coincidencias")
    i=1
    for libro in libros:
        if filtros.get("titulo")==libro["titulo"] or filtros.get("autor")==libro["autor"] or filtros.get("genero")==libro["genero"] or filtros.get("año_max")>=libro["año"]:
            print(f"{i}. Título: {libro["titulo"]} | Autor: {libro["autor"]} | Género: {libro["genero"]} | Año: {libro["año"]}")
            i+=1
    if i==1:
        print("No se encontraron coincidencias")

agregar_libros(
    "El principito", "Rebelión en la granja", "La casa de los espiritus" 
)

asignar_detalles("El principito","Antoine de Saint","novela",1943)
asignar_detalles("Rebelión en la granja", "George Orwell","novela",1943)
asignar_detalles("La casa de los espiritus", "Isabel Allende", "Realismo mágico", 1970)

mostrar_biblioteca()

buscar_libro(
    genero="novela",
    año_max=1943
)
buscar_libro(autor="Isabel Allende")