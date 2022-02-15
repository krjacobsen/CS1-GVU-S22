# Chapter 2.10 Question 12
# Create a function that returns the first n numbers in the fibonacci sequence

def fibonacci(n):
    print("Canary")
    
def main():
    # prints 1, 1, 2, 3, 5
    print(fibonacci(5))
    
    # prints 1, 1, 2, 3, 5, 8, 13, 21, 34, 55
    print(fibonacci(10))
    
    user_n = input("Enter a number: ")
    print(fibonacci(user_n))
