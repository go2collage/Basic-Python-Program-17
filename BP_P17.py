# Basic Python Program

# Fabonacci Series

num1, num2 = 0, 1
nterms = 10             # if its Negative

cnt = 0
num = 0

if nterms <= 0:
    print("Number is not positive.")
else:
    print("Fabonacci Sequence: ")
    while cnt < nterms:
        print(num1)
        num = num1 + num2
        num1 = num2
        num2 = num
        cnt += 1
