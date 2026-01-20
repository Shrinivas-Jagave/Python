'''
Author : Shrinivas Umakant Jagave
Question : Check if two strings are anagrams

'''

def are_anagrams(s1:str, s2:str)->bool:
    if not isinstance(s1, str) and not isinstance(s2, str):
        raise TypeError("Type Error")
    
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()

    return sorted(s1) == sorted(s2)

def main():
    str1 = "Listen"
    str2 = "Silent"

    if are_anagrams(str1, str2):
        print("Anagrams")
    else:
        print("Not Anagrams")

main()
