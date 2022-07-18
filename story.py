#reference - https://stackoverflow.com/questions/60208/replacements-for-switch-statement-in-python

from random import randint

def low():
    responses = {1 : "\nVIRUS: We're not gaining enough attention, consider an upgrade....",
                 2 : "\nVIRUS: I need an upgrade...",
                 3 : "\nVIRUS: Too much screaming and not enough dying around here...",
                 4 : "\nVIRUS: What kind of theatrics is this? We're getting nowhere, fast!",
                 5 : "\nVIRUS: Could you at least show a little enthusiam?",
                 6 : "\nVIRUS: What kind of low-level sorcery is this, we need more power!",
                 7 : "\nVIRUS: I can't even look at you right now, this just isn't good enough..."}

    choice = randint(1, 7)

    message = responses[choice]

    print(message)


def medium():
    responses = {1 : "\nVIRUS: Now we're creating a little panic.",
                 2 : "\nVIRUS: I'm starting to gain a little traction, don't disappoint me...",
                 3 : "\nVIRUS: We're finally starting to cause some damage!",
                 4 : "\nVIRUS: Much better, I'm sure we could push a little harder though.",
                 5 : "\nVIRUS: Progressing well, I do feel we could generate more power, perhaps consider mutation.",
                 6 : "\nVIRUS: A little positive reinforcement can go a long way!",
                 7 : "\nVIRUS: I may have just wiped out a whole town, don't you judge me!"}

    choice = randint(1, 7)

    message = responses[choice]

    print(message)

def uppermedium():
    responses = {1 : "\nVIRUS: I'm really stretching my legs now!",
                 2 : "\nVIRUS: I'm on schedule to tear this place apart.",
                 3 : "\nVIRUS: I've just about changed the face of this country's topography!",
                 4 : "\nVIRUS: Now we're making a point, causing some real damage now!",
                 5 : "\nVIRUS: It's like playing God in reverse!",
                 6 : "\nVIRUS: We've come so far, consider the end-game. Mutation could be our only hope for total extermination!",
                 7 : "\nVIRUS: I hope you're having as much fun as I am!"}    

    choice = randint(1, 7)

    message = responses[choice]

    print(message)

def high():
    responses = {1 : "\nVIRUS: Keep going! More confirmed kills coming up!",
                 2 : "\nVIRUS: We've almost taken over the entire country!",
                 3 : "\nVIRUS: This one's for the record book!",
                 4 : "\nVIRUS: Get me a map, I need to scribble this place off it!",
                 5 : "\nVIRUS: Spare no one, kill everyone and everything!",
                 6 : "\nVIRUS: We've almost successfully completed our mission!",
                 7 : "\nVIRUS: Veni Vidi VICI"}

    choice = randint(1, 7)

    message = responses[choice]

    print(message)
