def distance(vote1, vote2):
    """
    Function to calculate the distance between two votes.

    Parameters:
    - vote1: An integer candidate 1.
    - vote2: An integer candidate 2.

    Returns:
    - The distance between the two votes.
    """
    return abs(vote1 - vote2)

def calculate_weights(votes, a):
    """
    Function to calculate the weights for each vote based on the distance between votes.

    Parameters:
    - votes: A list of integers representing each candidate.
    - a: a fixed constant for scaling

    Returns:
    - A list of weights for each vote.
    - The sum of the weights for normalisation.
    """
    weights = []

    for i, vote in enumerate(votes):
        product = 1
        for j, other_vote in enumerate(votes):
            if i != j:
                product *= distance(vote, other_vote)/(a**2)
        weight = (1 + product)**-1
        weights.append(weight)

    return weights, sum(weights) 

def weighted_average_voter(votes, scale):
    """
    Function to determine the winner based on a weighted average vote. Weights are calculated based on the distance between votes, in such a way 
    that large numbers won't have a big impact on the result.

    Parameters:
    - votes: A list of integers representing the votes for each candidate.

    Returns:
    - The winning candidate index (1-indexed), or None if there is a tie.
    """
    weights, sum_weights = calculate_weights(votes, scale)
    return sum([vote*(weight/sum_weights) for vote, weight in zip(votes, weights)])

# Example usage:
votes = [0.18155, 0.18230, 0.18130, 0.18180, 0.18235, 0.183]
scale = 1
winner = min(votes, key=lambda x: abs(x - weighted_average_voter(votes, scale)))
print(f"The weighted average vote is {winner}.")