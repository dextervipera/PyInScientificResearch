# lisdta 5 kluczy typu 'klucz_1' licz¹c od 10 do 15
# s³ownik {klucz: kolejna wartroœæ z klucza dzielona przez 5

l5 = ['klucz_{}'.format(id) for id in range(10,15)]
print(l5)

d51 = {val:float(val[-2:])/5 for val in l5}
print(d51)
