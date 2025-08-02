def count_words(s):
    count = 0
    is_word = False
    for i in range(len(s)):
        if s[i] != " ":
            if not is_word:
                is_word = True
                count += 1
        else:
            assert s[i] == " "
            is_word = False

    assert count >= 0
    return count


print(count_words("подсчитывает количество слов в строке"))
