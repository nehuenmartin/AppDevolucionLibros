from datetime import date
from datetime import datetime, timedelta
def main():
    fecha_entrega = datetime.now() + timedelta(days=7)
    cantidad()
    print("Fecha de entrega: ", fecha_entrega)
def cantidad():
    value = int(input("Cantidad de libros: "))
    books = []
    for i in range(1, value+1):
        books.append(i)
    return realizar(books)

def realizar(books):
    lista_books = []
    for i in books:
        libro = {}
        libro["nombre"] = input("Nombre del libro: ")
        libro["categoria"] = input("Categoria: ")
        libro["autor"] = input("Autor: ")
        libro["piso"] = int(input("Piso Biblioteca: "))
        lista_books.append(libro)
    imprimir(lista_books)

def imprimir(lista_books):
    for libro in lista_books:
        print("---")
        print("Nombre:", libro["nombre"])
        print("Categoria:", libro["categoria"])
        print("Autor:", libro["autor"])
        print("Piso:", libro["piso"])
        print("---")
main()




