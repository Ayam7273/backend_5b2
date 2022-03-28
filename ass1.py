def check_fermat():
    a = int(input('Enter the value for A'))
    b = int(input('Enter the value for B'))
    c = int(input('Enter the value for C'))
    n = int(input('Enter the value for N'))


    x = (a**n)+(b**n)
    y =(c**n)

    if n > 2:
        if x == y:
            print('Holy smokes, Fermat was wrong!')
        else:
            print("No, that doesn't work!.")    
    else:
        print('N must be n>2')

check_fermat()

