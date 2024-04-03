def majority_voter(votes):
    """
    Function to determine the winner based on a majority vote.

    Parameters:
    - votes: A list of integers representing votes for each candidate.
             The first element represents votes for candidate A,
             and the second element represents votes for candidate B.

    Returns:
    - The winning candidate (A or B), or None if there is no majority.
    """

    total_votes = sum(votes)
    threshold = total_votes / 2

    if votes[0] > threshold:
        return 'Candidate A'
    elif votes[1] > threshold:
        return 'Candidate B'
    else:
        return None

candidate_A_votes = 60
candidate_B_votes = 80

winner = majority_voter([candidate_A_votes, candidate_B_votes])
if winner:
    print(f"The winner is {winner}.")
else:
    print("There is no majority winner.")
