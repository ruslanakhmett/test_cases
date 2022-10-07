def qsort(array):
    if len(array) < 2:
        return array
    point = array[0]
    lows = [x for x in array[1:] if x <= point]
    highs = [x for x in array[1:] if x > point]
    return qsort(lows) + [point] + qsort(highs)


if __name__ == "__main__":
    print(qsort([-5, -23, 5, 0, 23, -6, 23, 67]))
