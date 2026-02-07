n = int(input())
doc = {}

for _ in range(n):
    parts = input().split()

    if parts[0] == "set":
        _, key, value = parts
        doc[key] = value

    elif parts[0] == "get":
        _, key = parts
        if key in doc:
            print(doc[key])
        else:
            print(f"KE: no key {key} found in the document")
