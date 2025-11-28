def analyze_text(text):
    text = text.lower()
    clean = ""
    for ch in text:
        if ch.isalpha() or ch.isspace():
            clean += ch
        else:
            clean += " "
    words = clean.split()
    word_count = {}
    for w in words:
        word_count[w] = word_count.get(w, 0) + 1

    sorted_words = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
    top_words = sorted_words[:3]

    letter_count = {}
    for ch in clean:
        if ch.isalpha():
            letter_count[ch] = letter_count.get(ch, 0) + 1

    sorted_letters = sorted(letter_count.items(), key=lambda x: (-x[1], x[0]))
    top_letters = sorted_letters[:3]
    return top_words, top_letters
