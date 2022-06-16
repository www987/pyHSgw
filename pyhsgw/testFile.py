import pathlib
import datetime
from hsgw import HomeserverConnection

pathHS = pathlib.Path.cwd() / "fHSParameters.txt"


if "100" != "100":
    print("aka")
else:
    print("sss")

listTest = ['4/4/0    1000', "0/1/10   ", '0/1/1    1000']
listList = ['Lighting.Downlights', '0/1/1', '100', '2022.01.10 11:10:15', '2022.01.10 11:10:15', '0', '0\n']

print(listList[1], listTest)

print(r"ala\n ma kota")

index = [l for l,s in enumerate(listTest) if s.startswith(listList[1] + " ")]
print(index)
presentDate = datetime.datetime.now()
print()
