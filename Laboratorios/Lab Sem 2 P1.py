from sys import stdin
def quick(lista):
    if len(lista)<=1:
        return lista
    else:
        return(quick([x for x in lista if x <= lista[0]][1:])+[lista[0]]+quick([y for y in lista if y > lista[0]]))
    
def main():
    print("ingrese numeros serparados por espacios")
    a = list(map(int,stdin.readline().strip().split()))
    long = len(a)-1
    res = quick(a)
    print(res)
    res2 = res[long]*res[long-1]
    print(res2
          )
    
    
main()
