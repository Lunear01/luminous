def vocabulary(dataset: str) -> tuple[dict[str, int], dict[int, str]]:
    """
    Generate a vocabulary based on dataset.

    Returns a tuple of dictionaries
    Index 0: Character to token
    Index 1: Token to character
    """

    result = set()

    with open(dataset, encoding="utf-8") as ds:
        # Find unique characters by adding each letter in the set
        for c in ds.read():
            result.add(c)

    # Sort characters in order
    result = sorted (list(result))

    # Builds the vocabulary with input: unique token
    data_to_token = {}
    for i in range (len(result)):
        data_to_token[result[i]] = i

    # Builds the vocab with unique token: input
    token_to_data = {}
    for i in range (len(result)):
        token_to_data[i] = result[i]

    return data_to_token, token_to_data

def encode (data: str, data_to_token: dict[str, int]) -> list[int]:
    tokens = [data_to_token[c] for c in data]
    return tokens 

def decode(token: list[int], token_to_data: dict[int, str]) -> str:
    return "".join(token_to_data[i] for i in token)
