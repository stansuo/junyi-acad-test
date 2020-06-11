def reverser (s:str) -> str:
    '''
    Returns a string with reversed order of characters.
    Ex. reverser("junyiacademy") -> "ymedacaiynuj"
    '''
    return s[::-1]

def main():
    '''
    Accept the input string, 
    reverse it with the reverser function, print and return it.
    '''
    s = input("Please type in the string...")
    r = reverser(s)
    print(r)
    return r

if __name__ == "__main__":
    main()

# f("junyiacademy") == "ymedacaiynuj"