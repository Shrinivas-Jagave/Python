import sys

def main():
    a = 10
    b = 3.5
    c = "25"
    l = [1, 2, 3]

    print("Before Type Casting :")
    print(f"a = {a}, type = {type(a)}")
    print(f"a = {b}, type = {type(b)}")
    print(f"a = {c}, type = {type(c)}")
    print(f"a = {l}, type = {type(l)}")

    a = str(a)
    b = int(b)
    c = float(c)
    l = tuple(l)

    print("Before Type Casting :")
    print(f"a = {a}, type = {type(a)}")
    print(f"a = {b}, type = {type(b)}")
    print(f"a = {c}, type = {type(c)}")
    print(f"a = {l}, type = {type(l)}")

    sys.exit(0)

main()
