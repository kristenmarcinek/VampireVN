# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define mc = Character("[player]", color="#dead71", image="mc")
define l = Character("Laila", color="#b55151")
define c = Character("Cassandra", color="#5ba84c")
define a = Character("Anne", color="#b55151")
define h = Character("Han", color="#b55151")


# The game starts here.

label start:
    "You’re not sure why, but things feel different today. Today. Is it still even today?"

    "You sit up from your bed and look behind you, and although your drapes are drawn tight you can tell it’s dark out. Did you… did you sleep for a whole day?"

    "You try to remember what happened last night. There was that party out in the woods. And that strange woman and- was there a bite?"

    "You raise your hand to your neck and, sure enough, you feel two small indents, as if someone bit you."

    "You stand from your bed and all at once everything hurts. Every muscle screams out, demanding you lay back down. Your vision swims and you drop to your knees. You realize now that your mouth is so dry."

    "You stagger out of your bedroom and make it no further than your couch before you collapse, the exhaustion taking too much of a toll on you."

    "You feel a pulsing headache, your body sore as it has ever felt"

    "You want to lie down forever but you hear a worried voice"

    menu start_choice:
        "Wake up":
            jump c1a

label c1a:
    scene apartment

    "Your eyes open to the bright iridescent lights of your apartment. You feel hungover, but you don’t remember drinking last night?"

    "Well, that’s how it happens doesn’t it? You drink so much you don't remember… And yet…"

    "Something seems off… But before you have time to think of what you hear an overjoyed shriek"

    
        


    return
