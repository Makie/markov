""" Generate song lyrics in the style of a given artist.

Pulls artists lyrics from LYRICSnMUSIC and uses them to generate a
markov model, the generator then uses the model to form a chain that
should resemble that artists style.
"""

API_KEY = "929ec5f319ecb73e68b49bbb35612a"
API_URL = "http://api.lyricsnmusic.com/songs?api_key={key}&artist={artist}"
