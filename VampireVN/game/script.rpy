# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define mc = Character("[player]", color="#dead71", image="mc")
define l = Character("Laila", color="#b55151")
define c = Character("Cassandra", color="#5ba84c")
define a = Character("Anne", color="#b55151")
define h = Character("Han", color="#b55151")

#---LAILA---

image l angry = "/laila/l angry.png"
image l away = "/laila/l away.png"
image l excited = "/laila/l excited.png"
image l neutral = "/laila/l neutral.png"
image l smile = "/laila/l smile.png"

#---CASS---

image c confident = "/cassandra/c confident.png"
image c doubt = "/cassandra/c doubt.png"
image c neutral = "/cassandra/c neutral.png"
image c smile = "/cassandra/c smile.png"
image c wink = "/cassandra/c wink.png"

#---ANNE---

image a angry = "/anne/a angry.png"
image a annoyed = "/anne/a annoyed.png"
image a confused = "/anne/a confused.png"
image a frown = "/anne/a frown.png"
image a neutral = "/anne/a neutral.png"

#---HAN---

image h neutral = "/han/h neutral.png"
image h sigh = "/han/h sigh.png"
image h smile = "/han/h smile.png"
image h surprise = "/han/h surprise.png"
image h unsure = "/han/h unsure.png"

#---BACKGROUNDS---

image apartment = "/bg/apartment.png"
image cellar = "/bg/cellar.png"
image church = "/bg/church.png"
image clinic = "/bg/clinic.png"
image creepy house = "/bg/creepy house.png"
image diner = "/bg/diner.png"
image dungeon = "/bg/dungeon.png"
image forest = "/bg/forest.png"
image hideout = "/bg/hideout.png"
image library = "/bg/library.png"
image mansion ext = "/bg/mansion ext.png"
image mansion int = "/bg/mansion int.png"
image street = "/bg/street.png"

#---CODE UPKEEP---

define right = Position(xalign=0.8)
define left = Position(xalign=0.2)
define easeoutleft = ComposeTransition(dissolve, before=easeoutleft)
define easeinleft = ComposeTransition(dissolve, after=easeinleft)
define easeoutright = ComposeTransition(dissolve, before=easeoutright)
define easeinright = ComposeTransition(dissolve, after=easeinright)
define easeouttop = ComposeTransition(dissolve, before=easeouttop)
define easeintop = ComposeTransition(dissolve, after=easeintop)
define easeoutbottom = ComposeTransition(dissolve, before=easeoutbottom)
define easeinbottom = ComposeTransition(dissolve, after=easeinbottom)
define dissolve = Dissolve(.3)
define quickdissolve= Dissolve(.2)

init:
    $ menu_variable = 0
    $ laila_affection = 0
    $ cass_affection = 0



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

    c doubt "Oh my god! You’re awake! I was so worried about you!"

    "Cassandra Kalluri. Of course she’s here. She’s always looking out for you."

    "You’ve been inseparable since middle school. It was hard to find queer friends in a small Southern town like ____ but when you do the bond is unbreakable."

    menu who_what_where:
        "Where am I?":
            jump c1b
        "Who am I?":
            jump c1c
        "Why am I":
            jump c1d

label c1b:
    c doubt "Where are you? You’re in your apartment! Are you ok? Oh my god, Oh my god, does it cause memory loss?"

    c neutral "Quick, what’s your name?"

    jump nameEntry

label c1c:
    c doubt "Oh god, please tell me you remember your own name!"
    
    "My name is..."

    jump nameEntry

label c1d:
    c neutral "Don’t get philosophical on me! I’m worried about you, you lost a lot of blood!"

    "A lot of blood? What the hell happened last night?"

    "You feel dizzy and your mind feels clouded. You try to focus on a constant. Your name is…"

    jump nameEntry

label nameEntry
    # CODE HERE

    c "Ok, you remember your name is [player]. That’s good."

    
    return
