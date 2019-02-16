def main ():
  n = 9875
  res = Super(n)
  print(res)



def Super(n):
  a = str(n)
  if len(a)>1:  
    lista = []
    while n > 0:

      b = n%10
      n = n//10
      lista.append(b)
  else:
    lista =[]

  if len(lista) == 1:
    return n
  else:
    suma = 0
    for i in range(len(lista)):
      suma+=lista[i]
    return Super(suma)