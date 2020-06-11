def reverser (s:str) -> str:
    '''
    Returns a string with reversed order of characters.
    Ex. reverser("junyiacademy") -> "ymedacaiynuj"
    '''
    return s[::-1]

def flipper(s:str) -> str:
    '''
    Input (str): a sentence in string format
    Output (str): a sentence with same word order, but each word has reversed character order.
    '''
    s_list = list(s.split())
    rev_s_list = [reverser(s) for s in s_list]
    return (' '.join(rev_s_list))

def main():
    '''
    Accept the input sentence, 
    print the sentence with same word order, but each word has reversed character order.
    '''
    s = input("Please type in the sentence...")
    r = flipper(s)
    print(r)

if __name__ == "__main__":
    main()

# f("flipped class room is important") == "deppilf ssalc moor si tnatropmi"