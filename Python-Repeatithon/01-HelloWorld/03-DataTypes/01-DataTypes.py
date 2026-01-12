import sys

def main():
    Int = 10
    Float = 2.55
    String = "Shrinivas"
    Bool = True
    List = [1, 4, 2, 5]
    Tuple = (4, 4, 6, 1, 2)
    Dictionary = {"Name":"Shrinivas", "Age":20}
    Set = {1, 2, 3, 4}
    Complex = 2 + 4j

    print(f"Int : {Int}, Type : {type(Int)}")
    print(f"Float : {Float}, Type : {type(Float)}")
    print(f"String : {String}, Type : {type(String)}")
    print(f"Bool : {Bool}, Type : {type(Bool)}")
    print(f"List : {List}, Type : {type(List)}")
    print(f"Tuple : {Tuple}, Type : {type(Tuple)}")
    print(f"Dictionary : {Dictionary}, Type : {type(Dictionary)}")
    print(f"Set : {Set}, Type : {type(Set)}")
    print(f"Complex : {Complex}, Type : {type(Complex)}")

    sys.exit(0)

main()
