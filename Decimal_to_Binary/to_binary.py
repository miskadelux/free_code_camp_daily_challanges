def to_binary(decimal):
    binary = ""
    
    while decimal != 0:
        rest = decimal % 2
        decimal = decimal // 2
        binary = binary + str(rest)
        
    return str(binary[::-1])
