
print("\x1b[48;5;81m Больше 5 \x1b[0m","\u001b[48;5;82m Меньше 5 \x1b[0m")
print("")
length= " "*5
f=[i for i in open("sequence.txt"). readlines()]
f=[line.rstrip() for line in f]
up5=0
down5=0
for i in f:
    if not(float(i)<0) and float(i)!=5:
        if float(i)>5:
            up5+=1
        else:
            down5+=1


for line in range((max(up5,down5)-min(up5,down5))//4):
    if max(up5,down5) == up5:
        maxi=81
        mini=82
        print(f'\x1b[48;5;{maxi}m{length}\x1b[0m')

    else:
        maxi=82
        mini=81
        print(f'\x1b[48;5;{maxi}m{length}\x1b[0m')


for line in range(min(up5,down5)//4):
    print(f"\x1b[48;5;{maxi}m{length}\x1b[0m",f"\x1b[48;5;{mini}m{length}\x1b[0m")

sum = max(up5,down5) + min(up5,down5)

print(" ",str(round(max(up5,down5)* 100 / sum))+"%", " ", str(round(min(up5,down5)* 100 / sum))+"%")


    

    



