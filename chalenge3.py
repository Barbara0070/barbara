from string import ascii_letters

with open("danechal") as f:
    dane= f.read()
out=[]

for z in dane:
    if z in ascii_letters:
        out.append(z)
print(out)
#http://www.pythonchallenge.com/pc/def/ocr.html
#http://www.pythonchallenge.com/pc/def/equality.html
#chr()ord()