try:
    a=int(input("Enter the First Number:"))
    b=int(input("Enter the Second Number:"))
    print("Choose the options : \npress + for addition\npress - for substraction\npress * for multiplication\npress / for division")
    o=input("Enter the Symbol:")
    match o:
        case '+':
            print(f"The result is {a+b}")
        case '-':
            print(f"The result is {a-b}")
        case '*':
            print(f"The result is {a*b}")
        case '/':
            print(f"The result is {a/b}")
        case default:
            print("There was an Error")
        
except Exception as e:
    print("Enter a valid a and b")