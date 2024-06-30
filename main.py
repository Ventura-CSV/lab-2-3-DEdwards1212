def main():
    ##################################################
    # Comlete your code here
    ##################################################
    """
    Use following variables to save your result
    total 
    average
    """
    val1 = int(input('Enter first value:  '))
    val2 = int(input('Enter second value:  '))
    val3 = int(input('Enter third value:  '))
    sum = val1 + val2
    total = sum + val3
    average = (total/3)
    
    print (f"values : {val1, val2, val3}")
    print(f"total : {total:.2f}")
    print (f"average : {average:.2f}")
    
    ########################################
    # Do not delete the return statement
    ########################################
    return total, average


if __name__ == '__main__':
    main()
