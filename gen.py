import sys

s = r"\["
e = r"\]" + "\n"

beg = r"\begin{bmatrix}"
end = r"\end{bmatrix}"

def eucs(a, b):
    if b > a:
        a, b = b, a
    print(s)
    matrix = [[1,0,a], [0,1,b]]
    euc(matrix, False)
    print(e)

def output(m):
    print(beg)
    for l in m:
        print(' & '.join([str(x) for x in l]) + r" \\")
    print(end)
    print('=')
    

def euc(matrix, alt):
    output(matrix)
    if matrix[0][2] == 0 or matrix[1][2] == 0:
        return
    mult = matrix[alt][2] // matrix[not alt][2]

    # Subtract the smaller row from the bigger row without using SciPy matrices
    for x in range(3):
        matrix[alt][x] = matrix[alt][x] - matrix[not alt][x] * mult

    euc(matrix, not alt)

if __name__ == '__main__':
    for arg in sys.argv[1:]:
        try:
            a, b = arg.split(',')
            a, b = int(a), int(b)
        except:
            print("Argument parsing failed for arg '{}'".format(arg))
            continue
        eucs(a, b)
