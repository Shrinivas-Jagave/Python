def assignment_operators():
    print("1. Simple Assignment")
    a = 10
    print("a =", a)

    print("2. Add and Assign (+=)")
    a += 5
    print("a =", a)

    print("3. Subtract and Assign (-=)")
    a -= 3
    print("a =", a)

    print("4. Multiply and Assign (*=)")
    a *= 2
    print("a =", a)

    print("5. Divide and Assign (/=)")
    a /= 3
    print("a =", a, "Type:", type(a))

    print("6. Floor Divide and Assign (//=)")
    a //= 2
    print("a =", a)

    print("7. Modulus and Assign (%=)")
    a %= 3
    print("a =", a)

    print("8. Exponent and Assign (**=)")
    a **= 2
    print("a =", a)

def main():
    assignment_operators()

main()
