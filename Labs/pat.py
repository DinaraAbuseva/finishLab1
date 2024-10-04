
import time


def draw(offset,indent,length):
    line = " " * length
    indent_centre = " " * indent
    if indent == 0:
        print(f'{" " * offset}\x1b[48;5;9m{line+" "}\x1b[0m')
    elif indent>1:
        print(
            f'{" " * (offset-indent)}'
            f'\x1b[48;5;9m{line}\x1b[0m {indent_centre+" "}'
            f'\x1b[48;5;9m{line}\x1b[0m'
            )
    else:
        print(
            f'{" " * (offset-indent)}'
            f'\x1b[48;5;9m{line}\x1b[0m {indent_centre}'
            f'\x1b[48;5;9m{line}\x1b[0m'
            )


indents = [0,1,2,4,8,16]
def branch():
    height = 6
    offset = 20
    length = 1
    while True:
        for indent in indents:
            draw(offset, indent, length)
            if indent >= 2:
                length = indent
        length = 1
        print(f'\x1b[{height+2}B')
        print(f'\x1b[{offset}D')
        time.sleep(2)


if __name__ == "__main__":
    branch() 