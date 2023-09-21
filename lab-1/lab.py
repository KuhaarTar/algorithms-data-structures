
def initialize_arr(m, n):
    arr = [[0 for _ in range(n)] for _ in range(m)]
    num = 1
    for i in range(m):
        for j in range(n):
            arr[i][j] = num
            num += 1
    return arr


def plant_and_collect_pumpkins(m, n, arr=None):
    if arr is None:
        arr = initialize_arr(m, n)
    res = []
    left_border = 0
    right_border = n - 1
    move_ = False
    i = 0
    j = 0
    while True:
        if res.__len__() == n * m:
            return res
        if j == left_border:
            for k in range(n):
                res.append(arr[i][k])
                j = k
                move_ = False
        if move_:
            if j == right_border:
                for k in range(n - 1, -1, -1):
                    res.append(arr[i][k])
                    j = k
        else:
            move_ = True
        i += 1

