
def main():
  print("hola")
  n = 5
  res = fun(n)
  print(res)


def fun(n):
  if n == 1:
    return 1
  elif n== 2:
    return 2
  elif n == 3:
    return 4
  else:
    return fun(n-1)+fun(n-2)+fun(n-3)
main()
  