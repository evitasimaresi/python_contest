def weeks_amount(x,y):
    i = 0
    result = 0
    while y < x:
        result += 1
        i += 1
        if i % 4 == 0:
            y *= 0.97
        else:
            y *= 1.05
    return result
            
data = list(map(int,input().split()))
x = data[0]
y = data[1]

print(weeks_amount(x,y))