from b import analyze_text
with open("input.txt", "r", encoding="utf-8") as f:
    text = f.read()
top_words, top_letters = analyze_text(text)

for w, c in top_words:
    print(f"{w} {c}", end=" ")
print()
for l, c in top_letters:
    print(f"{l} {c}", end=" ")
print()
