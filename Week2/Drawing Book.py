def pageCount(n, p):
    # Write your code here
    from_front = p // 2

    # Adjust n if n is even and p is odd   
    if n % 2 == 0 and p % 2 != 0:
        n += 1

    # Calculate turns from the back
    from_back = (n // 2) - (p // 2)

    # Return the minimum of the two
    return min(from_front, from_back)
