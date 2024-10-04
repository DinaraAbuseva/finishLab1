

def draw(offset, y):
    print(" " * int(offset*y), "\x1b[48;5;9m|\x1b[0m")


def func():
    y = 100
    masY = [num for num in range(1,y,2)]
    offset = 0.2
    for x in masY[::-1]:
        draw(offset, y)
        offset = 1/x


if __name__ == "__main__":
    func()