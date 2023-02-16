import time
import re

## Exerício 1

def k_most_frequent(nums: list, k: int) -> list:

    ocurrences = {k: nums.count(k) for k in list(set(nums))}

    sorted_ocurrences = sorted(ocurrences.items(), key = lambda x: x[1], reverse = True)

    return list(dict(sorted_ocurrences).keys())[0:k]

## Exercício 2

def valid_input(s: str) -> bool:

    stack = []

    solution = True # válido até que se prove o contrário

    for symbol in s:

        if symbol in ["(", "[", "{"]:

            stack.append(symbol)

        else:
        
            if len(stack) > 0:

                # Nesse caso existe um elemento no topo da pilha que foi 
                # aberto e testamos correspondência entre os dois

                top = stack.pop()  

                if symbol == ")" and top != "(":

                    solution = False

                    break

                if symbol == "]" and top != "[":

                    solution = False

                    break

                if symbol == "}" and top != "{":

                    solution = False

                    break

            else:

                # se há um elemento sendo fechado sem nenhum aberto
                # correspondente na pilha então o input é inválido

                solution = False

                break

    return solution

valid_input("(){}[]")
valid_input("(](}")
valid_input("[[[]]]")
valid_input("[[[]])")

# Exercício 3

def tokenizer(s: str) -> list:

    return re.findall(r"([\d.]+|[-+*/^()])", s)

tokenizer('35+2/4')

def parser(s: str):

    output = ["_"] * len(s) # cria uma lista do tamanho certo

    for index, symbol in enumerate(s):

        if symbol not in ['+', '-', '/', '*']:

            output[index] = int(symbol)
        
        else:

            output[index] = symbol

    return output

def computer(input, feels_human = True):

    if isinstance(input, str):

        input = parser(tokenizer(input))

    if '*' in input:

        position = input.index('*')

        lhs = position - 1
        rhs = position + 1

        result = input[lhs] * input[rhs]

        print(f"Multiplied {input[lhs]} and {input[rhs]}, got {result}")

        new_input = input
        new_input[position] = result
        
        del new_input[lhs]
        del new_input[lhs + 1]

        if feels_human: time.sleep(0.2)

        return computer(new_input)

    if r"/" in input:
        # r"/" pois aqui temos um problema de escape character da / no windows?
        position = input.index(r"/")

        lhs = position - 1
        rhs = position + 1

        result = input[lhs].__floordiv__(input[rhs])

        print(f"Divided {input[lhs]} and {input[rhs]}, got {result}")

        new_input = input
        new_input[position] = result
        
        del new_input[lhs]
        del new_input[lhs + 1]

        if feels_human: time.sleep(0.2)

        return computer(new_input)

    if '+' in input:

        position = input.index('+')

        lhs = position - 1
        rhs = position + 1

        result = input[lhs] + input[rhs]

        print(f"Summed {input[lhs]} and {input[rhs]}, got {result}")

        new_input = input
        new_input[position] = result
        
        del new_input[lhs]
        del new_input[lhs + 1]

        if feels_human: time.sleep(0.2)

        return computer(new_input)

    if '-' in input:

        position = input.index('-')

        lhs = position - 1
        rhs = position + 1

        result = input[lhs] - input[rhs]

        print(f"Subtracted {input[lhs]} and {input[rhs]}, got {result}")

        new_input = input
        new_input[position] = result
        
        del new_input[lhs]
        del new_input[lhs + 1]

        if feels_human: time.sleep(0.2)

        return computer(new_input)
    
    else:

        return input[0]

# funciona dos dois jeitos :)

computer(parser(tokenizer("3*2+5")))

computer("3*2+5")