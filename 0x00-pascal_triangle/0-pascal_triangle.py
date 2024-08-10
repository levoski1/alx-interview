from math import factorial

def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to the nth row.
    
    Args:
    n (int): The number of rows of Pascal's Triangle to generate.
    
    Returns:
    list: A list of lists of integers representing Pascal's Triangle.
    """
    

    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        row = []
        for j in range(i + 1):
            ncr = factorial(i) // (factorial(j) * factorial(i - j))
            row.append(ncr)
        triangle.append(row)

    return triangle
