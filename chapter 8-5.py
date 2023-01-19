def rotate_word(s, rot):
    """
    A Caesar cypher. Returns str rotated by rot amount
    s - str
    rot - integer
    To rotate word circularly you have to take its ord, add to it rotation and modulo divide by 26
    since in English there are 26 chars and add remainder to 97(ord of 'a', first letter)
    """
    rotated = ''
    lower = s.lower()
    for c in lower:
        if c == ' ':
            rotated += ' '
            continue
        order = ord(c) + rot
        rotated += chr(97 + ((order - 97) % 26))
    return rotated

print(rotate_word('N cvnab', 13))
"""
ROT13 Jokes:
What do you call a song sung in an automobile? N pnegbba.

What do you call a fish with no eyes? Sfu.

What to you call a deer with no eyes? Ab rlr qrre.

How do you make a hot dog stand? Fgrny vgf punve.

What can you hold without ever touching it? N pbairefngvba.

What clothes does a house wear? Nqqerff.

What country makes you shiver? Puvyr.

What do you get when you cross a stream and a brook? Jrg srrg.

What do you get when you cross poison ivy with a 4-leaf clover? N enfu bs tbbq yhpx.

What has a lot of keys but can not open any doors? N cvnab.
"""
