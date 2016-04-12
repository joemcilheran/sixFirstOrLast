def sixfirstorlast():
    first_last6 = input("Please enter at least one integer \n ")
    first_element = int(first_last6[0])
    last_element = int(first_last6[-1])
    if (first_element == 6) or (last_element == 6):
       print("True")
    else:
       print("False")
sixfirstorlast()
