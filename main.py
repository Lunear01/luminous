import tokenizer

def main(): 
    vocab = tokenizer.vocabulary("data/tiny-shakespeare.txt")
    enc = tokenizer.encode("hello world", vocab[0])
    dec = tokenizer.decode(enc, vocab[1])

    # for c, tok in vocab[0].items(): print(c + " " + str(tok))

    for i in enc: print(i)
    print(dec)

    return

if __name__ == "__main__":
    main()