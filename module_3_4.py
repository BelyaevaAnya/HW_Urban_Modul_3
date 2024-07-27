def single_root_words(root_wood, *other_words):
    # сделали все слова в нижнем регистре
    root_wood = root_wood.lower()
    other_words = [word.lower() for word in other_words]
    # поиск внутри слова
    same_words = [same_word for same_word in other_words
                  if (root_wood in same_word) or (same_word in root_wood)]
    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
