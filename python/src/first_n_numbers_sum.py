def sum_of_first_n(n):
    total = 0

    for i in range(1, n + 1):
        total += i
        
    return total

# n = 10
# print(f'Sum of first {n} numbers is {sum_of_first_n(n)}')