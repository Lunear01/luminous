import numpy as np
import tokenizer

def bigram_probability(data: str, vocabulary: dict[str, int]) -> np.ndarray:
    # Initialize V x V size matrix with 0
    matrix = np.zeros((len(vocabulary), len(vocabulary))) 

    # Count pair frequency
    for i in range(len(data) - 1): 
        curr_ID = vocabulary[data[i]]
        next_ID = vocabulary[data[i+1]]

        matrix[curr_ID, next_ID] += 1

    #Smooth the matrix to prevent probability of zero
    matrix += 1

    # Return the probabilities of based on the frequencies
    return matrix / np.sum(matrix, axis=1, keepdims=True)


def run_bigram(dataset_path: str, seed: str, loops: int) -> None:

    # Generate vocabulary based on dataset
    vocabulary = tokenizer.vocabulary(dataset_path)

    # Get file text as str
    with open(dataset_path, encoding="utf-8") as f:
            text = f.read()

    # Calculate the bigram probability
    probs = bigram_probability(text, vocabulary[0])

    # Tokenize seed
    out = tokenizer.encode(seed, vocabulary[0])
    # The last character in out used to predict the next character
    curr = out[-1]

    for _ in range(loops):
        # Loop and randomluy choose from the probability matrix and add to seed
        curr = np.random.choice(len(probs), p=probs[curr])
        out.append(curr)

    # Output the decoded string
    print(tokenizer.decode(out, vocabulary[1]))
    return