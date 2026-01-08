import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer

SEED = 42  # TODO
torch.manual_seed(SEED)

model = GPT2LMHeadModel.from_pretrained("gpt2")
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

prompt = "The future of artificial intelligence is"
inputs = tokenizer(prompt, return_tensors="pt")

outputs = model.generate(
    **inputs,
    max_length=50,
)

text = tokenizer.decode(outputs[0], skip_special_tokens=True)
#print(text)
        

def generate_once(seed):
    torch.manual_seed(seed)
    out = model.generate(
        **inputs,
        max_length=50,
        do_sample=True,
        temperature=0.7,
        top_k=50,
        top_p=0.95,
    )
    return tokenizer.decode(out[0], skip_special_tokens=True)

for s in [1, 2, 3, 4, 5]:
    print("SEED", s)
    print(generate_once(s))
    print("-" * 40)

def generate_once(seed):
    torch.manual_seed(seed)
    out = model.generate(
        **inputs,
        max_length=50,
        do_sample=True,
        temperature=0.7,
        top_k=50,
        top_p=0.95,
        repetition_penalty = 2.0
    )
    return tokenizer.decode(out[0], skip_special_tokens=True)

for s in [1]:
    print("SEED", s)
    print(generate_once(s))
    print("-" * 40)


def generate_once(seed):
    torch.manual_seed(seed)
    out = model.generate(
        **inputs,
        max_length=50,
        do_sample=True,
        temperature=0.1,
        top_k=50,
        top_p=0.95
    )
    return tokenizer.decode(out[0], skip_special_tokens=True)

for s in [1]:
    print("SEED", s)
    print(generate_once(s))
    print("-" * 40)


def generate_once(seed):
    torch.manual_seed(seed)
    out = model.generate(
        **inputs,
        max_length=50,
        do_sample=True,
        temperature=2.0,
        top_k=50,
        top_p=0.95,
    )
    return tokenizer.decode(out[0], skip_special_tokens=True)

for s in [1]:
    print("SEED", s)
    print(generate_once(s))
    print("-" * 40)

def generate_once(seed):
    torch.manual_seed(seed)
    out = model.generate(
        **inputs,
        max_length=50,
        do_sample=True,
        temperature=0.1,
        top_k=50,
        top_p=0.95,
        repetition_penalty = 2.0
    )
    return tokenizer.decode(out[0], skip_special_tokens=True)

for s in [1]:
    print("SEED", s)
    print(generate_once(s))
    print("-" * 40)


        
import time 

start_time = time.time()

out_beam = model.generate(
    **inputs,
    max_length=50,
    num_beams=5,
    early_stopping=True
)
txt_beam = tokenizer.decode(out_beam[0], skip_special_tokens=True)

timing5 = time.time() - start_time 

start_time = time.time()

out_beam10 = model.generate(
    **inputs,
    max_length=50,
    num_beams=10,
    early_stopping=True
)
txt_beam10 = tokenizer.decode(out_beam10[0], skip_special_tokens=True)

timing10 = time.time() - start_time 

start_time = time.time()

out_beam20 = model.generate(
    **inputs,
    max_length=50,
    num_beams=10,
    early_stopping=True
)


txt_beam20 = tokenizer.decode(out_beam20[0], skip_special_tokens=True)

timing20 = time.time() - start_time 

print(f"5 Beam | Temps de calcul de {timing5} : \n")
print(txt_beam)
print(f"\n10 Beam | Temps de calcul de {timing10} : \n")
print(txt_beam10)
print(f"\n20 Beam | Temps de calcul de {timing20} : \n")
print(txt_beam20)



