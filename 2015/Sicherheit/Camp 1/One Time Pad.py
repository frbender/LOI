# XOR mit zwei Strings
# Vorraussetzung: s1 und s2 sind gleich lang

def otp (s1, s2):
    a1 = list(s1)
    a2 = list(s2)
    return [x1 != x2 for x1,x2 in zip(a1,a2)]

def otp2 (s1,s2):
    a1 = list(s1)
    a2 = list(s2)
    output = []
    for i in range(len(a1)):
        output.append(a1[i] != a2[i])
    return output
