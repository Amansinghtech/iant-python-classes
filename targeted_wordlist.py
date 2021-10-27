keywords = [
            "iant",
            "123",
            "1234",
            "12345",
            "nilesh",
            "rakesh",
            "aman"
        ]

symbols = [
            "$", "@", "#"
        ]

def wordlist():
    #with symbols
    for i in keywords:
        for j in keywords:
            if i==j:
                continue
            
            for k in symbols:
                yield "{}{}{}".format(i,k,j)

    #without symbols
    for i in keywords:
        for j in keywords:
            if i==j:
                continue

            yield "{}{}".format(i,j)

with open("wordlist.txt", 'w') as file:
    file.write("\n".join(list(wordlist())))
    file.close()
