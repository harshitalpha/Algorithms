if __name__ == "__main__":
    for _ in range(int(input())):
        x1, y1, x2, y2 = [int(s) for s in input().split()]
        r = y2 - y1
        d = x2 - x1
        print(r*d + 1)


