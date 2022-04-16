def between_markers(text: str, begin: str, end: str) -> str:
    """
        returns substring between two given markers
    """
    # your code here
    print("begin", text.find(begin))
    print("end",text.find(end))
    if text.find(begin) == -1 and text.find(end) == -1:
        return text
    else:
        if text.find(begin)>text.find(end) and not text.find(end) == -1 and not text.find(begin) == -1:
            return ''
            
    start = 0 if text.find(begin) == -1 else text.find(begin)+len(begin)
    fin   = len(text) if text.find(end) == -1 else text.find(end)
    print( text[start:fin] )
    return text[start:fin]



print('Example:')
print(between_markers('No [b]hi', '[b]', '[/b]'))

if __name__ == '__main__':
    # These "asserts" are used for self-checking and not for testing
    assert between_markers('What is >apple<', '>', '<') == "apple", "One sym"
    assert between_markers("<head><title>My new site</title></head>", "<title>", "</title>") == "My new site", "HTML"
    assert between_markers('No[/b] hi', '[b]', '[/b]') == 'No', 'No opened'
    assert between_markers('No [b]hi', '[b]', '[/b]') == 'hi', 'No close'
    assert between_markers('No hi', '[b]', '[/b]') == 'No hi', 'No markers at all'
    assert between_markers('No <hi>', '>', '<') == '', 'Wrong direction'
    print('Wow, you are doing pretty good. Time to check it!')
