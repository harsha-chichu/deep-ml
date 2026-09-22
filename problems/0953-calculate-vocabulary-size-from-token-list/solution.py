def vocab_size(tokens, special_tokens=None):
    """Return the vocabulary size from a list of preprocessed tokens.

    Args:
        tokens: list[str] of preprocessed tokens
        special_tokens: optional list[str] of special tokens to include
    Returns:
        int: number of unique tokens in the combined vocabulary
    """

    if tokens or special_tokens:
        table = {}

        for i in tokens:
            table[i] = table.get(i, 0) + 1
        
        if special_tokens is not None:
            for i in special_tokens:
                table[i] = table.get(i, 0) + 1
            
        return len(table)

    return 0