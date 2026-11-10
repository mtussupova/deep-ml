def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    # Your code here
    out = []
    n = len(a)
    m = len(a[0])
    for j in range(m):
        b = []
        for i in range(n):
            b.append(a[i][j])
        out.append(b)
    return out