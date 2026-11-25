def vocabulary(dataset: str) -> list[dict[str, int], dict[int, str]]:
    """
    Generate a vocabulary list based on dataset
    """

    result = set()
    vocabulary = []

    with open(dataset, encoding="utf-8") as ds:
        # Find unique characters
        for c in ds.read():
            result.add(c)

    result = sorted (list(result))

    data_to_token = {}
    for i in range (len(result)):
        data_to_token[result[i]] = i

    vocabulary.append(data_to_token)

    token_to_data = {}
    for i in range (len(result)):
        token_to_data[i] = result[i]

    vocabulary.append(token_to_data)

    return vocabulary

def encode (data: str, data_to_token: dict[str, int]) -> list[int]:

    tokens = []

    for c in data:
        tokens.append(data_to_token[c])

    return tokens 

def decode(token: list[int], token_to_data: dict[int, str]) -> str:

    decoded = ""

    for i in token:
         decoded += token_to_data[i]
        
    return decoded