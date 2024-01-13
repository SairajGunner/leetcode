def fractionToDecimal(numerator, denominator):
    """
    :type numerator: int
    :type denominator: int
    :rtype: str
    """
    quotient = str(numerator / denominator)
    first_digit = quotient[0]
    print("first_digit:", first_digit)
    current_pattern = [first_digit]
    isMatching = False
    for i in range(1,len(quotient)):
        current_pattern.append(quotient[i])
        if (quotient[i] == first_digit):
            print("current_pattern", current_pattern)
            print("quotient[i:i+len(current_pattern)-1]", quotient[i:i+len(current_pattern)-1])
            if (current_pattern == quotient[i:i+len(current_pattern)-1]):
                isMatching = True
            else:
                isMatching = False
                break
    if (isMatching == True):
        print(str(int(numerator / denominator)) + "(" + "".join(current_pattern) + ")")
    else:
        return print(quotient)
    
fractionToDecimal(4, 333)