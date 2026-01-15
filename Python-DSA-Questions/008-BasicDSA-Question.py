'''
Author : Shrinivas Umakant Jagave
Question : Check if a string is palindrome.

'''

def CheckPalindrome(string: str) -> bool:
    if not isinstance(string, str):
        raise TypeError("Type Error")

    n_string = ''.join(ch.lower() for ch in string if ch.isalnum())
    return n_string == n_string[::-1]

def main():
    string = "Able was I ere I saw Elba"
    if CheckPalindrome(string):
        print("String is palindrome")
    else:
        print("String is not palindrome")

main()
