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

def compute(input):

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

        print(f"Code Tree now looks like: {new_input}")

        return compute(new_input)

    if '\\/' in input:
        # aqui temos um problema de escape character da / no windows?
        position = input.index('/')

        lhs = position - 1
        rhs = position + 1

        result = input[lhs] // input[rhs]

        new_input = input
        new_input[position] = result
        
        del new_input[lhs]
        del new_input[lhs + 1]

        print(f"Code Tree now looks like: {new_input}")

        return compute(new_input)

    if '+' in input:

        position = input.index('+')

        lhs = position - 1
        rhs = position + 1

        result = input[lhs] + input[rhs]

        new_input = input
        new_input[position] = result
        
        del new_input[lhs]
        del new_input[lhs + 1]

        return compute(new_input)

    if '-' in input:

        position = input.index('-')

        lhs = position - 1
        rhs = position + 1

        result = input[lhs] - input[rhs]

        new_input = input
        new_input[position] = result
        
        del new_input[lhs]
        del new_input[lhs + 1]

        return compute(new_input)
    
    else:

        return input

# funciona dos dois jeitos :)

compute(parser(tokenizer("3*2+5")))
compute("3*2+5")

compute("192837 - 293847 * 123876")

compute(" 872 - 7623 / 5434 *18")






