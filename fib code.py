# LCCS HL Section C Mock Exam
# Question 2
# Name:
def fib(n: int) -> list:
    """
    This function returns a list of all
    Fibonacci numbers up to the nth number
    Assuming n is an integer and is greater than 0
    """
    # First two Fibonacci numbers
    fib_numbers = [0, 1]
    # If n is less than 3, return the first n Fibonacci numbers
    if n < 3:
        return fib_numbers[:n]
    # Otherwise, generate the next Fibonacci numbers up to n
    for i in range(2, n):
    # Append the sum of the two previous numbers
        fib_numbers.append(fib_numbers[i - 2] + fib_numbers[i - 1])
    # Return the list of Fibonacci numbers up to n
    return fib_numbers


number = int(input("Enter number of Fibonacci numbers to generate: "))
maximum = max(number)
minimum = min(number)
modeNum = max(number, key = number.count) 
mean = mean(number)
def median(number):
    sorted_data = sorted(number)
    data_len = len(sorted_data)
    middle = (data_len - 1) // 2
    if middle % 2:
        return sorted_data[middle]
    else:
        return (sorted_data[middle] + sorted_data[middle + 1]) / 2.0
# Calling fib() function
if number <= 1 :
    print("Sorry, the number is too small")
elif number >= 500:
    print("Sorry, the number is too big")
else :
    print("\nFirst", number, "Fibonacci numbers:")
    print(number)
    print("MAX:",maximum)
    print("MIN:",minimum)
    print("MEAN:",mean)
    print("MEDIAN:",median)
    print("MODE:",modeNum)
