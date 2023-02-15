

## Exerício 1

def k_most_frequent(nums: list, k: int) -> list:

    ocurrences = {k: nums.count(k) for k in list(set(nums))}

    sorted_ocurrences = sorted(ocurrences.items(), key = lambda x: x[1], reverse = True)

    return list(dict(sorted_ocurrences).keys())[0:k]


## Exercício 2

def valid_input(s: str) -> bool:

    stack = []

    solution = None

    for index, symbol in enumerate(s):

        if symbol in ["(", "[", "{"]:

            stack.append(symbol)

        else: 
        
            if len(stack) > 0:          

                if symbol is ")" and stack[0] is not "(":

                    solution = False

                    break

                if symbol is "]" and stack[0] is not "[":

                    solution = False

                    break

                if symbol is "}" and stack[0] is not "{":

                    solution = False

                    break

            else:

                solution = False

    return solution

valid_input("(){}[]")

