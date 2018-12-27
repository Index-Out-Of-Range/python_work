def tail(filename):
    with open(filename, 'r', encoding="utf-8") as f:
        while True:
            line = f.readline()
            if line.strip():
                yield line.strip()


g = tail("file.txt")
for i in g:
    if "python" in i:
        print("***", i)