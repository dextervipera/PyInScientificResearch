# capitelize every first (word || line) letter

## test string
s0='xxx xxx\nyy yy\nzzz zzzzz'

## simple solution
print('Simple solution')
chk = ''.join([s0[id].upper() if (s0[id-1] in [' ', '\n']) else s0.capitalize()[id] for id, _ in enumerate(s0)])
print(chk,'\n')

## simplier solution
def lab02_ch(str, sub=''):
 if len(str)<=1:
  return str.upper()+sub
 else:
  if str[-2] in (' ','\n'):
    return lab02_ch(str[:-1], str[-1:].upper()+sub)
  else:
    return lab02_ch(str[:-1], str[-1]+sub)

## even simplier solution
def lab021_ch(str, sub=''):
  return str.upper()+sub if len(str)<=1 else lab021_ch(str[:-1], str[-1:].upper()+sub) if str[-2] in (' ','\n') else lab021_ch(str[:-1], str[-1]+sub)

## simpliest solution
def lab023_ch(str):
	return str.upper() if len(str)<=1 else lab023_ch(str[:-1])+str[-1].upper() if str[-2] in {' ','\n'} else lab023_ch(str[:-1])+str[-1]
	
print('Simpliest solution')
print(lab023_ch(s0))

for func in (lab023_ch, lab021_ch, lab02_ch):
    assert func('') == ''
    assert func('a') == 'A'
    assert func('aaa bbb ccccc') == 'Aaa Bbb Ccccc'
    assert func(s0) == chk

