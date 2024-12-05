number = int(input())
data = []
for i in range(1,number+1):
    data.append(i)

while len(data) != 1:
    i = 0
    while i < len(data):
        if len(data) > 1:
            data.remove(data[i])
        i += 1
    i = len(data) - 1
    while i >= 0:
        if len(data) > 1:
            data.remove(data[i])
        i -= 2
        
    
    
print(data[0])