dr, mr, yr = [int(i) for i in input().split()]
de, me, ye = [int(i) for i in input().split()]

fine = 0
if yr > ye:
    fine = 10000
elif yr == ye:
    if mr > me:
        fine = 500*(mr-me)
    elif mr == me:
        if dr > de:
            fine = 15*(dr-de)
print(fine)