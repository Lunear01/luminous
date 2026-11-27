import tokenizer
import bigram

def main(): 
    vocab = tokenizer.vocabulary("data/tiny-shakespeare.txt")
    # enc = tokenizer.encode("hello world", vocab[0])
    # dec = tokenizer.decode(enc, vocab[1])

    # for c, tok in vocab[0].items(): print(c + " " + str(tok))

    for i in enc: print(i)
    print(dec)
    # for i in enc:
    #     print(i)

    # print(dec)
    # return

    array = bigram.create_empty_gram(3)
    print(array)

    bigram.frequency_counting(array, "aba", {"a": 0, "b": 1})

    print(array)

    return

if __name__ == "__main__":
    main()