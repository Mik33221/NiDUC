from asyncio.windows_events import NULL
from random import randint

def majority_voter_sets(votes, threshold):
    """
    Function to determine the winner based on a majority vote with a specified threshold.

    Parameters:
    - votes: A list of integers representing values to be voted on.
    - threshold: A float representing the maximum difference of between values to be considered "same"

    Returns:
    - subsets: A list of subsets of votes grouped by the threshold
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
    """
    Function to determine the winner based on a majority vote with a specified threshold.

    Parameters:
    - votes: A list of integers representing values to be voted on.
    - threshold: A float representing the maximum difference of between values to be considered "same"

    Returns:
    - The winning value or None if no majority is found.
    """
    N = len(votes)
    subsets = majority_voter_sets(votes, threshold)
    if not subsets:  # Check if subsets is empty
        return

    biggestSet = subsets[0]
    for set in subsets:
        if len(set) > len(biggestSet):
            biggestSet = set

    if len(biggestSet) < (N + 1) / 2:
        return

    subsets.remove(biggestSet)

    for set in subsets:
        if len(biggestSet) <= len(set):
            return

    return biggestSet[randint(0, len(biggestSet) - 1)]

