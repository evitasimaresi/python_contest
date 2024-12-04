#04.12.2024 Agata
N = int(input())
word = input()
planks = word.split()

for i in range(len(planks)):
    planks[i] = int(planks[i])

planks.sort(reverse=True)

if N == 1:
    answer = planks[i] // 4
else:
    # print("cala reszta")
    # we try use 1 plank
    if planks[0] // 4 >= planks[1]:
        # the best is to devide the longest plank into 4 planks
        answer = planks[0] // 4
    
    # we try use 2 planks
    elif planks[0] // 3 >= planks[1]:
        # we will use plank[1] and plank[0] divid to 3
        answer = planks[1]
    elif N == 2:
        #when we have only 2 planks we can not check the rest options
        if planks[0] // 3 > planks[1] // 2:
            answer = planks[0] // 3
        else:
            answer = planks[1] //2
    elif planks[0] // 3 >= planks[2]:
        # now we will try divide the longest plank to 3 pices and use shorter plank[1]
        answer = planks[0] // 3

    # now we will try divide the longest plank to 2 pices
    # and we want use 3 planks
    elif planks[0] // 2 >= planks[1]:
        if planks[1] // 2 <= planks[2]:
            answer = planks[2]
        else:
            #okey in this case we will use 2 planks
            answer = planks[1] // 2
    elif planks[0] // 2 >= planks[2]:
        answer = planks[2]
    elif N ==3:
        #for any reason
        answer = planks[2]
    elif planks[0] // 2 >= planks[3]:
        answer = planks[0] // 2
    else:
        answer = planks[3]

print(answer * answer)