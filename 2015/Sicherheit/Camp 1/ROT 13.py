def CAESAR(text):
    alp = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    text = text.upper()
    output = ""
    for character in text:
        if character in alp:
            index = (alp.index(character) + 13) % 26
            output += alp[index]
        else:
            output += character
    return output