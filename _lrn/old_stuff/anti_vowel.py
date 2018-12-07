__author__ = 'User'
text = 'Hey look Words!'
def anti_vowel(text):
    m = ""
    for r in text:
        if r in "aeiouy":
            pass
        elif r in "AEIOUY":
            pass
        else:
            m = m+r
    print(m)
anti_vowel(text)