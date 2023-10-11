# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define mc = Character("[player]", color="#dead71", image="mc")
define l = Character("Laila", color="#b55151", image="l")
define c = Character("Cassandra", color="#5ba84c", image="c")
define a = Character("Anne", color="#b55151", image="a")
define h = Character("Han", color="#b55151", image="h")
# define u = Character("Unknown", color="#b55151")

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


#---CG---

image cass cg 1 = "/cg/cass cg 1.png"

image laila cg 1 = "/cg/laila cg 1.png"

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

# side image code shit

init python:
    config.side_image_tag = "mc"
    config.default_show_empty_window = True
    config.nvl_paged_rollback = True
    config.window_hide_transition = dissolve
    config.window_show_transition = dissolve
    style.nvl_window.xpadding = 55
    style.nvl_window.ypadding = 55
    style.nvl_vbox.box_spacing = 20
    config.side_image_only_not_showing = True
    config.side_image_same_transform = None
    renpy.save_persistent()

transform change_transform(old, new):
    contains:
        old
        alpha 1.0 xalign 0.0 yalign 1.0
        linear 0.5 alpha 0.0 xalign 0.0 yalign 1.0
    contains:
        new
        alpha 0.0 xalign 0.0 yalign 1.0
        linear 0.5 alpha 1.0 xalign 0.0 yalign 1.0

define config.side_image_change_transform = change_transform


init:
    default persistent_ending = 0
    $ menu_variable = 0
    $ laila_affection = 0
    $ cass_affection = 0

    $ cass_kiss = False
    $ casspetname = "[player]"
    $ evil_cass = False
    $ cass_vamp = False
    $ cass_human = False

    $ anne_dead = False
    $ han_kill = False

    #questions for laila
    default q1 = False
    default q2 = False
    default q3 = False
    default q4 = False

    #questions about laila
    default lq1 = False
    default lq2 = False
    default lq3 = False
    default lq4 = False

    #anne fight chapter 4
    default a1 = False
    default a2 = False

label start:

    label chapter1:
        # Tense Music
        scene apartment

        play music "Ominous Forest.mp3" fadein 1 fadeout 1

        "You're not sure why, but things feel different today. Today. Is it still even today?"

        "You sit up from your bed and look behind you, and although your drapes are drawn tight you can tell it's dark out. Did you… did you sleep for a whole day?"

        "You try to remember what happened last night. There was that party out in the woods. And that strange woman and- was there a bite?"

        "You raise your hand to your neck and, sure enough, you feel two small indents, as if someone bit you."

        "You stand from your bed and all at once everything hurts."

        "Every muscle screams out, demanding you lay back down. Your vision swims and you drop to your knees. You realize now that your mouth is so dry."

        "You stagger out of your bedroom and make it no further than your couch before you collapse, the exhaustion taking too much of a toll on you."

        "You feel a pulsing headache, your body sore as it has ever felt."

        "You want to lie down forever but you hear a worried voice."

        menu:
            "Wake up":
                "Your eyes open to the bright iridescent lights of your apartment. You feel hungover, but you don't remember drinking last night?"

                "Well, that's how it happens doesn't it? You drink so much you don't remember… And yet…"

                "Something seems off… But before you have time to think of what you hear an overjoyed shriek:"

                show c doubt with dissolve

                #MUSIC: cass romantic

                c "Oh my god! You're awake! I was so worried about you!"

                "Cassandra Kalluri. Of course she's here. She's always looking out for you."

                "You've been inseparable since middle school. It was hard to find queer friends in a small Southern town like ____ but when you do the bond is unbreakable."

                hide c with dissolve

                menu:
                    "Where am I?":

                        show c doubt with dissolve

                        c "Where are you? You're in your apartment! Are you ok? Oh my god, Oh my god, does it cause memory loss?"

                        c neutral "Quick, what's your name?"

                    "Who am I?":

                        show c doubt with dissolve

                        c "Oh god, please tell me you remember your own name!"

                        "Your name is.."

                    "Why am I?":

                        show c neutral with dissolve

                        c "Don't get philosophical on me! I'm worried about you, you lost a lot of blood!"

                        "A lot of blood? What the hell happened last night?"

                        "You feel dizzy and your mind feels clouded. You try to focus on a constant. Your name is…"

        label nameEntry:
            $ player = renpy.input("What is your name?", length = 12)
            $ player = player.strip()
            $ player = player.title()

            c "Ok, you remember your name is [player]. That's good."

            # Tense Music

            c "Look, you had an accident, there was blood everywhere…"

            c "I thought you were dead but your heart was still beating and you seemed fine, your wounds healed before we could call 911..."

            c "I took you home and now you're awake and then you asked… and now we're here."

            mc "Blood? What do you mean blood? I don't feel any blood.."

            "You notice a sharp pain in your neck."

            "You reach up to feel it, two holes that seem to have healed up. They feel like decade old scars, and yet you definitely have not had them before today."

            hide c with dissolve

            menu:
                "This can't be happening.":
                    pass
                "This is so cool!":
                    pass
                "I'm so confused…":
                    pass

        show c neutral with dissolve

        c "This is going to sound crazy but… I think you got bitten by a vampire."
        c "It matches most of the books i read, the skin tone fluctuation and the eyes shifting color and the  two holes in your neck… What do you see here?"

        "Cassandra shows you her phone camera, but you don't see yourself in it. Could she be right? Are you a.."

        hide c with dissolve

        menu:
            "Vampire":
                pass
            "Monster":
                pass
            "Creature of the Night":
                pass

        #MUSIC: Cass Romantic

        show c smile with dissolve

        c smile "Oh my GOD!!! You don't have a reflection! This is so cool! I wonder what powers you have! I wonder if you can fly…"

        "Cassandra has always been a supernatural nerd for as long as you've known her. Its always been endearing, but now her knowledge could be the difference between life and death."

        hide c with dissolve

        menu:
            "This is a lot… I don't know what to do.":
                show c doubt with dissolve
                c "Sorry, this must be really overwhelming for you. I should be more cognizant of that… "

                c smile "Look, we'll work through this together ok? Let's get to the bottom of this!"

            "A vampire huh? Sounds like a dream come true!":
                show c smile with dissolve
                c smile "I know right! Oh my god, there is so much to discover, I can't wait! I'm sure if you got bit, there must be more vampires out there!"

            "This may be fun for you, but my whole life has been upended!":
                show c doubt with dissolve
                c doubt "Sorry, this must be really overwhelming for you. I should be more cognizant of that… "

                c smile "Look, we'll work through this together ok? Let's get to the bottom of this!"

        "You try to get up, but your sore body makes you utter an involuntary grunt. You feel like you're having the worst hangover of all time."

        c doubt "Look, until we know how vampirism is, you need to stay here where it's safe. I'm gonna run to the library and get every book I can on vampires and be right back."

        c smile "We'll figure this out together!"

        hide c with easeoutleft

        "As Cass leaves, you look behind her, a thousand thoughts running through your head."

        "What have you become? Is it a blessing or a curse?"

        "And as that thought crosses your mind, you hear a rumble."

        "You feel a deep hunger. You turn so you can ransack your fridge, and eat…"

        menu:
            "7 packs of instant ramen":
                pass
            "A bag of frozen chicken tenders":
                pass
            "A loaf of bread and a packet of cheese":
                pass

        "And yet… even though your belly is full you still feel it… the hunger."

        "You step over to the sink, turning on the faucet and stick your head underneath to drink directly from the tap, eschewing a glass."

        "This, though, does not seem to help. If anything, it only makes your appetite worse."

        "You shuffle over to your fridge and take a look inside again."

        "There! You remember something about pickle juice being good for hangovers, perhaps this is just one really fucked up hang over."

        "You grab the jar of pickles and remove the lid with surprising ease, before taking a big gulp of the brine within. You desperately want Cass's vampire theory to be wrong."

        "While this does not help a great deal with your now-ravenous thirst, the salty liquid does put you in the mindset of something less than conventional."

        "You replace the pickle jar and search your fridge once more."

        "After a moment you find it: nestled into a corner is a cut of beef you bought earlier in the week, but never got around to grilling."

        "You're unsure of what has inspired you to do it, but you tear open the store packaging and slurp the juices that have collected in the styrofoam tray."

        "And this is what hits the spot. Your muscles relax and your head clears. It should have been disgusting, but somehow it was almost pleasant."

        "There is a sharp rap at your door."

    label door:

        menu:
            "Answer the door":
                pass
            "Ignore it":
                "The knocking continues, insistent."
                jump door

        "You rise and make your way over to your door. You open it, and peer out into the hallway beyond."

        # tense music, mayhaps

        show l neutral with dissolve

        "Standing in front of your door is a remarkably pale woman, dressed in black, her face partially obscured by a wide-brimmed hat."

        "From her wrist dangles a little black purse. She gives you a closed lip smile."

        "???" "May I come in?"

        "Your voice seems to escape you. There's something about this woman, her voice- deep and charming- that causes you to step aside, allowing her entry into your apartment."

        "The woman steps languidly into your apartment, and looks around slowly. Her gaze lingers on your still-open fridge and the tray of beef haphazardly left on the counter next to it."

        l neutral "I'm Laila. Laila Mosshart."

        "She turns to face you."

        l neutral "What's your name?"

        mc "I'm [player]."

        l neutral "Good, I have the right place. May I sit?"

        "Without waiting for your response, Laila takes a seat on your couch. You take a seat next to her."

        l neutral "Some of my peers have asked me to oversee your… integration into this new lifestyle."

        mc "What are you talking about?"

        l away "Do you not remember? Of course, some people don't remember."
        l "You were out, last night, at a party in the woods. One of my peers, apparently she got too excited and, well there's no other way to put it, she bit you."
        hide l with dissolve

        menu:
            "She BIT me?!?":
                show l away with dissolve
                l away "Yes, I know, it's a lot and she really was not supposed to, I understand your discomfort."

            "I vaguely remember this.":
                show l smile with dissolve
                l smile "Oh, that's good, I'm glad some of your memory is coming back."

        "Everything Laila's said thus far seems to confirm Cass's theories. Still, though, you hold out hope this could be something else."

        l neutral "Anyway, myself or one of the others would have typically been with you much earlier, but one of your friends got there first and took you home. It was a whole thing."

        "Everything she's just said tracks with what c said. That's not great."

        "Laila pauses for a moment. She seems conflicted about what to say next."

        l away "Ugh, look I'm just going to come out and say it, and I hate having to be the one to do this, but you're a vampire now."
        hide l with dissolve

        menu:
            "You've got to be kidding.":
                show l away with dissolve
                l away "I really wish I was. Quite frankly it sucks to have to do this."

            "A vampire? That's badass!":
                show l neutral with dissolve
                l neutral "Well, I'm glad you're enthusiastic about it."

            "That's a lot.":
                show l away with dissolve
                l away "I know how you feel. It takes a while to process."

        l neutral "Perhaps you've already guessed, but I am also a vampire. I know, big surprise, right?"

        "Laila delivers this revelation in a very deadpan, unenthused manner. She sighs."

        l neutral "Our community of vamps here generally tends to look out for each other, and I'm supposed to guide you through the basics."

        l neutral "There's not a whole lot of time before the sun comes up, so I'll give you the basics. The sun will hurt and potentially kill you. You can get by on any blood, but human blood is most nutritious."

        "She pauses in thought for a moment."

        l neutral "You don't need to be invited in, garlic and holy water are chill, but stakes through the heart are not."

        l "That's the big things for right now. I'll be back to check on you sometime tomorrow night, but if you need me to come by sooner, just give me a ring."

        "Laila pulls a pen out of her purse, before grabbing your arm and scrawling her phone number across it."

        "She stands and makes her way towards the door before stopping suddenly, and turning to face you."

        l neutral "Ah, you should probably take this."

        "She reaches into her purse once again and tosses a little vial your way, which you catch with reflexes that befit your new identity."

        l excited "That's human blood, ethically sourced, I promise. It should be enough to get you through the next 24 hours. Remember, if you need anything, call."

        "The vampire gives you an actual smile this time, revealing her pointed incisors. With a wink, she turns and departs into the night."

        hide l with dissolve

        "Wow, that was a lot. You stare at the little glass vial in your hands, contemplating its contents."


##---CHAPTER 2---

    label chapter2:
        scene apartment with fade

        "You blearily open your eyes. Is it morning already? No, not morning, evening. It's going to take some getting used to this whole nocturnal thing."

        "The headache you had last night is not quite so bad now. And as you rise from your bed, you find your muscles are far less sore than they were before."

        "You run your tongue over your teeth. It seems overnight your new incisors have come in, sharp. You dread to think of what they're meant to be used for."

        "You put on some fresh clothes and make your way out of your bedroom and over to the couch. What to do now?"

        "You think on the two women who visited you last night- your old friend Cassandra, and the mysterious vampire Laila."

        "You have no doubt you'll see both of them tonight. That said, it might be best to call one of them now, whoever you feel you should speak with most."

        menu:
            "Call Cassandra":
                jump callCass
                $ cass_affection += 1
            "Call Laila":
                jump callLaila
                $ laila_affection += 1

    label callCass:
        # Romantic Music

        "You pick up and Cass starts excitedly talking."

        show c smile with dissolve

        c "Quick [player]! I found something really cool! Meet me in the woods near the old church!"

        c doubt "Wait, I think I'm losing service. See you there!"

        hide c with dissolve

        "Cassandra hangs up."

        "You wonder what she has planned…"

        scene forest with fade

        "You walk through the woods to the location Cassandra sent you. The woods used to feel scary at night, but now it seems… different."

        "It's as if everything seems brighter, and the unfamiliar has become almost cozy, or warm, or something."

        "The ick you used to feel from the bugs and the humid night air seems gone now."

        "It's strange, you expected vampirism to be this big unnatural thing but you feel more at one with the world than you ever have before."

        "You finally see Cassandra. The moonlight shines on her smiling face. Her smile is infectious."

        "On even your darkest days, seeing her overjoyed smile when geeking out over a fantasy novel or having a delicious meal or talking about some joke she saw online, made everything feel better."

        "It seems like recently, her smiles have been getting fewer and farther between, with the way the world has been."

        "It's nice to see her like this again."

        c "[player], hey! What are you thinking about? You seem lost in thought!"

        "Crap, you can't let her know you've been thinking about her smile! That's a weird thing to say!"

        "Quick, think of something else!"

        #CHANGE: Cass literally has no expressions here what the fuck

        menu:
            "Just how being a vampire feels so… different..":
                show c wink with dissolve
                c "Hmm interesting. Tell me how so?"

                "You tell Cass about your connection with the woods and the environment, as well as your enhanced eyesight"

                show c neutral
                c "That's so cool! I've been reading really conflicted narratives about vampires, but that seems to track the most with.."

            "I'm excited to get started!":
                pass

            "I was just thinking about how much I like seeing your smile!":
                "Why did you say that! It's like it spilled out of you. You hope Cassandra doesn't see your blush…"

                $ cass_affection += 1

                show c wink with dissolve
                c "Yeah, I'm just really excited about all this! Who would have thought my best friend would be a vampire! It's like I'm in a book!"

                show c neutral
                c "I know this is real, but things have been… too real recently. With the stuff with my family, and the laws being passed and the climate… It's nice to have something else to work on"

                c "Anyway, check this out!"

        "Cassandra pulls out a heavy book. The title is in English, but it is so frayed with age you can barely make it out. You think it says.."

        c smile "Bran Velcant's Journal. It's this autobiography from an old vampire, i've only been able to read the first half, but…"

        c smile "I have a feeling that it matches up with what you were describing as your symptoms!"

        c smile "And it has so much fascinating lore about how vampires used to live, the little pocket societies they made, what they wore, how they traveled…"
        hide c with dissolve

        menu:
            "(Say nothing.)":
                $ cass_affection += 1
                show c smile with dissolve

                c smile "and there's this kinda interesting romance he's having, like a kinda love triangle with these two other guys, and normally i'm not a fan of them but this one is really gripping!"

                c smile "and there's this brother character and they have this antagonistic relationship but it seems like he has this deep care in his heart for him, and…"

                c doubt "wait, I've been ranting, haven't I? I'm sorry, you know how I am with books…"

                menu:
                    "You're good!":
                        $ cass_affection += 1
                        pass
                    "I'm genuinely interested! The book seems cool":
                        $ cass_affection += 2
                        pass
                    "Let's get to training!":
                        pass

            "Cool, but let's get to the training!":
                show c doubt with dissolve
                pass

            "Dooon't Carree":
                $ cass_affection -= 2
                show c doubt with dissolve

                c doubt "Oh… i'm sorry."
                "Cass looks really dejected."
                c doubt "Let's just get to the training."


        c "Ok, so the powers the book mentions are hypnosis, bat transformation, and flight."

        c "Hypnosis is something Bran Velcant mentions a lot, but i'm not exactly sure what it entails or how to do it. He says something about looking people in the eye, so maybe try that on me?"

        c "Don't make me do anything weird, just test it out ok? I trust you"

        "You do as she says and stare into her eyes. There's something so reassuring about those big purple eyes of hers."

        "They remind you of fun talks after classes and giggles after watching a tv show."

        "You try to concentrate, thinking of something to hypnotize her with.."
        hide c with dissolve

        menu:
            "Do jumping jacks!":
                pass
            "Punch yourself in the face!":
                $ cass_affection -= 1
            "Take a nap!":
                pass

        show c doubt with dissolve
        c "Well, that didn't work… let's get back to that."

        c "I'm sure that we can figure more stuff out about hypnosis later. Next up is bat transformation. Velcant said he would visualize himself as a bat and it would just happen!"

        "You give it a try, and as if slipping into a slumber you shrink. Your arms grow skinnier and turn into wings. You feel your clothes slip away around you as you fly out of them. You…"
        hide c with dissolve

        menu:
            "Fly around for a bit":
                "You feel a wonderful breeze flow through you as you zoom through the forest. You feel so at peace."
                "As you fly back to Cassandra you are shocked by how big she is compared to you. You go back into your clothes and visualize yourself as a human again."

            "Go back into your clothes and turn back":
                pass

        show c wink with dissolve
        c "Wow. That's so cool! I'm gonna be real, I didn't expect you to get that first try. How do you feel?"
        hide c with dissolve

        menu:
            "I feel great!":
                pass
            "I feel nauseous…":
                pass
            "I feel nothing.":
                pass

        show c neutral with dissolve
        c "Ok, the only other thing I think you should try is floating. I was thinking you could jump off of that short tree and see if you can stay in the air! Don't worry, I'll be there to catch you."
        hide c with dissolve

        menu:
            "What? I'm not doing that!":
                pass
            "I got this, let's do it!":
                pass

        c "I'll be right below you, you'll be fine!"

        "You climb up the tree, breathing heavily."
        "You try as hard as you can to visualize yourself floating, and gravity not affecting you."
        "You jump and…"
        "It doesn't work. You crash into Cassandra and both fall into the ground."

        scene cass cg 1 with fade

        $ persistent.cass1 = True

        "You roll around for a bit before you open your eyes and see that you are on top of Cassandra in the grass."
        "You've known Cassandra for a long time but you've never been this close physically. You feel her breathing push against you."
        "You see the purple eyes you were staring at earlier, the smile you were thinking about earlier, and you are overwhelmed with emotion."
        "You can't tell if it's human or vampire, or both? But you feel a strange compulsion to…"

        menu:
            "Lean in for a kiss.":
                "You lean in, anxious but excited. Cassandra purses her lips and you slowly move closer together…"
                $ cass_kiss = True
                "But Cass pulls away."
                c "I… I'm sorry. I need to go back home, it's getting late."
                scene forest with fade
                "You both get up, and you give each other a hug goodbye before heading home. As you walk back you run the situation in your head again and again."
                "Do you have feelings for Cassandra? And does she have feelings for you?"
                "The almost kiss pounded in your brain until you willed it to stop. As you arrived home, you lay down in bed, a million thoughts in your mind."

            "Lean in for a bite.":
                "You lean in towards Cassandra's neck, as a strange bloodlust comes over you."
                "You open your mouth and you feel two fangs you did not notice before."
                "You feel a stange, intoxicating fear from Cassandra. The urge to bite consumes you, but you restrain yourself as best you can, jumping off of her."
                scene forest with fade

                menu:
                    "I'm sorry, I don't know what came over me.":
                        pass

                    "(Stay silent.)":
                        pass

                    "Well… that just happened…":
                        pass

                c "Woah… I… I'm sorry. I need to go back home, it's getting late."
                "She runs off. You want to run after her, to assure her than everything is ok, that your not a monster."
                "Is that really why you want to chase after her? Or is it the hunt? The desire to chase prey…"
                "You run back home, a million thoughts in your mind, and a pounding hunger tormenting you."

        jump chapter3


        label callLaila:
            # neutral music

            "You call up the vampire you met last night, dialing the number she wrote on your arm."

            show l neutral with dissolve

            l neutral "Hello? Is this [player]?"

            mc "Yes, I was hoping we could meet up."

            l excited "I'm glad you're being proactive! Let's meet outside your building in 10, we'll go for a little stroll."

            "With that, Laila hangs up and you head outside, waiting for her arrival."

            scene street with fade

            "The night air is cool, and the streets are illuminated by the soft orange glow of sodium lamps. You've been on your street at night before, but never has it felt so alive."

            "You can hear the soft footsteps of stray cats on the prowl, see rodents scurry through shadows that would have previously been pitch black to you. It's all a bit much to take in."

            show l neutral with dissolve

            "After a few minutes, Laila emerges from the gloom, stylish as the night before."

            l neutral "It's good to see you again. How are you feeling?"

            hide l with dissolve

            menu:
                "Not too bad.":
                    show l smile with dissolve
                    l smile "That's really good to hear. I'm glad you're feeling better."

                "Really shitty.":
                    show l away with dissolve
                    l away "Oh my goodness, I'm sorry about that. This whole process takes time."

        l neutral "I'm certain there's a lot going through your mind. Let's talk and walk."

        "With this declaration, Laila is off, strolling at a brisk pace down the street and towards the woods. You have no choice but to run after her. You get the sense she's used to giving orders."

        l neutral "So, I gave you some of the basics last night, but I figured we ought to test out some of your new abilities in the woods. It's quiet, and no one will get upset if you accidentally destroy something."

        "You begin to laugh at her last remark, but a steely look from Laila indicates she's being quite serious. Now walking beside her, you figure it could be a good time to ask some questions about her."
        hide l with dissolve

    label laila_questions:

        menu:
            "Are you from around here?" if not q1:
                show l neutral with dissolve
                l neutral "No, I'm not. Spent my youth out in New Mexico, but I've lived all over the country. This place is peaceful though, and that's what I've been looking for."
                hide l with dissolve

                $ q1 = True
                jump laila_questions

            "How long have you been a vampire?" if not q2:
                show l neutral with dissolve
                l neutral "I've been a vampire for about a decade. That would make me around 35 now? After the first couple years, keeping track of time doesn't feel quite so important."
                hide l with dissolve

                $ q2 = True
                jump laila_questions

            "Is the vampire-lady look intentional?" if not q3:
                show l angry with dissolve
                l angry "Intentional in that it is my chosen style, yes. I dressed like this before I was turned. I'm not going to buy a whole new wardrobe just because I'm a cliche now."
                hide l with dissolve

                $ q3 = True
                jump laila_questions

            "Are you single?" if not q4:
                show l smile with dissolve
                l smile "My, that's forward of you. I hope you aren't getting ideas in your head."

                "With this, she gives you a wry smile."

                l away "But to answer your question, yes. My girlfriend and I broke up a number of years ago. I do not view vampirism as a gift with no downsides, and she does."
                hide l with dissolve

                $ q4 = True
                jump laila_questions

            "Remain silent":
                "You walk beside Laila in silence now, making your way ever closer to the woods."

        scene forest with fade

        "Now you and Laila are into the woods, the darkness not quite as menacing as it was before you turned."

        "You are acutely aware of the cause of every rustle in the bushes, every distant snap of a twig- the forest is abound with creatures of the night."

        "Fittingly, that label includes you now."

        show l neutral with dissolve

        l neutral "You've probably already felt it, but your senses should be improved. You're an apex predator now."

        "After another minute or so of walking, Laila halts in a small clearing, and turns to face you."

        l neutral "Dodge."

        hide l with dissolve

        # exciting music

        menu:
            "What?":
                "As soon as the word leaves your mouth, Laila swings her arm out in a karate chop to your side. The blow strikes with surprising force, leaving you coughing."

                show l neutral with dissolve
                l neutral "Let's try that one more time. Dodge!"

                "This time you're ready for Laila's strike, leaping backwards and out of her reach with a speed you didn't know you had."

            "Tense up.":
                "When Laila swings her arm out to karate chop you, you're ready. You leap backwards and out of her reach with a speed you didn't know you had."

                "Laila gives you a nod, impressed."
                show l smile with dissolve

        l smile "As you can see, one of the pluses of our… condition is enhanced speed and agility. Strength, too."

        "Laila steps to the edge of the clearing and demonstrates this last remark, delivering a roundhouse kick that obliterates a small tree. She steps back, the motion effortless."

        l neutral "Now you try."
        hide l with dissolve

        menu:
            "Go full force.":
                "You try your best to deliver a fearsome kick to a venerable oak."
                "Unfortunately, you kick with far too much force and lose your balance before you even make contact with the tree, and start to fall."

                # romantic music

                "You don't hit the ground though. Laila has in an instant dashed across the clearing and caught you."

                "Your face is mere inches away from hers, gazing into her dark eyes. You look away, embarrassed, rushing to stand up. Laila chuckles."

                show l smile with dissolve

                l smile "It's alright, these kinds of things take practice."

            "Keep things simple.":
                "You take aim at a moderately sized tree, making sure to mimic the move you saw Laila perform."

                "With a twirl you deliver a blow to the tree, which cracks and collapses into the underbrush."

                "Laila approaches while giving you a polite golf clap."

                show l excited with dissolve

                l excited "Very good dear, you show some promise."


        "Laila pulls her phone out and glances at the time."

        l neutral "Hm, this has gone faster than I expected. I have to update the others about your progress before the night ends."

        mc "The others?"

        l neutral "Yes, the other vampires in town. I can take you to meet them tomorrow night. But you should be heading home now. We can do bat transformations another time."

        mc "Bat transformations?!"

        l angry "Yes, we can turn into bats. Quite frankly, I find it a loathsome experience. Bats smell horrible, and I'm quite content as I am."

        hide l with dissolve

        menu:
            "But becoming a bat sounds really cool!":
                $ laila_affection -= 1
                "Laila furrows her brow at your remark."

                show l angry with dissolve
                l angry "Yes, it is interesting the first couple of times you try it, but I can assure you becoming a winged rodent does not make for a good time."

            "Well that's good, I like you just the way you are.":
                $ laila_affection += 1
                "Laila bows her head demurely at your remark."

                show l smile with dissolve
                l smile "Please, [player], while your words flatter me, I don't think you quite understand me enough yet. Nonetheless, I appreciate it."

            "A new trial for another time, then.":
                "Laila nods at your remark."

                show l neutral with dissolve
                l neutral "Indeed. You've done good work this evening, and I look forward to more training with you in the future. Even if it means becoming a bat."


        l smile "Anyway, I'll let you get home, and I will see you tomorrow evening. And before I go, here."

        "With that, she tosses you another small vial of blood, as she did the night before. She gives you another closed lip smile, and darts off deeper into the woods with supernatural speed."

        scene street with fade

        "As you make your way out of the forest and back to your apartment building, you find Cass waiting at your front door."

        # Romantic Music

        show c smile with dissolve

        c smile "Hey! I tried calling you earlier and you didn't pick up so i decided to see if you were home cause I just hit a jackpot, research wise!"

        c confident "Check this out!"

        "Cassandra pulls out a heavy book. The title is in English, but it is so frayed with age you can barely make it out. You think it says.."

        c smile "Bran Velcant's Journal. It's this autobiography from an old vampire, i've only been able to read the first half, but…"

        c confident "I have a feeling that it matches up with what you were describing as your symptoms!"

        c smile "And it has so much fascinating lore about how vampires used to live, the little pocket societies they made, what they wore, how they traveled…"
        hide c with dissolve

        menu:
            "(Say nothing.)":
                show c smile with dissolve
                c smile "and there's this kinda interesting romance he's having, like a kinda love triangle with these two other guys, and normally i'm not a fan of them but this one is really gripping!"

                c "and there's this brother character and they have this antagonistic relationship but it seems like he has this deep care in his heart for him, and…"

                c doubt "wait, I've been ranting, haven't I? I'm sorry, you know how I am with books…"

                mc "You're good!"

                mc "I'm genuinely interested! The book seems cool!"

                mc "What does this mean for me?"

            "Cool, but what does this mean for me?":
                show c neutral with dissolve
                pass

            "Dooon't Carree":
                $ cas_affection -=2
                show c doubt with dissolve
                c doubt "Oh… i'm sorry."

                "Cassandra looks really dejected."

                c doubt "Look, basically what this means is I think I know what your powers are."

        c neutral "Bran Velcant so far has used three powers: Hypnosis, morphing into a bat, and floating."

        c smile "it's getting late, so we don't have time to test them out, but I thought you should know!"

        c smile"I'm gonna read the rest of this soon, and we'll get all the answers you need!"

        "As Cass leaves, you lie down, a thousand thoughts pulsing through your head."

        "What did Laila call you? An Apex Predator? Was that what you were becoming?"

        "And Cassandra's book… You wonder if this Velcant person felt the same way you do now, all those years ago."

        "You return to your apartment and drift into a slumber, wondering what new adventures might arise tomorrow."

    jump chapter3


#---CHAPTER 3---

    label chapter3:
        scene apartment with fade
        # Neutral Music
        "You awaken this evening feeling more like yourself than you did the last couple nights."
        "Well, still not quite yourself, but not as much pain as before."
        "As you rise from your bed, you sense something different in the air. There's tension, with a palpability to it."
        "You're not sure what, but something big is going down tonight. There's weight and finality in the actions you take this evening."
        "As you make your way into the living room, you notice a piece of paper has been slipped under your door."
        "You decide to investigate, and are perhaps unsurprised to find it is a letter from Laila."
        "Note" "[player], tonight, midnight. We'll be in a section of the woods we call the Blood Bank. You can meet the others."
        "Note" "Just head straight into the woods from your street. Keep walking until you start to hear the revels."
        "Note" "-Laila"

        "You glance at the clock on your microwave. It's- already eleven fifteen!?"
        "You really need to set an alarm going forward."
        "You hurriedly throw on some fresh clothes, and make your way out into the street."

        scene street with fade
        "You suspect Cass might be interested in joining you on this excursion."
        "You text Cassandra to meet you  and wait outside of her apartment."
        "A few minutes later Cass rushes out."

        show c smile with dissolve
        c smile "A Vampire Party! Oh my god!"
        c "It's like everything I dreamed of!"
        c "I put on my most emo clothes, do you think I'll fit in?"
        "You take a good long look at Cassandra's bright pink jacket and skirt."
        mc "I'm sure you'll be fine."
        "You walk into the woods, looking for the blood bank."
        "You wish Laila had written coordinates or something, cause you were deeply lost."

        c neutral "Maybe there's a vampire  thing that you can do to find it?"
        "You close your eyes and try to sense the forest as you walk."

        # Exciting Music, maybe even party music?
        "Finally, just on the edge of hearing, you detect the sound of laughter and mirth."
        mc "I think we've found it."

        "Cass gives you an excited smile but remains quiet as you move ever closer to the ongoing party."

        scene hideout with fade
        "After several more minutes of walking, you break through the trees into a massive clearing."
        "Fairy lights are strung across the clearing, which is decorated with picnic tables and populated by a couple dozen people who all look like they're having a very good time. Near the center of the clearing is a makeshift bar."

        show l excited with dissolve
        "As soon as you step into the clearing, Laila is at your side, appearing in what you are learning is typical vampiric speed."
        l excited "Hey, there [player], great to see you!"
        l neutral  "But who's this?"
        "There is deep concern in Laila's voice as she stares worriedly at Cass."

        show l at right with ease
        show c neutral at left with dissolve
        c "Hi, I'm [player]'s friend Cassandra!"
        l away "Yes, I gathered that much, but why are you here? You're not, you know-"
        "At this, Laila bares her fangs demonstratively."

        c "Well, I'm not, but me and [player] are close, and, well, I'm really into vampiric history and seeing a place like this…"
        c "It's just so cool! But if it's more of a vampires only thing I totally understand!"

        scene hideout with dissolve

        menu:
            "Defend Cass":
                $ cass_affection+=1
                "You push back against Laila, saying that Cass is your friend and deserves to be here."
                show c neutral with dissolve
                c "That's sweet [player], but i don't want to make anyone uncomfortable."
                c "I promise to be on my best behavior if you let me stay."
                hide c with dissolve

            "Support Laila":
                "You see the wisdom in what Laila is saying."
                mc "You know Cass, Laila might be right. It could be dangerous with all these vampires around, and you know, I don't really know any of them."


        "Laila looks taken aback at your remark."
        show l away with dissolve
        l away "Ah, you misunderstand, [player]. Your friend is not in any danger here. This is a gathering of… let's say civilized vamps. We can control ourselves. Mostly."
        l excited "Had we known a human guest was coming, we would have brought some non-blood based beverages."
        "Laila shows you and Cass over to the makeshift bar near the center of the clearing."
        "A rather portly vampire greets you in a deep jolly voice."
        "Shamus" "Hello there, you must be the new one. I'm Shamus, and this here is the Blood Bank."

        hide l with dissolve
        "The barkeep- Shamus- gestures at the bar."
        "Shamus" "We've got our own brewing operation here. We take blood- sourced from an actual blood bank, don't worry- and distill it in this here contraption."
        "He now indicates a small still sitting just behind the bar."
        "Shamus" "We call it ‘Bloodmoon Shine. First one's free."
        "At this, he passes you a red solo cup filled with a reddish liquid."
        "You take a hesitant sip and find you somewhat enjoy the surprisingly strong beverage."
        "You're a bit nervous too nervous to talk to anyone new just yet, so you hang by Laila and Cass."

        # Tense Music
        "The gentle sounds of the party are disrupted by a loud pop and the clearing is illuminated by a bright red glow. You look up and see a flare rising over the treeline."
        "All of the revelry stops and a hush falls over the gathered vampires."
        "Before anyone can comment, a flurry of nets are launched from beyond the clearing, ensnaring many of the partygoers, including Laila."
        "As she struggles to disentangle herself from the net, she pauses."

        show l angry with dissolve
        l angry "Is this garlic? Did someone really coat these nets in fucking garlic? My clothes are going to reek!"
        "Something whizzes past your head and you hear someone scream. You turn to see it's Shamus clawing at a large wooden spike that has lodged itself into their chest."
        "More and more of these stakes come flying out of the forest, so you grab Cass and drop to the ground to avoid getting hit. Laila, still in the net, follows suit."
        "The night air is filled with screams and shouts now, as more of your vampire brethren are impacted by this assault. "
        "Cassandra rushes to cut Laila and the other vampires out of the net. The panic sets in, but you need to act now."

        menu:
            "Guide Laila and Cass  to scurry under a picnic table":
                "As you hide under the table, you hear a sharp whirring sound coming from behind the bar."

            "Scamper into a bush":
                "You all hide in the bush near the bar, but you hear a sharp whirring sound coming from behind the bar."
                "Remembering the illicit brewing that the bartender mentioned earlier, you rush to hide beneath the picnic table away from the bar."

            "Play dead":
                "You all play dead, which will surely be a winning strategy against these attackers."
                "Things seem to quiet down and you breathe a sigh of relief."
                "However, your relief is cut short by a sharp whirring sound coming from behind the bar."
                "Remembering the illicit brewing that the bartender mentioned earlier, you rush to hide beneath the picnic table away from the bar."

        "The Blood MoonShine still quakes for a moment before exploding, showering flaming alcohol everywhere."
        "The smell is pungent and the heat is unbearable."
        "You hold Cassandra and Laila close to make sure the table shields everyone from the raining flame."
        "When the rain stops, you risk a glance upward and see two figures enter the burning clearing, shrouded by smoke."
        "The screaming has mostly died down now, as the other vampires are either dead or have fled off into the woods. It's just you, Laila, and Cass now, cowering beneath the table."
        "As you try to figure out next steps, you hear one of the figures start to speak."
        "???" "Well Han, we did it. We've found the vampire cell and routed them. All according to my plan!"

        "Han?" "Your \"plan\", Anne, was firing a hundred stakes randomly at this clearing. Don't pretend like the distillery blowing up was your idea."
        "Anne?" "And it worked out in our favor. Shock and awe, that's how we did it. Imagine how proud mummy and daddy would be of me in this moment."
        "Han?" "I can imagine dad telling us he would have done it better back in the day with a half smile right now. Memories."
        "Anne?" "Ugh, can't you see we've eclipsed them? We're forging a legacy that will outlast theirs!"
        "The smoke clears enough that you can get a good look at the two conversants- Anne and Han, you gather their names are."

        show a neutral at left
        show h neutral at right
        with dissolve

        "The pair dress in matching vests, although Anne is markedly more stylish than Han."
        a neutral "And the Velsing name will go down in history as that of the greatest vampire hunters in the world!"

        hide a
        hide h
        with dissolve

        show c doubt with dissolve
        c "Velsing???!"
        "Laila lets out a groan."
        show c at left with ease
        show l angry at right with dissolve

        l angry "Not these buffoons again."
        c smile "You know… the Velsings???"
        l angry "Unfortunately. These freaks inevitably come around to fuck up any nice vampire community I've managed to find. I thought we'd seen the last of them after the boat disaster in Grand Rapids, but I guess it's hard to kill stupid."
        #CHANGE: ask abt if this is supposed to be left in like this???

        c "They look… dated."
        l neutral "I know, the fashion is just insult to injury."

        menu:
            "I think it's kinda cool!":
                "Cass and Laila both look at you with thinly veiled disgust."
                show l angry at right
                show a neutral at left
                with dissolve
                l angry "You need some help."
                a neutral "Thanks for the compliment!"
                hide l with dissolve
                show a at center with ease

            "The Pony Express called, they want their uniforms back.":
                "Cass and Laila try to suppress giggles."
                show a frown with dissolve
                a frown "The Pony Express provided a valuable service, just as we do!"


            "You know, the rest of the outfit aside, I feel like that top would look good on me!":
                "Cass evaluates your current attire briefly."
                hide l with dissolve
                show c smile at right
                show h neutral at left
                with dissolve
                c "Yeah, I guess it could work."
                h "Not everyone can rock such stylish gear. Especially not a bloodsucker."
                hide c
                hide h
                with dissolve
                show a neutral at left with dissolve
                show h neutral at right with dissolve


        "You recoil in terror at the addressing of your remarks."
        a neutral "Oh yes little bat-spawn, we heard everything you and your compatriots were saying."
        "At this, the Velsings flip the picnic table over, exposing the three of you."
        "You find crossbows with stakes loaded in them leveled at your face."
        a angry "To think you could hide from us- what hubris! No one can hide from our incredible acumen and refined senses!"
        "As she boasts, Laila and Cassandra run away. You seize upon the opportunity and run as well."
        "Cassandra and Laila are splitting up in the woods. You  don't know who to chase after."
        "This is a matter of life and death."

        "You could follow Laila, further into the woods, or follow Cassandra, who's running back towards town."
        "It's possible you may never see the other one again."
        hide a with dissolve

        menu:
            "Follow Laila":
                "You know Cass will probably be fine- she's a regular human after all- and you feel a burgeoning connection with this vampire that's taken you under her wing."
                "You know in your heart this is the right decision."
                "You follow Laila into the night."
                jump laila_chapter4

            "Follow Cassandra":
                "Laila is far more experienced than you, you trust that she can take care of herself."
                "You run after Cass, unwilling to let your best friend get hurt."
                jump cass_chapter4

return
