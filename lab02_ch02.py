# capitelize every first (word || line) letter

## test string
s0='xxx xxx\nyy yy\nzzz zzzzz'

## simple solution
print('Simple solution')
chk = ''.join([s0[id].upper() if (s0[id-1] in [' ', '\n']) else s0.capitalize()[id] for id, _ in enumerate(s0)])
print(chk)

## simplier solution
def lab02_ch(str, sub=''):
 if len(str)==1:
  return str.upper()+sub
 else:
  if str[-2] in (' ','\n'):
    return lab02_ch(str[:-1], str[-1:].upper()+sub)
  else:
    return lab02_ch(str[:-1], str[-1]+sub)

## even simplier solution
def lab021_ch(str, sub=''):
  return str.upper()+sub if len(str)==1 else lab021_ch(str[:-1], str[-1:].upper()+sub) if str[-2] in (' ','\n') else lab021_ch(str[:-1], str[-1]+sub)

print('Even simplier')
print(lab021_ch(s0))
