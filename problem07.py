# get input(string), clean it from whitespaces, split it in list of strings, 
# translate the elemnts into integers and sort it
wagons = sorted(list(map(int, input().strip().split(" "))))

lenghtStation = int(input())

def count_combinations(wagons, lengthStation):
    # array that represent a station
    Station = [0] * (lenghtStation + 1)
    Station[0] = 1
    # for every position of the staion
    for i in range(0, lenghtStation + 1):
        # for every available wagon type
        for wagon in wagons:
            # check if the wagon can fit
            if wagon <= i:
                # add all possible combinations fiting current wagon in postion
                Station[i] += Station[i - wagon]
    
    return Station[lenghtStation]



print(count_combinations(wagons, lenghtStation))