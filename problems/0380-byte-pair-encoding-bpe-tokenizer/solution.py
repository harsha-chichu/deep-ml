def byte_pair_encoding(corpus: dict, num_merges: int) -> list:
    """
    Train a BPE tokenizer on the given corpus.
    
    Args:
        corpus: Dictionary mapping space-separated token sequences to their frequencies.
                Example: {"l o w </w>": 5, "n e w </w>": 6}
        num_merges: Number of merge operations to perform.
    
    Returns:
        List of tuples, where each tuple contains the two tokens that were merged.
        Example: [('l', 'o'), ('lo', 'w')]
    """

    # Convert corpus strings into token lists
    words = {
        tuple(word.split()): freq
        for word, freq in corpus.items()
    }

    merges = []

    for _ in range(num_merges):
        pair_counts = {}

        # 1. Count adjacent pairs weighted by frequency
        for tokens, freq in words.items():
            for i in range(len(tokens) - 1):
                pair = (tokens[i], tokens[i + 1])
                pair_counts[pair] = pair_counts.get(pair, 0) + freq

        # No more pairs available
        if not pair_counts:
            break

        # 2. Find the most frequent pair
        best_pair = max(pair_counts, key=pair_counts.get)

        merges.append(best_pair)

        # 3. Merge the best pair everywhere
        new_words = {}

        for tokens, freq in words.items():
            merged_tokens = []
            i = 0

            while i < len(tokens):
                if (
                    i < len(tokens) - 1
                    and tokens[i] == best_pair[0]
                    and tokens[i + 1] == best_pair[1]
                ):
                    merged_tokens.append(best_pair[0] + best_pair[1])
                    i += 2
                else:
                    merged_tokens.append(tokens[i])
                    i += 1

            new_words[tuple(merged_tokens)] = (
                new_words.get(tuple(merged_tokens), 0) + freq
            )

        words = new_words

    return merges