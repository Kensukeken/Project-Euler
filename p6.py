def sum_square_difference(n):
    # Sum of the squares of the first n natural numbers
    sum_of_squares = sum(i ** 2 for i in range(1, n + 1))
    
    # Square of the sum of the first n natural numbers
    square_of_sum = sum(range(1, n + 1)) ** 2

    # Return the difference
    return square_of_sum - sum_of_squares

# Example for the first 100 natural numbers
n = 100
difference = sum_square_difference(n)
print(f"The difference between the sum of the squares and the square of the sum for the first {n} natural numbers is: {difference}")
