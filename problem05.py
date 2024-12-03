#03.12.2024 Agata
def findPalindrom(a,i,results):
    j = len(a)-1
    while(a[i]!=a[j] and j!=i):
        j -=1
    if(j!=i):
        s = j
        i2 = i
        while(a[i2]==a[s] and i2!=s and i2+1!=s):
            s -=1
            i2 +=1
        if(i2==s and a[i2]==a[s]):
            results.append(a[i:j+1])
            #findPalindrom(a,j-1,results)
            return j
        if(i2+1==s and a[i2]==a[s]):
            results.append(a[i:j+1])
            #findPalindrom(a,j-2,results)
            return j
        elif(a[i]==a[j]):
            findPalindrom(a[0:s],i,results)
            #print(a[0:s+1])
    return 0
a = input()
results = []
for i in range(len(a)):
    findPalindrom(a,i,results)

#results = set(results.sort())
#results.sort()
results = list(set(results))
results.sort()

for word in results:
    print(word)
if(len(results)==0):
    print("No palindromes")
