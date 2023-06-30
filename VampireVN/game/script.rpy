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
            
            "You’ve been inseparable since middle school. It was hard to find queer friends in a small Southern town like ____ but when you do the bond is unbreakable."
            
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
                "Vampire":
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
            
            "Everything she’s just said tracks with what c said. That’s not great."
            
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
            
            hide l with dissolve
            
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
            
            c smile "Hey! I tried calling you earlier and you didn't pick up so i decided to see if you were home cause I just hit a jackpot, research wise!" 
            
            c confident "Check this out!"
            
            "Cassandra pulls out a heavy book. The title is in English, but it is so frayed with age you can barely make it out. You think it says.."
            
            c smile "Bran Velcant’s Journal. It’s this autobiography from an old vampire, i’ve only been able to read the first half, but…"
            
            c confident "I have a feeling that it matches up with what you were describing as your symptoms!"
            
            c smile "And it has so much fascinating lore about how vampires used to live, the little pocket societies they made, what they wore, how they traveled…"
            
            menu:
                "(say nothing)":
                    jump c2db
                "Cool, but what does this mean for me?":
                    jump c2eb
                "Dooon’t Carree":
                    $ cas_affection -=2
                    jump c2fb
    
        label c2db:
            c smile "and there’s this kinda interesting romance he’s having, like a kinda love triangle with these two other guys, and normally i’m not a fan of them but this one is really gripping!"
            
            c "and there’s this brother character and they have this antagonistic relationship but it seems like he has this deep care in his heart for him, and…"
            
            c doubt "wait, I’ve been ranting, haven’t I? I’m sorry, you know how I am with books…"
            
            mc "You’re good!"
            
            mc "I’m genuinely interested! The book seems cool!"
            
            mc "What does this mean for me?"
            
            jump c2eb

        label c2fb:
            c doubt "Oh… i’m sorry."
            
            "Cassandra looks really dejected."
            
            c doubt "Look, basically what this means is I think I know what your powers are." 
            
            jump c2eb
    
        label c2eb:
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
            
            jump c2b
        
        label c2c:
            "Why did you say that! It’s like it spilled out of you. You hope Cassandra doesn’t see your blush…"
            
            $ cass_affection += 1
            
            c "Yeah, I’m just really excited about all this! Who would have thought my best friend would be a vampire! It’s like I’m in a book!"
            
            c "I know this is real, but things have been… too real recently. With the stuff with my family, and the laws being passed and the climate… It’s nice to have something else to work on"
            
            c "Anyway, check this out!"
            
            jump c2b
        
        label c2b:
            "Cassandra pulls out a heavy book. The title is in English, but it is so frayed with age you can barely make it out. You think it says.."
            
            c smile "Bran Velcant’s Journal. It’s this autobiography from an old vampire, i’ve only been able to read the first half, but…"
            
            c smile "I have a feeling that it matches up with what you were describing as your symptoms!"
            
            c smile "And it has so much fascinating lore about how vampires used to live, the little pocket societies they made, what they wore, how they traveled…"

            menu:
                "(say nothing)":
                    $ cass_affection += 1
                    jump c2d
                "Cool, but let’s get to the training!":
                    jump c2e
                "Dooon’t Carree":
                    $ cass_affection -= 2
                    jump c2f
       
        label c2d:
            c smile "and there’s this kinda interesting romance he’s having, like a kinda love triangle with these two other guys, and normally i’m not a fan of them but this one is really gripping!"
            
            c smile "and there’s this brother character and they have this antagonistic relationship but it seems like he has this deep care in his heart for him, and…"
            
            c doubt "wait, I’ve been ranting, haven’t I? I’m sorry, you know how I am with books…"
            
            menu:
                "You’re good!":
                    $ cass_affection += 1
                    jump c2e
                "I’m genuinely interested! The book seems cool":
                    $ cass_affection += 2
                    jump c2e
                "Let's get to training!":
                    jump c2e
        
        label c2f:
            c doubt "Oh… i’m sorry."
            "Cass looks really dejected."
            c doubt "Let’s just get to the training."
            jump c2e
        
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
