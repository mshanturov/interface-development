import module_1

SMALL = module_1.SMALL

def vector_gauss(a, b):
    a, b, d = a.copy(), b.copy(), len(a)

    # прямой
    ind = 0
    for i in range(d):
        if abs(a[i][ind]) >= SMALL:
            for j in range(i + 1, d):
                cfc = a[j][ind] / a[i][ind]
                a[j], b[j] = a[j] - a[i] * cfc, b[j] - b[i] * cfc
            ind += 1
        else:
            continue
    # обратный
    for i in range(d - 1, -1, -1):
        for j in range(d - 1, i - 1, -1):
            if (abs(j - i) < SMALL):
                b[i] /= a[i][j]
            else:
                b[i] -= a[i][j] * b[j]
    return b