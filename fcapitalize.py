#HW - 2 function capitalizer

s="xxxx xxxx\nyyyy yyyy\nzzz zzzz"

def strprep(s:str):
    return  [line.split(' ') for line in s.split('\n')]

def listprocess(lst):
    for ln, line in enumerate(lst):
        for wn, word in enumerate(line):
            lst[ln][wn] = lst[ln][wn].capitalize()
    
    return ('\n'.join([' '.join(word) for word in [line for line in lst] ]))

print( listprocess( strprep(s) ) )

