def Vigenere(text,verschiebung):
    alp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    text = text.upper()
    output = ""
    i = 0
    for character in text:
        if character in alp:
            index = (alp.index(character) + alp.index(verschiebung[i % len(verschiebung)])) % 26
            output += alp[index]
            i += 1
        else:
            output += character
    return output
