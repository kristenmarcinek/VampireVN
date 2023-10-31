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
    $ menu_variable = 0
    $ laila_affection = 0
    $ cass_affection = 0

label start:

    label chapter1:
        # Tense Music
        scene apartment

        "You’re not sure why, but things feel different today. Today. Is it still even today?"

        "You sit up from your bed and look behind you, and although your drapes are drawn tight you can tell it’s dark out. Did you… did you sleep for a whole day?"
        
        "You try to remember what happened last night. There was that party out in the woods. And that strange woman and- was there a bite?"
        
        "You raise your hand to your neck and, sure enough, you feel two small indents, as if someone bit you."
        
        "You stand from your bed and all at once everything hurts. Every muscle screams out, demanding you lay back down. Your vision swims and you drop to your knees. You realize now that your mouth is so dry."
        
        "You stagger out of your bedroom and make it no further than your couch before you collapse, the exhaustion taking too much of a toll on you."
        
        "You feel a pulsing headache, your body sore as it has ever felt"
        
        "You want to lie down forever but you hear a worried voice"
        menu:
            "Wake up":
                jump c1a
        label c1a:
            "Your eyes open to the bright iridescent lights of your apartment. You feel hungover, but you don’t remember drinking last night?"
            
            "Well, that’s how it happens doesn’t it? You drink so much you don't remember… And yet…"
            
            "Something seems off… But before you have time to think of what you hear an overjoyed shriek:"
            
            show c doubt with dissolve

            # Romantic Music
            
            c doubt "Oh my god! You’re awake! I was so worried about you!"
            
            "Cassandra Kalluri. Of course she’s here. She’s always looking out for you."
            
            "You’ve been inseparable since middle school. It was hard to find queer friends in a small Southern town like this one, but when you do the bond is unbreakable."
            
            menu:
                "Where am I?":
                    jump c1b
                "Who am I?":
                    jump c1c
                "Why am I?":
                    jump c1d
        
        label c1b:
            c doubt "Where are you? You’re in your apartment! Are you ok? Oh my god, Oh my god, does it cause memory loss?"
            
            c neutral "Quick, what’s your name?"
            
            jump nameEntry
        
        label c1c:
            c doubt "Oh god, please tell me you remember your own name!"
            
            "My name is.."
            
            jump nameEntry
        
        label c1d:
            c neutral "Don’t get philosophical on me! I’m worried about you, you lost a lot of blood!"
            
            "A lot of blood? What the hell happened last night?"
            
            "You feel dizzy and your mind feels clouded. You try to focus on a constant. Your name is…"
            
            jump nameEntry
        
        label nameEntry:
            $ player = renpy.input("What is your name?", length = 12)
            $ player = player.strip()
            $ player = player.title()

            c "Ok, you remember your name is [player]. That’s good."
            
            # Tense Music
            
            c "Look, you had an accident, there was blood everywhere… I thought you were dead but your heart was still beating and you seemed fine, your wounds healed before we could call 911, I took you home and now you’re awake and then you asked… and now we’re here."
            
            "Blood? What do you mean blood? I don’t feel any blood.."(Single Choice)
            
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
            # Romantic Music
            
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
            c doubt "Sorry, this must be really overwhelming for you. I should be more cognizant of that… "
            
            c smile "Look, we’ll work through this together ok? Let’s get to the bottom of this!"
            
            jump c1i
        
        label c1h:
            c smile "I know right! Oh my god, there is so much to discover, I can’t wait! I’m sure if you got bit, there must be more vampires out there!"
        
            jump c1i 
        
        label c1i:
            "You try to get up, but your sore body makes you utter an involuntary grunt. You feel like you’re having the worst hangover of all time."
            
            c Doubt "Look, until we know how vampirism is, you need to stay here where it’s safe. I’m gonna run to the library and get every book I can on vampires and be right back."
            
            c smile "We’ll figure this out together!"
            
            "As Cass leaves, you look behind her, a thousand thoughts running through your head."
            
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
            
            menu:
                "Answer the door":
                    jump door1
                "Ignore it":
                    jump door2

        label door2:
            "The knocking continues, insistent."

            menu: 
                "Answer the door":
                    jump door1
                "Ignore it":
                    jump door2

        label door1:
            "You rise and make your way over to your door. You open it, and peer out into the hallway beyond."
            
            # tense music, mayhaps
            
            show l neutral with dissolve
            
            "Standing in front of your door is a remarkably pale woman, dressed in black, her face partially obscured by a wide-brimmed hat. From her wrist dangles a little black purse. She gives you a closed lip smile."
            
            u "May I come in?"
            
            "Your voice seems to escape you. There’s something about this woman, her voice- deep and charming- that causes you to step aside, allowing her entry into your apartment."
            
            "The woman steps languidly into your apartment, and looks around slowly. Her gaze lingers on your still-open fridge and the tray of beef haphazardly left on the counter next to it."
            
            l neutral "I’m Laila. Laila Mosshart."
            
            "She turns to face you."
            
            l neutral "What’s your name?"
            
            mc "I’m [player]."

            l neutral "Good, I have the right place. May I sit?"
            
            "Without waiting for your response, Laila takes a seat on your couch. You take a seat next to her."
            
            l neutral "Some of my peers have asked me to oversee your… integration into this new lifestyle."
            
            mc "What are you talking about?"

            l away "Do you not remember? Of course, some people don’t remember. You were out, last night, at a party in the woods. One of my peers, apparently she got too excited and, well there’s no other way to put it, she bit you."
            
            menu:
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
                "You’ve got to be kidding.":
                    jump inquiry3a
                "A vampire? That’s badass!":
                    jump inquiry3b
                "That’s a lot.":
                    jump inquiry3c

        label inquiry3a:
            l away "I really wish I was. Quite frankly it sucks to have to do this."
            
            jump inquiry3common

        label inquiry3b:
            l neutral "Well, I’m glad you’re enthusiastic about it."
            
            jump inquiry3common

        label inquiry3c:
            l away "I know how you feel. It takes a while to process."
            
            jump inquiry3common

        label inquiry3common:
            l neutral "Perhaps you’ve already guessed, but I am also a vampire. I know, big surprise, right?"
            
            "Laila delivers this revelation in a very deadpan, unenthused manner. She sighs."
            
            l neutral "Our community of vamps here generally tends to look out for each other, and I’m supposed to guide you through the basics."
            
            l neutral "There’s not a whole lot of time before the sun comes up, so I’ll give you the basics. The sun will hurt and potentially kill you. You can get by on any blood, but human blood is most nutritious."
            
            "She pauses in thought for a moment."
            
            l neutral "You don’t need to be invited in, garlic and holy water are chill, but stakes through the heart are not. That’s the big things for right now. I’ll be back to check on you sometime tomorrow night, but if you need me to come by sooner, just give me a ring."
            
            "Laila pulls a pen out of her purse, before grabbing your arm and scrawling her phone number across it."
            
            "She stands and makes her way towards the door before stopping suddenly, and turning to face you."
            
            l neutral "Ah, you should probably take this."
            
            "She reaches into her purse once again and tosses a little vial your way, which you catch with reflexes that befit your new identity."
            
            l excited "That’s human blood, ethically sourced, I promise. It should be enough to get you through the next 24 hours. Remember, if you need anything, call."
            
            "The vampire gives you an actual smile this time, revealing her pointed incisors. With a wink, she turns and departs into the night."
            
            Hide l with dissolve
            
            "Wow, that was a lot. You stare at the little glass vial in your hands, contemplating its contents."
    
    jump chapter2


    label chapter2:
        scene apartment
        
        "You blearily open your eyes. Is it morning already? No, not morning, evening. It’s going to take some getting used to this whole nocturnal thing."
        
        "The headache you had last night is not quite so bad now. And as you rise from your bed, you find your muscles are far less sore than they were before."
        
        "You run your tongue over your teeth. It seems overnight your new incisors have come in, sharp. You dread to think of what they’re meant to be used for."
        
        "You put on some fresh clothes and make your way out of your bedroom and over to the couch. What to do now?"
        
        "You think on the two women who visited you last night- your old friend Cassandra, and the mysterious vampire Laila. You have no doubt you’ll see both of them tonight. That said, it might be best to call one of them now, whoever you feel you should speak with most."
        
        menu:
            "Call Cassandra":
                jump callCass
                $ cass_affection += 1
            "Call Laila":
                jump callLaila
                $ laila_affection += 1

        label callLaila:
            # neutral music
            
            "You call up the vampire you met last night, dialing the number she wrote on your arm."
            
            l neutral "Hello? Is this [player]?"
            
            mc "Yes, I was hoping we could meet up."
            
            l excited "I’m glad you’re being proactive! Let’s meet outside your building in 10, we’ll go for a little stroll."
            
            "With that, Laila hangs up and you head outside, waiting for her arrival."
            
            scene street
            
            "The night air is cool, and the streets are illuminated by the soft orange glow of sodium lamps. You’ve been on your street at night before, but never has it felt so alive."
            
            "You can hear the soft footsteps of stray cats on the prowl, see rodents scurry through shadows that would have previously been pitch black to you. It’s all a bit much to take in."
            
            show l neutral with dissolve
            
            "After a few minutes, Laila emerges from the gloom, stylish as the night before."
            
            l neutral "It’s good to see you again. How are you feeling?"
            
            menu:
                "Not too bad.":
                    jump inquiry4a
                "Really shitty.":
                    jump inquiry4b

        label inquiry4a:
            l smile "That’s really good to hear. I’m glad you’re feeling better."
            
            jump inquiry4common

        label inquiry4b:
            l away "Oh my goodness, I’m sorry about that. This whole process takes time."
            
            jump inquiry4common

        label inquiry4common:
            l neutral "I’m certain there’s a lot going through your mind. Let’s talk and walk."
            
            "With this declaration, Laila is off, strolling at a brisk pace down the street and towards the woods. You have no choice but to run after her. You get the sense she’s used to giving orders."
            
            l neutral "So, I gave you some of the basics last night, but I figured we ought to test out some of your new abilities in the woods. It’s quiet, and no one will get upset if you accidentally destroy something."
            
            "You begin to laugh at her last remark, but a steely look from Laila indicates she’s being quite serious. Now walking beside her, you figure it could be a good time to ask some questions about her."
            
            menu:
                "Are you from around here?":
                    jump inquiry5a
                "How long have you been a vampire?":
                    jump inquiry5b
                "Is the vampire-lady look intentional?":
                    jump inquiry5c
                "Are you single?":
                    jump inquiry5d
                "Remain silent":
                    jump inquiry5e

        label inquiry5a:
            l neutral "No, I’m not. Spent my youth out in New Mexico, but I’ve lived all over the country. This place is peaceful though, and that’s what I’ve been looking for."

        label inquiry5b:
            l neutral "I’ve been a vampire for about a decade. That would make me around 35 now? After the first couple years, keeping track of time doesn’t feel quite so important."

        label inquiry5c:
            l angry "Intentional in that it is my chosen style, yes. I dressed like this before I was turned. I’m not going to buy a whole new wardrobe just because I’m a cliche now."

        label inquiry5d:
            l smile "My, that’s forward of you. I hope you aren’t getting ideas in your head."
            
            "With this, she gives you a wry smile."
            
            l away "But to answer your question, yes. My girlfriend and I broke up a number of years ago. I do not view vampirism as a gift with no downsides, and she does."
        
        # NOTE: Figure out how to code this so that the player can ask 4(?) questions before the next scene starts, unless they remain silent.

        label inquiry5e:
            "You walk beside Laila in silence now, making your way ever closer to the woods."

            jump inquiry5common

        label inquiry5common:
            scene forest
            
            "Now you and Laila are into the woods, the darkness not quite as menacing as it was before you turned. You are acutely aware of the cause of every rustle in the bushes, every distant snap of a twig- the forest is abound with creatures of the night."
            
            "Fittingly, that label includes you now."
            
            show l neutral with dissolve
            
            l neutral "You’ve probably already felt it, but your senses should be improved. You’re an apex predator now."
            
            "After another minute or so of walking, Laila halts in a small clearing, and turns to face you."
            
            l neutral "Dodge."
            
            # exciting music
            menu:
                "What?":
                    jump reaction1a
                "Tense up.":
                    jump reaction1b

        label reaction1a:
            "As soon as the word leaves your mouth, Laila swings her arm out in a karate chop to your side. The blow strikes with surprising force, leaving you coughing."
            
            l neutral "Let’s try that one more time. Dodge!"
            
            "This time you’re ready for Laila’s strike, leaping backwards and out of her reach with a speed you didn’t know you had."
            
            jump reaction1common

        label reaction1b:
            "When Laila swings her arm out to karate chop you, you’re ready. You leap backwards and out of her reach with a speed you didn’t know you had."
            
            "Laila gives you a nod, impressed."
            
            jump reaction1common

        label reaction1common:
            l smile "As you can see, one of the pluses of our… condition is enhanced speed and agility. Strength, too."
            
            "Laila steps to the edge of the clearing and demonstrates this last remark, delivering a roundhouse kick that obliterates a small tree. She steps back, the motion effortless."
            
            l neutral "Now you try."
            
            menu:
                "Go full force.":
                    jump reaction2a
                "Keep things simple.":
                    jump reaction2b

        label reaction2a:
            "You try your best to deliver a fearsome kick to a venerable oak. Unfortunately, you kick with far too much force and lose your balance before you even make contact with the tree, and start to fall."
            
            # romantic music
        
            "You don’t hit the ground though. Laila has in an instant dashed across the clearing and caught you."
        
            "Your face is mere inches away from hers, gazing into her dark eyes. You look away, embarrassed, rushing to stand up. Laila chuckles."
            
            l smile "It’s alright, these kinds of things take practice."
            
            jump reaction2common

        label reaction2b:
            "You take aim at a moderately sized tree, making sure to mimic the move you saw Laila perform."
            
            "With a twirl you deliver a blow to the tree, which cracks and collapses into the underbrush."
            
            "Laila approaches while giving you a polite golf clap."

            l excited "Very good dear, you show some promise."
            
            jump reaction2common

        label reaction2common:
            "Laila pulls her phone out and glances at the time."
            
            l neutral "Hm, this has gone faster than I expected. I have to update the others about your progress before the night ends."
            
            mc "The others?"
            
            l neutral "Yes, the other vampires in town. I can take you to meet them tomorrow night. But you should be heading home now. We can do bat transformations another time."
            
            mc "Bat transformations?!"
            
            l angry "Yes, we can turn into bats. Quite frankly, I find it a loathsome experience. Bats smell horrible, and I’m quite content as I am."
            
            menu:
                "But becoming a bat sounds really cool!":
                    jump reaction3a
                    $ laila_affection -= 1
                "Well that’s good, I like you just the way you are.":
                    jump reaction3b
                    $ laila_affection += 1
                "A new trial for another time, then.":
                    jump reaction3c

        label reaction3a:
            "Laila furrows her brow at your remark."
            
            l angry "Yes, it is interesting the first couple of times you try it, but I can assure you becoming a winged rodent does not make for a good time."
            
            jump reaction3common

        label reaction3b:
            "Laila bows her head demurely at your remark."
            
            l smile "Please, [player], while your words flatter me, I don’t think you quite understand me enough yet. Nonetheless, I appreciate it."
            
            jump reaction3common

        label reaction3c:
            "Laila nods at your remark."
            
            l neutral "Indeed. You’ve done good work this evening, and I look forward to more training with you in the future. Even if it means becoming a bat."
            
            jump reaction3common

        label reaction3common:
            l smile "Anyway, I’ll let you get home, and I will see you tomorrow evening. And before I go, here."
            
            "With that, she tosses you another small vial of blood, as she did the night before. She gives you another closed lip smile, and darts off deeper into the woods with supernatural speed."
            
            hide l with dissolve
            
            scene street
            
            "As you make your way out of the forest and back to your apartment building, you find Cass waiting at your front door."
            
            # Romantic Music
            
            c smile "Hey! I tried calling you earlier and you didn't pick up so I decided to see if you were home cause I just hit a jackpot, research wise!"
            
            c confident "Check this out!"
            
            "Cassandra pulls out a heavy book. The title is in English, but it is so frayed with age you can barely make it out. You think it says.."
            
            c smile "Bran Velcant’s Journal. It’s this autobiography from an old vampire, i’ve only been able to read the first half, but…"
            
            c confident "I have a feeling that it matches up with what you were describing as your symptoms!"
            
            c smile "And it has so much fascinating lore about how vampires used to live, the little pocket societies they made, what they wore, how they traveled…"
            
            menu:
                "(say nothing)":
                    jump to c2db
                "Cool, but what does this mean for me?":
                    jump to c2eb
                "Dooon’t Carree":
                    cass_affection -=2
                    jump to c2fb
    
        label c2db:
            c smile "and there’s this kinda interesting romance he’s having, like a kinda love triangle with these two other guys, and normally i’m not a fan of them but this one is really gripping!"
            
            c "and there’s this brother character and they have this antagonistic relationship but it seems like he has this deep care in his heart for him, and…"
            
            c doubt "wait, I’ve been ranting, haven’t I? I’m sorry, you know how I am with books…"
            
            mc "You’re good!"
            
            mc "I’m genuinely interested! The book seems cool!"
            
            mc "What does this mean for me?"
            
            jump to c2eb

        label c2fb:
            c doubt "Oh… i’m sorry."
            
            "Cassandra looks really dejected."
            
            c doubt "Look, basically what this means is I think I know what your powers are." 
            
            jump to c2eb
    
        label c2eb
            c "Bran Velcant so far has used three powers: Hypnosis, morphing into a bat, and floating." 
            
            c smile "it’s getting late, so we don’t have time to test them out, but I thought you should know!"
            
            c smile"I’m gonna read the rest of this soon, and we’ll get all the answers you need!"
            
            "As Cass leaves, you lie down, a thousand thoughts pulsing through your head."
            
            "What did Laila call you? An Apex Predator? Was that what you were becoming?"
            
            "And Cassandra’s book… You wonder if this Velcant person felt the same way you do now, all those years ago."
            
            "You return to your apartment and drift into a slumber, wondering what new adventures might arise tomorrow."
    
    jump chapter3

        label callCass:
            # Romantic Music
            
            "You pick up and Cass starts excitedly talking."
            
            show c smile with dissolve
            
            c "Quick [player]! I found something really cool! Meet me in the woods near the old church!"
            
            c doubt "Wait, I think I’m losing service. See you there!"
            
            hide c with dissolve
            
            "Cassandra hangs up"
            
            "You wonder what she has planned…"
            
            scene forest
            
            "You walk through the woods to the location Cassandra sent you. The woods used to feel scary at night, but now it seems… different"
            
            "It’s as if everything seems brighter, and the unfamiliar has become almost cozy, or warm, or something"
            
            "The ick you used to feel from the bugs and the humid night air seems gone now."
            
            "It’s strange, you expected vampirism to be this big unnatural thing but you feel more at one with the world than you ever have before."
            
            "You finally see Cassandra. The moonlight shines on her smiling face. Her smile is infectious."
            
            "On even your darkest days, seeing her overjoyed smile when geeking out over a fantasy novel or having a delicious meal or talking about some joke she saw online, made everything feel better."
            
            "It seems like recently, her smiles have been getting fewer and farther between, with the way the world has been."
            
            "It’s nice to see her like this again."
            
            c "[player], hey! What are you thinking about? You seem lost in thought!"
            
            "Crap, you can’t let her know you’ve been thinking about her smile! That's a weird thing to say!"
            
            "Quick, think of something else!"

            menu:
                "Just how being a vampire feels so… different..":
                    jump c2a
                "I’m excited to get started!":
                    jump c2b
                "I was just thinking about how much I like seeing your smile!":
                    jump c2c
        
        label c2a:
            c "Hmm interesting. Tell me how so?"
            
            "You tell Cass about your connection with the woods and the environment, as well as your enhanced eyesight"
            
            c "That’s so cool! I’ve been reading really conflicted narratives about vampires, but that seems to track the most with.."
            
            jump to c2b
        
        label c2c:
            "Why did you say that! It’s like it spilled out of you. You hope Cassandra doesn’t see your blush…"
            
            $ cass_affection += 1
            
            c "Yeah, I’m just really excited about all this! Who would have thought my best friend would be a vampire! It’s like I’m in a book!"
            
            c "I know this is real, but things have been… too real recently. With the stuff with my family, and the laws being passed and the climate… It’s nice to have something else to work on"
            
            c "Anyway, check this out!"
            
            jump to c2b
        
        label c2b:
            "Cassandra pulls out a heavy book. The title is in English, but it is so frayed with age you can barely make it out. You think it says.."
            
            c smile "Bran Velcant’s Journal. It’s this autobiography from an old vampire, i’ve only been able to read the first half, but…"
            
            c smile "I have a feeling that it matches up with what you were describing as your symptoms!"
            
            c smile "And it has so much fascinating lore about how vampires used to live, the little pocket societies they made, what they wore, how they traveled…"

            menu:
                "(say nothing)":
                    $ cass_affection += 1
                    jump to c2d
                "Cool, but let’s get to the training!":
                    jump to c2e
                "Dooon’t Carree":
                    $ cass_affection -= 2
                    jump to c2f
       
        label c2d:
            c smile "and there’s this kinda interesting romance he’s having, like a kinda love triangle with these two other guys, and normally i’m not a fan of them but this one is really gripping!"
            
            c smile "and there’s this brother character and they have this antagonistic relationship but it seems like he has this deep care in his heart for him, and…"
            
            c doubt "wait, I’ve been ranting, haven’t I? I’m sorry, you know how I am with books…"
            
            menu:
                "You’re good!":
                    $ cass_affection += 1
                    jump to c2e
                "I’m genuinely interested! The book seems cool":
                    $ cass_affection += 2
                    jump to c2e
                "Let's get to training!":
                    jump to c2e
        
        label c2f
            c doubt "Oh… i’m sorry."
            "Cass looks really dejected."
            c doubt "Let’s just get to the training."
            jump to c2e
        
        label c2e:
            c "Ok, so the powers the book mentions are hypnosis, bat transformation, and flight."  
            
            c "Hypnosis is something Bran Velcant mentions a lot, but i’m not exactly sure what it entails or how to do it. He says something about looking people in the eye, so maybe try that on me?"
        
            c "Don’t make me do anything weird, just test it out ok? I trust you"
        
            "You do as she says and stare into her eyes. There's something so reassuring about those big purple eyes of hers."
        
            "They remind you of fun talks after classes and giggles after watching a tv show."
            
            "You try to concentrate, thinking of something to hypnotize her with.."
        
            menu:
                "Do jumping jacks!":
                    pass
                "Punch yourself in the face!":
                    $ cass_affection -= 1
                "Take a nap!":
                    pass

            c "Well, that didn’t work… let’s get back to that. I’m sure that we can figure more stuff out about hypnosis later. Next up is bat transformation. Velcant said he would visualize himself as a bat and it would just happen!"
            
            "You give it a try, and as if slipping into a slumber you shrink. Your arms grow skinnier and turn into wings. You feel your clothes slip away around you as you fly out of them. You…"
            
            menu:
                "Fly around for a bit":
                    "You feel a wonderful breeze flow through you as you zoom through the forest. You feel so at peace. As you fly back to Cassandra you are shocked by how big she is compared to you. You go back into your clothes and visualize yourself as a human again."
                "Go back into your clothes and turn back":
                    pass
        
            c "Wow. That’s so cool! I’m gonna be real, I didn't expect you to get that first try. How do you feel?"

            menu:
                "I feel great!":
                    pass
                "I feel nauseous…":
                    pass
                "I feel nothing.":
                    pass

            c "Ok, the only other thing I think you should try is floating. I was thinking you could jump off of that short tree and see if you can stay in the air! Don’t worry, I’ll be there to catch you."
            
            menu:
                "What? I’m not doing that!":
                    pass
                "I got this, let’s do it!":
                    pass

return

        c "I’ll be right below you, you’ll be fine!"
        "You climb up the tree, breathing heavily."
        "You try as hard as you can to visualize yourself floating, and gravity not affecting you. 
        "You jump and…"
        "It doesn’t work. You crash into Cassandra and both fall into the ground. "
        "You roll around for a bit before you open your eyes and see that you are on top of Cassandra in the grass."
        You’ve known Cassandra for a long time but you’ve never been this close physically. You feel her breathing push against you."
        "You see the purple eyes you were staring at earlier, the smile you were thinking about earlier, and you are overwhelmed with emotion.
        "You can’t tell if it's human or vampire, or both? But you feel a strange compulsion to…"
        menu:
        ‘/" "Lean in for a kiss":
            $ cass_affection+=2
            jump to label c2f
        "/" "Lean in for a bite"
            $ cass_affection-=5
            jump to label c2g
        label c2f
        "You lean in, anxious but excited. Cassandra purses her lips and you slowly move closer together…"
        "But Cass pulls away."
        c "I… I’m sorry. I need to go back home, it's getting late."
        "You both get up, and you give each other a hug goodbye before heading home. As you walk back you run the situation in your head again and again. Do you have feelings for Cassandra? And does she have feelings for you?"
        "The almost kiss pounded in your brain until you willed it to stop. As you arrived home, you lay down in bed, a million thoughts in your mind."
        label c2g
        # Tense Music
        "You lean in towards Cassandra’s neck, as a strange bloodlust comes over you. You open your mouth and you feel two fangs you did not notice before."
        "You feel a stange, intoxicating fear from Cassandra. The urge to bite consumes you, but you restrain yourself as best you can, jumping off of her."
        menu:
        "/" I’m sorry, I don’t know what came over me.":
            $ cass_affection+=1
        "/" "*stay silent*":
        "/" "Well… that just happened…":
        c "Woah… I… I’m sorry. I need to go back home, it's getting late."
        "She runs off. You want to run after her, to assure her than everything is ok, that your not a monster."
        "Is that really why you want to chase after her? Or is it the hunt? The desire to chase prey…"
        "You run back home, a million thoughts in your mind, and a pounding hunger tormenting you."
        scene apartment
        "When you arrive at your apartment, you are surprised to find Laila waiting at your door."
        Show l neutral with dissolve
        # romantic music
        L neutral "Good evening [player]. Having fun?"
        menu:
        "\"Yeah, you could say that."":
            jump inquiry6a
        "\"Not really."":
            jump inquiry6b

        label inquiry6a
        "Laila raises an eyebrow in mild surprise."
        L neutral "Interesting. My first few days- and I suppose many subsequent ones- were rough, so I’m glad to see you’ve taken to this well."
            jump inquiry6common

        label inquiry6b
        "Laila nods in understanding."
        L away "It’s not easy being one of us. There’s a lot that takes getting used to. And there will be some things you never get used to."
            jump inquiry6common

        label inquiry6common
        L neutral "I take it you went out with your friend who rescued you?"
        menu:
        "Be honest with Laila":
            jump inquiry7a
            $ laila_affection+=1
        "Dodge the question"
            jump inquiry7b
        "Lie to Laila"
            jump inquiry7c
            $ laila_affection-=1

        label inquiry7a
        "\"Yeah, Cass and I went out into the forest to see what I could do now.""
        L neutral "I’m not surprised. I can tell you two are close. Just, be careful, okay? It’s not easy having mortal friends when we’re like this."
            jump inquiry7common

        label inquiry7b
        "\"Well, you know, I was out and I saw some people, but more importantly how are you doing?""
        "Laila widens her eyes in bewilderment before narrowing them at you."
        L angry "You know you could have just said yes and I wouldn’t have inquired any further, but now I’m concerned."
            jump inquiry7common

        label inquiry7c
        "\"Nope, I was just out on my own.""
        "Laila gives you a look that could make hell freeze over. Her gaze is withering."
        L angry "Don’t lie to me. I don’t appreciate it, and you certainly won’t make a friend out of me this way."
            jump inquiry7common

        label inquiry7common
        "Laila lets out a sigh and absentmindedly brushes some hair out of her eyes."
        L away "Look, I don’t have a whole lot of time before I need to be getting back to the others, but here."
        "She passes you another small vial of blood, as she did the night before."
        L neutral "If you are going to be hanging out around regular folk, make sure you don’t do anything dumb, okay? Call me if you’re feeling urges you don’t know how to handle."
        "Laila pauses for a half a second before continuing."
        #comedic music, if possible
        L neutral "Okay that sounded weird. You know what I mean by urges. Not the normal kind, the other kind."
        "She pauses again and grows flustered, something you’ve not seen from her before."
        L away "Uh, you know what, if you feel the desire to bite someone, you can call-"
        "Laila looks at the ground and lets out an angry sigh."
        L away "Just, call me if you have any vampire problems."
        "As she turns to go, she stops to look over her shoulder at you."
        L neutral "By the way, some of us are meeting in the woods tomorrow night. I’ll make sure you get the invite."
        "With that, the vampire disappears into the night."
        Hide l with dissolve
        "You enter your apartment and lay down, contemplating the events of the evening, and wondering what new adventures might arise tomorrow."
            jump chapter3



    Chapter three
    label chapter3
    scene apartment
    # Neutral Music
    "You awaken this evening feeling more like yourself than you did the last couple nights."
    "Well, still not quite yourself, but not as much pain as before."
    "As you rise from your bed, you sense something different in the air. There’s tension, with a palpability to it."
    "You’re not sure what, but something big is going down tonight. There’s weight and finality in the actions you take this evening."
    "As you make your way into the living room, you notice a piece of paper has been slipped under your door."
    "You decide to investigate, and are perhaps unsurprised to find it is a letter from Laila."
    "Note" "[player], tonight, midnight. We’ll be in a section of the woods we call the Blood Bank. You can meet the others."
    "Note" "Just head straight into the woods from your street. Keep walking until you start to hear the revels."
    "Note" "-Laila"
    "You glance at the clock on your microwave. It’s- already eleven fifteen!?"
    "You really need to set an alarm going forward."
    "You hurriedly throw on some fresh clothes, and make your way out into the street."
    scene street
    "You suspect Cass might be interested in joining you on this excursion."
    "You text Cassandra to meet you  and wait outside of her apartment."
    "A few minutes later Cass rushes out."
    C excited "A Vampire Party! Oh my god!"
    C "It’s like everything I dreamed of!"
    C "I put on my most emo clothes, do you think I’ll fit in?"
    "You take a good long look at Cassandra’s bright pink jacket and skirt."
    mc " I’m sure you’ll be fine."
    "You walk into the woods, looking for the blood bank."
    "You wish Laila had written coordinates or something, cause you were deeply lost."
    C neutral "Maybe there’s a vampire  thing that you can do to find it?
    "You close your eyes and try to sense the forest as you walk."
    # Exciting Music, maybe even party music?
    "Finally, just on the edge of hearing, you detect the sound of laughter and mirth."
    "\"I think we’ve found it.""
    "Cass gives you an excited smile but remains quiet as you move ever closer to the ongoing party."
    scene hideout
    "After several more minutes of walking, you break through the trees into a massive clearing."
    "Fairy lights are strung across the clearing, which is decorated with picnic tables and populated by a couple dozen people who all look like they’re having a very good time. Near the center of the clearing is a makeshift bar."
    Show l excited with dissolve
    "As soon as you step into the clearing, Laila is at your side, appearing in what you are learning is typical vampiric speed."
    L excited "Hey, there [player], great to see you!"
    L neutral  "But who’s this?"
    "There is deep concern in Laila’s voice as she stares worriedly at Cass."
    c "Hi, I’m [player]’s friend Cassandra!"
    L away "Yes, I gathered that much, but why are you here? You’re not, you know-"
    "At this, Laila bares her fangs demonstratively."
    c Well, I’m not, but me and [player] are close, and, well, I’m really into vampiric history and seeing a place like this…"
    c "It’s just so cool! But if it's more of a vampire's only thing I totally understand!"
    menu:
    "Defend Cass":
        $ cass_affection+=1
        jump partychoice1
    "Support Laila":
        jump partychoice2

    label partychoice1
    "You push back against Laila, saying that Cass is your friend and deserves to be here."
    " "That’s sweet [player], but i don’t want to make anyone uncomfortable."
    c"I promise to be on my best behavior if you let me stay.":
    jump partychoicecommon

    label partychoice2
    "You see the wisdom in what Laila is saying."
    "\"You know Cass, Laila might be right. It could be dangerous with all these vampires around, and you know, I don’t really know any of them.":
        jump partychoiceCommon

    label partychoiceCommon
    "Laila looks taken aback at your remark."
    L away "Ah, you misunderstand, [player]. Your friend is not in any danger here. This is a gathering of… let’s say civilized vamps. We can control ourselves. Mostly."
    L excited "Had we known a human guest was coming, we would have brought some non-blood based beverages."
    "Laila shows you and Cass over to the makeshift bar near the center of the clearing."
    "A rather portly vampire greets you in a deep jolly voice."
    "Shamus" "Hello there, you must be the new one. I’m Shamus, and this here is the Blood Bank."
    "The barkeep- Shamus- gestures at the bar."
    "Shamus" "We’ve got our own brewing operation here. We take blood- sourced from an actual blood bank, don’t worry- and distill it in this here contraption."
    "He now indicates a small still sitting just behind the bar."
    "Shamus" "We call it ‘Bloodmoon Shine. First one’s free."
    "At this, he passes you a red solo cup filled with a reddish liquid."
    "You take a hesitant sip and find you somewhat enjoy the surprisingly strong beverage."
    "You’re a bit nervous too nervous to talk to anyone new just yet, so you hang by Laila and Cass."
    # Tense Music
    "The gentle sounds of the party are disrupted by a loud pop and the clearing is illuminated by a bright red glow. You look up and see a flare rising over the treeline."
    "All of the revelry stops and a hush falls over the gathered vampires."
    "Before anyone can comment, a flurry of nets are launched from beyond the clearing, ensnaring many of the partygoers, including Laila."
    "As she struggles to disentangle herself from the net, she pauses."
    L angry "Is this garlic? Did someone really coat these nets in fucking garlic? My clothes are going to reek!"
    "Something whizzes past your head and you hear someone scream. You turn to see it’s Shamus clawing at a large wooden spike that has lodged itself into their chest."
    "More and more of these stakes come flying out of the forest, so you grab Cass and drop to the ground to avoid getting hit. Laila, still in the net, follows suit."
    "The night air is filled with screams and shouts now, as more of your vampire brethren are impacted by this assault. "
    "Cassandra rushes to cut Laila and the other vampires out of the net. The panic sets in, but you need to act now. You:"
    menu:
    "Guide Laila and Cass  to scurry under a picnic table":
        jump PartyAttack1
    "Scamper into a bush":
        jump partyAttack2
    "Play dead":
        jump partyAttack3
    label PartyAttack1
    "As you hide under the table, you hear a sharp whirring sound coming from behind the bar.":
    jump explosion1

    label party attack2
    "You all hide in the bush near the bar, but you hear a sharp whirring sound coming from behind the bar."
    "Remembering the illicit brewing that the bartender mentioned earlier, you rush to hide beneath the picnic table away from the bar."
    jump explosion1 

    label partyattack3
    "You all play dead, which will surely be a winning strategy against these attackers."
    "Things seem to quiet down and you breathe a sigh of relief."
    "However, your relief is cut short by a sharp whirring sound coming from behind the bar."
    "Remembering the illicit brewing that the bartender mentioned earlier, you rush to hide beneath the picnic table away from the bar."
    jump explosion1 

    label explosion1
    " The Blood MoonShine still quakes for a moment before exploding, showering flaming alcohol everywhere."
    "The smell is pungent and the heat is unbearable."
    "You hold Cassandra and Laila close to make sure the table shields everyone from the raining flame."
    "When the rain stops, you risk a glance upward and see two figures enter the burning clearing, shrouded by smoke."
    "The screaming has mostly died down now, as the other vampires are either dead or have fled off into the woods. It’s just you, Laila, and Cass now, cowering beneath the table."
    "As you try to figure out next steps, you hear one of the figures start to speak."
    "Unknown" "Well Han, we did it. We’ve found the vampire cell and routed them. All according to my plan!"
    "Unknown- Han?" "Your \"plan", Anne, was firing a hundred stakes randomly at this clearing. Don’t pretend like the distillery blowing up was your idea."
    "Unknown- Anne?" "And it worked out in our favor. Shock and awe, that’s how we did it. Imagine how proud mummy and daddy would be of me in this moment."
    "Unknown- Han?" "I can imagine dad telling us he would have done it better back in the day with a half smile right now. Memories."
    "Unknown- Anne?" "Ugh, can’t you see we’ve eclipsed them? We’re forging a legacy that will outlast theirs!"
    "The smoke clears enough that you can get a good look at the two conversants- Anne and Han, you gather their names are."
    Show a neutral with dissolve
    Show h neutral with dissolve
    "The pair dress in matching vests, although Anne is markedly more stylish than Han."
    A neutral "And the Velsing name will go down in history as that of the greatest vampire hunters in the world!"
    c "Velsing???!"
    "Laila lets out a groan."
    L angry "Not these buffoons again."
    c "You know… the Velsings???"
    L angry "Unfortunately. These freaks inevitably come around to fuck up any nice vampire community I’ve managed to find. I thought we’d seen the last of them after the boat disaster in Grand Rapids, but I guess it’s hard to kill stupid."
    c "They look… (insert line about their outfit)
    L neutral "I know, the fashion is just insult to injury."
    menu
    "\"I think it’s kinda cool!"":
        jump quip1a
    "\"The Pony Express called, they want their uniforms back."":
        jump quip1b
    "\" "You know the rest of the fit aside, I feel like that top would look good on me":
        jump quip1c

    label quip1a
    "Cass and Laila both look at you with thinly veiled disgust."
    L angry "You need some help."
    A neutral "Thanks for the compliment!":
        jump quip1common

    label quip1b
    "Cass and Laila try to suppress giggles."
    A frown "The Pony Express provided a valuable service, just as we do!":
        jump quip1common

    label quip1c
    "Cass evaluates your current attire briefly."
    c "Yeah, I guess it could work."
    "Han" "Not everyone can rock such stylish gear. Especially not a bloodsucker":
        jump quip1common
    label quip1common
    "You recoil in terror at the addressing of your remarks."
    A neutral "Oh yes little bat-spawn, we heard everything you and your compatriots were saying."
    "At this, the Velsings flip the picnic table over, exposing the three of you."
    "You find crossbows with stakes loaded in them leveled at your face."
    A angry "To think you could hide from us- what hubris! No one can hide from our incredible acumen and refined senses!"
    "As she boasts, Laila and Cassandra run away. You seize upon the opportunity and run as well."
    "Cassandra and Laila are splitting up in the woods. You  don’t know who to chase after."
    "This is a matter of life and death."
    Hide l with dissolve
    Hide c with dissolve
    "You could follow Laila, further into the woods, or follow Cassandra, who’s running back towards town."
    "It’s possible you may never see the other one again."
    menu:
    "This choice is binding." (Maybe? What’s typical in the genre? Ask Kayla)
    "Follow Laila":
        jump LailaRoute
    "Follow Cassandra":
        jump CassRoute

    label LailaRoute
    "You know Cass will probably be fine- she’s a regular human after all- and you feel a burgeoning connection with this vampire that’s taken you under her wing."
    "You know in your heart this is the right decision."
    "You follow Laila into the night."
        jump laila_chapter4

    label CassRoute
    "Laila is far more experienced than you, you trust that she can take care of herself."
    "You run after Cass, unwilling to let your best friend get hurt."
        jump cass_chapter4



    LAILA CHAPTER 4
    label laila_chapter4
    scene forest
    # tense music
    "You dash after Laila deeper into the woods. All the vampires you met at the party- how many of them are dead? And those hunters, who are they?"
    "You don’t have time to think about those things now. You keep going."
    "You push your way through undergrowth that becomes ever-denser as you go on. You move at such speed that branches nick your face as you fly past."
    "Behind you, you hear the shouting of the Velsings and their rampage in your wake."
    A annoyed "Faster Han, you fool! They’re getting away!"
    "You hesitate for half a second and a stake lodges itself into the tree next to you. You keep moving."
    "All of sudden, the ground you were running on gives way to some sort of abandoned drainage ditch, and you make a half leap to cross it and roll into the bushes on the other side."
    "You turn around and spot the Velsings, who have neither your keen senses nor your enhanced reflexes."
    "Anne starts to stumble, but catches herself before she can trip and fall in. Her success is short-lived though, as Han runs straight into her, sending both of them tumbling."
    "The two lie in a disheveled heap in the ditch."
    A annoyed "We’re going to lose them now, you oaf! There will be hell to pay for how you’ve bungled MY great triumph!"
    "As Anne berates her brother, you take this opportunity to slip away into the shadows of the forest."
    "After a couple more minutes of running, you figure it’s probably safe to stop, and take a moment to catch your breath."
    "You’re only alone for a moment before you hear a snap from the trees behind you."
    Show l neutral with dissolve
    # neutral music
    "You spin to see it’s Laila, her clothes somewhat dirty, but otherwise none the worse for wear."
    menu:
    "\"Oh thank god, you’re alright!"’:
        jump chase1a
        $ laila_affection+=2
    "\"Don’t sneak up on me like that!"":
        jump chase1b
        $ laila_affection+=1
    "\"Took you long enough."’:
        jump chase1c
    $ laila_affection-=1
    "Remain silent.":
        jump chase1d
        $ laila_affection-=1

    label chase1a
    "Laila’s countenance, somewhat grim, now lightens."
    L excited "I’m glad to see you’re okay too, [player].":
        jump chase1common

    label chase1b
    "Laila lets out a soft chuckle."
    L excited "I didn’t know you were such a fraidy cat. Are you sure you’re qualified to be a creature of the night?":
        jump chase1common

    label chase1c
    "Laila gives you a withering stare."
    L angry "Perhaps had you not made such a racket in your escape, I would not have had to run quite so far to hide.":
        jump chase1common

    label chase1d
    "Laila looks at you expectantly, then speaks in an exasperated tone."
    L away "Yeah, thanks [player], I’m glad to see you’re okay too. Jeez.":
        jump chase1common

    label chase1common
    L neutral "So, I don’t think we’ll be able to make it back to town safely before the sun rises. Thankfully, yours truly has thoroughly explored these woods, so I know a place we can go."
    "Laila beckons you to follow her before marching off. You follow close behind."
    "Several long minutes pass in silence. Neither of you speaks for fear that the Velsings might still be roaming."
    "Finally, you reach your destination: a cabin, but one incredibly dilapidated. The roof is partially collapsed, and none of the windows have any intact glass remaining."
    "\"We’re staying here?""
    L neutral "There’s more to this place than meets the eye."
    "Laila cracks open the door and leads you inside. The inside is not much better than the outside: the furniture that has not been covered by the collapsed roof is aged and covered with moss."
    "Then you see it. Beneath a dining table is a small hatch in the floor. You only spot it because of your vampiric vision- it’s so overgrown with foliage it would be hard to see even in the day."
    "Laila kneels down and lifts the hatch, and you’re assailed by a wave of dank air."
    L neutral "Get in. It’s deep enough, and no light’s going to get through. I’ve slept over here on more than one occasion."
    "You approach the hatch."
    L away "It will be, uh, a bit of a tight fit for the both of us."
    "You have no other choice though. You descend a rickety steel ladder into the dark, and Laila follows, closing the hatch behind you."
    scene cellar
    "At the bottom of the ladder is a small room- if you can call it a room- not more than a foot and a half long by a foot and a half wide."
    "As Laila reaches the bottom, it becomes immediately clear just how small a space it is."
    Show l neutral with dissolve
    "There is no room for either of you to sit. Your back is pressed up against a mossy stone wall- at least, you hope it’s moss- and you are only inches away from Laila."
    "You feel the unnatural coolness radiating from her, and realize she probably feels the same from you."
    # comedic music maybe
    L smile "I didn’t think we’d be sleeping together this soon."
    "She lets out a little laugh."
    menu:
    "Stay quiet.":
        jump pit1a
        $ laila_affection-=1
    "Give a little laugh.":
        jump pit1b
        $ laila_affection+=1
    "Make a quip back.":
        jump pit1c
        $ laila_affection+=1

    label pit1a
    "You remain silent and Laila’s laugh peters out."
    L away "Sorry, wrong time, yeah.":
        jump pit1common

    label pit1b
    "You release a little giggle at Laila’s joke, and she gives you a broad smile."
    L excited "I’m glad you found it funny."
        jump pit1common

    label pit1c
    "\"Yeah, I expected you to buy me a drink first.""
    "Laila chuckles at your remark."
    L excited "Next time, [player]."
        jump pit1common

    label pit1common
    L neutral "Well, we’re going to be here for a while. I guess I can answer any questions you might have."
    #romantic music
    menu:
    "Ask about Laila’s past.":
        jump pitInquiry1a
    "Ask about Laila’s life now.":
        jump pitInquiry1b
    "Ask about the other vampires in town.":
        jump pitInquiry1c
    "Ask what Laila thinks of you.":
        jump pitInquiry1d
    Kristen, can we have these questions go back to the menu minus options already chosen?

    label pitInquiry1a
    "\"If you don’t mind, could I know some more about your past?"
    L neutral "Like, before I came to town? Yeah, I suppose."
    L neutral "Well, I was turned about 10 years ago, at a punk rock show in Houston. It was an unpleasant end to an otherwise great evening."
    L away "Since then, I’ve kinda been hopping around from community to community. Vampires can’t really settle down anywhere in anything resembling large numbers for very long. We attract the attention of people like the Velsings."
    L away "I mentioned Grand Rapids earlier. Before I came here, it was the longest place I had stayed- about a year. Too many of us were too open there, and they came and it all went up in flames."
    L angry "Like it always does."
    "Laila pauses now and takes a deep breath before continuing."
    L neutral "It’s fine."

    label pitInquiry1b
    "\"Can you tell me what things have been like for you recently?""
    L neutral "I mean, I’ve been living here for something like 9 months? After Grand Rapids, I needed to find a new place to settle down. My ex, some of her friends were out here. Felt like it could be safe. And it has been."
    L away "But there’s not a whole lot to life here beyond subsisting. I take shifts at some of the local bars a few nights a week. It’s enough to get by here."
    "\"You’re a bartender?""
    L neutral "Yeah. Not what I imagined spending my life doing, but there’s not a whole lot of employment options for people in our position. It’s not awful."
    L away "But it’s not great, either."

    label pitInquiry1c
    "\"Can you tell me about the other vampires living in town?""
    L neutral "The ones that are left you mean? There’s something like 20ish of us? I knew a couple of them through my ex and they’re good enough folks."
    L away "It’s pretty tough to find vampires who aren’t into the whole live feeding thing. The New York City vamps are living it up, they disguise their kills as regular murders, they never have to worry about getting caught."
    L away "Vampire hunters always go after us- they look for blood banks with mysteriously missing blood. This is why I split with my ex. She didn’t share my objections about killing, and wanted to protect herself."
    L neutral "I’d rather not discuss it further."

    label pitInquiry1d
    "\"Well, what do you think of me?""
    "Laila’s eyes widen briefly at your question, then she looks away."
    L away "Look, I think you’re nice enough. But I don’t really know you all that well yet. And things aren’t great, you know?"

    label pitInquiry1common
    "From everything Laila’s said, you’re picking up on something."
    "\"Do you like being a vampire?""
    "At this, Laila lets out a deep sigh."
    L away "No."
    "She is silent for a long while."
    L neutral "Okay, I probably owe you more of an explanation than that."
    L neutral "I tried very hard to adapt. But the sort of existence I have to live- the things we have to do just to survive- is miserable. The speed and the strength is neat, but it’s not worth never getting to feel the sun on my skin again."
    L away "Living this way forever? I see it as a curse."
    L neutral "I’m sorry, I’m sure you’re enjoying the experience. I don’t mean to upset you."
    "It’s all for her to share, and a great deal for you to process."
    menu:
    "\"It’s okay, I get where you’re coming from, I feel that a bit too."":
        jump pitInquiry2a
        $ laila_affection+=2
    "\"I’m loving it, but your feelings are totally valid."":
        jump pitInquiry2b
        $ laila_affection+=1
    "\"Yeah, how could anyone not love this?"":
        jump pitInquiry2c
        $ laila_affection-=2

    label pitInquiry2a
    "Laila cheers up a bit at your response."
    L smile "Thank you [player]. I appreciate your empathy. And I’m glad someone else feels the way I do."
    "Laila stares into your eyes, raising a hand and allowing her fingers to brush lightly against your cheek, before she quickly pulls away."
    L away "Sorry, I’m going through a lot right now."
        jump pitInquiry2common

    label pitInquiry2b
    "Laila takes a deep breath and nods at your response."
    L neutral "That’s more understanding than I get from most others, so I appreciate it."
        jump pitInquiry2common

    label pitInquiry2c
    "Laila goes from quiet and contemplative to furious in an instant."
    L angry "Yeah, of course, your feelings are the only ones that matter. Sorry I bothered to open up to you. You’re just like all the others."
    "The two of you sit in the silence uncomfortably."
        jump pitInquiry2common

    label pitInquiry2common
    "After several minutes of quiet, Laila speaks up again."
    L neutral "Well, I think we should at least try to get some sleep. I can only imagine tomorrow night will be busy. Sleep tight, [player]."
    "With this, Laila closes her eyes and, still standing, settles into a slumber like death."
    "You decide to follow suit, and rapidly fall into a deep and dreamless abyss."
    jump laila_chapter5

    label laila_chapter5
    scene cellar
    "You awaken to find Laila’s head resting on your shoulder- it appears she shifted in her sleep."
    # romantic music
    menu:
    "Let her stay like this for a minute.":
        jump wake1a
        $ laila_affection+=2
    "Gently wake her up.":
        jump wake1b
        $ laila_affection+=1
    "Shake her awake.":
        jump wake1c
        $ laila_affection-=2

    label wake1a
    "You’re not in any particular rush, so you decide to let Laila rest for as long as she needs to."
    "Despite your best attempts at keeping still, Laila wakes within a couple minutes."
    "When Laila becomes aware of exactly where she’s been sleeping, she stumbles back as far as she can in the enclosed space."
    Show l away with dissolve
    L away "Oh, [player], I’m so sorry, I hope I didn’t disturb your sleep."
    "Laila takes a moment to compose herself."
        jump wake1common

    label wake1b
    "You give Laila a light tap on the shoulder, and she begins to come awake."
    "When Laila becomes aware of exactly where she’s been sleeping, she stumbles back as far as she can in the enclosed space."
    Show l away with dissolve
    L away "Oh, [player], I’m so sorry, I hope I didn’t disturb your sleep."
    "Laila takes a moment to compose herself."
    L smile "Still, I appreciate the care you took in waking me."
        jump wake1common

    label wake1c
    #tense music
    "You’re not a fan of Laila being in your personal space, and you grab her shoulders and shake her awake."
    Show l angry with dissolve
    "She is alert in an instant and slaps you in the face."
    L angry "What is your problem? We’re not in any sort of danger, can’t you at least try to be polite?"
    L angry "Would you like it if someone woke you in that way? Jerk."
    "She leans back against the wall and simmers in anger for a bit, before composing herself."
        jump wake1common

    label wake1common
    # neutral music
    "With the two of you sufficiently awake, Laila gestures for you to make your way up the ladder."
    "You make your way to the surface, opening the trapdoor, and emerging into the cool air of the early evening. Laila emerges from the hatch a moment after you/"
    scene forest
    Show l neutral with dissolve
    L neutral "Alright, we have to find out who survived that disaster last night. The problem is I have no idea where’s safe anymore."
    "\"Is there no other secret vampires-only hideout?""
    L neutral "No, I don’t think- wait a minute. We could visit Gabrielle’s. But that may be worse than the Velsings."
    "\"Who is Gabrielle?""
    "Laila looks away, somewhat embarrassed."
    L away "She’s an older vampire, who doesn’t like new vampires. She has a bad habit of killing them."
    "\"What?!? She kills other vampires?!""
    L away "She’s a little bit like me, she doesn’t think vampirism is a gift. And she wants to spare new vampires- like you- from the suffering."
    "You take a moment to consider what you’ve just been told."
    "Laila takes a deep breath and straightens her posture."
    L neutral "I think these are exceptional circumstances. Gabrielle won’t kill you. Maybe. Probably. I hope."
    "These words do not, in fact, inspire you with hope."
    "Still, you follow Laila as she begins sprinting in the direction of town with vampiric speed."
    "While you are quick, you still struggle to keep up with Laila, who is able to dodge and weave around trees without breaking her stride. You, unfortunately, run into more than one tree on your journey."
    "Once you emerge from the forest, somewhat battered for your efforts, you stop Laila to chat."
    scene street
    Show l neutral with dissolve
    "\"Wouldn’t it have just been simpler to, you know, turn into a bat and fly here?""
    "Laila shakes her head."
    L smile "And leave all of our clothes in the forest? Sorry [player], I like you, but not that much. Yet."
    L angry "Besides, I hate turning into bats."
    "With that, Laila leads you through town. It’s not terribly late, so there are still people on the streets- running now would draw too much attention to you."
    scene creepy house
    # tense music
    "Soon you arrive in a neighborhood that you’re not quite familiar with. Dilapidated single family homes line the streets. Laila stops in front of one that somehow looks worse than all the rest- vines cover half the house, and the yard is filled with weeds."
    Show l neutral with dissolve
    "\"Gabrielle lives here?""
    L neutral "Yeah. It’s, uh, easier to dispose of corpses here."
    "\"Oh my god.""
    "Laila turns to face you with concern in her eyes."
    L neutral "Look, I don’t approve of what Gabrielle does, okay? Not many of us do. But right now if we want to live longer than the next couple nights, she’s our best shot."
    "With this, Laila turns resolutely towards the door and approaches it. As she raises her arm to knock, the door swings open and a shape flies out past Laila."
    "In an instant you are knocked to the ground, pinned there. You gather your bearings and find your assailant is an old woman, her hand raised above your heart, clutching a stake."
    "She is about to plunge it down into your chest when Laila rushes over and grabs her wrist."
    L angry "Gabrielle, no! This is [player], my friend. We need your help."
    "The old woman, Gabrielle, bares her teeth in a snarl, revealing her lengthened incisors."
    "Gabrielle" "Laila, it’s a new blood, no more than a few days old. I can smell it! Let me give the soul a chance to make it to heaven, before the taint of hell stains it forever."
    L angry "That’s not happening Gabrielle. Now get off of my friend, or you and I are going to have a problem."
    "Gabrielle gives you one last snarl before easing off of you, and standing back up. You take a moment to get up and dust yourself off. Laila turns to you."
    L neutral "Gabrielle is rather religious. She thinks vampires less than a couple weeks old can still go to heaven."
    "Gabrielle nods stiffly at this."
    "Gabrielle" "I don’t think it. I know it."
    L neutral "Anyway, Gabrielle, the Velsings are in town. They destroyed the Blood Bank."
    "At the Velsings’ mention, the older vampire shudders."
    "Gabrielle" "Monstrous, they are. I know of the destruction you speak of. Their hunt is driven by hatred, not compassion."
    "\"You’ve got a funny way of showing compassion.""
    "Laila gestures for you to stop talking."
    "Gabrielle" "I’ll let the impudence go. I had a whole lifetime of experience under my belt before I was turned, and I know what it’s like to be a youngster, with no clear view of the bigger picture. There will be a day, [player], that you will come to disdain Laila for not letting me impart my mercy unto you."
    "Laila rubs her temples in frustration."
    L neutral "Gabrielle, do you know if anyone survived the attack?"
    "The old woman nods."
    "Gabrielle" "A handful dropped by on their way out of town. They wanted to warn old Gabrielle. They didn’t listen to me though, and kept on their way."
    L neutral "Well of course Gabrielle, they’re running for their lives."
    "Laila turns to you."
    L neutral "Just like we will. I’ll get you through this [player]."
    "Gabrielle chuckles."
    "Gabrielle" "You don’t need to flee. Old Gabrielle knows of the cure."
    "A cure? What is this mad old woman talking about?"
    menu:
    "Ask her to explain.":
        jump cure1a
    "Remain silent.":
        jump cure1b

    label cure1a
    "\"What do you mean a cure?"
    "Gabrielle gives you a sickening grin."
    "Gabrielle" "Oh now you’re interested, eh? I’ll tell you."
    "She takes a dramatic pause."
    "Gabrielle" "A new vampire came to town last week. They spoke of having found a way to remove our curse. Some ritual or concoction, or something, I don’t know. It’s beyond my ken."
    "These words have affected some sort of change in Laila. Her eyes are wider, her stance poised as if to leap off running."
    L neutral "Speak more on this."
    "Gabrielle" "I don’t know much more than what I’ve told ya. Just that this fellow is staying in the abandoned mansion on the big hill."
    "You know the place Gabrielle speaks of. The house is infamous for being in a state of disrepair in an otherwise upscale part of town."
        jump cure1common

    label cure1b
    "You elect to remain silent, but Laila speaks up, her voice hopeful."
    L neutral "What cure?"
    "Gabrielle gives Laila a sickening grin."
    "Gabrielle" "Oh now you’re interested, eh? I’ll tell you."
    "She takes a dramatic pause."
    "Gabrielle" "A new vampire came to town last week. They spoke of having found a way to remove our curse. Some ritual or concoction, or something, I don’t know. It’s beyond my ken."
    "Laila is like a changed woman on hearing this. Her eyes are wider, her stance poised as if to leap off running."
    L neutral "Speak more on this."
    "Gabrielle" "I don’t know much more than what I’ve told ya. Just that this fellow is staying in the abandoned mansion on the big hill."
    "You know the place Gabrielle speaks of. The house is infamous for being in a state of disrepair in an otherwise upscale part of town."
        jump cure1common

    label cure1common
    # romantic music
    "Laila turns to you now."
    L neutral "[Player], this is a lot to ask of you, and I understand if this quest is not for you."
    L neutral "But I must seek out this cure. I cannot pass on this opportunity."
    L neutral "Will you join me?"
    menu:
    "\"Yes Laila, I’m with you all the way. Together, we can be free of this.""
        jump cure2a
        $ laila_affection+=2
    "\"I can’t say I’ll use any cure we might find, but I will help you find peace.""
        jump cure2b
        $ laila_affection+=1
    "\"No, there’s too much risk. I’m just going to leave town and make it on my own.""
        jump cure2badending

    label cure2a
    "You let Laila know that you will join her on her quest, and she embraces you in a hug."
    L excited "Thank you so much [player]. I know we’ve only known each other for a couple days, but I will forever appreciate this."
    "She releases you from the hug, and you find yourself wishing she had held you for just a moment longer."
    "Laila now steels herself with resolve."
    L smile "Thank you, Gabrielle. We’ll be going. Stay safe."
    "The old woman merely stares as you and Laila depart."
        jump cure2common

    label cure2b
    "You inform Laila that even though you might wish to remain a vampire, you’ll help her find a cure."
    "Laila gives you a big smile and clasps your hands in thanks."
    L excited "Thank you [player]. Even if we have different ideas about what it means to be a vampire, I’m glad I can rely on you."
    "Laila now steels herself with resolve."
    L smile "Thank you, Gabrielle. We’ll be going. Stay safe."
    "The old woman merely stares as you and Laila depart."
        jump cure2common

    label cure2badending
    # sad music
    "You inform Laila that you’re done with all this, and intend to leave town and escape the Velsings."
    "Laila is visibly disappointed in your response."
    L away "I won’t begrudge you your decision. And I’m not upset. But I can’t say I’m not surprised. I thought you and I had at least some sort of connection. But I guess I was wrong."
    "She composes herself."
    L neutral "I wish you well, [player]. Good luck."
    "Laila departs into the night. You do not know it now, but you will never see her again."
    "You return home, and sleep through the day. The following night you make your way out of town, catching a bus heading to some place far away from here."
    "You manage to survive in your new home for a time, finding other vampires, before the Velsings inevitably find your new haunt. And so you flee again."
    "And so it goes on, year after year, a life on the run. Until one night, you are not quite as lucky as you were in the past. Perhaps you were hit by a stake like Shamus was at the Blood Bank, or maybe you simply got caught outside as the dawn came."
    "It matters not how. Simply that your life has come to an ignominious end."
    [End]

    label cure2common
    L neutral "I don’t think we’ll have time to get to and explore the mansion this evening. Mind if we stay the day at your place?"
    "Laila’s right, and so you agree to open your home up to your vampire friend."
    scene apartment
    "When you get to your apartment, Laila begins to crawl under your bed."
    Show l away with dissolve
    "At your evident shock, Laila begins to explain."
    L away "This is kind of embarrassing, but at home I actually, uh, do sleep in a coffin."
    L away "I’m used to the confined spaces, and can’t really sleep otherwise."
    "Of all the things you’ve experienced over the last few nights, this might be the weirdest."
    "Still, the evening’s escapades have left you exhausted, and you collapse onto your bed, and fall into another dreamless slumber."
        jump laila_chapter6

    label laila_chapter6
    scene apartment
    # tense music
    "You awaken with a pulsing headache, worse than your first night as a vampire. Your head feels like it might explode at any second."
    "And, as if things couldn’t get any worse, your thirst for blood is all-encompassing.You realize you never had any blood last night."
    "You stagger out of bed and try to make your way towards the kitchen. You don’t make it more than a handful of steps before you collapse."
    "You resort to feral behavior, crawling along the floor like some sort of animal, driven almost entirely by instinct."
    "In your hunger, your senses seem heightened, and you can hear the beating hearts of your slumbering neighbors."
    "You want them."
    "You rise shakily to your feet, and have almost made it to the door, when some force tackles you from behind."
    Show l angry with dissolve
    L angry "[player], no!"
    "It seems Laila is awake and intends to stop you. Despite knowing she’s probably acting in your best interest, your body resists her without conscious effort. It’s like you’re no longer in control."
    "Laila manages to flip you over, and pins your arms to the ground. Despite her slender frame, she is holding you down with ease."
    L neutral "Listen to me, you have to fight it. It gets easier to skip a day or two as you get older, I promise. But for now, you need to be strong!"
    "Laila is pleading with you as your body struggles against her. You try to speak, but your lips refuse to do anything other than curl into a snarl."
    L away "Okay, I can try something crazy, if you can’t calm yourself."
    "Laila hesitates before speaking again."
    L neutral "We’re not supposed to, but I can give you some of my blood- vampire blood- and it should sate you. For a time. But you and I will forever be bound."
    L neutral "Our emotions, our thoughts, we will share them, even over long distances. It will take time for the bond to manifest. But should either one of us perish, we shall feel it as if we ourselves died."
    L neutral "I will do it to help you."
    "Laila shifts her weight so she now has you pinned with one arm, while using her free hand to make a small cut in her neck. Pale red blood begins to seep from the incision.
    menu:
    "Accept Laila’s offer."
        jump offer1a
        $ laila_affection+=2
        $ drank_blood = true
    "Reject Laila’s offer, and resist the hunger."
        jump offer1b
        $ laila_affection+=1

    label offer1a
    # romantic music
    "You nod, and Laila eases her hold on you. You lunge forward and press your lips to her neck."
    "Laila is stiff initially, but softens at your touch, and her breathing becomes ragged and hitched as you feed."
    "You’ve never fed like this before, your skin against Laila’s skin, the salty ichor passing directly from her veins into you. It’s an ecstasy you’ve never felt before."
    "As you drink, you feel Laila’s emotions as if they’re your own- fear for the future, concern for you, and her excitement at this taboo action you now engage in."
    "You take more of Laila in, desirous for this connection to last forever, but you feel her emotions begin to weaken in clarity. Somehow, you know, you are about to drink too much."
    "You release your hold on Laila, pulling away, and she gasps as if waking from a dream."
    "The two of you fall away from each other, laying on the floor, exhausted, even though the whole endeavor lasted no more than thirty seconds. Your hunger is no more."
    "After some time passes, the two of you rise from the ground, and Laila looks at you somewhat shyly."
    L away "Let’s not speak of what happened between us until this business with the cure is settled. We may not even have to worry about the consequences."
    "Laila bites her lip before speaking again."
    L smile "It felt good though."
    "With that, you and Laila depart your apartment and head in the direction of the manor Gabrielle told you about."
        jump offer1common

    label offer1b
    "With a great deal of effort, you manage to purse your lips together and shake your head."
    "Laila eases up on you, covering the wound on her throat."
    "You sit up, shaking, and try to get control of your body. Every muscle screams out, driven to act by the vampiric essence flowing through you."
    "Laila watches you nervously, evidently ill at ease. Still, she offers you encouragement."
    L neutral "I believe in you, [player], you can beat it."
    "Despite this, you continue to detect the presence of your neighbors, the flow of their blood growing to a torrent in your ears."
    "Your fangs dig into your lips as you bite down, spilling your own blood."
    "Your shaking grows into full force convulsions, spasming on the floor of your apartment."
    "It would be so easy to give in- but you don’t. You hold strong."
    "It seems like this suffering will have no end."
    "And, just as suddenly as it all started, it’s over. You collapse to the floor, exhausted. The hunger is gone."
    "Laila approaches and helps you sit up. She looks on you with tenderness and care."
    L excited "You did it, I’m amazed. You truly are something special."
    "After you’ve taken some time to compose yourself, you rise to your feet, and Laila gives you a nod of respect."
    L neutral "The night’s getting on, we should get over to the mansion."
    "With that, you and Laila depart your apartment and head in the direction of the manor Gabrielle told you about."
        jump offer1common

    label offer1common
    # neutral music
    scene street
    "You and Laila traverse the quiet streets of town quickly, avoiding other pedestrians when possible. Dark clouds obscure the sky- there will be no moon or stars to light your evening, just the orange sodium glow of street lamps."
    "You’re unsure of why, but you feel an urgency in the air, as if the whole of history is coming to a head tonight, in this town."
    "Before you arrive at your destination, you have a question for Laila."
    Show l neutral with dissolve
    "\"Laila, this cure, what will you do with your life if it’s real?"
    "Laila stops walking and contemplates your question for a time."
    L neutral "I think I want to go back to New Mexico for a time, though. Just be away from the night and the shadows in a place baked by the sun."
    L away "I guess most of all I want to live a life where I don’t have to run anymore. Find someone to settle down with."
    L away "You’ve only lived this life a little while, but it takes a toll on you. I’ve barely lasted a decade like this, I can’t imagine an eternity on the run."
    L smile "Anyway, I’m confident we’ll find it."
    "With that, Laila continues on her way, and you follow close at hand."
    "On  the way to the mansion, you run into Cassandra, sipping a Demon energy drink and carrying a tote full of books."
    # exciting music
    Show c smile with dissolve
    C "[player]! And Laila! What a coincidence! I was just on my way back from the library, studying up on vampire history."
    L smile "Oh, I’m so glad to see you’re alright. Sorry about the party going south, it’s uh, part of the vampire experience, unfortunately."
    C doubt "Don’t be sorry, it’s not your fault."
    C smile "Where are the two of you headed tonight?"
    L excited "We’re off to find a cure! The old mansion on the hill, we’ve heard there could be answers there."
    C doubt "The mansion… "
    "Cassandra pulls out a hefty book about old architecture in the town."
    C "I was reading about the history of vampire hunters, and Logan Velsing, a huge landowner in the 1980’s, owned a lot of buildings with ties to vampire hunters."
    "\ "Velsing… Like Anne Velsing? And Han Velsing?""
    C "Exactly. They own a bunch of the older buildings in town, including that mansion."
    C "It doesn’t necessarily mean anything, but just be careful, ok?"
    L neutral "It could be something, but probably nothing. No one’s lived there for years I’ve heard. Still, thank you Cassandra. Stay safe."
    C wink "You too!"
    Hide c with dissolve
    # neutral music
    "With that, you and Laila proceed across town to the mansion, the houses growing larger and more decadent as you approach.
    scene mansionExt
    "Now the mansion rises out of the gloom of the night, still regal despite its decrepitude. It is of gothic style, imposing and austere."
    Show l neutral with dissolve
    L neutral "Well our mystery vampire certainly picked one hell of a haunt."
    "You and Laila approach the vast doors of the manor, hesitating before you open the door. Laila turns to face you."
    L away "[player], I don’t know what waits for us beyond these doors, but I want to thank you for sticking with me through this."
    menu:
    "Kiss Laila":
        jump lailakiss1a
        $ laila_affection+=2
    "Give her a handshake":
        jump lailakiss1b

    label lailakiss1a
    # romantic music
    "You reach out to Laila and pull her in close to you. There is confusion in her eyes for half a second, before she realizes what’s going on and gives you a gentle smile."
    "You lean in and press your lips to Laila’s, and she returns your affection, holding you tightly. Despite the unnatural chill of both your bodies, it feels right."
    "After several moments in each other’s embrace, you and Laila separate."
    L smile "That was nice. Let’s do it again sometime."
    L neutral "But it’s time we ended this. Let’s go."
        jump lailakiss1common

    label lailakiss1b
    "You extend a hand to Laila, who looks at you somewhat confused."
    L away "Oh, okay, uh. Not quite what I was expecting, but okay."
    "Laila grabs your hand and gives a somewhat halfhearted handshake."
    L neutral "Kind of overly formal for me."
    "You and Laila release each others’ hands, and Laila turns to face the door again."
    L neutral "Alright, let’s finish this."
        jump lailakiss1common

    label lailakiss1common
    scene mansionInt
    # tense music
    Show l neutral with dissolve
    "You and Laila proceed through the aged doors of the manner, closing them behind you."
    "You find yourself in a grand hall, filled with antique furniture and suits of armor, walls bedecked by renaissance paintings, lit by oil lamps and candles. A balcony overlooks the room from the second floor. Laila takes a few steps forward."
    L neutral "Hello? Is anyone here?"
    "There is no response to Laila’s inquiry."
    "\"Can you sense anyone?""
    "Laila angles her head to the side and listens intently."
    L neutral "There’s something messing with my hearing. Something I can’t actually hear is getting in the way."
    "You try to listen too, and sure enough you feel whatever it is Laila is talking about. Like some sort of subsonic hum, dampening your senses."
    "Whatever it is blocking your hearing, it’s also making you feel a little bit dizzy. You take a step back and lean against the wall for support."
    L away "I don’t like this. Combined with what Cassandra told us, this does not bode well. We’re leaving."
    "Laila turns to make her way to the door, and is halted by loud sounds of metal clanging."
    "You look around and see that metal bars have come down over all the windows. Laila tries to open the front door but finds it locked."
    L neutral "I think we’re trapped."
    A neutral "Indeed you are, vampire brats!"
    "Anne Velsing’s voice feels like it comes from all around you."
    A neutral "Welcome to one of our many ancestral residences, designed with vampire entrapment in mind. I’m glad to see my snare has caught some of the runaways from our little surprise in the forest."
    L angry "Fuck, how many times do I have to deal with this bitch?"
    "Laila’s voice is filled with exasperation. Despite this interjection, Anne continues on."
    Show a neutral with dissolve
    A neutral "Now is the moment of my supreme triumph!"
    "Anne now reveals herself on the balcony, glaring down at you and Laila."
    A annoyed "You wretches will find abilities hampered by my brilliant inverse echolocator!"
    "Anne hoists a very complex-looking mechanical device, about the size of a smartphone."
    A annoyed "This broadcasts sound at the same level bats can hear, above human detection, powerful enough to weaken vampire brats like you!"
    L angry "Can you stop calling us that? It’s not as clever as you think it is."
    A angry "You fool! I am the mighty Anne Velsing; I am nonpareil! My whelp of a brother has been dealt with, and no one will stand between me and glory!"
    "Anne stows the inverse echolocator in a pocket, and leaps from the balcony, landing on the ground with a somersault. She vaults to her feet and brandishes her knife."
    A neutral "As the bard wrote, damned be him that first cries hold, enough!"
    "With a mighty cry, Anne charges you."
        jump laila_chapter7


    label laila_chapter7
    scene mansionInt
    # tense or exciting music. Not sure which is better for a fight
    "You and Laila find yourselves dodging Anne’s furious knife swipes. You’re not sure how much damage a knife can do to you, but you’d still rather not get stabbed."
    "Even that simple task, though, proves hard enough in its own right. Anne’s device has you and Laila seriously off-kilter, and your movements are sluggish, like moving through water."
    "As you try to move away from the vampire hunter, you stumble backwards over an ottoman and into a plush leather armchair. Anne takes this chance to leap at you, her blade aimed at your neck."
    "Laila intercepts Anne, throwing herself into the hunter, causing her to lose her balance momentarily, giving you an opportunity to dive from the chair and onto the floor."
    "This defense has left Laila winded, sending her stumbling across the hall. Anne, not deterred, renews her assault, focusing solely on Laila now."
    "Laila avoids strike after strike, but only barely, Anne’s knife getting closer and closer with each swing."
    "You pull yourself to your feet and move to help Laila, but it is too late. Laila, too focused on Anne, has neglected paying attention to her surroundings, and leaps backwards- crashing into a suit of armor, and impaling herself on the sword it held."
    # sad music
    "Laila lets out a gasp, the air driven from her lungs as the blade embeds itself below her ribcage. She appears unable to move."
    Show a frown with dissolve
    A frown "Oh. I wasn’t expecting that."
    A neutral "Fortune smiles on me, I suppose."
    "Anne now turns to face you. Despite her relentless assault, she hardly seems out of breath."
    A neutral "Alright vampire. Surrender now, and I’ll make the deaths of you and your companion swift. For I will kill you both. It is simply a matter of whether I stake you, or leave you in the sun to burn. Or perhaps I shall bury you alive in the basement and let you starve to death over decades."
    A neutral "The only difference is the amount of suffering you go through. And the enjoyment I derive."
    # tense music
    menu:
    "\"Why are you doing this?"":
        jump anneinquiry1a
    "\"I think you’ve got a problem lady."":
        jump anneinquiry1b

    label anneinquiry1a
    "Anne looks genuinely puzzled at your question."
    A confused "Why am I doing this? Surely you jest? The Velsings have always hunted your kind."
    A neutral "I merely aim to be the very best; as I said before, the nonpareil. To go down in history as the greatest Velsing that ever lived."
    A neutral "But if you mean this particular plan, it’s part of that bigger picture. You see, my brother, he was a fool. I lost you the other night because of him. But I anticipated that sort of failure."
    A neutral "I paid off the old woman, Gabrielle. While she is one of you, we are not entirely dissimilar. Her body count of your kind is impressive. I had her direct all those she could here."
    A frown "As for my brother, well. He won’t be getting in my way again."
    A neutral "I hope that answers your question, brat."
        jump anneinquiry1common

    label anneinquiry1b
    "Anne is taken aback."
    A angry "What impudence! Were I not feeling gracious in my moment of triumph, I would smite you for that."
    "Anne shakes her head."
    A neutral "But it is no matter. You see, I aim to be the very best; as I said before, the nonpareil. To go down in history as the greatest Velsing that ever lived."
    A neutral "And this particular scheme, it’s part of that bigger picture. You see, my brother, he was a fool. I lost you the other night because of him. But I anticipated that sort of failure."
    A neutral "I paid off the old woman, Gabrielle. While she is one of you, we are not entirely dissimilar. Her body count of your kind is impressive. I had her direct all those she could here."
    A frown "As for my brother, well: he won’t be getting in my way again."
    A neutral "So I assure you, there is no problem. Except for you."
        jump anneinquiry1common

    label anneinquiry1common
    "As Anne monologues, you look over to Laila, who remains slumped against the armor, in obvious pain. She doesn’t look good."
    A neutral "Come now vampire, do not make this harder than it has to be for the both of us."
    menu:
    "\"Surely we can come to some sort of arrangement?"":
        jump anneinquiry2a
    "\"Why would I ever want to make killing me easier for you?"":
        jump anneinquiry2b

    label anneinquiry2a
    "Anne raises an eyebrow at you."
    A confused "You are very different from other vampires I have met. Most try to kill me without a thought. Yet you want to make a deal with me? Very curious indeed."
    A neutral "I suppose I’m open to discussing alternatives with you.
        jump anneinquiry2common

    label anneinquiry2b
    "Anne scowls and opens her mouth as if to snap back at you, but pauses."
    A frown "You’re right, why would you ever willingly surrender? I never would. And yet, while I will assuredly beat you in a contest of strength, I should not risk life and limb needlessly. I have won this battle."
    A neutral "So vampire, let us discuss alternatives to needlessly shedding each other’s blood."
        jump anneinquiry2common

    label anneinquiry2common
    "As she thinks, Anne idly twirls her knife in your direction."
    A confused "What might I do with a vampire brat such as you? I can tell you’re new, so you’d be malleable."
    A neutral "Ooh, perhaps you could be an infiltrator for me, work your way into other vampire clusters. We could eradicate them together. An acceptable evil for the greater good."
    "Laila coughs now as she tries to speak."
    Show l away with dissolve
    L away "Don’t… help her."
    "Laila’s voice is hoarse, her breathing strained. Still Anne whirls around to look at her."
    A annoyed "Silence, you! Perhaps if you had half the brains as this one here, you wouldn’t be in this position."
    "Anne now returns her attention to you."
    A neutral "Now, where were we? Ah yes, you, joining me."
    A neutral "You have no kindred ties to the other vampires. You’re practically still human. You’d be ridding the world of a plague that sunk its fangs into you."
    "Anne chuckles."
    A neutral "I will admit, that was not an intentional pun. Haha."
    A neutral "Anyway, I suppose it’s worth mentioning that I will protect you from other vampire hunters. You could live a normal life. Well, close to one."
    A frown "And, should we ever find a cure, you would be amongst the first to get it."
    # sad music
    "Laila coughs and attempts speaking again."
    L away "You mean… there’s no… cure?"
    "At this, Laila coughs up blood. Anne glances over her shoulder at her."
    A angry "No you fool, haven’t you picked up on it? It was part of my ruse, my brilliant plan. And you fell for it."
    "Somehow, even battered as she is, Laila looks even more defeated at this definitive confirmation. She closes her eyes."
    A frown "Poor thing. Really killing the mood of my moment of triumph though. Perhaps I shall just end her now."
    "Anne takes a step towards Laila."
    "\"No!""
    "Anne halts her advance."
    A confused "And tell me, why should I spare this one AND you? I do not see how she will be of any use to my goals."
    "\"Well, just leave her until we’re done speaking.""
    A frown "I do suppose killing her now would be rather poor form, especially if you are to become my agent. Is agent the right word? Perhaps I shall call you my familiar. What delicious irony that would be."
    "You take a deep breath. Laila is safe for the time being."
    Hide l with dissolve
    # tense music
    A annoyed "Alright vampire, enough stalling. Time to make up your mind. Are you with me? Or shall I destroy you like so many that have come before?"
    "You have Anne where you want her. You can save Laila, it’s just a matter of choosing your tactics."
    menu:
    "\"Yes Anne, I’ll join you."":
        jump anneinquiry3a
    "\"I have a better idea. What if you and I became… lovers?"":
        jump anneinquiry3b

    label anneinquiry3a
    "Anne gives you a smugly satisfied smile."
    A neutral "I knew you could not resist the temptation of working with a huntress of my skill and power."
    A frown "Of course, we will have to work out the details. After all, there is the matter of how you get fed."
    "She looks you up and down, then sheathes her knife."
    A frown "But I think you will be of great use to me. And think of the joy you will receive, knowing that you are a part of making me a legend."
    A neutral "Yes, there is a bright future ahead of us, my new vampire friend."
    "Anne approaches and clasps your shoulders in a comradely fashion."
    A neutral "Perhaps we shall become friends through this endeavor. And hopefully you prove more competent than my idiot brother."
    "Anne releases you and turns towards Laila now."
    A annoyed "Now, time to finish off the broken one. Then we can clear out the rest of this disgusting backwater of a town."
    "Anne’s attention is away from you. Now is your chance."
    menu:
    "Bite her":
        jump anneinquiry5a
    "Go for her knife":
        jump anneinquiry5b

    label anneinquiry5a
    "Anne has let her guard down, and you take the opportunity to strike."
    "You lunge forward, and before Anne can react, you’ve sunk your teeth into her jugular vein."
    "Anne releases a pained gasp, and struggles to shake you off her back, but you remain attached."
    "You bite down harder, and her blood begins to flow into you. You’re invigorated, strength you’ve never known empowering you all the way to your core."
    A angry "You… traitor."
    "Anne’s voice, while weak, is full of fury. She swings her fists over her back and into you, futilely trying to beat you back."
    "You taste Anne’s feelings in her blood- her overwhelming pride in herself, her self-assuredness, her burning hatred for vampires, and her bewilderment, astonishment at how you’ve outplayed her."
    A angry "I will not go out like some animal."
    "As Anne spits these words, she throws her whole body backwards, slamming you into the floor, and you lose your grip on her."
    "She staggers to her feet and limps away from you, blood gushing from her neck in a torrent. Anne makes no attempt to cover her wound- she knows she’s dead."
    "She makes it no more than a few steps before she falters, stumbling, then collapsing to the ground, still. Her blood pools around her on the floor."
    "You rise shakily to your feet. With Anne defeated, you turn your attention to Laila."
    Hide a with dissolve
        jump chap7endcommon

    label anneinquiry5b
    "Anne has let her guard down, and you take the opportunity to strike."
    "You dash forward and pull Anne’s knife. Before she can react, you drive it into her side, between the ribs."
    "Anne’s breath is forced from her lungs and she faces you, shock and bewilderment in her eyes rapidly replaced by rage."
    "She tries to swing her fists at you, but she is off balance, and you easily step out of the way, with each attempted blow further winding her."
    "Anne opens her mouth to speak, and instead only coughs up blood. Evidently your attack has punctured a lung."
    "Still, Anne manages to recover enough breath to utter a single word."
    A frown "Why?"
    "You look pointedly past her at Laila. The huntress shakes her head."
    A angry "You… fool. My triumph… reduced to nothing."
    "Her words come slowly and forcefully, each exhalation a battle in a war she is losing."
    "Anne makes a final desperate attempt to claw at you, but you continue to back out of her reach with ease. She drops to her knees."
    You look down on the once-mighty huntress, brought low by her hubris. She glares back, her golden eyes burning with hatred. And then, the fire in her eyes begins to dim."
    "With a final violent cough of blood, Anne keels over, dead."
    "Now that the Velsing has been taken care of, you turn your attention towards Laila."
    Hide a with dissolve
        jump chap7endcommon

    label anneinquiry3b
    "Anne stares at you, baffled"
    A confused "What? Where is this coming from?"
    "She looks as if she is about to shout at you, then relaxes."
    A frown "No, I see where this is coming from. You cannot deny my fabulous looks and regal poise."
    A neutral "I’m so glad that even your kind can appreciate true beauty."
    "Anne cocks her head to examine you from a new angle."
    A frown "And indeed, you are not of an unseemly sort. You’re almost… comely."
    A confused "But to be romantically involved with a vampire? It would be unheard of, it is unprecedented, it-"
    "Anne’s eyes alight with a new realization."
    A neutral "It would be a first of its kind conquest. I, the Velsing to tame the most dangerous of creatures."
    "A change has come about Anne. She re-sheaths her knife and approaches you slowly."
    "You see her eyes gleaming gold over the top of her glasses. They burn with a new intensity, one you have not seen before."
    "Before you know it, she has crossed the room and stands before you."
    "She leans in close to you and you feel her breath, hot, animalistic, on your neck. She smells of woodlands, of vast nature untamed, of life unbridled. You can feel her passion, almost as if it’s your own, a raging fire which cannot be quelled. Still, within you an even greater hunger resides."
    "Anne runs a hand across your cheek- she is warm, and that warmth lingers on your face even after she has withdrawn."
    "She whispers directly in your ear, almost silent, her words carried on the barest vibrations passing her lips. The once-loquacious huntress is now reduced to something much simpler."
    A neutral "Yes. I want you."
    "Indeed, you want her too. You hear her heart pounding with desire, blood flowing through her, more vibrant and full of life than any other you have perceived since you turned."
    "There is no room between the two of you, and Anne closes her eyes to kiss you. Now is your chance."
    menu:
    "Bite her":
        jump anneinquiry4a
    "Go for her knife":
        jump anneinquiry4b

    label anneinquiry4a
    "As Anne lets her guard down, you strike."
    "The vampire hunter is not expecting your teeth in her jugular vein, and she writhes in panic trying to pull you off of her, but even her athletic skill is no match for your vampiric power."
    "She wheezes in protest."
    A angry "Not… like… this."
    "Still, you bite down harder, and her blood begins to flow into you. You’re invigorated, strength you’ve never known empowering you all the way to your core."
    "As you feed, Anne’s terror intensifies, the once haughty huntress brought low. Her heart beats faster, only accelerating her demise."
    "You taste Anne’s feelings in her blood- her overwhelming pride in herself, her self-assuredness, her burning hatred for vampires, and just a hint of begrudging admiration for you. You’ve outplayed her."
    "Anne’s heartbeat reaches a crescendo now, and the huntress’s struggles cease. The heartbeat now slows to a crawl, and Anne releases one last exhausted breath, before going limp. The heartbeat is gone, and Anne with it."
    "You detach from Anne, whose lifeless body collapses to the ground in an undignified manner. Now you turn your attention to Laila."
    Hide a with dissolve
        jump chap7endcommon

    label anneinquiry4b
    "As Anne lets her guard down, you strike."
    "While her lips press against yours, you draw her knife and drive it into her right side, between her ribs."
    "Anne breaks away from you gasping. You’ve evidently succeeded in puncturing a lung, and now the huntress struggles for breath."
    "Anne stumbles back, trying to pull the blade from her side, but doubles over in pain. She coughs and blood trickles from her mouth."
    A frown "...Why?"
    "You look pointedly in Laila’s direction. Anne scowls."
    A angry "We could… have been amazing. You… fool."
    "Her words come slowly and forcefully, each exhalation a battle in a war she is losing."
    "You approach Anne, who shambles further back."
    A angry "Stay back, you monster."
    "She spits these words with venom, and breaks out into a fit of coughing, blood splattering on the floor in front of her."
    "You look down on the once-mighty huntress, brought low by her vanity. She glares back, her golden eyes burning with hatred. And then, the fire in her eyes begins to dim."
    "Anne topples over with a death rattle, landing on the ground with a dull thud."
    "With the Velsing taken care of, you turn your attention to Laila."
    Hide a with dissolve
        jump chap7endcommon

    label chap7endcommon
    "Before you approach Laila, quickly examine Anne’s corpse, finding the reverse echolocator and disabling it. Without the interference you hope to better help Laila."
    "As you step towards Laila, you realize things are worse than you thought. There is a concerning amount of blood pooled on the floor around her, and Laila looks even paler than she normally does. The sword remains lodged in her."
    "You’re not sure how, but you can sense that Laila is dying."
        jump laila_chapter8
    End of chapter 7

    label laila_chapter8
    scene mansionInt
    # sad music
    "Anne Velsing is dead, and Laila could soon be joining her, the vampire bleeding out before your eyes."
    "\"Laila, this shouldn’t be able to kill you!""
    "Laila struggles to open her eyes. She gives you a bleary look."
    Show l away with dissolve
    L away "Well, I’m not a vampire biologist. We need blood to live, and I’ve lost a lot of it, it looks like."
    "She stops for a moment, the pain of speaking evident in her face."
    L away "And I think… there’s something on the sword. It stings, my body can’t heal itself like it normally can."
    "Laila winces now, her speech shifting the sword."
    "\"Okay, well the first thing we need to do is get that sword out of you.""
    "Laila shakes her head."
    L away "No, I’m dying [player]. You need to leave. We don’t know if miss bitch over there has friends."
    "She gives an angry look at Anne’s corpse."
    "\"I’m not leaving you after how far we’ve come.""
    "Before Laila can protest any further, you hoist her off of the sword. She coughs up a surprising amount of blood."
    "You cradle Laila’s bloody form in your arms, taking her to the chair you fell into earlier and set her down gently."
    L angry "Damn that hurt. Some warning would be appreciated next time."
    L neutral "Sorry, thank you. But I don’t know what you can do for me."
    "You kneel next to Laila. Though you have only known her a few days, you cannot deny the deep feelings you’ve developed for her."
    "You would be devastated if you were to lose her."
    "\"Surely there’s something we can try!""
    "Laila merely stares at you grimly."
    L away "Even if I were to start healing now, I don’t know if I’d want to."
    "\"What do you mean?""
    L away "There is no cure. And this, the events of the last few days, I cannot bear to go through it again. I’ve run for so long, and for what? To watch more friends die?"
    L away "No, better to go now, knowing you’re safe and Anne is in hell."
    "You gaze into her eyes, and see they are filled with grief. While she is not terribly older than you, the weight of the last decade rests heavily on her."\
    "\"What if I got you some of Anne’s blood, she’s not… empty? You could get some of your strength back.""
    L away "I told you, I don’t want to go on."
    "\"Please, just try, for me.""
        
        If laila_affection >14 jump lailaTrueEnding
        If laila_affection > 6 & drank her blood jump lailaGoodEndingA
        If laila_affection > 6 & did not drink her blood jump lailaGoodEndingB
        If laila_affection < 7 & drank her blood jump lailaBadEndingA
        If laila_affection < 7 & did not drink her blood jump lailaBadEndingB

    label lailaTrueEnding
    # romantic music
    "Laila stares into your eyes for a long while before responding."
    L neutral "Okay. Let’s try it. I don’t want my passing to hurt you."
    "You run over to Anne’s corpse and scoop some of the pooling blood into your hands. It’s still warm and consequently rather disgusting."
    "You return to Laila and hold your cupped hands out to her, which she sips from delicately."
    "Once she’s done drinking, Laila makes a face at you."
    L angry "This better work, because that blood was foul, and I refuse to let that be my last meal."
    "Even as she speaks, you notice the wound in Laila’s abdomen beginning to heal- the jagged hole ripped by the sword is growing back into unbroken skin."
    "Laila follows your eyes down."
    L excitedl "Well, I’ll be damned."
    "Laila is able to sit up straighter now, and takes a deep breath in, no longer in nearly as much pain."
    L neutral "Well, here I am, ready to keep going on living, with nothing to live for."
    "You pointedly frown at her."
    L neutral "What?"
    "\"You have me.""
    "Laila falters a moment before speaking."
    L away "I… I suppose you’re right. I didn’t want to admit it. But I don’t think I can deny it."
    L neutral "You’ve done more for me, [player], than anyone else in recent memory. You came with me on this crazy adventure that nearly got us both killed."
    L smile "Without the Velsings to worry about, I don’t have to run anymore. I can settle down, start a life… with you."
    L smile "I’ve got it bad for you, [player]. I want to be with you. You’ve given me something to look forward to."
    "Before Laila can say more, you lean in and kiss her. She seems startled for a moment, perhaps not expecting you to return her feelings quite so suddenly, but any hesitancy is gone quickly."
    "Laila returns the kiss with passion, pulling you close to her. You make no objection. The two of you embrace with the vigor of those who have just escaped a brush with death, seeking to make the most of your time."
    "After a couple minutes pass- during which your kiss almost certainly became a makeout session- Laila stops you, gasping for breath."
    L neutral "You know [player], we’ve been together for every step of your journey, and quite frankly I’m amazed at how well we understand each other."
    L smile "I don’t think it’s chance that we met. I don’t believe in stuff like fate or destiny, but it’s hard to deny what has passed between us."
    L smile "And you know, an eternity like this would have been unbearable without someone who understands me, who understands what I feel about being a vampire."
    L away "And I know this is weird to come in the middle of a heated moment between us, but I felt it needed to be said. I’m sorry."
    L smile "I guess I could have put it more simply- I love you, [player]. I hope you realize that."
    "Laila averts her eyes and gives a shy smile."
    L away "It’s been a while since I’ve said that to anyone."
    menu:
    "\"I love you too, Laila."":
        jump lTrueEndingA
    "Kiss her"
        jump lTrueEndingB

    label lTrueEndingA
    "You confess your shared feelings to Laila, and her smile widens."
    L smile "That means the world to me."
        jump lTrueEndingCommon

    label lTrueEndingB
    "You take hold of Laila’s hand and pull her close to you, before gently kissing her. She returns the kiss with an intensity unlike any you have experienced thus far. After a moment she breaks away."
    L smile "That means the world to me."
        jump lTrueEndingCommon

    label lTrueEndingCommon
    L excited "You know player, let’s leave this all behind. This town, these people. We can go someplace new and be ourselves. Come with me back to New Mexico."
    "\"Really?""
    L excited "Really! So what if we can’t live by day, we’ll be together. Even at night, the desert is beautiful."
    "\"Alright, let’s do it.""
    "And so you and Laila return to your apartments and pack your belongings. Before you go, though, you relieve the mansion of some of the portraits upon its walls. You have no doubt you could fund a comfortable life with their sale."
    "You otherwise leave the Velsing mansion, and Anne’s corpse, abandoned."
    "The following evening the two of you hit the road- much to your surprise, Laila happens to drive a black 1990 corvette."
    "As she explains, she inherited the car from her mother who was, in her words, a certified badass."
    "The two of you travel by night and sleep by day in the various motels that dot the vast expanse of the American countryside. Well, when you two manage to sleep. You are, after all, a newly minted couple eager to become intimately acquainted."
    "After many miles forests give way to plains, and plains give way to desert scrub. Mesas and cacti rise out of the night and you find yourselves in New Mexico."
    "The two of you decide to settle in Santa Fe. The paintings from the Velsing mansion prove just as valuable as you suspected, and you and Laila are soon able to move into a modest home with the proceeds from their sale."
    "As time passes, you find your supernatural bond with Laila, formed from drinking her blood, has begun to develop. You can sense each other’s feelings, and sometimes communicate wordlessly."
    "Your relationship only deepens and strengthens because of this newfound connection, with disagreements between the two of you resolving quickly and amicably. Perhaps this should be standard practice for all couples."
    "You and Laila become known amongst the artists and bohemians of Santa Fe as the lovely eccentric couple who host fabulous midnight parties, and are remarkably supportive of the local blood bank."
    "Laila’s dissatisfaction with the vampiric life rapidly fades as the stability of your new lives becomes evident. She is happy and safe with the one she loves, far from the worries that once plagued her."
    "You, too, are content, living a life you could have once only imagined, with the woman you love by your side."
    ""And so it was, you and Laila together, into the future, forever."


    label lailaGoodEndingA
    # romantic music
    "Laila stares into your eyes for a long while before responding."
    L neutral "Okay. Let’s try it. I don’t want my passing to hurt you."
    "You run over to Anne’s corpse and scoop some of the pooling blood into your hands. It’s still warm and consequently rather disgusting."
    "You return to Laila and hold your cupped hands out to her, which she sips from delicately."
    "Once she’s done drinking, Laila makes a face at you."
    L angry "This better work, because that blood was foul, and I refuse to let that be my last meal."
    "Even as she speaks, you notice the wound in Laila’s abdomen beginning to heal- the jagged hole ripped by the sword is growing back into unbroken skin."
    "Laila follows your eyes down."
    L excitedl "Well, I’ll be damned."
    "Laila is able to sit up straighter now, and takes a deep breath in, no longer in nearly as much pain."
    L neutral "Well, here I am, ready to keep going on living, with nothing to live for."
    "You pointedly frown at her."
    L neutral "What?"
    "\"You have me.""
    "Laila falters a moment before speaking."
    L away "I… I suppose you’re right. I didn’t want to admit it. But I don’t think I can deny it."
    L neutral "You’ve done more for me, [player], than anyone else in recent memory. You came with me on this crazy adventure that nearly got us both killed."
    L smile "Without the Velsings to worry about, I don’t have to run anymore. I can settle down, start a life… with you."
    L smile "I’ve got it bad for you, [player]. I want to be with you. You’ve given me something to look forward to."
    "Before Laila can say more, you lean in and kiss her. She seems startled for a moment, perhaps not expecting you to return her feelings quite so suddenly, but any hesitancy is gone quickly."
    "Laila returns the kiss with passion, pulling you close to her. You make no objection. The two of you embrace with the vigor of those who have just escaped a brush with death, seeking to make the most of your time."
    "After a couple minutes pass- during which your kiss almost certainly became a makeout session- Laila stops you, gasping for breath."
    L neutral "Before we go any further, let’s do something about the corpse. Even dead the bitch is spoiling my fun."
    "She casts a somewhat rueful gaze towards Anne’s body."
    "Laila, now fully healed it seems, assists you in dragging the huntress’s corpse out of the grand hall and a remote drawing room- where you also happen to find the levers which deactivate the mansion’s lockdown mechanism."
    "Afterwards, you and Laila spend some time discussing your future. This mansion, with all its accouterments and lavish furniture, would make a lovely place to live, provided its exterior sees some renovation. This is where your future will be."
    "You and Laila spend the remainder of the night, and much of the following day, … ‘breaking in’ each of the mansion’s numerous rooms. By the end of it, even with your vampiric enhancements, the two of you are thoroughly exhausted."
    "The following evening, you call up Cass and she assists you and Laila in burying Anne out in the woods. For all the trouble she caused, she deserves at least that much."
    "You and Laila are together almost always in the subsequent nights, splitting your time between repairing the mansion and locating the remaining vampires in town. You let them know the danger has passed and, should they need it, your doors are open to provide a safe haven."
    "As time passes, you find your bond with Laila, formed from drinking her blood, has begun to develop. You can sense each other’s feelings, and sometimes communicate wordlessly."
    "Your relationship only deepens and strengthens because of this newfound connection, with disagreements between the two of you resolving quickly and amicably. Perhaps this should be standard practice for all couples."
    "In a few months, the mansion is repaired, and you and Laila open it for fabulous midnight parties. Vampires and regular humans attend, with the vampires on their very best behavior, and the humans never suspecting a thing."
    "All in town would come to know of the eccentric kind-hearted couple who fixed up the old mansion on the hill, were never seen by day, and were remarkably supportive of town blood drives; a point of pride for all."
    "And so it was, you and Laila together, into the future."
    END

    label lailaGoodEndingB
    # romantic music
    "Laila stares into your eyes for a long while before responding."
    L neutral "Okay. Let’s try it. I don’t want my passing to hurt you."
    "You run over to Anne’s corpse and scoop some of the pooling blood into your hands. It’s still warm and consequently rather disgusting."
    "You return to Laila and hold your cupped hands out to her, which she sips from delicately."
    "Once she’s done drinking, Laila makes a face at you."
    L angry "This better work, because that blood was foul, and I refuse to let that be my last meal."
    "Even as she speaks, you notice the wound in Laila’s abdomen beginning to heal- the jagged hole ripped by the sword is growing back into unbroken skin."
    "Laila follows your eyes down."
    L excited "Well, I’ll be damned."
    "Laila is able to sit up straighter now, and takes a deep breath in, no longer in nearly as much pain."
    L neutral "Well, here I am, ready to keep going on living, with nothing to live for."
    "You pointedly frown at her."
    L neutral "What?"
    "\"You have me.""
    "Laila falters a moment before speaking."
    L away "I… I suppose you’re right. I didn’t want to admit it. But I don’t think I can deny it."
    L neutral "You’ve done more for me, [player], than anyone else in recent memory. You came with me on this crazy adventure that nearly got us both killed."
    L smile "Without the Velsings to worry about, I don’t have to run anymore. I can settle down, start a life… with you."
    L smile "I’ve got it bad for you, [player]. I want to be with you. You’ve given me something to look forward to."
    "Before Laila can say more, you lean in and kiss her. She seems startled for a moment, perhaps not expecting you to return her feelings quite so suddenly, but any hesitancy is gone quickly."
    "Laila returns the kiss with passion, pulling you close to her. You make no objection. The two of you embrace with the vigor of those who have just escaped a brush with death, seeking to make the most of your time."
    "After a couple minutes pass- during which your kiss almost certainly became a makeout session- Laila stops you, gasping for breath."
    L neutral "Before we go any further, let’s do something about the corpse. Even dead the bitch is spoiling my fun."
    "She casts a somewhat rueful gaze towards Anne’s body."
    "Laila, now fully healed it seems, assists you in dragging the huntress’s corpse out of the grand hall and a remote drawing room- where you also happen to find the levers which deactivate the mansion’s lockdown mechanism."
    "Afterwards, you and Laila spend some time discussing your future. This mansion, with all its accouterments and lavish furniture, would make a lovely place to live, provided its exterior sees some renovation. This is where your future will be."
    "You and Laila spend the remainder of the night, and much of the following day, … ‘breaking in’ each of the mansion’s numerous rooms. By the end of it, even with your vampiric enhancements, the two of you are thoroughly exhausted."
    "The following evening, you call up Cass and she assists you and Laila in burying Anne out in the woods. For all the trouble she caused, she deserves at least that much."
    "You and Laila are together almost always in the subsequent nights, splitting your time between repairing the mansion and locating the remaining vampires in town. You let them know the danger has passed and, should they need it, your doors are open to provide a safe haven."
    "As time passes, you and Laila find you are not quite a perfect couple. There are occasional squabbles, a tiff here and there. But you two emerge from each conflict stronger and closer."
    "Nothing can break the bond you two have formed."
    "In a few months, the mansion is repaired, and you and Laila open it for fabulous midnight parties. Vampires and regular humans attend, with the vampires on their very best behavior, and the humans never suspecting a thing."
    "All in town would come to know of the eccentric kind-hearted couple who fixed up the old mansion on the hill, were never seen by day, and were remarkably supportive of town blood drives; a point of pride for all."
    "And so it was, you and Laila together, into the future."
    END

    label lailaBadEndingA
    #sad music
    "Laila looks at you firmly."
    L angry "No [player], I don’t have anything left to live for. I get you might feel deeply for me, but I can’t say I feel the same way. This is it."
    "She lets out a rough cough, and a stream of blood spews forth."
    L away "Please, I don’t have much longer, don’t fight with me in my last moments. Let’s think about the good you’ve done here."
    L smile "So many other vampires are going to be safe because of you. They can live the kind of life I would have wanted."
    L smile "Go out and bring good into the world, okay? And try to avoid turning into a winged rodent, if you can. Do that specifically for me."
    "Though it is very difficult for her, Laila laughs at her final remark."
    "With a deep sigh, Laila closes her eyes, her body takes on a stillness like death, and you know she is gone from the world."
    Hide l with dissolve
    "You are about to be overcome with grief when you feel a shooting pain that begins in your heart, and radiates out to every extremity of your body."
    "You fall back onto the floor, your body shaking uncontrollably. There is a burning inside your very veins you cannot escape."
    "You’re baffled. What is going on? You weren’t cut by the Velsing sword, and yet it feels as if you’re dying."
    "And then you remember- you took Laila’s blood. Whatever bond you two shared has been severed by death, and now it is as if you yourself are dying."
    "You regain enough control to drag yourself across the floor towards the front door. Maybe you can find Cass, maybe she can help."
    "After much effort you manage to get to your feet and you try the front door- it’s locked. Whatever mechanism Anne used to seal you in has not yet been disabled. All the while, the pain within you grows worse."
    "You decide to make your way deeper into the mansion, to see if there’s another way out."
    "You make it to Anne’s body before your legs lock beneath you, and you fall over. Your arms almost immediately follow suit, growing stiff and immobile."
    "As you lie on the floor, you listen for the rush of your blood- and find it is almost nonexistent. You realize in horror that Laila’s death has caused the coagulation of your own blood."
    "You can still think, and look straight ahead- it appears your eyes have grown still as well- but your body is effectively a corpse, with you locked inside as a prisoner."
    "And so you lie like that. For hours."
    "Then the hours turn to days."
    "And the days turn to weeks."
    "And the weeks to months."
    "And the months to years."
    "The mansion lies abandoned, no other Velsings come to check up. No one from the town cares enough to investigate the locked mansion on the hill."
    "You pass into a thoughtless oblivion, aware, unageing, but immobile, mute, frozen."
    "..."
    "..."
    "..."
    "One day, in the distant future, the door to the mansion is kicked in- a high rise is to be built here, and the place cleared out. The sun’s rays that filter in are a merciful release, and you burn away."
    "And you are no more."
    END

    label lailaBadEndingB
    #sad music
    "Laila looks at you firmly."
    L angry "No [player], I don’t have anything left to live for. I get you might feel deeply for me, but I can’t say I feel the same way. This is it."
    "She lets out a rough cough, and a stream of blood spews forth."
    L away "Please, I don’t have much longer, don’t fight with me in my last moments. Let’s think about the good you’ve done here."
    L smile "So many other vampires are going to be safe because of you. They can live the kind of life I would have wanted."
    L smile "Go out and bring good into the world, okay? And try to avoid turning into a winged rodent, if you can. Do that specifically for me."
    "Though it is very difficult for her, Laila laughs at her final remark."
    "With a deep sigh, Laila closes her eyes, her body takes on a stillness like death, and you know she is gone from the world."
    Hide l with dissolve
    "You are overcome with overwhelming grief. This beautiful wonderful woman is gone. If only things had been different, had you been closer to her, things might have played out differently."
    "Despite the injuries she suffered before passing, Laila looks serene. She passed from this world to a better place, happy."
    "You leave Laila where she is, and decide to investigate the mansion for a way to disable whatever mechanism locked the doors and barred the windows."
    "After some time searching, you find some levers in a drawing room on the second floor, which seem to lift the security of the place."
    "You phone Cass to let her know what has happened, and she arrives to keep you company, and help you deal with the remains."
    "You sleep in the mansion during the day, and the following evening you and Cass bury Laila in the forest. You leave Anne’s body in the mansion, perhaps as a warning to any future Velsings who might come."
    "You return to your apartment and begin doing what Laila did- working nights at bars to eke out a living."
    "Afterwards, you and Cass drift apart. You are listless with Laila gone, and Cass has a full human life to live."
    "You seek out what’s left of the vampire community in town, but after the Velsing assault, those who aren’t dead dare not congregate. The current threat may have passed, but few believe it is gone for good."
    "Many of those who remain blame you for Laila’s death. She was well-liked, and the troubles started after she took you under her wing, after all."
    "You think often of her- her kindness, her humor and, perhaps most of all, the great sorrow she lived with. The plight of her condition, her desire to return to the world of the living, to the waking world and the sun."
    "You know you will never forget her. And you respect her final wishes. You do what you can to bring some small amount of good into the world- you will sometimes stop petty criminals and miscreants in the night."
    "And, of course, you never turn into a bat, the ‘winged rodent’ Laila so disdained."
    "And so your nights go on, monotonous, alone. The town changes around you, but you do not. You are a fixture stuck in the past."
    End






    Chapter 4 Cassandra
    label cass_chapter4
    # Tense Music
    "You lose sight of Cass after a while, but for some reason you can still tell where she is."
    "It’s as if you can sense her, hear her heartbeat in the air"
    "You hear the Velsings gaining on you, and you remember the powers Cassandra mentioned earlier."
    Show a with dissolve
    "You see Anne Velsing chasing after you with ferocity."
    #angry Anne
    A "Come here bloodsucker!"
    label 4fightAnne
    menu:
    "Turn into a bat"
    jump battempt
    "Try hypnosis"
        jump hypnosis
    "Try floating"
        jump floattempt
    label battempt
    "You try to picture yourself as a bat but you can’t focus."
    "Anne is gaining on you."
    #Anne Amused
    A "I’m screaming! You can’t even turn into a bat! Pathetic."
        jump 4fightAnne
    label battempt
    "You jump as high as you can but you can’t get yourself to float"
    "You trip and fall, causing Anne to gain on you."
    #Anne Amused
    A "Are you trying to fly? How long have you been a Vampire, a day!"
    "She doesn’t know that she’s more or less right…"
        jump 4fightAnne
    label hypnosis
    "This is a gambit you can’t afford to fail on."
    "You stare into Anne’s eyes, trying desperately to get her to stop chasing you."
    "It doesn’t seem to be working, but then…"
    "You both freeze in your tracks."
    "She can’t move, but you can’t move either."
    "You stare at each other, both powerless."
    "Even though her mouth isn’t moving, you can almost hear Anne say:"
    A "You Vermin! I should have known you’d be a E-vamp!"
    "E-Vamp? What the hell is an E- Vamp?"
    A "Emphatic Vampire? E Vamp? Hypnotiser? Oh my god, you are one day old. Can’t let Han hear about this."
    "How did she hear your thoughts?"
    A "Oh for crying out… ARE YOU STUPID? You are hypnotizing me! You’ve made a perverse psychic link between us!"
    A "You’re freshly stolen blood, so you don't know how to do any actual hypnosis stuff, but as long as you don't move, I don’t move."
    A "BUT! Before you gloat, keep in mind that as soon as you move or break concentration even a little, I’ll slit your pretty little throat!
    "You see. You're both in a stalemate. If you move, she kills you. But if you don’t, she’s trapped."
    "You hear a rustling in the wood, and as if in sync, you both think–"
    A "Oh Shit"
    "Han Velsing Appears , lugging an barely conscious Cassandra behind him.
    Show h with dissolve
    Show c doubt with dissolve
    "You take the moment to let Anne go and dash into the bushes"
    #Batbashers are just like standin name
    H "The heir to the Velsing bloodline, head of the Batbashers, and you couldn’t even kill a day old vamp?"
    A " I got caught off guard ok! Don’t tell the others."
    H "Like you didn’t tell dad about Ren? Oh wait…"
    A "We were young Ok! It was ages ago! Why are you still fixated on that!"
    H "Why am I still… WHY AM I STILL FIXATED ON THAT?
    H "Are you for real?"
    "As they bicker, you have time to focus." 
    "You finally turn into a bat and sneakily fly into the trees and hide"
    A "Look, I’ve said I’m sorry for outing you a million times. It’s in the past! Dad’s gone!"
    H " So you betray me, exploit my weakness, stab me in the back… and now that it’s all over-"
    H " You get to be all "We’re all in this together! We’re family!"
    H "In case you forgot, I was supposed to be the successor!"
    H " And it wasn’t until you exploited my weakness that you got in charge!"
    H "So yes, I am gonna tell the others."
    A "OH COME ON!" 
    A "You never know when to give up!"
    A "I’m being magnanimous! I’m winning with grace!"
    A "If I were a worse person, you wouldn’t even be a vampire hunter anymore!"
    H "Forget it. 
    #Maybe this oscillates with some angry and disgusted faces for the Velsings
    "You feel powerless"
    "These aren’t just some vampire hunters, they’re the heads of the whole organization."
    "You need to figure out how to get Cassandra out of there!"
    menu:
    "Attack the Velsings"
        jump 4cvelsingattack
    "Get the Velsings to chase you"
        jump 4cvelsingchase
    "Wait in the tree"
        jump 4cwaitintree
    label 4cvelsing attack
    "You decide that an all out brawl is the only way to allow Cassandra to escape."
    " You aren’t much of a fighter, but you could maybe turn back into a human and fall on someone?"
    menu:
    "Fall on Han"
    "Fall on Anne"
    "You miss both and fall on the ground next to them."
    "Your whole body hurts like hell, but you seem to have created a cloud of dust."
    "Both Velsings are coughing as you grab Cassandra and run as far away as possible."
        jump 4cwalk
    "You walk as fast as you can until you get out of the woods and reenter the town"
    scene street
    label 4cvelsingchase
    "You fly in front of the Velsing’s and dash away."
    #both objective
    A "You won't be able to tell the others anything once I catch [pronoun]!"
    H "Sigh… not if i’m the one who catches [pronoun]"
    "You fly as fast as you can as the Vellsings fire stakes and bullets at you."
    Hide h with dissolve
    Hide a with dissolve
    "Once you zoom far enough that you don’t hear them, you transform back, tumbling into the grass."
    "Turning to a bat has you beyond exhausted. You luckily still have your phone on you, so you text  Cassandra your location and pass out."
    scene black with fade
    scene forest
    Show c neutral with dissolve
    C neutral "Hey, you. You’re finally awake."
    menu: 
        "What.. happened..":
        "Are you ok?":
            $ cass_affection+=1
        "I’m in deep, deep pain.":
    C neutral "Let’s get you up, we need to head home.
    "You walk as fast as you can until you get out of the woods and reenter the town"
    scene street
        jump 4cwalk
    label 4cwaitintree
    "You wait in the tree hoping for an opening."
    A "Anyways, who’s the girl?"
    H "She’s a human. She seems to be close to some of the vampires, but…"
    H "... she’s not a vampire yet. I’ve been cooking up a plan for her.
    H "For tonight though, I just wanted to get her to safety."
    C "Wha… Whats going on?"
    A "Ahh, she’s awake! Now what?"
    H "Now we find the other vamps. She can find her way back home."
    Hide h with dissolve
    Hide a with dissolve
    "Once you made sure the Velsings were far enough away, you followed Cassandra as she ran home.
    "What was Han talking about? What did he have planned for her?"
    scene street
    "As You both finally get back in town, you turn back into a human."
    menu
    "Cassandra! It’s me"
    C "[player]! I’m so happy you’re ok! That was terrifying!
        jump 4cwalk
    label 4cwalk
    # Neutral Music
    "You both walk down the street, catching your breath after the trauma you just experienced."
    "It all slowly starts to sink in."
    "You’re being hunted. Hunted by trained professionals."
    "Laila hasn’t been returning your calls, she might be dead."
    "Who knows what could have happened to Cassandra?"
    "You look at her, thinking about everything that happened so far"
    #Want to have a couple variables here, need help.
    #If you chose kiss:
    " The fall, the almost kiss."
    "The adrenaline of it all, the danger."
    "You feel like you can’t let anything go unsaid."
    "You don’t want to regret not telling her how you feel.
    "But you also worry about bringing her closer into your life."
    "Closer to danger."
    C "Look, I know you have something on your mind, please tell me!"
    menu
    "/""Cassandra, I don’t think you should be around me anymore.":
    jump 4cavoid
    "/"Cassandra, I need to tell you something":
    jump 4cconfess
    label 4cavoid
    C doubt "What… look i knew you being a vampire was dangerous from the get go, ok?"
    C "I’m not going to let you die just so I can be safe ok!"
    C "You know me. You know I’d never give up on you. Because I care about you!
    C "Because i Lo-"
    C "Because I like you!"
    "You heard that. You heard what she wanted to say."
    "But why is she holding back?"
    "Is it fear of losing a friendship?"
    "Or something else?"
    jump 4cend
    label 4cconfess
    "/"Cassandra, what if I turned you into a vampire?"
    "/" With these hunters after us… with the danger I'm putting you in…"
    "/" Maybe you could have powers too?
    C smile "Really? Wow, I need a minute to think about this…"
    C "I've been dreaming of being a vampire since I was a kid…"
    "She was right. You remember nights in middle school where you played vampires and werewolves together."
    "Reading the moonlight trilogy…watching Nosferatu…"
    C "But… 
    "Cassandra seems conflicted, lost in thought"
    "Clearly something is holding her back… but what?"
    "You decide not to press her on it. It's been a long night."
    jump 4cend
    label 4cend
    scene apartment
    "You finally make it home and the exhaustion starts to hit.
    "You let Cassandra stay over, knowing she wouldn’t leave you alone after all this." 
    "In exhaustion you fall asleep in each other’s arms."
    "You drift away, anxious for what comes next."
        jump cass_chapter5
    END OF PART 4
    Ch 5
    # Tense Music
    "You feel it. The hunger."
    "It grows every day, tormenting you, torturing you."
    "You haven’t heard from Laila since the night of the attack, and you have no idea how to get blood otherwise."
    "Well… except for the obvious." 
    "But you wouldn’t do that…Would you?"
    "Cassandra’s been bringing you raw meat, and it's been keeping you alive."
    "But the hunger is getting worse."
    "You get a text from Cassandra, inviting you to the library."
    scene street
    "You strut through the night streets, hunger pounding through you."
    "A strange figure approaches you, pushing you down."
    "Stranger""This is for the Bloodbashers!"
    "As you get back, the stranger trips and falls."
    "They knock themselves unconscious."
    "They attacked you first… would it really be so bad if you drank their blood?"
    menu
    "Drink their blood"
        jump 5cblooddrink
    "Leave them alone"
        jump 5clte
    label 5cblooddrink
    "You bite into their neck and suck their blood."
    "After all of your hunger, you feel a sense of relief."
    "You let go before you kill them, and rush to the library."
    scene library
    Show c smile with dissolve
    c"Hi [player]!"
    C doubt "Is that fresh blood on your mouth?"
    "\ "Umm… No?"
    $ cass_affection-=3
    "\ "Anyway… Why did you call me here?"
    jump 5cb
    label  5clte
    "You leave them knocked out and rush to the library."
    scene library
    Show c smile with dissolve
    c"Hi [player]!"
    C confident "I’ve got something important to show you!"
    jump 5cb
    label 5cb
    # Romantic Music
    C neutral"You know the book I told you about? The diary of Bran Velcant?"
    C " I finished it, and well.."
    C doubt "It does not end well…"
    C "Bran Velcant’s brother, Abram, always had a contentious relationship with him."
    C neutral "They used to be a part of this group of vampire hunters called Batbashers."
    C "But when Bran turned, Abram was unwilling to sell out his own brother."
    C "I was kind of hoping that Abram would learn to accept Bran…"
    C doubt "But he didn’t."
    C neutral "The diary stops abruptly, it was never finished."
    C "But in this book.."
    "Cassandra pushes another huge book titled A Historie of the Order of the Batbasher towards you"
    C" Someone named Abram kills his own vampire brother to found this order."
    C "And look at his last name"
    "You open the book and see Abram’s full name."
    "\ "Abram Van Velsing."
    C "Abram killed Bran, and coined the motto "firmitas voluntatis in fraudem ""
    C smile "It’s been a while since I took Latin, so it’s a little rusty…"
    C "But it translates to "strength of will over the deceit of the heart"
    C "Basically, Abram founded this organization on betrayal, on hurting even those you care about the most for "justice"
    "\ And that organization became the Batbashers, led by the Velsing siblings.."
    C wink "You’re so sharp, [player]!"
    C smile "So, I grabbed every book I could find with any relevance."
    "You eye Cassandra’s mountain of books…"
    "This is going to be a really long day isn’t it."
    C "Let’s get researching!"
    "You toil through the mountain of books, hoping to find more information about the Batbashers."
    "After a while, you start to get into a groove."
    "It reminds you of when you and Cassandra studied together before a big test."
    "Just like back then, Cass brought a bunch of cans of Demon Energy Drinks to fuel the study sesh."
    "She had gone through the "Big Blue Betrayal", "Red Anguish", and "Emerald Elation" flavors."
    "You were getting tired, so you decided to drink the…"
    menu
        "Green Apple Envy":
        "Ultra Sour Ushy Gushy":
        "Brorple Smorp":
        "That one trans flavor you forget the name of, but it has baby blue and hot pink on it":
            $ cass_affection+=1

    C wink "Nice choice, [player]"
    Show c smile
    "You both take a break and chat for a while."
    ‘You talk about the bizarre things you only discuss during a long study sesh on 3 cans of monster."
    "Would you be my friend if you were a worm, would you rather bend fire or water, etc."
    "And eventually, as the day goes on, the conversation steers towards…"
    C smile "You know, Pet Names! Like fun little names people call their partner!"
    C doubt "My awful ex Darryl called me honey bun, and at the time I liked it…"
    C smile "But now I can’t even look at a honey bun without gagging."
    C "I feel like I’d love to be called something like Sand Pie, or Cutums, or something cool like C-sharp!"
    jump 5cpetnamechoice
    label 5cpetnamechoice
    #Save this as $casspetname variable except honeybun
    "I feel like what suits you the most is…"
    menu:
        "Sand Pie"
            Set $casspetname to "Sand Pie"
            jump to 5cc
        "Cutums"
            Set $casspetname to "Cutums"
            jump to 5cc
        "C-Sharp"
            Set $casspetname to "C-Sharp"
    jump to 5cc
        "Honey Bun"
            jump to honeybun
    label honey bun
    C doubt "Haha, very funny. What’s your real choice?"
    jump 5cpetnamechoice
    C smile "[casspetname], huh."
    C wink "I love it!"
    C smile " I’d love for my next partner to call me that some day."
    C confident "Wait, now I HAVE to figure out one for you!"
    C smile "You’ll find a cool person someday, and they have to call you a cool name too!"
    C "Something like Red, you know, cause of the blood?"
    C neutral "Or Echo, cause of echolocation, cause… you can turn into a bat?"
    C wink "Or Cutums! You know… cause you’re cute?"
    C smile "What do you think?"
    "\ Hmm, I really like…"
    #Save this as $petname variable
    menu:
        "Red"
            Set $petname to "Red"
        "Echo"
            Set $petname to "Echo"
        "Cutums"
            Set $petname to "Cutums"
        "\ "Actually, I feel like I just like being called by my first name."
            Set $petname to $name
    C smile "[petname] suits you best of all, for sure."
    C "I’m sure your next partner would love calling you that, it really suits you."
    C doubt "I know your last relationship didn’t go so well…"
    C smile "But you’ll get someone you deserve soon! I feel it in my bones!"
    "You casually hold each other's hands."
    "It’s something you’ve always done, as friends…"
    "But there’s something about the conversation you just had, and the events since you turned…"
    "And you both start blushing."
    C neutral "Let’s get back to studying!"
    "Cass buries herself in her book, but doesn’t let go of your hand."
    "It feels nice and comforting."
    "You go back to reading the huge pile of books."
    "Hours go by and you don’t find anything really useful until Cassandra pushes an open book towards you."
    "You read the chapter heading…"
    "\ "The Church at Stephan Lane"
    "\ "In the early 1800’s, the old church had a bat infestation…"
    "\ Shutting it down permanently…"
    "\ "But it was restored partially in the 80’s
    "\ " By Logan "Gan" Velsing", hunting gear mogul."
    "\ " VELSING!"
    "Cassandra beams at you"
    "\ " This has to be their hideout!"
    "\ We should go check it out tonight!"
    C smile "Yeah, we definitely.. *yawn*... definitely should…"
    "Cassandra looks absolutely exhausted…"
    "You kind of forgot that vampires needed a lot less rest than humans did."
    "\ "Hey, I can scout it out tonight on my own. You get some rest."
    C doubt "You sure, [player]?"
    "\ "Yeah, don’t worry. I’ll just turn into a bat and watch from afar."
    "\ "It’ll be fine!"
    C  "Ok… If you.. *yawn*... insist."
    "Cassandra rests her head on the table and takes a nap."
    "The library is 24/7, so she should be fine."
    "Plus, If all goes well, you’ll be back before you know it!"
    "You leave the library, curious about what the Batbashers are up to."
    END CHAPTER 5




    Ch 6
    scene forest
    # Tense Music
    " You fly as a bat through the thick forest trees"
    "Thanks to training with Cassandra, you’ve gotten pretty good at flying."
    "It’s a lot easier than you may have imagined."
    "It’s as if the wind wants you to float, to zoom."
    "And you just need to let it carry you forward."
    "You see the abandoned church before you."
    "You must have passed by it a couple of times on walks before."
    "An old, rusty, haggard building, abandoned decades ago."
    "It was only notable now as a spot for teens to smoke weed…"
    "And, apparently, for vampire hunters to plot their hunts."
    scene church
    "You perch at the very height of the church, getting a good vantage point on the meeting."
    Show a neutral with dissolve
    Show h smile with dissolve
    "Sure enough You see Anne and Han at the front, and a crowd of masked vampire hunters watching them."
    A "Glad to see you all here. Plenty of unfamiliar faces, I assume, beneath the mask."
    "The crowd chuckles. Damn, they must be easy to please."
    A "For those of you who were at the culling of the vampire hideout, a toast!"
    "Thunderous applause"
    H "Our Organization has a proud history, and a success rate beyond any other."
    H "Looking today, you may not know that this town used to be a huge center for vampire activity!"
    H "There were shops, schools, communities…more than anywhere else in the south"
    "This stuns you. Cassandra theorized that there was an old vampire community here, but a hub?"
    H sigh" And then came my ancestor. He killed the monstrous Bran Velcant, founded the ______, and brought the vampire community to its knees."
    H neutral "And now, here we are. Us an organization sprawling across Georgia, Alabama, Mississippi, Tennessee, The Virginias…"
    A "Even Kentucky starting next spring!"
    H sigh"And the vampires are all but stamped out. But now is not the time for complacency!
    "/" Crowd Member: Yeah, You’d know about complacency."
    "The crowd starts giggling."
    "This must be about the relationship Anne mentioned earlier? The nosy in you needs more information."
    H neutral "Yeah I was complacent. I let myself be manipulated. But so have we all."
    H sigh "We’ve grown complacent. We’ve let vampires not a day old slip through our fingers."
    "The crown murmurs. It seems the news of you escaping Anne has gone out."
    H neutral "We cannot rest until every last one of them is stamped out."
    H smile "The escapees have a camp in the deep woods. Tomorrow, we strike, and kill them all."
    "Relief and fear twirl into you. Laila and the others might be safe… But…"
    "You thought a few dozen people raiding you last time was bad…"
    "There’s over a hundred vampire hunters in this room right now."
    "If they weren’t wiped out now, after another attack they very well might be."
    A neutral "Anyway, enough speeches. One of our proudest sponsors, Fish-Fil-A, has graciously given us free sandwiches for this meeting!"
    A "Chow Down!"
    "The meeting adjourns as ravenous vampire hunters descend upon the catering."
    A
    Hide a with dissolve
    "Anne joins them, but Han wanders off , bringing one of the hunters with him."
    "You fly closer to Han, still out of sight."
    H sigh ‘We need to talk"
    # reveal thing
    ? "Look, I'm only here because of the initiation spell. I don’t support what you're doing."
    "That voice seems familiar…"
    H "Doubt is something every initiate goes through. I know this more than anyone."
    ? "Why single me out then? There are dozens of other initiates here."
    H smile "Because you live here. Because you know a vampire. Because you remind me of me."
    H " Cmon, take off your mask. We’re all family here."
    Show c doubt with dissolve
    "The figure takes off her mask to reveal Cassandra."
    # Sad Music
    "Cassandra?!?"
    "What is she… Why is she…"
    #obj pronoun
    C "We aren’t family. The person I love, [player], has been there for me since forever. I’m not going to betray [pronoun] for you!"
    H smile "Let me tell you a story." 
    H sigh " I was in love once. Adrian Lansberry. He was handsome, devoted, kind."
    H smile " We did everything together. I hid it from my dad, but my sis knew."
    H sigh "It was just lovely… until he got bit."
    H unsure "At first, i loved him so much, I betrayed the whole organization for him. Covered for him."
    H " My father disowned me. I was meant to take over as head but Anne seized the opportunity. I was alone and scared and we only had each other."
    H "But i noticed he was different. He wasn’t the man I fell in love with anymore."
    H "He grew violent. His bloodlust grew and grew. He… tried to bite me."
    H neutral "That’s what vampirism is Kalluri. A disease."
    #contraction
    H" Your friend isn’t the same one you fell in love with. That vampire is different, a monster, a killer now."
    # subject pronoun
    C "That’s not true, [player]…. "
    #Code in depending on affinity level either $ cass_affection >5 jump highcassaffection
    # or if  $ cass_affection <=5 jump lowcassaffection

    label highcassaffection
    # pronoun obj
    C "They’ve been acting the exact same as long as i’ve known [pronoun]!"
    H "That’s how it starts. Pretty soon the bloodsucker will be.."
    C "Pretty soon what? Don’t think I don’t see you trying to worm your way back to the top!
    C"You killed your boyfriend to get your old job back!"
    H surprise " Kalluri, Kalluri, I get you’re upset but no need to get emotional!"
    H unsure "You’re going through a lot right now, I get it. I’ve helped dozens of people like you. Like me."
    H "take your time. You’ll realize sooner or later.
    label lowcassaffection
    C "Well, they have been acting a bit different… but.. "
    H surprise "How different?
    #pronoun obj
    C " A little more aggressive, but that’s not [pronoun] fault! There has to be a better way!
    H unsure "I’ve been where you are! I’ve said what you’ve said, I’ve done what you’ve done."
    H "You’re going through a lot right now, I get it. I’ve helped dozens of people like you. Like me."
    H "take your time. You’ll realize sooner or later.
    #then
    H "Look, my sister, Anne, lusts for the kill. She doesn’t know vampires like we do. How dangerous they are, how human they are."
    H neutral "I have plans. Restructure the organization. More strategic hunts. Protect people like your friend before they get bit. A cure."
    H "That means I need allies. I see potential in you. Something to consider."
    "You sense worry and conflict in Cassandra's face."
    C "I need some air…"
    H smile "Whatever you need, friend.
    "Cassandra runs out,  leaving the church."
    "You don’t know how to feel."
    "The situation is difficult to process."
    "You zoom out of a window to follow her and confront her.
    END CHAPTER 6

    CHAPTER 7
    # Sad Music
    scene forest
    Show C doubt
    "Once you are both far enough away, you poof back to confront her.
    C smile " [player]! I’m so happy to see you!"
    menu:
    "/"What the hell! How could you join the vampire hunters!"
    "/" I heard everything… I promise I’m not dangerous Cassandra."
    "/ "You betrayed me!"
    C doubt "please, let me explain, I…"
    "Cassandra freezes. It’s as if she’s trying to say something, but she can’t."
    "You remember what Cassandra was saying earlier about the initiation ritual."
    "Maybe that was stopping her from being able to talk?"
    "To tell you the truth?"
    "You think back to the library. She never actually told you where the hideout was, you found it out yourself…"
    "She guided you to the answer without saying anything…"
        menu:
        "Are you under a spell?"
        "What can you tell me?"
    C doubt "I am prohibited from discussing the organization… I would get hurt if I did."
    C "I want to help you as best as I could, but I can't tell you anything."
    "Cassandra seems to be struggling, but her precise words seem to be mostly avoiding the curse."
    C "If I disobey, If i reveal a secret, if I do anything… "
    "She doesn’t finish, but you get the implication. She would die."
    C "I didn’t think it was real. I’ve joined larps and role plays and conventions all the time…"
    C "So I took the oath no problem."
    C "That night in the woods… I realized it was real."
    "When she met Han… When Han dragged her unconscious…"
    C "I wanted to tell you… they told me that you were some kind of monster, that you weren’t yourself…
    #ANother affinity check, if enough affinity jump 5cfriend, else jump 5cfoe
    #Code in depending on affinity level either $ cass_affection >5 jump highcassaffection
    # or if  $ cass_affection <=5 jump lowcassaffection
    label 5cfriend
    C "But I know you! You’re still the sweet beautiful person I've known forever!"
    C "Vampire’s aren’t a danger!"
    C "You aren’t a danger!"
    C "You’re…"
    "She hesitates again, but this time it doesn’t seem like the curse."
    C "You're my rock, [player]. When was bullied, when I came out, when I transitioned, you were always there for me."
    C "And i tried so hard to repay that, repay everything you’ve done for me but in the end i keep hurting you.
    C "I don’t deserve your friendship… so why do I…"
    "She pauses again."
    C "I love you, [player]. 
    C "I wanted to tell you before this whole thing, but now it's too late."
    C "Now we’re on opposite sides of this war."
    C "And I can’t fight them without dying… But I can’t fight you without wishing I was dead."
    "You stare into Cassandra’s eyes, the gravity of the situation sinking in."
    "That’s why she was acting distant recently."
    # Romantic Music
    "She loves you?"
    "This whole time, she’s been holding back because of this big secret."
    "She loves you?"
    "She feels so close to you now, in the cold night wind."
    "Quick, say something smooth!"
    menu: 
    "Well… That just happened…":
    "Erm… What the Scallop?":
    "(Stare at the floor awkwardly)""
    C "*giggles*"
    $ cass_affection+=1
    " Cassandra’s smile is infectious as always. Despite everything, you both giggle together."
    "Cassandra holds her hand in yours."
    "You look into each others eyes."
    menu
    "Kiss"
    jump Kiss
    label Kiss
    "You close your eyes as Cassandra presses her lips against yours."
    $ cass_affection+=10
    "It’s like a decade of emotions have flowed through you both, left with a peaceful bliss."
    "As you hold her close, and she holds you close.."
    "All the fear and anguish melts away."
    "You stay like this for a while, kissing and kissing and.."
    #hear voice without seeing person?
    # Tense Music
    H "Oh Kalluri… I’m disappointed."
    Show H neutral with dissolve
    H "After all my precautions, you led the bloodsucker right to us."
    "A net falls over you, barely missing Cassandra."
    H sigh "I guess I need to tighten the spell a little more for the next batch."
    H "Well, at least this should work."
    H "Kalluri, kill the bloodsucker."
    "Cassandra stays back from you, aghast."
    C doubt "I’m not going to do that, you freak!"
    H surprise "Freak?"
    C "No matter what you say I’ll never hu-"
    "Pain courses through Cassandra as she resists."
    H sigh"Look Kalluri, this is going to be good for you."
    H "In a year or so, when you’ll be head of a raid up north, you’ll thank me."
    "Cassandra looks like she wants to rebut, but the pain is preventing her."
    "\" Stop it!"
    "Han moves next to her and puts a stake in her hand."
    H "Come on, Kalluri. It’ll be quick."
    Hide C with dissolve
    "Cassandra resists and collapses to the ground."
    "It seems like the pain is intensifying."
    "You struggle against the net, trying to escape."
    "Cassandra passes out, still writhing."
    "Eventually the writhing stops and she lies still."
    H neutral "A pity. So much potential."
    "Rage boils in you. You burst through the net to attack Han."
    " A stake grazes your side and you fall down again."
    Show A neutral with dissolve.
    A "Heh.. I got you! Finally! Wait till the Batbashers hear about this!
    H "Step aside Anne, this is my business."
    A "That bloodsucker was going to kill you, idiot!"
    "As they bicker, you stumble to grab Cassandra and crawl away."
    "Anne points a shotgun at you."
    A: "Hannn, he’s getting away.
    "Han walks behind Anne"
    #pronoun obj
    H neutral "Then shoot [pronoun]"
    "Anne pulls the trigger. Pain shoots through your arm as you look behind you to see Han shoot Anne with a net gun. "
    #Hide A with dissolve.
    A annoyed "What the hell Han
    H " Vampire, You’re weak, you need blood… kill her."
    A "What?"
    H "Kill her, and you’ll heal enough to escape."
    H "You wrestled the net gun from her, killed her, and I found her dead."
    H "Catch my drift?"
    "You hate to admit it, but he’s right about you needing blood."
    "You wouldn’t make it a few feet without healing, much less to a hospital."
    "But you don’t like being a pawn in Han’s game."
    "He’d blame you for Anne’s death, he’d use you as a tool to gain power."
    "Maybe you're through being a tool.."
    "But you don’t want Anne to die…"
    menu
    "Kill Anne"
        jump killanne
    "Fight Han"
        jump fighthan
    label killanne
    Hid a with dissolve
        "You barrel towards Anne. Her death is swift. It's the first time you’ve really drank someone's blood."
    "You feel like the numbness you’ve felt for a while has gone away."
    "You’re alert, like you’ve drunk four matcha’s all at once."
    "You grab Cassandra and run into the night.
    # set $AnneDead to true
    END PART 7
    label fighthan
    # Tense Music
    "You reject Han’s order and attack him"
    "You feel a stake dig into your back."
    "You bite into him as the pain sinks in."
    "It's the first time you’ve really drank someone's blood."
    "You try to drink more but he pulls you off of him."
    "He lets go and you scurry away with Cassandra, deeply wounded."
    "You hear Anne escape her net."
    A angry "Really dude? After all I did for you?"
    H sigh "You took away my birthright! I’m the eldest boy!"
    A neutral "Aww, look at you grumble! You're turning into a bloodsucker just like your little boyfriend!"
    A "And you know what I do to bloodsuckers.."
    H" I HATE YOU!"
    "As you escape, you hear the two tussle."
    "You run as far away as you can, hoping to sense the other vampires and find safety."
    # set $HankillsAnne to true
    END PART 7
    label 5cfoe
    # Tense Music
    C doubt "And I wanted to say you were the same person as always, but.."
    C "You’ve been acting so different lately:
    #Have a section listing all the evil things m/c did
    C "There's so many violent mean things you’ve done that the old you wouldn’t have done…"
    C "I didn’t want to believe it, but you’ve changed."
    C " I was selfish. I thought I was living my fun vampire dream, and I didn’t consider that I would lose my best friend."
    "You have been acting more aggressive lately."
    "Was Cassandra right? Were you not the same person you were before the bite?"
    "You have the same memories, but.."
    C "I’m sure there’s a way to bring you back, I just know it."
    C "A lot of the people in the Batbashers are just bloodthirsty violent people, but…"
    C "Some of them were researching a cure. Han was saying…"
    "\"A cure?"
    "Regardless of how you feel about your vampirism, you don’t really trust a cure made by Han.."
    "You may have been a jerk to Cassandra recently…"
    # if you picked bite "And you did almost kill her that one time…"
    "But Cassandra was the one who showed you that there’s beauty in vampirism…"
    "Maybe you can convince her that you aren’t dangerous…"
    Show H neutral with dissolve
    H  "Ahh, what have we here…"
    #pronoun obj
    C "Han… please don’t hurt [pronoun]..."
    H "This is the one you wanted to cure, huh…"
    "Han shoots you with a net."
    C "You said you needed me right? Leave [player] alone, and I’ll help you take over."
    H "Glad to see you change your mind Kalluri."
    H "I promise, I’ll keep [player] safe."
    "You feel the sharp prick of a tranquilizer and pass out."
    scene dungeon
    Show H smile with dissolve
    H"Hey buddy."
    H"Your girlfriend is safe right now, don’t worry."
    "\" What do you want with me?"
    H"I told Cassandra I would humanely give you a cure."
    H sigh"I lied."
    H neutral "I tend to do that."
    H smile "But I get away with it cause I'm such a charming little fella."
    H surprise "I’m such a little goof sometimes!"
    H neutral "Anyway… Yeah, i’m gonna kill you."
    H "Sorry! It’s just that I’m a vampire hunter, and you’re, you know.’
    "You feel your strength returning. It’s now or never…"
    menu:
    "Break free and Attack Han":
        jump maulHan2
    "Stay in the Net  and yell.":
        jump spareHan2
    label maulHan2
    "You  burst free from your net and maul Han"
    H surprise "Woah, quit it!"
    "You hear a creak from the door just as you're about to finish Han off."
    Hide h with dissolve
    "You bite your teeth into him, sucking his blood."
    Show C doubt with dissolve
    C"Han, I can’t let you do this… What…"
    C "[player], no…"
    $ cass_affection-=10
    "It's the first time you’ve really drank someone's blood."
    "You feel like the numbness you’ve felt for a while has gone away."
    "You’re alert, like you’ve drunk four latte’s all at once."
    C "This isn’t you, please, I know [player] would never murder someone…"
    "You run away, out of the cellar, away from Cassandra."
    scene church
    "Your bloodlust  fuels you as you maul as many members as you can"
    Show a annoyed
    "Hey, isn’t that–"
    "You pounce on Anne and suck her blood too."
    "Your emotions flow through you, your anguish."
    "Until you feel a bullet go through your arm."
    Show c doubt with dissolve.
    C "[player], please. Don’t make me do this."
    "You look in Cassandra’s eyes and see fear."
    "Your best friend, your… maybe more, in another life.."
    "Looks at you with fear as you look back, covered in the blood of others."
    "You run, in fear, in shame"
    scene forest
    "Away from everything. "
    "Away from her."
    # set $EvilCass to true
    END CH 7
    label sparehan2
    H "You remind me a lot of my old partner, Adrian Lansberry."
    H smile"He was a great, wonderful person…"
    H neutral"But in the end, vampirism twisted him into a monster."
    H"I’m saving Kalluri a lot of trouble, a lot of heartbreak."
    H"Loving a creature like you, it never ends well."
    H" This is going to hurt, but you need to remember…"
    H" You’re already dead."
    H "I’m just sending you where you were meant to go."
    "You hear a creak at the door"
    Show C doubt with dissolve
    C"Han, I can’t let you do this.. What?"
    H surprise "Oh, Hey Kalluri! Ummm…. Yeah I can’t think of an excuse. Sorry?"
    C "You said you were going to cure [player]! That was the promise you made!"
    #obj
    C "I won’t let you hurt [pronoun]!"
    "Cassandra wrestles with Han, but pain shoots through her."
    "It must be the initiation spell…"
    Hide h with dissolve
    Hide c with dissolve
    "Cass struggles through it and punches Han to the ground before passing out."
    "You bust through the net and grab Cassandra’s passed out body, rushing out."
    "You climb through the cellar and…"
    scene church
    "You rush through the convention, still wounded from the net."
    "The stakes and bullets of the Batbashers pierce your skin.."
    scene forest
    "You escape, wounded, tired, on the brink of death, but safe…"
    "At least for now. 
    "You totter towards where the Batbashers said the other vampires would be…"
    "But you collapse halfway there, tired out of your mind.
    "You pass out…"
    "scene daywoods"
    "And wake up, the sun in your eyes."
    "You feel the sharp pain of the sun as you witness one last sunrise."
    "Cass wakes up just as you start to fade out."
    Show c doubt with dissolve
    C "[player], please… no. Please, please."
    C "I need you, please don’t go."
    "You die in Cassandra’s arms."

    END OF GAME, BAD ENDING








    PART 8
    # if $evilcass jump evilcass
    #if $dyingMc jump wakeup8
    scene forest
    # Tense Music
    "You drag Cassandra’s unconscious body into the vampire hideout"
    "\" I need a doctor! Please!"
    "It’s all a blur. Someone takes Cassandra away and you collapse from exhaustion."
    "You fall asleep, the long run sinking in…"
    label wakeup8
    Show l smile with dissolve
    "You wake up to see Laila, at long last."
    # Neutral Music
    menu:
    "\"Laila? Oh my god you’re alive!""
    "\"Where’s Cassandra? Is she safe? Is she alright?""
    "\"What’s Happening? Where am I?""
    L neutral "Calm down, you’re in a safe place. Well, as safe as any place can get for a vampire."
    "You look around and find that you’re still in the forest, albeit surrounded by a cluster of tents."
    L away "After the destruction at the Blood Bank, we were scattered for a bit. I had to hide in this root cellar, it was a whole thing."
    L neutral "I was able to find a few others and we’ve decided to set up here. The town’s almost certainly not safe."
    L neutral "In fact, we were planning on moving on to some other town when we found you. I thought you were dead!"
    "\ "I almost was…""
    "You tell Laila about everything that happened, and that the Batbashers are on their way to attack the hideout."
    L angry "Damn, okay. I need to speak with the others and figure out what we’re going to do. Are you going to be okay on your own?"
    "\ "Well, I’ve managed this far…""
    "\ "Also, where’s Cassandra? Is she ok?"
    L neutral "She’s at the clinic. But, she’s not been responsive since you arrived."
    "As Laila goes to figure out the plan, you beeline to the clinic to see if Cassandra is ok."
    scene clinic
    Show c doubt with dissolve
    # Tense Music

    "You see her, awake but tired"
    menu
    "Cassandra!!"
    "Are you ok?"

    C "I’m ok, thanks to Dr. Fang. She’s been researching the spell and… there may be a way to undo the damage."
    C "The spell wounded me deeply. Doc says my internal organs are bleeding."
    C "I’m dying. And the spell is going to keep hurting me until… until…"
    C "Han told me that  being bit would trigger the curse and kill me, but the doctor says that vampire healing may be the only way I live. 
    C "Maybe Han lied. Maybe he didn’t, I don't know. But it’s my only shot."
    "You didn’t truly expect the vampires to have a 100% solution."
    "Turning Cassandra into a vampire could kill her…"
    "But what other option was there?"
    "Maybe you could beat the solution out of Han.."
    "But that’s a risk too."
    C neutral "I’m so sorry about all of this, [player]."
    C "I want you to know, no matter what you choose, no matter what happens to me."
    C "I still feel the same way I did when we kissed…"
    C "I love you, [player]."
    "You kiss again, this time a somberness pervading the whole thing. "
    $ cass_affection+=1
    C "You’re the only one I trust to turn me, [player]."
    C "But I understand if you don’t want to."
    "You have to make a decision…"
    menu:
    "Bite Cassandra":
        jump biteof87
    "Try to find a cure":
        jump cure
    label biteof87
    "You kiss her again."
    $ cass_affection+=1
    "But this time you slowly extend your fangs into her lips."
    "You let the blood flow through you."
    "After a while, you feel her go limp."
    Hide c with dissolve
    "You let go and she collapses onto the bed."
    "\ What’s happening! Is she ok?"
    "The Doctor assures you that everyone passes out after getting bitten."
    "It happened to you too, so it makes sense."
    "Still, you can’t help but worry if you made the wrong decision
        jump 8craid.
    #set $Cassvamp to true
    label cure
    "You kiss her one more time"
    $ cass_affection+=1
    "\" I’m sorry Cassandra, I don’t want to risk you dying by my hand."
    "\"I’ll find Han and get him to stop the spell somehow."
    "\"Cassandra… Cassandra?"
    Hide c with dissolve
    "She’s passed out again."
    "You stay at her side for a bit before running out."
    "You hope you made the right choice."
    # set $Casshuman to true
    jump 8craid.
    label 8craid
    scene forest
    Show l away with dissolve
    "You leave the clinic, emotional, and run into Laila."
    L neutral "[player], are you ok?’
    menu
    "(lie) "I’m fine!"":
        jump 8c1
    "\"No, I’m not doing well right now."":
        jump8c2
    label 8c1
        L away "[player], it’s okay to be upset. It’s not easy being like this, and that comes with difficulties that you normally would never have to face."
        jump 8c3
    label 8c3
        L neutral "I’m sorry. I hope Cynthia will be ok."
        "\" It’s Cassandra.""
        L neutral "Oh, uh, yeah. Sorry. Long night."
    jump 8c3
    label 8c3
    # Exciting Music
    L angry "We are in general agreement that we should leave this place, sooner rather than later."
    L neutral "This camp was always meant to be temporary, and we’re just going to leave ahead of schedule."
    L excited "However, we have a plan to make our exit… memorable."
    L neutral "This camp is in a valley."
    L neutral "If we set some traps here before we leave, we can take a bunch of these hunters out, maybe scare them away, make it harder for them to follow us."
    L neutral "After what happened at the Blood Bank, I had an idea."
    L smile "If we set a bunch of kegs on fire, we could give the Velsings a taste of their own medicine for once."
    L away "We just need someone to stay put and trigger the trap."
    # if( $cassvamp) jump Cassfight
    # if( !$cassvamp) jump MCfight
    label Cassfight
    Show c confident with dissolve
    C "I’ve got this."
    "You see Cassandra, fit as a fiddle, awake and filled with vampiric energy."
    "\"Cassandra!"
    Show l neutral with dissolve
    "You rush to give her a hug before kissing her. Her lips feel different now, colder, but still lovely as ever."
    L neutral "Don’t let me interrupt you love birds."
    "You pull apart, acutely aware of your surroundings."
    C smile "Look, after everything the Vellsings did, everything I was complicit in, I can’t let them get away with it. I need to fight them."
    "You feel the same way. After all the Vellsings put you through, you can’t just turn and run. 
    L smile "I would stay, but I’ve lived through this kind of thing too many times already. I can’t bear to witness it again. I wish you luck, [player]. Your nobility is touching."
    "You say goodbye to Laila and prepare for the fight. With Cassandra at your side, you feel ready for anything. 
    Hide l with dissolve
        jump fightalongcass
    label mcfight
    "You realize what you have to do."
    "\I need to fight Han and figure out how to cure Cass."
    "\I need to be the one to stay here and trigger the explosion."
    "Laila nods grimly."
    L smile "I would stay, but I’ve lived through this kind of thing too many times already. I can’t bear to witness it again. I wish you luck, [player]. Your nobility is touching."
    "You say goodbye to Laila and prepare for the fight. Without Cassandra at your side, you feel uneasy."
    Hide l with dissolve
    "You hope you can handle Han alone…"
    jump fightalone
    label fightalongCass
    "As the town evacuates, you and Cassandra stand next to the empty clinic."
    # Romantic Music
    C smile "You know, It's really sinking in how, this might be our last day.."
    "Cassandra moves closer to you."
    C smile "And I’m so glad I get to spend it with you."
    "Cassandra gives you a little kiss on the neck."
    C"You know, the clinic is empty…"
    C" Nobody would bother us if we wanted to.. You know…"
    menu:
    "I know…"
    jump Iknow
    $ cass_affection+=1
    "What what?"
        jump WaitWhat
    label Iknow
    "Cassandra giggles."
    C smile "Well, what are we waiting for, [petname]?
    "You follow Cassandra into the clinic and lock the door behind you."
        jump Casssexscene
    label WaitWhat
    "Cassandra giggles"
    C"You know… spend some… quality time together… of a risque variety.."
    menu:
    "Oh, I see! Yeah,  I’m down":
        $ cass_affection+=1
        jump Iknow
    "I’d rather not right now.":
        jump nosex
    "I’m still confused.’:
        jump Waitwhat2
    label Waitwhat2
    C "You know, have sex… bang… fuck…etcetera…"
    menu:
    "Oh, I see! Yeah,  I’m down"
        $ cass_affection+=1
        jump Iknow
    "I’d rather not right now."
        jump nosex
    "I’m still confused.’
        jump Waitwhat3
    label Waitwhat3
    C doubt"Ummm, oh boy,  You know, like… when two birds love each other very much…"
    "Oh, I see! Yeah,  I’m down"
        $ cass_affection+=1
        jump Iknow
    "I’d rather not right now.":
        jump nosex
    "I’m a proud virgin, I don’t want to sully myself with such things until marriage.":
        jump virgin
    "I’m still confused.’
        jump Waitwhat4
    label Waitwhat4
    C doubt "Nevermind, I’m not feeling it anymore. Lets just train for battle, ok?
    $ cass_affection-=1
        jump to finalbattleCass
    label virgin
    C doubt "Oh. Umm… I didn’t know that about you… Let’s discuss this later ok?"
    C smile "For now, lets train for tonight!"
        jump to finalbattleCass
    label nosex
    C smile ‘That’s ok! How about we train for tonight instead!"
    $ cass_affection+=1
    label Casssexscene
    scene clinic 
    Show C smile with dissolve
    C "How about here in this empty bed? Noones used it, and noone is going to use it any more…"
    "You nod and turn off the lights
    scene black with fade
    C "Come here, you!"
    $ cass_affection+=10
    scene woods
    Show Cass smile with dissolve
    "After a few hours of fun, you stumble out of the clinic with Cassandra."
    C "That was fun… I feel so energized! Let's train before those dickheads show up!"
        jump to finalbattleCass
    label final battleCass
    # Exciting Music
    "After a while, the battle begins."
    "You stand in the center of the hideout."
    "You watch as dozens of Batbashers rush towards you."
    "You gesture to  Cassandra at the right moment."
    "She uses a lighter to set a string near a blood moonshine keg on fire"
    "She speeds towards you, pushing you to the ground as…"
    scene fire
    "BOOOM"
    "The Kegs explode, lighting most of the batbashers on fire."
    "As the survivors rush to fight you, you and Cass go on a rampage."
    "Cassandra has gotten used to being a vampire a lot faster than you did."
    "She floats and zooms, knocking out a bunch of the Batbashers."
    "You zoom past towards Han, bloody bruised and angry."
    scene forest
    Show h neutral with dissolve
    #if $AnneDead
    H "Ah, [player]. Thanks for the help with the coup. Couldn’t have done it without you."
    #else
    H "I took care of my own sister for this, I’m not going to let a punk like you stop my dominion."

    #Can we have this many options?
    menu:
    "Looks like it's going to be a short reign."
    "I am going to kill you."
    "I am going to unalive you."
    "I genuinely hate you on a deep level."
    "You’re kinda hot, but I have to kill you."
    "Sorry for this, babygirl."
    "Yeah, I’m thinking you're gonna die."

    "You and Cassandra beat the crap out of Han"
    Show h surprise with dissolve
    "He gets off a few shots of his gun, but the two of you easily take him down."
    c confident "So, what should we do with him?"
    menu:
    "Give him a quick death."
        jump quickdeatha
    "Make him a vampire"
        jump hanvampa
    "Let Cass decide"
        jump cassdecide
    label quickdeatha
    Hide h with dissolve
    "Cassandra snaps Han’s neck."
    "He collapses to the ground, instantly dead."
    "You toss his corpse into the raging fire that has started around the moonshine kegs."
    "You and Cassandra leave, heading back home"
        jump cassgoodending
    label hanvampa
    "You bite down on Han’s neck, sucking his blood."
    "You let go, and he collapses."
    "You tie his leg to a root and leave him there."
    "Han wakes up."
    H suprise"Please, don’t leave me here! Kill me! I’d rather die than be one of you, please!"
    "You and Cassandra leave, heading back home"
        jump cassgoodending
    label cassdecide
    C "I think we should flip the spell on him."
    "Cassandra grabs the book of names from Han’s pocket and starts chanting."
    C"You will protect all vampires from harm till your dying breath."
    C "If you disobey, the spell will torture and kill you."
    H suprise "Nooo! Not the consequences of my own actions!"
    "Han tries to attack you, but gets hurt in every attempt."
    "You and Cassandra giggle and walk away calmly."
    H "Damn you, Kalluri! And you too, Bloodsucker!"
    jump cassgoodending

    scene diner
    # Romantic Music
    "ONE MONTH LATER"
    "You rush into the town Waffle Home."
    "You hope you aren’t too late for your date with…"
    Show c wink with dissolve
    c"[player]!!!"
    "Cassandra pulls you into an embrace"
    c"Oh my god it's been so long!"
    "\ [Casspetname], it's been two days."
    "Cassandra giggles"
    c"I’m so happy to see you though!"
    C smile "We’ve been so busy helping rebuild the local vampire community, we’ve haven’t had time for a date like this!"
    "\"I guess this is technically our first real date as a couple, huh"
    C smile "What are you gonna have, [petname]? I’m thinking strawberry pancakes and some whisky.
    menu:
    "Chicken and Waffles"
    "Pancakes and syrup"
    "Eggs, Hot sauce and Hashbrowns"

    "\ And I’ll drink:"
    menu:
    "Whisky"
    "Moonshine"
    "A fruity cocktail"
    C wink "Nice choice, [petname]!"
    "You smile. With the Vellsings and the Batbashers dealt with, the town has become a new safe haven for the vampire community." 
    "More and more new vampires have come into town to help rebuild the hideout."
    "The world finally feels safe."
    "You and Cassandra talk and eat for a while, giggling and laughing and smiling."
    C "I’m so happy with you, [player]."
    "\ "Me too"
    "You both lean in for a kiss."
    $ cass_affection+=1000
    END OF PART 8 GOOD ENDING
    label fightalone
    #exciting music
    "After a while, the battle begins."
    "You stand in the center of the hideout."
    "You watch as dozens of Batbashers rush towards you."
    "As the get close, you use a lighter to set a string near a blood moonshine keg on fire"
    "You run away as fast as you can"
    scene fire
    "BOOOM"
    "The Kegs explode, lighting most of the batbashers on fire."
    "As the survivors rush to fight you, you fly away."
    "Their bullets graze you, but you have one focus."
    "Fighting Han"
    "You zoom past the fire, grab Han, and drag him deeper into the woods"
    scene forest
    Show h smile with dissolve
    H smile "Ahh, bloodsucker. There you are."
    H "Let me guess, you want to get me to let Kalluri free from the spell."
    H "That’s not going to happen."
    "Han stabs you, and you fall to the side."
    "You see a book strapped to his pants"
    "Maybe the book has something to save Cass."
    menu
    "Fight Han"
        jump dietoHan
    "Grab the book"
        jump grabbook8c
    label dietoHan
    # Tense Music
    "You tackle Han, wrestling him to the ground."
    "You’re pretty strong with your vampire powers…"
    "But Han is a trained fighter."
    "He pins you down and stabs you in the chest with a stake."
    "As you lie, bleeding out, you see Han get up and brush himself off."
    H surprise "Damn, that’s crazy."
    "Han scratches his head."
    H smile "Anyways… let's go slaughter these vamps!"
    "You lie in deep pain, dying."
    "Staring as Han descends to go off and murder other vampires."
    "As Cassandra dies away from you, unable to break the curse."
    "The light leaves your eyes as you lay defeated, conquered, slain."
    END OF GAME BAD ENDING
    label grabbook8c
    # Tense Music
    "You swipe the book and dash as far as you can from Han."
    Hide h with dissolve
    "He chases after you, shooting bullets that graze you."
    "You need to get this book to Cassandra and the Doctor fast."
    "But if you go on the shorter path to where Cass and the vampires were, you may lead Han right to them."
    "If you take the long way, you may not make it in time."
    menu:
    "Take the shortcut"
        jump shortcut
    "Take the long way"
    jump longway
    label longway
    "You sprint as fast as you can and lose Han in the woods."
    "You dash through hedges and around logs, desperate to get to Cassandra."
    "But to your horror…"
    "The sun starts to rise."
    scene daywoods
    "You start to feel sharp, agonizing pain throughout your body."
    "You duck under the shade of a lone tree."
    "Trapped"
    "Waiting, knowing you have the very thing that can save Cassandra and can’t get it to her."
    "As the sun rises, your future falls."
    END OF GAME BAD ENDING
    label shortcut
    # Tense Music
    Hide h with dissolve
    "You zoom through the shortcut until you can’t see Han behind you anymore."
    "You sense where the new vampire hideout is and dash towards it."
    "Just as you make it, you feel a stake puncture your foot."
    H sigh "looks like you led me right to them"
    "Han cocks his shotgun at you."
    H "Say your prayers, bloodsucker."
    "Suddenly, bats swarm all around Han."
    H suprise "GET OFF ME GET OFF ME GET OFF ME!"
    "As the Bat’s bite and peck at Han, you feel yourself slipping from consciousness"
    "Quick, say something cool before you die!"
    menu:
    "Looks like it's… Bats out, for you!"
    "I genuinely hate you on a deep level."
    "You’re kinda hot, but I have to kill you. Sowwy."
    "Sorry for this, babygirl."
    "Yeah, I’m thinking you're gonna die."

    "You pass out, watching Han die."
    "THREE MONTHS LATER"
    scene diner
    # Romantic Music
    "You stumble into the town Waffle Home."
    "You hope you aren’t too late for your date with…"
    Show c wink with dissolve
    c"[player]!!!"
    "Cassandra pulls you into an embrace"
    C smile"Oh my god it's been so long!"
    "You’ve both been in recovery for the last couple months, but you’ve both finally healed enough to go on a real date!"
    "You smile. With the Vellsings and the Batbashers dealt with, $townname has become a new safe haven for the vampire community." 
    C "What are you gonna have, $petname? I’m thinking strawberry pancakes and some whisky.
    "\ Hmm, I’ll have…"
    menu:
    "Chicken and Waffles"
    "Pancakes and syrup"
    "Eggs, Hot sauce and Hashbrowns"

    "\ And I’ll drink:"
    menu:
    "Whisky"
    "Moonshine"
    "A fruity cocktail"
    C wink "Nice choice, [petname]!"
    "You and Cassandra talk and eat for a while, giggling and laughing and smiling."
    C smile "More and more new vampires have come into town to help rebuild the hideout!"
    "You nod, smiling."
    "\"The world feels safe for once"
    "As you finish your meal, you hold Cassandra’s hand."
    "She looks lovely in the fluorescent lights of the waffle home."
    C "I’m so happy with you, [player]."
    "\ "Me too"
    "You both lean in for a kiss."
    $ cass_affection+=100
    END OF PART 8 GOOD ENDING

    label evilCass
    # Sad Music
    scene forest
    "You crawl into the vampire camp, wounded beyond belief."
    "Exhausted, you pass out."
    scene clinic
    # Tense Music
    "You wake up in a clinic, but noone is there…"
    "How strange…"
    scene fire
    "You walk outside the clinic and see fire."
    "Raging fire."
    "The moonshine kegs must have exploded again."
    "The town is abandoned, vampire corpses everywhere."
    "You look to the end of the camp and see in the smoke…"
    "A long line of Batbashers."
    "And at the front of it all… "
    Show c doubt with dissolve
    "It’s Cassandra."
    "You stand in shock. She sees you, and motions for the Batbashers to kill you."
    " You turn into a bat and fly, the smoke masking your escape."
    "Tears in your eyes, you fly as far as you can."
    "Alone, afraid."
    "Lost."
    scene street
    "SEVERAL MONTHS LATER"
    "The last several months have been hell."
    "The Batbashers have been targeting you specifically."
    "Cassandra seems to think that you aren’t you…"
    "And that in a way, you killed her best friend."
    "After months of desperate fleeing, you received a letter from a mysterious fellow vampire, promising a reunion."
    "Could it be Laila?"
    # Romantic Music
    "You wait at the spot they mentioned, anxious."
    "You see them appear from the shadows."
    "It’s…"
    Show h smile w dissolve
    #Neutral Music or Goofy music
    H "Howdy, bloodsucker."
    "\ "HAN?"
    H surprise "Woah, not so loud!"
    H unsure "Sorry for all the uh… Murdering and stuff."
    H "No hard feelings?"
    "\" NO HARD FEELINGS?"
    H surprise "Calm down! You’ll get us both killed…"
    H unsure "look, you turned me into a vampire, and, well.."
    H "I kinda lied to Cassandra, and the others."
    H sigh "You are the same person when you turn."
    H unsure "Adrian was the same person."
    H "I just wanted to make killing him easier, you know?"
    H "Anyway, now Cassandra thinks you aren’t you."
    H "That you are the reason why her best friend/crush is dead."
    "\" Crush?"
    H smile"Yeah, it’s really obvious."
    H "The will they won’t they of it all was getting deeply annoying."
    H "Like, make out already! You know?"
    H unsure "Anyway…"
    H "Now that I'm a vampire, I feel really guilty about everything."
    H "Kalluri, I hate to admit, is much better at vampire hunting than I ever was."
    H "She’s like, fueled by her grief about you."
    H "I want to stop her from running the Batbashers…"
    H "You want her to realize you're the same person."
    H smile "Let’s team up! Enemies to lovers except without the lovers!"
    "You don’t really have any other options…"
    "This is a real sad state of affairs."
    "\ "Okay, I guess i don’t have another choice…"
    H surprised "Really? Wow, honestly expected you to tell me to fuck off or something…"
    H smile "Don’t worry, I won’t let you down."
    "Filled with new found confidence, you both head towards the church."
    scene church
    # Tense Music
    Show h smile with dissolve
    "You feel anxious and afraid."
    H "Cassandra Kalluri, I challenge you to a Velsing Valorian for the title of head of the Batbashers!"
    Show c doubt with dissolve
    "Cassandra appears from the shadows."
    "She looks depressed, broken."
    C "You can’t do that as a vampire, as you well know, Han."
    C "Or should I say, Hankiller."
    H "Well, the first one  was between  a Vellsing and a Vampire Velsing! It’s my birthright!"
    C "I… suppose you're right."
    C "And that’s why you’ve brought [player]’s corpse here right! To taunt me, to phase me."
    H unsure "Well, not exactly."
    H smile "This bloodsucker is my champion!"
    "Han looks at you"
    H "You’re going to fight for me, friend!"
    "Wait what?"
    "\" That was never part of the plan!"
    H smile"Oh my god, are you naive? It’s me!"
    H smile "Of course I’m going to betray you."
    C "Well, at least I’ll be able to put [player] to rest."
    H "Look, you’ve got this bloodsucker! Pull some Stephen Universe redemption shit on her!"
    "/" Screw you…"
    Hide h with dissolve
    "Soon enough, you face off against Cassandra."
    "You don’t want to hurt her…"
    "Maybe you can convince her somehow…"
    menu:
    "/ "You can make it different…""
        jump to suflop
    "/"I am the same as [player]! I can prove it!""
        jump to redeemCass
    "/"Screw it, it's on!""
        jump to CassConflict
    label suflop
    "\You can make it right,"
    "\You can make it better!"
    "\ We don’t have to fi-"
    "Cassandra stabs you in the chest with a stake."
    "She starts crying."
    c"I know this isn’t you, [player]."
    c"But I don't know who to say this to…"
    c"Now that [player] is gone…"
    c"[player] made my life worth living."
    # all obj
    c"Made me smile every time I saw [pronoun]."
    c"I loved [pronoun]."
    #sing
    c"And when [player] turned, I was so excited."
    #obj
    c"I didn’t even realize that I lost [pronoun]"
    c"I’ll always feel guilty for that."
    C "I just hope now, [player]’s soul will finally rest."
    c"You fade into death, Cassandra’s tears the last thing you see before you die."
    END OF GAME BAD ENDING
    label Cassconflict
    "You brawl with Cassandra."
    "She fights with a deep sorrow and anger."
    "It seems like she’s spent the last several months studying how to be a great fighter."
    "She pins you to the ground."
    "You see a weak point in her defense."
    "But taking it might kill her…"
    menu:
    "Use the weak point."
        jump youkillCass
    "Don’t use the weak point."
        jump Casskillsyou
    label youkillCass
    "You take advantage of the weak point and punch Cassandra."
    "But you don’t know your own vampiric strength."
    "You kill her."
    Hide c with dissolve
    "As she dies, you hold her in your arms."
    "You didn’t mean for this to happen."
    Show h surprise with dissolve
    H surprise "Damn, that’s crazy…"
    H "Anyways…"
    H smile "I guess that makes me the head of the Batbashers!"
    H "Everyone, kill that vamp!"
    "What feels like a hundred stakes pierce through you as you hold Cassandra."
    "You feel the guilt carry you to the other side."
    "Maybe in another life, things would be different."
    "Or maybe, this tragic end was fate."
    "Your last sight is Han, a bright smile on his face."
    "He really did win it all."
    END OF GAME BAD ENDING
    label Casskillsyou
    "You miss the chance to hurt Cass."
    "You tussle for a bit…"
    "You try your best…"
    "But in the end, Cassandra stabs you in the chest with a stake."
    "She starts crying."
    c"I know this isn’t you, [player]."
    c"But I don't know who to say this to…"
    c"Now that [player] is gone…"
    c"[player] made my life worth living."
    # all obj
    c"Made me smile every time I saw [pronoun]."
    c"I loved [pronoun]."
    #sing
    c"And when [player] turned, I was so excited."
    #obj
    c"I didn’t even realize that I lost [pronoun]"
    c"I’ll always feel guilty for that."
    C "I just hope now, [player]’s soul will finally rest."
    c"You fade into death, Cassandra’s tears the last thing you see before you die."
    END OF GAME BAD ENDING
    label redeemCass
    c"Prove it? Prove it how?"
    "\ Ask me anything. Anything you think the real [player] would know."
    C "fine… what’s my favorite color?
    menu:
    "Orange":
            jump Quizdeath
    "Blue":
    jump Quizdeath
    "Pink":
    jump Quiz2
    "Green":
        jump Quizdeath
    label Quiz2
    C "Ok, that was easy. I mean, look at me."
    C "How about… What’s my favorite book?"
    menu:
    "What They do in the Shade"
    jump Quizdeath
    "The Werewolf Diaries"
        jump Quizdeath
    "The Moonlight Trilogy"
        jump Quiz3
    "Nosferatu"
        jump Quizdeath
    label Quiz3
    c"Ok, Ok. Who was my crush in elementary school?"
    "Michelle"
        jump Quizdeath
    "Gwen"
        jump Quizdeath
    "I don’t know"
    jump Quiz4
    c"Right, you wouldn’t know. Because we only met in middle school."
    C "Sorry, I had to do a trick question."
    C "You have all of [player]’s memories…
    #obj
    C "You look just like [pronoun]…"
    C "But you have to be different somehow!"
    "You explain that Han lied, and that vampires remained the same after turning."
    C "So you mean… All this time…"
    "It all hit her like a pile of bricks. She was on the wrong side of history. She was fighting her best friend."
    "Cassandra screamed in anguish and ran away from the church."
    "You try to run after her, but…"
    Show h smile with dissolve
    h"What do you think of that, Batbashers?"
    H "This is my perfect victory!"
    H sigh "That’s right, I win!"
    H smile"By the rules of the Batbashers, with no other legitimate heir in sight, I’m in charge now!"
    H sigh"And by the rules of the initiation spell…"
    H smile"You all have to listen to me!"
    H "It’s the Han dynasty, baby!"
    H "As my first order of business…"
    H sigh"Kill that vamp!"
    "You scamper out of the church."
    scene forest
    "You try to find Cassandra, but she’s gone, long gone."
    "You hear the marching of the Batbashers as they hunt you down, and you run. "
    "Back into hiding again."
    "Alone once more."
    "ONE YEAR LATER"
    #sad music
    scene street
    "After a year of searching, you finally find her."
    Show c doubt with dissolve
    "\"Cassandra."
    "You’ve tried confronting her before, but she’s always slipped away."
    "But now, in the light of the moon, she finally says."
    c"[player]." 
    "You look at each other, tears in both of your eyes."
    c"I… I’m sorry for running."
    c"I didn’t know what else to do."
    C "After everything I did to you, to the other vampires…"
    C "I couldn’t live with myself."
    C "I’ve been fighting off Batbashers, hoping to atone in someway…"
    C "But after everything we’ve been through, I couldn’t look you in the eyes."
    C "I’m so so sorry, for everything."
    "The guilt on her face is heartbreaking."
    menu:
    "I forgive you"
        jump forgiveness
    "I can’t forgive you"
        jump noforgiveness
    label noforgiveness
    # Sad Music
    C "I know. That’s why I can’t see you anymore."
    C "Goodbye, [player]."
    C "I’ll always remember you, and treasure what we had, and mourn what we lost."
    "Cassandra leaves, and you let her."
    Hide c with dissolve
    "You stand alone for a while, letting it all sink in."
    "Imagining what could have been."
    "Before you too walk away in the night."
    END OF GAME BAD ENDING
    label forgiveness
    C "But i can’t forgive myself."
    C "All the horrible things i did."
    C "I’m a monster."
    C "You deserve better."
    C "You deserve a better friend."
    menu:
    "You’re right."
        jump noforgiveness
    "You were manipulated, misled"
        jump forgiveness2
    label forgiveness2
    "\ Han tricked you."
    "\ If I were in your place, I may have been tricked too."
    "\ Please, I need you."
    "\ I’ve lost so much already, I can’t lose you too."
    "\ You mean so much to me."
    "\ I miss meeting you in the library"
    "\ I miss seeing you smile after geeking out about something."
    "\ I miss being with you."
    "\ I… "
    menu:
    "I like you platonically."
        jump platonic
    "I love you. Most ardently."
        jump ardent
    label platonic
    C smile "Wow…"
    "Cassandra giggles"
    $ cass_affection+=1
    # Neutral Music
    C smile "I haven’t laughed in so long…"
    C "I like you platonically too, [player]."
    C "Let’s be friends again."
    "You and Cassandra laugh and catch up as the sun rises."
    "You walk to Cassandra’s new place in the shade."
    "Han Velsing might still be out there…"
    "But at least you have your best friend back."
    END OF GAME MEDIUM ENDING
    label ardent
    C neutral "Pride and Predjudice?"
    C smile "You’re really using pride and prejudice on me?"
    $ cass_affection+=10
    "Cassandra breaks out into laughter."
    # Romantic Music
    C "Oh my god, It’s like Sophomore Lit when Mr. Stoker.."
    C "Wait, I’m going off on a tangent… I love you too."
    C confident "I love you most ardently."
    C "You mean the world to me."
    C doubt "When I thought you were gone… It broke my heart."
    C smile "If you really mean it, that you forgive me…"
    C wink "I’d love to be your girlfriend."
    C smile"I’d love to brave this messed up world with you."
    C "What do you say, [player]?"
    menu:
    "Yes"
        jump Peakend
    "I love you, Cassandra Kalluri."
        jump Peakend
    "I don’t know If i really forgive you…"
    jump noforgiveness
    label Peakend
    "Cassandra gives you a kiss."
    $ cass_affection+=100
    "The moonlight shines bright as you embrace her."
    "Even though Han is still out there somewhere…"
    "You feel like the world is perfect right now."

    END OF GAME GOOD ENDING




return



































    





























