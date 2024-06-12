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

    subsets.remove(biggestSet)

    for set in subsets:
        if len(biggestSet) <= len(set):
            return "No output"
    return biggestSet[randint(0, len(biggestSet) - 1)]

##modyfikacja majority_voter, aby zawsze można było zwrócić wynik