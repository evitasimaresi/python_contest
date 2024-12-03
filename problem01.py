N = int(input())
if N%2 == 1:
    print(N//2+1)
    print(1,N)
    for i in range(1,N//2+1):
        print(2, i, N-i)

else:  
    print(N//2)
    for i in range(1,N//2+1):
        print(2, i, N-i+1)
