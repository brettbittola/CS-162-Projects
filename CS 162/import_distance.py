from math import sqrt

def distance(x1, y1, x2, y2):
    return sqrt((x2-x1)**2 + (y2-y1)**2)

def main():
    d1 = distance(3, 5, -1, 2)  # Your function should return d = 5
    d2 = distance(0, 0, 0, 0)  # Your function should return d = 0
    print(d1)
    print(d2)

if __name__ == '__main__':
    main()