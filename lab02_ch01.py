# lisdta 5 kluczy typu 'klucz_1' licz�c od 10 do 15
# s�ownik {klucz: kolejna wartro�� z klucza dzielona przez 5

l5 = ['klucz_{}'.format(id) for id in range(10,15)]
print(l5)

d51 = {val:float(val[-2:])/5 for val in l5}
print(d51)
