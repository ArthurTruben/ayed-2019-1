import json
def recurcion(numbers,pares,impares):

    if len(numbers)==1:
        if numbers[0]%2 == 0:
            pares.append(numbers[0])
        else:
            impares.append(numbers[0])
        return (numbers[0],pares,impares)
    else:
        if numbers[0]%2 == 0:
            pares.append(numbers[0])
        else:
            impares.append(numbers[0])
        return recurcion(numbers[1:],pares,impares)

# TODO Complete!
def arrange(numbers):
    pares = []
    impares = []
    a,b,c = recurcion(numbers,pares,impares)
    resultado = b+c
    return(resultado)


if __name__ == '__main__':
    with open('./data.json') as f:
        tests = json.load(f)
        for i, test in enumerate(tests):
            numbers = test["numbers"]
            actual = arrange(numbers)
            expected = test['result']
            assert actual == expected, f'Test {i} | expected: {expected}, actual: {actual}'
        print('OK!')
