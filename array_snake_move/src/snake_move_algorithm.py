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
    bottom_border = n - 1
    top_border = 0
    move_ = False
    i = 0
    j = 0
    while True:
        if len(res) == n * m:
            return res
        if i == top_border:
            for k in range(m):
                res.append(arr[k][j])
                i = k
                move_ = False
            j += 1
        if move_:
            if i == bottom_border:
                for k in (m - 1, -1, -1):
                    res.append(arr[k][j])
                    i = k
                    move_ = False
                j += 1
        else:
            move_ = True


