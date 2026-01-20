'''
Author : Shrinivas Umakant Jagave
Question : Count vowels and consonants in a string.

'''

def CountVowelsConsonants(s: str) -> tuple:
    if not isinstance(s, str):
        raise TypeError("Input must be a string")

    vowels = "aeiou"
    vowels_count = 0
    consonants_count = 0

    for ch in s.lower():
        if ch.isalpha():          
            if ch in vowels:
                vowels_count += 1
            else:
                consonants_count += 1

    return vowels_count, consonants_count


def main():
    string = "Able was I ere I saw Elba"
    vowels, consonants = CountVowelsConsonants(string)
    print("Vowels:", vowels)
    print("Consonants:", consonants)


main()
