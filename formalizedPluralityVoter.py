from random import randint

def plurality_voter_sets(votes, threshold):
    subsets = []
    i = 0
    while len(votes) > 0 and i < len(votes):
        subset = [votes[i]]
        j = i + 1
        while j < len(votes):
            if abs(votes[i] - votes[j]) <= threshold:
                subset.append(votes[j])
                votes.pop(j)
            else:
                j += 1
        subsets.append(subset)
        votes.pop(i)
    return subsets

def plurality_voter(votes, threshold):
    subsets = plurality_voter_sets(votes, threshold)
    biggestSet = subsets[0]
    for set in subsets:
        if len(set) > len(biggestSet):
            biggestSet = set
    return biggestSet[randint(0, len(biggestSet) - 1)]


print(plurality_voter_sets([0.18155, 0.18230, 0.18130, 0.18180, 0.18235], 0.0005))
print(plurality_voter([0.18155, 0.18230, 0.18130, 0.18180, 0.18235], 0.0005))


##modyfikacja majority_voter, aby zawsze można było zwrócić wynik