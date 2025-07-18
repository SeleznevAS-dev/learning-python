import logging

logging.basicConfig(filename="is_substring_modified.log", level=logging.INFO, encoding="UTF-8")


def is_substring(string: str, substring: str) -> bool:
    result = None
    logging.info(f"Исходная строка {string}, подстрока {substring}")
    if substring == "":
        result = True
        assert result
        return result

    for i in range(len(string) - len(substring) + 1):
        for j in range(len(substring)):
            assert (i + j) < len(string)
            logging.info(
                f"Символ строки: {string[i + j]}, символ подстроки: {substring[j]}"
            )
            if string[i + j] != substring[j]:
                break

            if j == (len(substring) - 1):
                result = True
                assert result
                return result
    result = False
    assert not result
    return result


print(is_substring("12345", "234"))
print(is_substring("12345", "235"))
print(is_substring("123", ""))
