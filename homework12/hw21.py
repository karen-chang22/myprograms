# Most Number of Factors from 1 to N

num = int(input("enter value of N: "))
final_num = 0
factor_count = 0
max_factors = 0
for n in range(1, num+1):
    factor_count = 0
    for divider in range(1, n+1):
        if n % divider == 0:
            factor_count += 1
    if factor_count > max_factors:
        final_num = n
        max_factors = factor_count
    

print(f"{final_num} has the most factors, with {max_factors} factors.")
    