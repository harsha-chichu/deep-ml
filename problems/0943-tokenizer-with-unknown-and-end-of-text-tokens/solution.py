import re

def tokenize(vocab, text, mode):
    """
    vocab: dict[str, int] containing '<|unk|>' and '<|endoftext|>'
    text: str (if mode='encode') or list[int] (if mode='decode')
    mode: 'encode' or 'decode'
    """
    if mode == "encode":
        pieces = re.split(r'([,.:;?_!"()\']|--|\s)', text)
        pieces = [p.strip() for p in pieces if p.strip()]
        unk_id = vocab['<|unk|>']
        return [vocab[p] if p in vocab else unk_id for p in pieces]
            
    elif mode == "decode":
        inv_vocab = {i: t for t, i in vocab.items()}
        tokens = [inv_vocab[i] for i in text]
        joined = ' '.join(tokens)
        result = re.sub(r'\s+([,.?!"()\':;])', r'\1', joined)
        return result