import sys

text = sys.stdin.read()
text = text.replace("?", ".").replace("!", ".")
sentences = text.split(".")
for sentence in sentences:
    sentence = sentence.strip()
    if any(c.isalnum() for c in sentence):
        sentence = " ".join(sentence.split())
        sentence = sentence.lower()
        sentence = sentence[0].upper() + sentence[1:]
        print(sentence)