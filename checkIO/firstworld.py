# checkio Elementary+: First Word

def first_word(text: str) -> str:
    sepset = {' ','.',','}
    if text[0] in sepset:
        return first_word(text[1:])
    else:
        seps = [pos for pos, char in enumerate(list(text)) if char in sepset]
        return text if len(seps)==0 else text[:seps[0]]
        

if __name__ == "__main__":
    print("Example:")
    print(first_word("Hello world"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert first_word("Hello world") == "Hello"
    assert first_word(" a word ") == "a"
    assert first_word("don't touch it") == "don't"
    assert first_word("greetings, friends") == "greetings"
    assert first_word("... and so on ...") == "and"
    assert first_word("hi") == "hi"
    assert first_word("Hello.World") == "Hello"
    print("Coding complete? Click 'Check' to earn cool rewards!")
