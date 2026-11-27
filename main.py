import tokenizer
import bigram
import numpy as np

def main(): 
    vocab = tokenizer.vocabulary("data/tiny_shakespeare.txt")
    # enc = tokenizer.encode("hello world", vocab[0])
    # dec = tokenizer.decode(enc, vocab[1])

    # for c, tok in vocab[0].items(): print(c + " " + str(tok))

    # for i in enc: print(i)

    # array = bigram.create_empty_gram(3)
    # print(array)

    # bigram.frequency_counting(array, "aba", {"a": 0, "b": 1})

    # print(array)

    bigram.run_bigram("data/tiny_shakespeare.txt", "hello", 10)

if __name__ == "__main__":
    main()