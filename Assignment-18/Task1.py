def print_numbers():
    """
    Print the first 10 natural numbers using a loop.
    
    This function uses a for loop to iterate through numbers 1-10
    and prints each number on a separate line.
    
    Returns:
        None
    
    Example:
        >>> print_numbers()
        1
        2
        3
        4
        5
        6
        7
        8
        9
        10
    """
    for num in range(1, 11):
        print(num)


# Call the function
if __name__ == "__main__":
    print_numbers()