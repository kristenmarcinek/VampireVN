# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define mc = Character("[player]", color="#dead71", image="mc")
define l = Character("Laila", color="#b55151")
define c = Character("Cassandra", color="#5ba84c")
define a = Character("Anne", color="#b55151")
define h = Character("Han", color="#b55151")
define u = Character("Unknown", color="#b55151")

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

label nameEntry:
    # CODE HERE

    c "Ok, you remember your name is [player]. That’s good."

    c "Look, you had an accident, there was blood everywhere… I thought you were dead but your heart was still beating and you seemed fine, your wounds healed before we could call 911, I took you home and now you’re awake and then you asked… and now we’re here."

    "Blood? What do you mean blood? I don’t feel any blood.."

    "You notice a sharp pain in your neck. You reach up to feel it, two holes that seem to have healed up. They feel like decade old scars, and yet you definitely have not had them before today."

    menu how_you_feel:
        "This can't be happening.":
            jump c1e
        "This is so cool!":
            jump c1e
        "I’m so confused…":
            jump c1e
label c1e:
    c neutral "This is going to sound crazy but… I think you got bitten by a vampire. It matches most of the books i read, the skin tone fluctuation and the eyes shifting color and the  two holes in your neck… What do you see here?"

    "Cassandra shows you her phone camera, but you don’t see yourself in it. Could she be right? Are you a.."

    menu vampire_monster:
        "Vampie":
            jump c1f
        "Monster":
            jump c1f
        "Creature of the Night":
            jump c1f
label c1f:
    c smile "Oh my GOD!!! You don’t have a reflection! This is so cool! I wonder what powers you have! I wonder if you can fly…"
    
    "Cassandra has always been a supernatural nerd for as long as you’ve known her. Its always been endearing, but now her knowledge could be the difference between life and death."

    menu c1f_menu:
        "This is a lot… I don’t know what to do.":
            jump c1g
        "A vampire huh? Sounds like a dream come true!":
            jump c1h
        "This may be fun for you, but my whole life has been upended!":
            jump c1g

label c1g:
    c doubt "Sorry, this must be really overwhelming for you. I should be more cognizant of that…"

    c smile "Look, we’ll work through this together ok? Let’s get to the bottom of this!"

    jump c1i

label c1h:
    c smile "“I know right! Oh my god, there is so much to discover, I can’t wait! I’m sure if you got bit, there must be more vampires out there!"

    jump c1i

label c1i:
    "You try to get up, but your sore body makes you utter an involuntary grunt. You feel like you’re having the worst hangover of all time."

    c doubt "“Look, until we know how vampirism is, you need to stay here where it’s safe. I’m gonna run to the library and get every book I can on vampires and be right back."

    c smile "We’ll figure this out together!"

    "As Cassandra, you look behind her, a thousand thoughts running through your head."

    "What have you become? Is it a blessing or a curse?"

    "And as that thought crosses your mind, you hear a rumble"

    "You feel a deep hunger. You turn so you can ransack your fridge, and eat…"

    menu hunger:
        "7 packs of instant ramen":
            jump c1j
        "A bag of frozen chicken tenders":
            jump c1j
        "A loaf of bread and a packet of cheese":
            jump c1j

label c1j:
    "And yet… even though your belly is full you still feel it… the hunger."

    "You step over to the sink, turning on the faucet and stick your head underneath to drink directly from the tap, eschewing a glass."

    "This, though, does not seem to help. If anything, it only makes your appetite worse."

    "You shuffle over to your fridge and take a look inside again. There! You remember something about pickle juice being good for hangovers, perhaps this is just one really fucked up hang over."

    "You grab the jar of pickles and remove the lid with surprising ease, before taking a big gulp of the brine within. You desperately want Cass’s vampire theory to be wrong."

    "While this does not help a great deal with your now-ravenous thirst, the salty liquid does put you in the mindset of something less than conventional. You replace the pickle jar and search your fridge once more."

    "After a moment you find it: nestled into a corner is a cut of beef you bought earlier in the week, but never got around to grilling. You’re unsure of what has inspired you to do it, but you tear open the store packaging and slurp the juices that have collected in the styrofoam tray."

    "And this is what hits the spot. Your muscles relax and your head clears. It should have been disgusting, but somehow it was almost pleasant."

    "There is a sharp rap at your door."

    menu door:
        "Answer the door.":
            jump door1
        "Ignore it":
            jump door2

label door2:
    "The knocking continues, insistent"

    menu:
        "Answer the door":
            jump door1
        "Ignore it":
            jump door2

label door1:
    "You rise and make your way over to your door. You open it, and peer out into the hallway beyond."

    show l neutral with dissolve

    "Standing in front of your door is a remarkably pale woman, dressed in black, her face partially obscured by a wide-brimmed hat. From her wrist dangles a little black purse. She gives you a closed lip smile"

    u "May I come in?"

    "Your voice seems to escape you. There’s something about this woman, her voice- deep and charming- that causes you to step aside, allowing her entry into your apartment."

    "The woman steps languidly into your apartment, and looks around slowly. Her gaze lingers on your still-open fridge and the tray of beef haphazardly left on the counter next to it"

    l neutral "“I’m Laila. Laila Mosshart."

    "She turns to face you."

    mc "I’m [player]."

    l neutral "Good, I have the right place. May I sit?"

    "Without waiting for your response, Laila takes a seat on your couch. You take a seat next to her."

    l neutral "Some of my peers have asked me to oversee your… integration into this new lifestyle."

    mc "What are you talking about?"

    l away "Do you not remember? Of course, some people don’t remember. You were out, last night, at a party in the woods. One of my peers, apparently she got too excited and, well there’s no other way to put it, she bit you."

    menu bite:
        "She BIT me?!?":
            jump inquiry2a
        "I vaguely remember this.":
            jump inquiry2b

label inquiry2a:
    l away "Yes, I know, it’s a lot and she really was not supposed to, I understand your discomfort."

    jump inquiry2common

label inquiry2b:
    l smile "Oh, that’s good, I’m glad some of your memory is coming back."

    jump inquiry2common

label inquiry2common:
    "Everything Laila’s said thus far seems to confirm Cass’s theories. Still, though, you hold out hope this could be something else."

    l neutral "Anyway, myself or one of the others would have typically been with you much earlier, but one of your friends got there first and took you home. It was a whole thing."

    "Everything she’s just said tracks with what Cass said. That’s not great."

    "Laila pauses for a moment. She seems conflicted about what to say next."

    l away "Ugh, look I’m just going to come out and say it, and I hate having to be the one to do this, but you’re a vampire now."

    menu:
        "You’ve got to be kidding":
            jump inquiry3a
        "A vampire? That’s badass!":
            jump inquiry3b
        "That’s a lot":
            jump inquiry3c

label inquiry3a:
    l away "I really wish I was. Quite frankly it sucks to have to do this"

    jump inquiry3common

label inquiry3b:
    l neutral "Well, I’m glad you’re enthusiastic about it"

    jump inquiry3common

label inquiry3c:
    l away "I know how you feel. It takes a while to process"

    jump inquiry3common

label inquiry3common:
    l neutral "Perhaps you’ve already guessed, but I am also a vampire. I know, big surprise, right?"

    "Laila delivers this revelation in a very deadpan, unenthused manner. She sighs."

    l neutral "Our community of vamps here generally tends to look out for each other, and I’m supposed to guide you through the basics."

    l "There’s not a whole lot of time before the sun comes up, so I’ll give you the basics. The sun will hurt and potentially kill you. You can get by on any blood, but human blood is most nutritious."

    "She pauses in thought for a moment"

    l neutral "You don’t need to be invited in, garlic and holy water are chill, but stakes through the heart are not. That’s the big things for right now. I’ll be back to check on you sometime tomorrow night, but if you need me to come by sooner, just give me a ring."

    "Laila pulls a pen out of her purse, before grabbing your arm and scrawling her phone number across it."

    "She stands and makes her way towards the door before stopping suddenly, and turning to face you."

    l neutral "Ah, you should probably take this."

    "She reaches into her purse once again and tosses a little vial your way, which you catch with reflexes that befit your new identity"

    l excited "That’s human blood, ethically sourced, I promise. It should be enough to get you through the next 24 hours. Remember, if you need anything, call."

    "The vampire gives you an actual smile this time, revealing her pointed incisors. With a wink, she turns and departs into the night."

    hide l with dissolve

    "Wow, that was a lot. You stare at the little glass vial in your hands, contemplating its contents"

    jump chapter2

label chapter2:
    scene apartment

    "You blearily open your eyes. Is it morning already? No, not morning, evening. It’s going to take some getting used to this whole nocturnal thing."

    "The headache you had last night is not quite so bad now. And as you rise from your bed, you find your muscles are far less sore than they were before."

    "You run your tongue over your teeth. It seems overnight your new incisors have come in, sharp. You dread to think of what they’re meant to be used for."

    "You put on some fresh clothes and make your way out of your bedroom and over to the couch. What to do now?"

    "You think on the two women who visited you last night- your old friend Cassandra, and the mysterious vampire Laila. You have no doubt you’ll see both of them tonight. That said, it might be best to call one of them now, whoever you feel you should speak with most."

    menu call:
        "Call Cassandra":
            jump label callcass
            $ cass_affection += 1
        "Call Laila":
            jump calllaila
            $ laila_affection += 1

    label callcass:
        "You call up the vampire you met last night, dialing the number she wrote on your arm."

        l neutral "Hello? Is this [player]?"

        mc "Yes, I was hoping we could meet up."

        l excited "I’m glad you’re being proactive! Let’s meet outside your building in 10, we’ll go for a little stroll"

        "With that, Laila hangs up and you head outside, waiting for her arrival."

        scene street

        "The night air is cool, and the streets are illuminated by the soft orange glow of sodium lamps. You’ve been on your street at night before, but never has it felt so alive."

        "You can hear the soft footsteps of stray cats on the prowl, see rodents scurry through shadows that would have previously been pitch black to you. It’s all a bit much to take in."

        show l neutral with dissolve

        "After a few minutes, Laila emerges from the gloom, stylish as the night before."

        l neutral "It’s good to see you again. How are you feeling?"

        menu:
            "Not too bad":
                jump inquiry4a
            "Really shitty":
                jump inquriy4b
    label inquiry4a:
        l smile "That’s really good to hear. I’m glad you’re feeling better."

        jump inquiry4common
    label inquiry4b:
        l away "Oh my goodness, I’m sorry about that. This whole process takes time."

        jump inquiry4common

    # FIND OUT HOW TO CYCLE THROUGH QUESTIONS!
    label inquiry4common:
        l neutral "I’m certain there’s a lot going through your mind. Let’s talk and walk."

        "With this declaration, Laila is off, strolling at a brisk pace down the street and towards the woods. You have no choice but to run after her. You get the sense she’s used to giving orders."

        l neutral "So, I gave you some of the basics last night, but I figured we ought to test out some of your new abilities in the woods. It’s quiet, and no one will get upset if you accidentally destroy something."

        "You begin to laugh at her last remark, but a steely look from Laila indicates she’s being quite serious. Now walking beside her, you figure it could be a good time to ask some questions about her."

        menu:
            "Are you from around here?":
                jump inquiry5a
            "How long have you been a vampire?"
                jump inquiry5b
            "Is the vampire-lady look intentional?"
                jump iqnury5c
            "Are you single?"
                jump inquiry5d
            "Remain silent"
                jump inquiry5e


    return
