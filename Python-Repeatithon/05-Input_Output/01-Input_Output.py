def main():
    Name = input("Enter Your Name : ")
    Age = int(input("Enter Your Age : ")) # input() returns a string by default, so it is explicitly typecast to int

    print(f"Name : {Name}")
    print(f"Age : {Age}")

main()
