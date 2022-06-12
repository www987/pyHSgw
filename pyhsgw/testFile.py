import pathlib
import datetime
pathHS = pathlib.Path.cwd() / "fHSParameters.txt"
f_hs = "a"
with open(pathHS, "r") as fileHs:
    f_hs = fileHs.readlines()
    #print(f_hs, type(f_hs))
    split_string = f_hs[0].split("\t")
    split_string[6] = '0'
    split_string = ''.join(split_string)


presentDate = datetime.datetime.now()
print()
