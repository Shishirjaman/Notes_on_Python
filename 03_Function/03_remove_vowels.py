def remove_vowels(string):
    vowels = ('a', 'e', 'i', 'o', 'u')
    
    for c in string:
        if c in vowels:
            string = string.replace(c, "")
            
    return string


if __name__ == "__main__":
    string = input("Enter string to remove vowels from that: ")
    
    string = remove_vowels(string.lower())
    print("The new string after removing vowels is "+ string)