def is_probable_topper_number(number):
    number_str = str(number)
    odd_sum = 0
    even_sum = 0
    for digit in number_str:
        digit = int(digit)
        if digit % 2 == 0:
            even_sum += digit
        else:
            odd_sum += digit
    if odd_sum == even_sum:
        return True
    else:
        return False
number = int(input("Enter the number: "))
if is_probable_topper_number(number):
    print("true")
else:
    print("false")
    
