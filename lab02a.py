def foo(str):
	return str.upper() if len(str)<=1 \
    else foo(str[:-1])+str[-1].upper() if str[-2] in {' ','\n'} \
    else foo(str[:-1])+str[-1]

print(foo('xxx xxx\nyy yy\nzzz zzzzz'))

