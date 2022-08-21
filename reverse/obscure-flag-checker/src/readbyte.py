f = open("check", "rb")
print("char filebytes[] = {", ", ".join(map(str, list(f.read()))), "};")
