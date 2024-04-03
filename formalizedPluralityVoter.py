def plurality_voter(votes):
    """
    Function to determine the winner based on a plurality vote.

    Parameters:
    - votes: A dictionary where keys are candidate names and values are the number of votes each candidate received.

    Returns:
    - The winning candidate, or None if there is a tie.
    """

    max_votes = max(votes.values())
    winners = [candidate for candidate, vote_count in votes.items() if vote_count == max_votes]

    if len(winners) == 1:
        return winners[0]  # Return the winner if there's only one
    else:
        return None  # Return None if there's a tie


# Example usage:
candidate_votes = {
    "Candidate A": 150,
    "Candidate B": 200,
    "Candidate C": 150,
    "Candidate D": 180
}

winner = plurality_voter(candidate_votes)
if winner:
    print(f"The winner is {winner}.")
else:
    print("There is a tie.")
