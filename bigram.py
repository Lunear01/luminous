import numpy as np

def create_empty_gram(vocabulary_size: int ) -> np.ndarray: 
    return np.zeros((vocabulary_size, vocabulary_size)) 

def frequency_counting(matrix: np.ndarray, data: str, vocabulary: dict[str, int])-> None:

    for i in range(len(data) - 1): 
        curr = vocabulary[data[i]]
        next = vocabulary[data[i+1]]

        matrix[curr][next] += 1

    return