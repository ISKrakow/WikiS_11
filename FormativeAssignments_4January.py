def sum_sublist(L, i, j):
    return sum(L[i:j])

L = input("Enter a list of numbers: ").split()
L = [int(num) for num in L]

i = int(input("Enter the starting index: "))
j = int(input("Enter the ending index: "))

result = sum_sublist(L, i, j)
print("Sum of sublist L[{}:{}] = {}".format(i, j, result))

