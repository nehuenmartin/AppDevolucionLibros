from datetime import date
from datetime import datetime, timedelta
import calendar

def main():
    fecha_entrega = date.today() + timedelta(days=14)
    day = fecha_entrega.day
    yy = fecha_entrega.year
    mm = fecha_entrega.month
    cal = calendar.monthcalendar(yy, mm)
   
    cantidad()
    print("Fecha de entrega: ", fecha_entrega)
    for i in cal:
        for j in i:
            if j == 0:
                print("   ", end="")
            elif j == day:
                print("[%2d]" % j, end="")
            else:
                print(" %2d " % j, end="")
        print("")

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
        print("--- Libro a entregrar ---")
        print("Nombre:", libro["nombre"])
        print("Categoria:", libro["categoria"])
        print("Autor:", libro["autor"])
        print("Piso:", libro["piso"])
        print("------------------------")
main()
