def replace_pair(sequences, pair, new_id):
    # Your code here
    a, b = pair
    result = []

    for seq in sequences:
        i = 0 
        merge = []

        while i<len(seq):
            if i<len(seq)-1 and seq[i]==a and seq[i+1]==b:
                merge.append(new_id)
                i += 2
            else:
                merge.append(seq[i])
                i += 1
        result.append(merge)
    return result