from random import randint

def majority_voter_sets(votes, threshold):
    """
    Function to determine the winner based on a majority vote with a specified threshold.

    Parameters:
    - votes: A list of integers representing values to be voted on.
    - threshold: A float representing the maximum difference of between values to be considered "same"

    Returns:
    - The winning value.
    """
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

def majority_voter(votes, threshold):
    N = len(votes)
    subsets = majority_voter_sets(votes, threshold)
    biggestSet = subsets[0]
    for set in subsets:
        if len(set) > len(biggestSet):
            biggestSet = set

    if len(biggestSet) < (N + 1) / 2:
        return "No output"

    subsets.remove(biggestSet)

    for set in subsets:
        if len(biggestSet) <= len(set):
            return "No output"

    return biggestSet[randint(0, len(biggestSet) - 1)]

print(majority_voter_sets([0.18155, 0.18230, 0.18130, 0.18180, 0.18235], 0.0005))
print(majority_voter([0.18155, 0.18230, 0.18130, 0.18180, 0.18235], 0.0005))

print(majority_voter_sets([0.18155, 0.18230, 0.18130, 0.18180, 0.18235, 1, 2, 3, 4], 0.0005))
print(majority_voter([0.18155, 0.18230, 0.18130, 0.18180, 0.18235, 1, 2, 3, 4], 0.0005))
##kolejność danych ma wpływ na wynik, do zapytania.

