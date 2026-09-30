def bpe_decode(ids, vocab):
    """
    Args:
        ids: list[int] - token IDs to decode
        vocab: dict[int, str] - mapping from token ID to token string
    Returns:
        str - the decoded text
    """
    decoded = []

    for token_id in ids:
        token = vocab[token_id]

        if token.startswith('G'):
            token = ' ' + token[1:]

        decoded.append(token)

    return ''.join(decoded)