def compute_distance_matrix(outputs):
    """
    Compute the distance matrix for a given set of outputs.

    Parameters:
    - outputs: List of outputs

    Returns:
    - dist_matrix: 2D list representing the distance matrix
    """
    num_outputs = len(outputs)
    dist_matrix = [[0] * num_outputs for _ in range(num_outputs)]
    for i in range(num_outputs):
        for j in range(i + 1, num_outputs):
            dist_matrix[i][j] = abs(outputs[i] - outputs[j])
            dist_matrix[j][i] = dist_matrix[i][j]  # Distance matrix is symmetric
    return dist_matrix


def generalized_median_voter(outputs):
    """
    Generalized median voter algorithm to select the median output from a set of outputs.

    Parameters:
    - outputs: List of outputs

    Returns:
    - median_output: The median output
    """
    while len(outputs) > 1:
        dist_matrix = compute_distance_matrix(outputs)
        max_distance = max(max(row) for row in dist_matrix)
        max_indices = [(i, j) for i, row in enumerate(dist_matrix) for j, val in enumerate(row) if val == max_distance]
        x_idx, y_idx = max_indices[0]
        x, y = outputs[x_idx], outputs[y_idx]

        current_median = sum(outputs) / len(outputs)
        if abs(x - current_median) < abs(y - current_median):
            outputs.remove(y)
        else:
            outputs.remove(x)
    return outputs[0]


# Example usage:
outputs = [2,2,2,3,3]
median_output = generalized_median_voter(outputs)
print("Median output:", median_output)
#Algorytm generuje zly output dla n % 2 == 0 :)