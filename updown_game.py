import random

tar_num = random.randint(0,100)
print('숫자를 맞춰 보세요.(0-100)')
i=0

while i<1:
    inp_num = int(input())
    if tar_num > inp_num :
        print(f"{inp_num}보다 큽니다. UP!")
    elif tar_num < inp_num :
        print(f"{inp_num}보다 작습니다. DOWN!")
    else :
        print(f"맞았습니다. 숫자는 {tar_num}입니다.")
        i+=1 
           