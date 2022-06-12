import pathlib
pathHS = pathlib.Path.cwd() / "fHsParameters.txt"

with open(pathHS, "r") as fileHs:
    f_hs = fileHs.readlines()
    print(f_hs, type(f_hs))
print(f_hs)