def count_ten_pairs(n):
    if n < 10:
        return 0
    
    last_digit = n % 10
    remaining_digits = n // 10
    
    count = count_ten_pairs(remaining_digits)
    
    for digit in str(remaining_digits):
        if int(digit) + last_digit == 10:
            count += 1
    
    return count

print(count_ten_pairs(7823952))