def MissingNumberInList(L: list) -> int:
    if not isinstance(L, list):
        raise TypeError("Bad type")

    if not L:
        raise ValueError("List should not be empty")

    if not all(isinstance(x, int) for x in L):
        raise ValueError("Values should be integers")

    n = max(L)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(L)

    missing = expected_sum - actual_sum

    if missing == 0:
        return n + 1

    return missing


def main():
    L = [1, 2, 3, 4, 6, 7, 8, 9]
    print(MissingNumberInList(L))


main()
