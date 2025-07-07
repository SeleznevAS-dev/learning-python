def is_substring(string: str, substring: str) -> bool:
    for i in range(len(string) - len(substring) + 1):
        for j in range(len(substring)):
            if string[i + j] != substring[j]:
                break

            if j == (len(substring) - 1):
                return True
    return False


print(is_substring("12345", "234"))
print(is_substring("12345", "235"))
