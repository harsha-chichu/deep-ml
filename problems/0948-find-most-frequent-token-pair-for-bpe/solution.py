def most_frequent_pair(sequences):
    """
    Args:
        sequences: list[list[int]] - list of token ID sequences

    Returns:
        tuple(int, int) or None - the most frequent adjacent pair, with ties
        broken by first appearance. Returns None if no pair exists.
    """
    pair_counts = {}
    first_seen = {}
    position = 0

    for seq in sequences:
        for i in range(len(seq) - 1):
            pair = (seq[i], seq[i + 1])

            if pair not in pair_counts:
                pair_counts[pair] = 0
                first_seen[pair] = position

            pair_counts[pair] += 1
            position += 1

    if not pair_counts:
        return None

    max_count = max(pair_counts.values())

    best_pair = None
    best_pos = float("inf")

    for pair, count in pair_counts.items():
        if count == max_count and first_seen[pair] < best_pos:
            best_pair = pair
            best_pos = first_seen[pair]

    return best_pair