nk = list(input().split())
t = 0 
linux =1
while linux <= int(nk[0]) :
    if linux == int(nk[0]) :
        break
    linux += min(int(nk[1]), linux)
    t+=1
print(t)
