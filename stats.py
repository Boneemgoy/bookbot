def number_of_words(book_text):
    words = book_text.split()
    return len(words)
def number_of_characters(book_text):
    book_text = book_text.lower()
    num_chara = {}
    for char in book_text:
        if char in num_chara:
            num_chara[char] += 1
        else:
            num_chara[char] = 1
    return num_chara
def character_count(book_text):
    book_text = book_text.lower()
    chara_count = {}
    for chara in book_text:
        if chara in chara_count:
            chara_count[chara] += 1
        else:
            chara_count[chara] = 1
    sorted_count = sorted(
        [{"character": char, "count": count} for char, count in chara_count.items()],
        key=lambda item: item["count"],
        reverse=True
    )
    return sorted_count