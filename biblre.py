import re
s="Ala ma kota ko!lubi mleko! nie lubi ryb"
print(re.findall(".{3} ma", s))

#print(re.findall("\w+ ma", s))
print(re.findall(r'[A-Z].*?\.', s))

print(re.findall(r'[ \!]', s))


