def format_number(number):
    phone_number = "+"
    D = number[0]
    phone_number = phone_number + D
    DDD = number[1:4]
    phone_number = phone_number + f" ({DDD}) "
    DDD_1 = number[4:7]
    phone_number += f"{DDD_1}-"
    DDDD = number[7:]
    phone_number += f"{DDDD}"
    
    return str(phone_number)
