def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
    # Return a list where each element is the dot product of a row of 'a' with 'b'.
    # If the number of columns in 'a' does not match the length of 'b', return -1.
    out = []
    n = len(a)
    m = len(a[0])

    if n != len(b):
        return -1
    for i in range(m):
        k = 0
        for j in range(n):
            k += a[i][j]*b[j]
        out.append(k)
    return out

