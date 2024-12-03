numofcourses = int(input())
numofrules = int(input())

rules = []
result = []

#creating a list of rules
for i in range(numofrules):
    rules.append(input().strip().split())

for i in range(len(rules)):
    for j in range(len(rules[i])):
        rules[i][j] = int(rules[i][j])

#creating a hashmap to track dependencies      
dependencies = {}
for i in range(numofcourses):
    dependencies[i] = []

for i in range(len(rules)):
    dependencies[rules[i][0]].append(rules[i][1])
    
#function to check if it's possible to sort the numbers
def doable(x):
    y = 0
    for i in x:
        if len(x[i]) == 0:
            y += 1
    if y == 0:
        return False
    else:
        return True

#choosing the key with empty value and deleting it afterwards until the hashmap is empty
while len(dependencies) > 0:
    if not doable(dependencies):
        break
    for i in dependencies:
        if len(dependencies[i]) == 0:
            result.append(i)
            for j in dependencies:
                if i in dependencies[j]:
                    dependencies[j].remove(i)
            del dependencies[i]
            break

print(result)

