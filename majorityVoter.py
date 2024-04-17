from random import random

def majority_voter(votes, threshold):
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

print(majority_voter([0.18155, 0.18230, 0.18130, 0.18180, 0.18235], 0.0005)) 
##kolejność danych ma wpływ na wynik, do zapytania.

