from random import choice


def generate_model(text, order):
    """ Generate a markov model. """
    model = {}
    for i in range(0, len(text) - order):
        fragment = text[i:i + order]
        next_letter = text[i + order]
        if fragment not in model:
            model[fragment] = {}
        if next_letter not in model[fragment]:
            model[fragment][next_letter] = 1
        else:
            model[fragment][next_letter] += 1
    return model


def get_next_character(model, fragment):
    """ Choose next character based on the given model and fragment. """
    letters = []

    if fragment not in model:
        return ""

    for letter in model[fragment].keys():
        for _ in range(0, model[fragment][letter]):
            letters.append(letter)
    return choice(letters)


def generate_text(text, order, length):
    """ Docstring for generate_text. """
    model = generate_model(text, order)

    current_fragment = text[0:order]
    output = ""

    for i in range(0, length - order):
        new_character = get_next_character(model, current_fragment)
        output += new_character
        current_fragment = current_fragment[1:] + new_character

    return output

if __name__ == '__main__':
    key = "929ec5f319ecb73e68b49bbb35612a"
    url = "http://api.lyricsnmusic.com/songs?api_key={key}&artist={artist}"
    for artist in ("Slipknot", "Slash"):
        print(url.format(artist=artist, key=key))
