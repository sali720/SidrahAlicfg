def is_pangram(input_string):
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    lowercase_input = input_string.lower()

    return all(char in lowercase_input for char in alphabet)
test_strings = [
    "The quick brown fox jumps over the lazy dog",
    "The five boxing wizards jump quickly",
    "Sphinx of black quartz, judge my vow",
    "Hello, world!",
]
for test_string in test_strings:
    result = is_pangram(test_string)
    print(f"'{test_string}' is a pangram: {result}")

