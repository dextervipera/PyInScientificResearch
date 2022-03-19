s0='xxx xxx\nyy yy\nzzz zzzzz'
chk = ''.join([s0[id].upper() if (s0[id-1] in [' ', '\n']) else s0.capitalize()[id] for id, _ in enumerate(s0)])
print(chk)

def lab02_ch(str, sub='',i=0):
 if len(str)==1:
  return str.upper()+sub
 else:
  if str[-2] in (' ','\n'):
    return lab02_ch(str[:-1], str[-1:].upper()+sub,i)
  else:
    return lab02_ch(str[:-1], str[-1]+sub,i)


def lab021_ch(str, sub=''):
  return str.upper()+sub if len(str)==1 else lab02_ch(str[:-1], str[-1:].upper()+sub if str[-2] in (' ','\n') else str[-1:]+sub)
  
print(lab021_ch(s0))
