def median_voter(preferences):
    """
    Function to determine the median voter based on a list of preferences.

    Parameters:
    - preferences: A list of integers representing the preferences of voters.

    Returns:
    - The median voter's preference.
    """

    sorted_preferences = sorted(preferences)
    num_voters = len(sorted_preferences)

    if num_voters % 2 == 0:
        # If there's an even number of voters, take the average of the two middle preferences
        median_index = num_voters // 2
        median_preference = (sorted_preferences[median_index - 1] + sorted_preferences[median_index]) / 2
    else:
        # If there's an odd number of voters, simply take the middle preference
        median_index = num_voters // 2
        median_preference = sorted_preferences[median_index]

    return median_preference

voter_preferences = [3, 7, 2, 5, 9, 4, 8, 6, 1]
median = median_voter(voter_preferences)
print(f"The median voter's preference is {median}.")

voter_preferences = [1,1,100,2,2]
median = median_voter(voter_preferences)
print(f"The median voter's preference is {median}.")