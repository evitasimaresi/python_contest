dna = input().strip()
x = len(dna)
letters = {"A":0,"C":0,"T":0,"G":0}
longest_mutant = 0
strings = []
done = 0

def check(word):
    letters = {"A":0,"C":0,"T":0,"G":0}
    for i in range(len(word)):
        letters[word[i]] += 1
        if len(word) % 2 == 0:
            y = len(word)//2
        else:
            y = len(word)//2 + 1
        if letters[word[i]] >= y:
            return len(word)
    return 0

for i in range(len(dna)):
    for j in range(len(dna)):
        if dna[i:len(dna)-j] != "" and dna[i:len(dna)-j] not in strings:
            strings.append(dna[i:len(dna)-j])
            
if check(dna) == 0:
    for i in range(len(strings)):
        if check(strings[i]) > longest_mutant:
            longest_mutant = len(strings[i])
else:
    longest_mutant = check(dna)

print(longest_mutant)
    
    
