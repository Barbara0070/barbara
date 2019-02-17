import re
with open("input.txt", encoding="utf-8") as f:
    napis=f.read()
    kody_pocztowe=re.findall("\D(\d{2}-\d{3})\D", napis)
    print(kody_pocztowe)
    adresy=re.findall("[\w\-+.]+@[\w\-.]+", napis)
    print(adresy)
    daty=re.findall("\d\d \w\w\w \d\d\d\d", napis)
    print(daty)
