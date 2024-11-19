RHYME = ["" for i in range(13)]
RHYME[1] = "This is the house that Jack built."

RHYME[2] = (
    "This is the malt\
 that lay in the house that Jack built."
)

RHYME[3] = (
    "This is the rat\
 that ate the malt\
 that lay in the house that Jack built."
)

RHYME[4] = (
    "This is the cat\
 that killed the rat\
 that ate the malt\
 that lay in the house that Jack built."
)

RHYME[5] = (
    "This is the dog\
 that worried the cat\
 that killed the rat\
 that ate the malt\
 that lay in the house that Jack built."
)

RHYME[6] = (
    "This is the cow with the crumpled horn\
 that tossed the dog\
 that worried the cat\
 that killed the rat\
 that ate the malt\
 that lay in the house that Jack built."
)

RHYME[7] = (
    "This is the maiden all forlorn\
 that milked the cow with the crumpled horn\
 that tossed the dog\
 that worried the cat\
 that killed the rat\
 that ate the malt\
 that lay in the house that Jack built."
)

RHYME[8] = (
    "This is the man all tattered and torn\
 that kissed the maiden all forlorn\
 that milked the cow with the crumpled horn\
 that tossed the dog\
 that worried the cat\
 that killed the rat\
 that ate the malt\
 that lay in the house that Jack built."
)

RHYME[9] = (
    "This is the priest all shaven and shorn\
 that married the man all tattered and torn\
 that kissed the maiden all forlorn\
 that milked the cow with the crumpled horn\
 that tossed the dog\
 that worried the cat\
 that killed the rat\
 that ate the malt\
 that lay in the house that Jack built."
)

RHYME[10] = (
    "This is the rooster that crowed in the morn\
 that woke the priest all shaven and shorn\
 that married the man all tattered and torn\
 that kissed the maiden all forlorn\
 that milked the cow with the crumpled horn\
 that tossed the dog\
 that worried the cat\
 that killed the rat\
 that ate the malt\
 that lay in the house that Jack built."
)

RHYME[11] = (
    "This is the farmer sowing his corn\
 that kept the rooster that crowed in the morn\
 that woke the priest all shaven and shorn\
 that married the man all tattered and torn\
 that kissed the maiden all forlorn\
 that milked the cow with the crumpled horn\
 that tossed the dog\
 that worried the cat\
 that killed the rat\
 that ate the malt\
 that lay in the house that Jack built."
)

RHYME[12] = (
    "This is the horse and the hound and the horn\
 that belonged to the farmer sowing his corn\
 that kept the rooster that crowed in the morn\
 that woke the priest all shaven and shorn\
 that married the man all tattered and torn\
 that kissed the maiden all forlorn\
 that milked the cow with the crumpled horn\
 that tossed the dog\
 that worried the cat\
 that killed the rat\
 that ate the malt\
 that lay in the house that Jack built."
)


def recite(start_verse, end_verse):
    return RHYME[start_verse : end_verse + 1]
