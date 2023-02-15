

## Exerício 1

def k_most_frequent(nums: list, k: int) -> list:

    ocurrences = {k: nums.count(k) for k in list(set(nums))}

    sorted_ocurrences = sorted(ocurrences.items(), key = lambda x: x[1], reverse = True)

    return list(dict(sorted_ocurrences).keys())[0:k]