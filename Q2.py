def processor (n:int) -> int:
    '''
    Input 是一個數字，
    Output 是從 1 到這個數字，扣除掉所有 3 的倍數以及 5 的倍數，
    但是保留同時是 3 和 5 的倍數的總數字數。 
    '''
    num_list = []
    for num in range (1, n+1):
        if num % 15 == 0:
            num_list.append(num)
        elif num % 3 == 0 or num % 5 == 0:
            continue
        else:
            num_list.append(num)
    return len(num_list)

def main():
    '''
    Accept the input number process it with the processor function
    '''
    n = int(input("Please type in a number..."))
    print(processor(n))

if __name__ == "__main__":
    main()