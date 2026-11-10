def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
    # Your code here
    out = []
    for i in range(len(matrix)):
        a = []
        for j in range(len(matrix[i])):
            a.append(matrix[i][j]*scalar)
        out.append(a)
    return out