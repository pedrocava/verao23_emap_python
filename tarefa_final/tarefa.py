

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

    return [*s.strip()]

tokenizer('3+2/4')

def parser(s: str):

    output = ["_"] * len(s) # cria uma lista do tamanho certo

    for index, symbol in enumerate(s):

        print(f"Index: {index}, symbol: {symbol}")

        if symbol not in ['+', '-', '/', '*']:

            output[index] = int(symbol)
        
        else:

            output[index] = symbol

    return output

def computer(input: str) -> int:

    if '*' in input:

        position = input.find('*')

        lhs = position - 1
        rhs = position + 1

        result = input[lhs] * input[rhs]

        new_input = input
        new_input[position] = result
        
        del new_input[lhs]
        del new_input[rhs]

        return computer(new_input)

computer(parser(tokenizer("3*2+5")))






