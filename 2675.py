for i in range(int(input())):
    txt = list(input().split(sep=" "))
    full_txt = ""
    for i in range(0, len(txt[1])):
        full_txt += txt[1][i]*int(txt[0])
    print(full_txt)
