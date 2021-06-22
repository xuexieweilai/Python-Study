if __name__ == '__main__':
    qt = ['q', 'i', 'n', 'g', 'teng']
    num = [1, 2, 3, 4, 5]
    A0 = dict(zip(qt, num))
    A1 = range(8)
    A2 = [i + 1 for i in A1 if i in A0]
    A3 = [A0[s] for s in A0]
    A4 = [i + 2 for i in A1 if i in A3]
    A5 = [[i, i * i] for i in A1]
    A6 = [i * j for i in A1 if i % 2 if i > 3 for j in A0]

    print("A0", A0) # {"q": 1, "i": 2, "n": 3, "g": 4, "teng": 5}
    print("A1", A1) # [0, 1, 2, 3, 4, 5, 6, 7]
    print("A2", A2) # [1, 2, 3, 4, 5, 6, 7, 8] x
    print("A3", A3) # [1,2,3,4,5]
    print("A4", A4) # [3,4,5,6,7]
    print("A5", A5) # [0, 1, 4, 9, 16, 25, 36, 49]
    print("A6", A6) # [qqqq, iiii, nnnn]