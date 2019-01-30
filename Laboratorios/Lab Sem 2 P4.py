from sys import stdin

def main():
    print("ingrese el numero de elementos ")
    n = int(stdin.readline().strip())
    print("ingrese numeros separados por espacio")
    a = list(map(int,stdin.readline().strip().split()))
    respuesta = 0
    divi = (n//2)+1
    for i in range(n):
        b = a[i]
        cont = 0
        for k in range(n):
##            print(a[i],cont,divi)
            if b == a[k]:
                cont+=1
        if cont>= divi:
            respuesta+=1
            break
    if respuesta == 1:
        print(True)
    else:
        print(False)
main()
    
    
