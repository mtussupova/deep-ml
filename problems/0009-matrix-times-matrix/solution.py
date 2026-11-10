def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
    n1 = len(a)
    m1 = len(a[0])
    n2 = len(b)
    m2 = len(b[0])

    if m1 != n2:
        return -1
    out = []

    for i in range(n1):
        v = []
        for j in range(m2):
            l = 0
            for k in range(n2):
                l += a[i][k]*b[k][j]
            v.append(l)
        out.append(v)
    return out



