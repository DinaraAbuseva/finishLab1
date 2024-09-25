
line = " "*20
def tailand(line, colour):
    print(f"\x1b[48;5;{colour}m{line}\x1b[0m", end="\n")


cont=[1,7,18]
for i in cont:
    tailand(line,i)
for i in cont[::-1]:
    tailand(line,i)
