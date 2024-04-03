def weighted_average_voter(votes, weights):
    """
    Function to determine the winner based on a weighted average vote.

    Parameters:
    - votes: A list of integers representing the votes for each candidate.
    - weights: A list of integers representing the weights corresponding to each vote.

    Returns:
    - The winning candidate index (0-indexed), or None if there is a tie.
    """

    # Calculate the weighted average for each candidate
    weighted_averages = [vote * weight for vote, weight in zip(votes, weights)]

    # Find the index of the candidate with the highest weighted average
    max_average = max(weighted_averages)
    winners = [i for i, average in enumerate(weighted_averages) if average == max_average]

    if len(winners) == 1:
        return winners[0]  # Return the index of the winning candidate
    else:
        return None  # Return None if there is a tie


# Example usage:
candidate_votes = [50, 40, 60, 45]
candidate_weights = [1, 2, 1, 1]

winner_index = weighted_average_voter(candidate_votes, candidate_weights)
if winner_index is not None:
    print(f"The winning candidate is Candidate {winner_index + 1}.")
else:
    print("There is a tie.")
