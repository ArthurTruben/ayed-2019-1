from sys import stdin
from time import time
def quick(lista): #costo de el programa log2(n)
    if len(lista)<=1:
        return lista
    else:
        return(quick([x for x in lista if x >= lista[0]][1:])+[lista[0]]+quick([y for y in lista if y < lista[0]]))
    
    
def main():
    print("ingrese numeros separados por un espacio ")
    a = list(map(int,stdin.readline().strip().split()))
    Tiempo = time()
    lista = quick(a)
    print (lista)
    print(lista[:10])
    TTime = time() - Tiempo
    print ("el tiempo de el programa es",TTime)
main()

