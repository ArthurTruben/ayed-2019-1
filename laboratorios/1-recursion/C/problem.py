import json
vocales = ["a","e","i","o","u"]

def recurcion(s,contV,contC):
    print(s,contV,contC)
    if len(s)==1:
        if (s[0]in vocales) == True:
            contV+=1
        else:
            contC+=1
        return(s[0],contV,contC)
    else:
        if (s[0]in vocales) == True:
            contV+=1
        else:
            contC+=1
        return recurcion(s[1:],contV,contC) #falta completar 
        

# TODO Complete!
def has_more_vowels(s):
    g = s.lower()
    print(g)
    contV = 0
    contC = 0
    s,vocales,consonantes = recurcion(s,contV,contC)
    print(s,vocales,consonantes)
    if vocales > consonantes:
        return(True)
    else:
        return(False)


if __name__ == '__main__':
    with open('./data.json') as f:
        tests = json.load(f)
        for i, test in enumerate(tests):
            s = test["s"]
            actual = has_more_vowels(s)
            expected = test['result']
            assert actual == expected, f'Test {i} | expected: {expected}, actual: {actual}'
        print('OK!')
