def Caesar(text,verschiebung):
    alp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    text = text.upper()
    output = ""
    for character in text:
        if character in alp:
            index = (alp.index(character) + verschiebung) % 26
            output += alp[index]
        else:
            output += character
    return output
