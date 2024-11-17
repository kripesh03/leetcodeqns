def sum_until_single_digit(num):
    while num >= 10:
        total = 0
        while num > 0:
            total += num % 10 
            num //= 10  
        num = total 
    return num
print(sum_until_single_digit(999))  
print(sum_until_single_digit(1234))  
