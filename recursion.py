# ­ Implement the Fibonnaci Sequence
def fibonnaci(n):
    if n <= 0:
        return " Invalid  Input. PLease provide a positve interger"
    elif n == 2:
        return 1
    elif n == 1:
        return 0
    else:
        return fibonnaci(n - 1) + fibonnaci(n - 2)


# getting user input
fin_input = int(input("Enter a positive integer for Fibonacci calculation: "))
fin_results = fibonnaci(fin_input)
print(f"The {fin_input}th fibonnaci number is :{fin_results} ")

# print("***************************************************")


# Implement Euclid’s GCD Algorithm
def gcd(a, b):
    # base case
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


# getting user input
gcd_a = int(input("Enter the first integer for GCD calculation: "))
gcd_b = int(input("Enter the second integer for GCD calculation: "))
gcd_result = gcd(gcd_a, gcd_b)
print(f"The gcd of {gcd_a} and {gcd_b} is :{gcd_result}")


def compareTo(s1, s2):
    # base case 1 : If both are empty they are equal
    if not s1 and not s2:
        return 0
    # base case 2 : if s1 is a prefix of s2 then s1 is smaller
    if not s1:
        return -1
    # base case 3 : if s2 is a prefix of s1 the s2 is smaller
    if not s2:
        return 1

    # comparing the first character of the string
    if s1[0] < s2[0]:
        return -1
    elif s1[0] > s2[0]:
        return 1
    else:
        return compareTo(s1[1:], s2[1:])


string_1 = input("Enter the first string for comparison: ")
string_2 = input("Enter the second string for comparison: ")
string_results = compareTo(string_1, string_2)
print(f"String Comparison results :{string_results}")