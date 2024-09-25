
import time


def draw(offset,ots,length):
    line = ' ' * length
    otst=" " * ots
    if ots == 0:
        print(f'{" " * offset}\x1b[48;5;9m{line+" "}\x1b[0m')
    elif ots>1:
        print(f'{" " * (offset-ots)}\x1b[48;5;9m{line}\x1b[0m {otst+" "}\x1b[48;5;9m{line}\x1b[0m')
    else:
        print(f'{" " * (offset-ots)}\x1b[48;5;9m{line}\x1b[0m {otst}\x1b[48;5;9m{line}\x1b[0m')


otstup = [0,1,2,4,8,16]
def branch():
    height = 6
    offset=20
    length = 1
    while True:
        for ots in otstup:
            draw(offset,ots, length)
            if ots >= 2:
                length = ots
        length=1
        print(f'\x1b[{height+2}B')
        print(f'\x1b[{offset}D')
        time.sleep(2)


if __name__ == '__main__':
    branch() 