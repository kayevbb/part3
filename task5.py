def twoStrings(s1, s2):
    a = 0

    for i in s1:
        if i in s2:
            a+=1

    if a == 0:
        return 'NO'
    else:
        return 'YES'
