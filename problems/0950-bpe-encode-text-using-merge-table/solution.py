def bpe_encode(text, token_to_id, merges):
    # Your code here
    if not text:
            return []

    tokens = [token_to_id[ch] for ch in text]

    while True:
        best_pair = None
        best_rank = float('inf')

        for i in range(len(tokens)-1):
            pair = (tokens[i], tokens[i+1])

            if pair in merges and merges[pair] < best_rank:
                best_pair = pair
                best_rank = merges[pair]

        if best_pair is None:
            break
        
        new_id = merges[best_pair]

        merged = []
        i = 0

        while i<len(tokens):
            if i<len(tokens)-1 and tokens[i]==best_pair[0] and tokens[i+1]==best_pair[1]:
                merged.append(new_id)
                i += 2
            else:
                merged.append(tokens[i])
                i += 1

        tokens = merged

    return tokens