from transformers import GPT2Tokenizer

tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
phrase = "Artificial intelligence is metamorphosing the world!"

tokens = tokenizer.tokenize(phrase)
print(tokens)


token_ids = tokenizer.encode(phrase)
print("Token IDs:", token_ids)

print("Détails par token:")
for tid in token_ids:
    txt = tokenizer.decode([tid])
    print(tid, repr(txt))


phrase2 = "antidisestablishmentarianism."

tokens2 = tokenizer.encode(phrase2)
print("Détails par token:")
for tid in tokens2:
    txt = tokenizer.decode([tid])
    print(tid, repr(txt))