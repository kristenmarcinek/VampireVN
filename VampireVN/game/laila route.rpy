 #---CHAPTER 4---

label laila_chapter4:
    scene forest with fade
    # tense music
    play music "Ominous Forest.mp3" fadein 1 fadeout 1
    "You dash after Laila deeper into the woods. All the vampires you met at the party- how many of them are dead? And those hunters, who are they?"
    "You don’t have time to think about those things now. You keep going."
    "You push your way through undergrowth that becomes ever-denser as you go on. You move at such speed that branches nick your face as you fly past."
    "Behind you, you hear the shouting of the Velsings and their rampage in your wake."

    show a annoyed with dissolve
    a annoyed "Faster Han, you fool! They’re getting away!"
    "You hesitate for half a second and a stake lodges itself into the tree next to you. You keep moving."
    "All of sudden, the ground you were running on gives way to some sort of abandoned drainage ditch, and you make a half leap to cross it and roll into the bushes on the other side."
    "You turn around and spot the Velsings, who have neither your keen senses nor your enhanced reflexes."
    "Anne starts to stumble, but catches herself before she can trip and fall in. Her success is short-lived though, as Han runs straight into her, sending both of them tumbling."
    "The two lie in a disheveled heap in the ditch."
    a angry "We’re going to lose them now, you oaf! There will be hell to pay for how you’ve bungled MY great triumph!"
    hide a with dissolve

    "As Anne berates her brother, you take this opportunity to slip away into the shadows of the forest."
    "After a couple more minutes of running, you figure it’s probably safe to stop, and take a moment to catch your breath."
    "You’re only alone for a moment before you hear a snap from the trees behind you."

    show l neutral with dissolve
    # neutral music
    "You spin to see it’s Laila, her clothes somewhat dirty, but otherwise none the worse for wear."
    hide l with dissolve
    window hide

    menu:
        "\"Oh thank god, you’re alright!\"":
            window show
            "Laila’s countenance, somewhat grim, now lightens."
            show l excited with dissolve
            l excited "I’m glad to see you’re okay too, [player]."
            $ laila_affection+=2

        "\"Don’t sneak up on me like that!\"":
            window show
            "Laila lets out a soft chuckle."
            show l excited with dissolve
            l excited "I didn’t know you were such a fraidy cat. Are you sure you’re qualified to be a creature of the night?"
            $ laila_affection+=1

        "\"Took you long enough.\"":
            window show
            "Laila gives you a withering stare."
            show l angry with dissolve
            l angry "Perhaps had you not made such a racket in your escape, I would not have had to run quite so far to hide."
            $ laila_affection-=1

        "Remain silent.":
            window show
            "Laila looks at you expectantly, then speaks in an exasperated tone."
            show l away with dissolve
            l away "Yeah, thanks [player], I’m glad to see you’re okay too. Jeez."
            $ laila_affection-=1


    l neutral "So, I don’t think we’ll be able to make it back to town safely before the sun rises. Thankfully, yours truly has thoroughly explored these woods, so I know a place we can go."
    "Laila beckons you to follow her before marching off. You follow close behind."
    "Several long minutes pass in silence. Neither of you speaks for fear that the Velsings might still be roaming."
    "Finally, you reach your destination: a cabin, but one incredibly dilapidated. The roof is partially collapsed, and none of the windows have any intact glass remaining."
    mc "We’re staying here?"
    l neutral "There’s more to this place than meets the eye."

    #CHANGE: I think there's supposed to be a cabin scene here

    "Laila cracks open the door and leads you inside. The inside is not much better than the outside: the furniture that has not been covered by the collapsed roof is aged and covered with moss."
    "Then you see it. Beneath a dining table is a small hatch in the floor. You only spot it because of your vampiric vision- it’s so overgrown with foliage it would be hard to see even in the day."
    "Laila kneels down and lifts the hatch, and you’re assailed by a wave of dank air."
    l neutral "Get in. It’s deep enough, and no light’s going to get through. I’ve slept over here on more than one occasion."
    "You approach the hatch."
    l away "It will be, uh, a bit of a tight fit for the both of us."
    "You have no other choice though. You descend a rickety steel ladder into the dark, and Laila follows, closing the hatch behind you."

    scene cellar with fade

    "At the bottom of the ladder is a small room- if you can call it a room- not more than a foot and a half long by a foot and a half wide."
    "As Laila reaches the bottom, it becomes immediately clear just how small a space it is."
    show l neutral with dissolve
    "There is no room for either of you to sit. Your back is pressed up against a mossy stone wall- at least, you hope it’s moss- and you are only inches away from Laila."
    "You feel the unnatural coolness radiating from her, and realize she probably feels the same from you."
    # comedic music maybe
    l smile "I didn’t think we’d be sleeping together this soon."
    play music "Strange Forest.mp3" fadein 1 fadeout 1
    "She lets out a little laugh."
    hide l with dissolve
    window hide

    menu:
        "Stay quiet.":
            "You remain silent and Laila’s laugh peters out."
            window show
            show l away with dissolve
            l away "Sorry, wrong time, yeah."
            $ laila_affection-=1

        "Give a little laugh.":
            window show
            "You release a little giggle at Laila’s joke, and she gives you a broad smile."
            show l excited with dissolve
            l excited "I’m glad you found it funny."
            $ laila_affection+=1

        "Make a quip back.":
            window show
            mc "Yeah, I expected you to buy me a drink first."
            "Laila chuckles at your remark."
            show l excited with dissolve
            l excited "Next time, [player]."
            $ laila_affection+=1


    l neutral "Well, we’re going to be here for a while. I guess I can answer any questions you might have."
    #romantic music



label laila_pit:
    hide l with dissolve
    window hide

    menu:
        "Ask about Laila’s past." if not lq1:
            window show
            mc "If you don’t mind, could I know some more about your past?"
            show l neutral with dissolve
            l neutral "Like, before I came to town? Yeah, I suppose."
            l neutral "Well, I was turned about 10 years ago, at a punk rock show in Houston. It was an unpleasant end to an otherwise great evening."
            l away "Since then, I’ve kinda been hopping around from community to community. Vampires can’t really settle down anywhere in anything resembling large numbers for very long. We attract the attention of people like the Velsings."
            l away "I mentioned Grand Rapids earlier. Before I came here, it was the longest place I had stayed- about a year. Too many of us were too open there, and they came and it all went up in flames."
            l angry "Like it always does."
            "Laila pauses now and takes a deep breath before continuing."
            l neutral "It’s fine."
            $lq1 = True

            jump laila_pit

        "Ask about Laila’s life now." if not lq2:
            window show
            mc "Can you tell me what things have been like for you recently?"
            show l neutral with dissolve
            l neutral "I mean, I’ve been living here for something like 9 months? After Grand Rapids, I needed to find a new place to settle down. My ex, some of her friends were out here. Felt like it could be safe. And it has been."
            l away "But there’s not a whole lot to life here beyond subsisting. I take shifts at some of the local bars a few nights a week. It’s enough to get by here."
            mc "You’re a bartender?"
            l neutral "Yeah. Not what I imagined spending my life doing, but there’s not a whole lot of employment options for people in our position. It’s not awful."
            l away "But it’s not great, either."
            $lq2 = True

            jump laila_pit

        "Ask about the other vampires in town." if not lq3:
            window show
            mc "Can you tell me about the other vampires living in town?"
            show l neutral with dissolve
            l neutral "The ones that are left you mean? There’s something like 20ish of us? I knew a couple of them through my ex and they’re good enough folks."
            l away "It’s pretty tough to find vampires who aren’t into the whole live feeding thing. The New York City vamps are living it up, they disguise their kills as regular murders, they never have to worry about getting caught."
            l away "Vampire hunters always go after us- they look for blood banks with mysteriously missing blood. This is why I split with my ex. She didn’t share my objections about killing, and wanted to protect herself."
            l neutral "I’d rather not discuss it further."
            $lq3 = True

            jump laila_pit

        "Ask what Laila thinks of you." if not lq4:
            window show
            mc "Well, what do you think of me?"
            "Laila’s eyes widen briefly at your question, then she looks away."
            show l away with dissolve
            l away "Look, I think you’re nice enough. But I don’t really know you all that well yet. And things aren’t great, you know?"
            $lq4 = True

            jump laila_pit

    window show
    "From everything Laila’s said, you’re picking up on something."
    mc "Do you like being a vampire?"
    "At this, Laila lets out a deep sigh."
    play music "One Small Light.mp3" fadein 1 fadeout 1
    show l away with dissolve
    l away "No."
    "She is silent for a long while."
    l neutral "Okay, I probably owe you more of an explanation than that."
    l neutral "I tried very hard to adapt. But the sort of existence I have to live- the things we have to do just to survive- is miserable. The speed and the strength is neat, but it’s not worth never getting to feel the sun on my skin again."
    l away "Living this way forever? I see it as a curse."
    l neutral "I’m sorry, I’m sure you’re enjoying the experience. I don’t mean to upset you."
    "It’s all for her to share, and a great deal for you to process."

    hide l with dissolve
    window hide

    menu:
        "\"It’s okay, I get where you’re coming from, I feel that a bit too.\"":
            window show
            "Laila cheers up a bit at your response."
            show l smile with dissolve
            l smile "Thank you [player]. I appreciate your empathy. And I’m glad someone else feels the way I do."
            "Laila stares into your eyes, raising a hand and allowing her fingers to brush lightly against your cheek, before she quickly pulls away."
            l away "Sorry, I’m going through a lot right now."
            $ laila_affection+=2

        "\"I’m loving it, but your feelings are totally valid.\"":
            window show
            "Laila takes a deep breath and nods at your response."
            show l neutral with dissolve
            l neutral "That’s more understanding than I get from most others, so I appreciate it."
            $ laila_affection+=1

        "\"Yeah, how could anyone not love this?\"":
            window show
            "Laila goes from quiet and contemplative to furious in an instant."
            show l angry with dissolve
            l angry "Yeah, of course, your feelings are the only ones that matter. Sorry I bothered to open up to you. You’re just like all the others."
            "The two of you sit in the silence uncomfortably."
            $ laila_affection-=2

    "After several minutes of quiet, Laila speaks up again."
    l neutral "Well, I think we should at least try to get some sleep. I can only imagine tomorrow night will be busy. Sleep tight, [player]."
    "With this, Laila closes her eyes and, still standing, settles into a slumber like death."
    "You decide to follow suit, and rapidly fall into a deep and dreamless abyss."

##---CHAPTER 5---

label laila_chapter5:
    scene cellar with fade
    play music "Slow Life.mp3" fadein 1 fadeout 1
    "You awaken to find Laila’s head resting on your shoulder- it appears she shifted in her sleep."
    # $ player = "Raven"
    # romantic music
    window hide

    menu:
        "Let her stay like this for a minute.":
            window show
            "You’re not in any particular rush, so you decide to let Laila rest for as long as she needs to."
            "Despite your best attempts at keeping still, Laila wakes within a couple minutes."
            "When Laila becomes aware of exactly where she’s been sleeping, she stumbles back as far as she can in the enclosed space."
            show l away with dissolve
            l away "Oh, [player], I’m so sorry, I hope I didn’t disturb your sleep."
            "Laila takes a moment to compose herself."

            $ laila_affection+=2

        "Gently wake her up.":
            window show
            "You give Laila a light tap on the shoulder, and she begins to come awake."
            "When Laila becomes aware of exactly where she’s been sleeping, she stumbles back as far as she can in the enclosed space."
            show l away with dissolve
            l away "Oh, [player], I’m so sorry, I hope I didn’t disturb your sleep."
            "Laila takes a moment to compose herself."
            l smile "Still, I appreciate the care you took in waking me."
            $ laila_affection+=1

        "Shake her awake.":
            window show
            #tense music
            "You’re not a fan of Laila being in your personal space, and you grab her shoulders and shake her awake."
            show l angry with dissolve
            "She is alert in an instant and slaps you in the face."
            l angry "What is your problem? We’re not in any sort of danger, can’t you at least try to be polite?"
            l angry "Would you like it if someone woke you in that way? Jerk."
            "She leans back against the wall and simmers in anger for a bit, before composing herself."
            $ laila_affection-=2

    # neutral music
    play music "Ominous Forest.mp3" fadein 1 fadeout 1
    "With the two of you sufficiently awake, Laila gestures for you to make your way up the ladder."
    "You make your way to the surface, opening the trapdoor, and emerging into the cool air of the early evening. Laila emerges from the hatch a moment after you."

    scene forest with fade
    show l neutral with dissolve

    l neutral "Alright, we have to find out who survived that disaster last night. The problem is I have no idea where’s safe anymore."
    mc "Is there no other secret vampires-only hideout?"
    l neutral "No, I don’t think- wait a minute. We could visit Gabrielle’s. But that may be worse than the Velsings."
    mc "Who is Gabrielle?"
    "Laila looks away, somewhat embarrassed."
    l away "She’s an older vampire, who doesn’t like new vampires. She has a bad habit of killing them."
    mc "What?!? She kills other vampires?!"
    l away "She’s a little bit like me, she doesn’t think vampirism is a gift. And she wants to spare new vampires- like you- from the suffering."
    "You take a moment to consider what you’ve just been told."
    "Laila takes a deep breath and straightens her posture."
    l neutral "I think these are exceptional circumstances. Gabrielle won’t kill you. Maybe. Probably. I hope."
    "These words do not, in fact, inspire you with hope."
    "Still, you follow Laila as she begins sprinting in the direction of town with vampiric speed."
    "While you are quick, you still struggle to keep up with Laila, who is able to dodge and weave around trees without breaking her stride. You, unfortunately, run into more than one tree on your journey."
    "Once you emerge from the forest, somewhat battered for your efforts, you stop Laila to chat."

    scene street
    show l neutral with dissolve

    mc "Wouldn’t it have just been simpler to, you know, turn into a bat and fly here?"
    "Laila shakes her head."
    l smile "And leave all of our clothes in the forest? Sorry [player], I like you, but not that much. Yet."
    l angry "Besides, I hate turning into bats."
    "With that, Laila leads you through town. It’s not terribly late, so there are still people on the streets- running now would draw too much attention to you."

    scene creepy house with fade
    # tense music

    "Soon you arrive in a neighborhood that you’re not quite familiar with. Dilapidated single family homes line the streets. Laila stops in front of one that somehow looks worse than all the rest- vines cover half the house, and the yard is filled with weeds."
    show l neutral with dissolve
    mc "Gabrielle lives here?"
    l neutral "Yeah. It’s, uh, easier to dispose of corpses here."
    mc "Oh my god."

    "Laila turns to face you with concern in her eyes."
    l neutral "Look, I don’t approve of what Gabrielle does, okay? Not many of us do. But right now if we want to live longer than the next couple nights, she’s our best shot."
    "With this, Laila turns resolutely towards the door and approaches it. As she raises her arm to knock, the door swings open and a shape flies out past Laila."
    "In an instant you are knocked to the ground, pinned there. You gather your bearings and find your assailant is an old woman, her hand raised above your heart, clutching a stake."
    "She is about to plunge it down into your chest when Laila rushes over and grabs her wrist."

    l angry "Gabrielle, no! This is [player], my friend. We need your help."
    "The old woman, Gabrielle, bares her teeth in a snarl, revealing her lengthened incisors."
    "Gabrielle" "Laila, it’s a new blood, no more than a few days old. I can smell it! Let me give the soul a chance to make it to heaven, before the taint of hell stains it forever."
    l angry "That’s not happening Gabrielle. Now get off of my friend, or you and I are going to have a problem."
    "Gabrielle gives you one last snarl before easing off of you, and standing back up. You take a moment to get up and dust yourself off. Laila turns to you."
    l neutral "Gabrielle is rather religious. She thinks vampires less than a couple weeks old can still go to heaven."

    "Gabrielle nods stiffly at this."
    "Gabrielle" "I don’t think it. I know it."
    l neutral "Anyway, Gabrielle, the Velsings are in town. They destroyed the Blood Bank."
    "At the Velsings’ mention, the older vampire shudders."
    "Gabrielle" "Monstrous, they are. I know of the destruction you speak of. Their hunt is driven by hatred, not compassion."
    mc "You’ve got a funny way of showing compassion."
    "Laila gestures for you to stop talking."
    "Gabrielle" "I’ll let the impudence go. I had a whole lifetime of experience under my belt before I was turned, and I know what it’s like to be a youngster, with no clear view of the bigger picture."
    "Gabrielle" "There will be a day, [player], that you will come to disdain Laila for not letting me impart my mercy unto you."
    "Laila rubs her temples in frustration."

    l neutral "Gabrielle, do you know if anyone survived the attack?"
    "The old woman nods."
    "Gabrielle" "A handful dropped by on their way out of town. They wanted to warn old Gabrielle. They didn’t listen to me though, and kept on their way."
    l neutral "Well of course Gabrielle, they’re running for their lives."
    "Laila turns to you."
    l neutral "Just like we will. I’ll get you through this [player]."
    "Gabrielle chuckles."
    "Gabrielle" "You don’t need to flee. Old Gabrielle knows of the cure."
    "A cure? What is this mad old woman talking about?"

    hide l with dissolve
    window hide

    menu:
        "Ask her to explain.":
            window show
            mc "What do you mean a cure?"
            "Gabrielle gives you a sickening grin."
            "Gabrielle" "Oh now you’re interested, eh? I’ll tell you."
            "She takes a dramatic pause."
            "Gabrielle" "A new vampire came to town last week. They spoke of having found a way to remove our curse. Some ritual or concoction, or something, I don’t know. It’s beyond my ken."
            "These words have affected some sort of change in Laila. Her eyes are wider, her stance poised as if to leap off running."
            show l netural with dissolve
            l neutral "Speak more on this."
            "Gabrielle" "I don’t know much more than what I’ve told ya. Just that this fellow is staying in the abandoned mansion on the big hill."
            "You know the place Gabrielle speaks of. The house is infamous for being in a state of disrepair in an otherwise upscale part of town."

        "Remain silent.":
            window show
            "You elect to remain silent, but Laila speaks up, her voice hopeful."
            show l neutral with dissolve
            l neutral "What cure?"
            "Gabrielle gives Laila a sickening grin."
            "Gabrielle" "Oh now you’re interested, eh? I’ll tell you."
            "She takes a dramatic pause."
            "Gabrielle" "A new vampire came to town last week. They spoke of having found a way to remove our curse. Some ritual or concoction, or something, I don’t know. It’s beyond my ken."
            "Laila is like a changed woman on hearing this. Her eyes are wider, her stance poised as if to leap off running."
            l neutral "Speak more on this."
            "Gabrielle" "I don’t know much more than what I’ve told ya. Just that this fellow is staying in the abandoned mansion on the big hill."
            "You know the place Gabrielle speaks of. The house is infamous for being in a state of disrepair in an otherwise upscale part of town."

    # romantic music
    play music "Slow Life.mp3" fadein 1 fadeout 1
    "Laila turns to you now."
    l neutral "[player], this is a lot to ask of you, and I understand if this quest is not for you."
    l neutral "But I must seek out this cure. I cannot pass on this opportunity."
    l neutral "Will you join me?"

    hide l with dissolve
    window hide

    menu:
        "\"Yes Laila, I’m with you all the way. Together, we can be free of this.\"":
            window show
            "You let Laila know that you will join her on her quest, and she embraces you in a hug."
            l excited "Thank you so much [player]. I know we’ve only known each other for a couple days, but I will forever appreciate this."
            "She releases you from the hug, and you find yourself wishing she had held you for just a moment longer."
            "Laila now steels herself with resolve."
            l smile "Thank you, Gabrielle. We’ll be going. Stay safe."
            "The old woman merely stares as you and Laila depart."
            $ laila_affection+=2

        "\"I can’t say I’ll use any cure we might find, but I will help you find peace.\"":
            window show
            "You inform Laila that even though you might wish to remain a vampire, you’ll help her find a cure."
            "Laila gives you a big smile and clasps your hands in thanks."
            show l excited with dissolve
            l excited "Thank you [player]. Even if we have different ideas about what it means to be a vampire, I’m glad I can rely on you."
            "Laila now steels herself with resolve."
            l smile "Thank you, Gabrielle. We’ll be going. Stay safe."
            "The old woman merely stares as you and Laila depart."
            $ laila_affection+=1

        "\"No, there’s too much risk. I’m just going to leave town and make it on my own.\"":
            window show
            #sad music
            play music "Monologue.mp3" fadein 1 fadeout 1
            "You inform Laila that you’re done with all this, and intend to leave town and escape the Velsings."
            "Laila is visibly disappointed in your response."
            show l away with dissolve
            l away "I won’t begrudge you your decision. And I’m not upset. But I can’t say I’m not surprised. I thought you and I had at least some sort of connection. But I guess I was wrong."
            "She composes herself."
            l neutral "I wish you well, [player]. Good luck."
            "Laila departs into the night. You do not know it now, but you will never see her again."
            "You return home, and sleep through the day. The following night you make your way out of town, catching a bus heading to some place far away from here."
            "You manage to survive in your new home for a time, finding other vampires, before the Velsings inevitably find your new haunt. And so you flee again."
            "And so it goes on, year after year, a life on the run. Until one night, you are not quite as lucky as you were in the past. Perhaps you were hit by a stake like Shamus was at the Blood Bank, or maybe you simply got caught outside as the dawn came."
            "It matters not how. Simply that your life has come to an ignominious end."

            $ persistent.ending = 4

            return

    l neutral "I don’t think we’ll have time to get to and explore the mansion this evening. Mind if we stay the day at your place?"
    "Laila’s right, and so you agree to open your home up to your vampire friend."
    scene apartment with fade
    "When you get to your apartment, Laila begins to crawl under your bed."
    show l away with dissolve
    "At your evident shock, Laila begins to explain."
    l away "This is kind of embarrassing, but at home I actually, uh, do sleep in a coffin."
    l away "I’m used to the confined spaces, and can’t really sleep otherwise."

    "Of all the things you’ve experienced over the last few nights, this might be the weirdest."
    "Still, the evening’s escapades have left you exhausted, and you collapse onto your bed, and fall into another dreamless slumber."

##---CHAPTER 6---
label laila_chapter6:
    scene apartment with fade
    # tense music
    play music "Ominous Forest.mp3" fadein 1 fadeout 1
    "You awaken with a pulsing headache, worse than your first night as a vampire. Your head feels like it might explode at any second."
    "And, as if things couldn’t get any worse, your thirst for blood is all-encompassing. You realize you never had any blood last night."
    "You stagger out of bed and try to make your way towards the kitchen. You don’t make it more than a handful of steps before you collapse."
    "You resort to feral behavior, crawling along the floor like some sort of animal, driven almost entirely by instinct."
    "In your hunger, your senses seem heightened, and you can hear the beating hearts of your slumbering neighbors."
    "You want them."
    "You rise shakily to your feet, and have almost made it to the door, when some force tackles you from behind."

    show l angry with dissolve
    l angry "[player], no!"
    "It seems Laila is awake and intends to stop you. Despite knowing she’s probably acting in your best interest, your body resists her without conscious effort. It’s like you’re no longer in control."

    scene laila cg 1 with fade
    "Laila manages to flip you over, and pins your arms to the ground. Despite her slender frame, she is holding you down with ease."
    l "Listen to me, you have to fight it. It gets easier to skip a day or two as you get older, I promise. But for now, you need to be strong!"
    "Laila is pleading with you as your body struggles against her. You try to speak, but your lips refuse to do anything other than curl into a snarl."
    l "Okay, I can try something crazy, if you can’t calm yourself."
    "Laila hesitates before speaking again."
    $ persistent.laila1 = True

    scene apartment with fade
    show l neutral with dissolve
    l "We’re not supposed to, but I can give you some of my blood- vampire blood- and it should sate you. For a time. But you and I will forever be bound."
    l neutral "Our emotions, our thoughts, we will share them, even over long distances. It will take time for the bond to manifest. But should either one of us perish, we shall feel it as if we ourselves died."
    l neutral "I will do it to help you."
    "Laila shifts her weight so she now has you pinned with one arm, while using her free hand to make a small cut in her neck. Pale red blood begins to seep from the incision."
    hide l with dissolve
    window hide

    menu:
        "Accept Laila’s offer.":
            window show
            #romantic music
            play music "Slow Life.mp3" fadein 1 fadeout 1
            "You nod, and Laila eases her hold on you. You lunge forward and press your lips to her neck."
            "Laila is stiff initially, but softens at your touch, and her breathing becomes ragged and hitched as you feed."
            "You’ve never fed like this before, your skin against Laila’s skin, the salty ichor passing directly from her veins into you. It’s an ecstasy you’ve never felt before."
            "As you drink, you feel Laila’s emotions as if they’re your own- fear for the future, concern for you, and her excitement at this taboo action you now engage in."
            "You take more of Laila in, desirous for this connection to last forever, but you feel her emotions begin to weaken in clarity. Somehow, you know, you are about to drink too much."
            "You release your hold on Laila, pulling away, and she gasps as if waking from a dream."
            "The two of you fall away from each other, laying on the floor, exhausted, even though the whole endeavor lasted no more than thirty seconds. Your hunger is no more."
            "After some time passes, the two of you rise from the ground, and Laila looks at you somewhat shyly."

            show l away with dissolve
            l away "Let’s not speak of what happened between us until this business with the cure is settled. We may not even have to worry about the consequences."
            "Laila bites her lip before speaking again."
            l smile "It felt good though."
            "With that, you and Laila depart your apartment and head in the direction of the manor Gabrielle told you about."
            $ laila_affection+=2
            $ drank_blood = True

        "Reject Laila’s offer, and resist the hunger.":
            window show
            "With a great deal of effort, you manage to purse your lips together and shake your head."
            "Laila eases up on you, covering the wound on her throat."
            "You sit up, shaking, and try to get control of your body. Every muscle screams out, driven to act by the vampiric essence flowing through you."
            "Laila watches you nervously, evidently ill at ease. Still, she offers you encouragement."
            show l neutral with dissolve
            l neutral "I believe in you, [player], you can beat it."
            "Despite this, you continue to detect the presence of your neighbors, the flow of their blood growing to a torrent in your ears."
            "Your fangs dig into your lips as you bite down, spilling your own blood."
            "Your shaking grows into full force convulsions, spasming on the floor of your apartment."
            "It would be so easy to give in- but you don’t. You hold strong."
            "It seems like this suffering will have no end."
            "And, just as suddenly as it all started, it’s over. You collapse to the floor, exhausted. The hunger is gone."
            "Laila approaches and helps you sit up. She looks on you with tenderness and care."
            l excited "You did it, I’m amazed. You truly are something special."
            "After you’ve taken some time to compose yourself, you rise to your feet, and Laila gives you a nod of respect."
            l neutral "The night’s getting on, we should get over to the mansion."
            "With that, you and Laila depart your apartment and head in the direction of the manor Gabrielle told you about."
            $ laila_affection+=1

    # neutral music
    scene street with fade
    play music "Strange Forest.mp3" fadein 1 fadeout 1
    "You and Laila traverse the quiet streets of town quickly, avoiding other pedestrians when possible."
    "Dark clouds obscure the sky- there will be no moon or stars to light your evening, just the orange sodium glow of street lamps."
    "You’re unsure of why, but you feel an urgency in the air, as if the whole of history is coming to a head tonight, in this town."
    "Before you arrive at your destination, you have a question for Laila."

    show l neutral with dissolve
    mc "Laila, this cure, what will you do with your life if it’s real?"
    "Laila stops walking and contemplates your question for a time."
    l neutral "I think I want to go back to New Mexico for a time, though. Just be away from the night and the shadows in a place baked by the sun."
    l away "I guess most of all I want to live a life where I don’t have to run anymore. Find someone to settle down with."
    l away "You’ve only lived this life a little while, but it takes a toll on you. I’ve barely lasted a decade like this, I can’t imagine an eternity on the run."
    l smile "Anyway, I’m confident we’ll find it."
    "With that, Laila continues on her way, and you follow close at hand."
    "On  the way to the mansion, you run into Cassandra, sipping a Demon energy drink and carrying a tote full of books."

    # exciting music
    play music "Cloudy Jewel.mp3" fadein 1 fadeout 1
    show l at left with ease
    show c smile at right with dissolve
    c "[player]! And Laila! What a coincidence! I was just on my way back from the library, studying up on vampire history."
    l smile "Oh, I’m so glad to see you’re alright. Sorry about the party going south, it’s uh, part of the vampire experience, unfortunately."
    c doubt "Don’t be sorry, it’s not your fault."
    c smile "Where are the two of you headed tonight?"
    l excited "We’re off to find a cure! The old mansion on the hill, we’ve heard there could be answers there."
    c doubt "The mansion… "
    "Cassandra pulls out a hefty book about old architecture in the town."
    c "I was reading about the history of vampire hunters, and Logan Velsing, a huge landowner in the 1980’s, owned a lot of buildings with ties to vampire hunters."

    mc"Velsing… Like Anne Velsing? And Han Velsing?"
    c "Exactly. They own a bunch of the older buildings in town, including that mansion."
    c "It doesn’t necessarily mean anything, but just be careful, ok?"
    l neutral "It could be something, but probably nothing. No one’s lived there for years I’ve heard. Still, thank you Cassandra. Stay safe."
    c wink "You too!"
    hide c with dissolve
    show l at center with ease

    # neutral music
    play music "Ominous Forest.mp3" fadein 1 fadeout 1
    "With that, you and Laila proceed across town to the mansion, the houses growing larger and more decadent as you approach."
    scene mansion ext with fade

    "Now the mansion rises out of the gloom of the night, still regal despite its decrepitude. It is of gothic style, imposing and austere."
    show l neutral with dissolve
    l neutral "Well our mystery vampire certainly picked one hell of a haunt."
    "You and Laila approach the vast doors of the manor, hesitating before you open the door. Laila turns to face you."
    l away "[player], I don’t know what waits for us beyond these doors, but I want to thank you for sticking with me through this."
    hide l with dissolve
    window hide

    menu:
        "Kiss Laila":
            window show
            # romantic music
            "You reach out to Laila and pull her in close to you. There is confusion in her eyes for half a second, before she realizes what’s going on and gives you a gentle smile."
            "You lean in and press your lips to Laila’s, and she returns your affection, holding you tightly. Despite the unnatural chill of both your bodies, it feels right."
            "After several moments in each other’s embrace, you and Laila separate."
            show l smile with dissolve
            l smile "That was nice. Let’s do it again sometime."
            l neutral "But it’s time we ended this. Let’s go."
            $ laila_affection+=2

        "Give her a handshake":
            window show
            "You extend a hand to Laila, who looks at you somewhat confused."
            show l away with dissolve
            l away "Oh, okay, uh. Not quite what I was expecting, but okay."
            "Laila grabs your hand and gives a somewhat halfhearted handshake."
            l neutral "Kind of overly formal for me."
            "You and Laila release each others’ hands, and Laila turns to face the door again."
            l neutral "Alright, let’s finish this."

    scene mansion int

    # tense music
    show l neutral with dissolve
    "You and Laila proceed through the aged doors of the manner, closing them behind you."
    "You find yourself in a grand hall, filled with antique furniture and suits of armor, walls bedecked by renaissance paintings, lit by oil lamps and candles. A balcony overlooks the room from the second floor. Laila takes a few steps forward."
    l neutral "Hello? Is anyone here?"
    "There is no response to Laila’s inquiry."
    mc "Can you sense anyone?"

    "Laila angles her head to the side and listens intently."
    l neutral "There’s something messing with my hearing. Something I can’t actually hear is getting in the way."
    "You try to listen too, and sure enough you feel whatever it is Laila is talking about. Like some sort of subsonic hum, dampening your senses."
    "Whatever it is blocking your hearing, it’s also making you feel a little bit dizzy. You take a step back and lean against the wall for support."
    l away "I don’t like this. Combined with what Cassandra told us, this does not bode well. We’re leaving."
    "Laila turns to make her way to the door, and is halted by loud sounds of metal clanging."
    "You look around and see that metal bars have come down over all the windows. Laila tries to open the front door but finds it locked."
    l neutral "I think we’re trapped."

    play music "Strange Guide.mp3" fadein 1 fadeout 1

    a "Indeed you are, vampire brats!"
    "Anne Velsing’s voice feels like it comes from all around you."
    a "Welcome to one of our many ancestral residences, designed with vampire entrapment in mind. I’m glad to see my snare has caught some of the runaways from our little surprise in the forest."
    l angry "Fuck, how many times do I have to deal with this bitch?"
    "Laila’s voice is filled with exasperation. Despite this interjection, Anne continues on."

    show l at left with ease
    show a neutral at right with dissolve
    a neutral "Now is the moment of my supreme triumph!"
    "Anne now reveals herself on the balcony, glaring down at you and Laila."
    a annoyed "You wretches will find abilities hampered by my brilliant inverse echolocator!"
    "Anne hoists a very complex-looking mechanical device, about the size of a smartphone."
    a annoyed "This broadcasts sound at the same level bats can hear, above human detection, powerful enough to weaken vampire brats like you!"
    l angry "Can you stop calling us that? It’s not as clever as you think it is."
    a angry "You fool! I am the mighty Anne Velsing; I am nonpareil! My whelp of a brother has been dealt with, and no one will stand between me and glory!"
    "Anne stows the inverse echolocator in a pocket, and leaps from the balcony, landing on the ground with a somersault. She vaults to her feet and brandishes her knife."
    a neutral "As the bard wrote, damned be him that first cries hold, enough!"
    "With a mighty cry, Anne charges you."

##---CHAPTER 7---

label laila_chapter7:
    scene mansion int with fade
    # tense or exciting music. Not sure which is better for a fight
    play music "Caravan.mp3" fadein 1 fadeout 1
    "You and Laila find yourselves dodging Anne’s furious knife swipes. You’re not sure how much damage a knife can do to you, but you’d still rather not get stabbed."
    "Even that simple task, though, proves hard enough in its own right. Anne’s device has you and Laila seriously off-kilter, and your movements are sluggish, like moving through water."
    "As you try to move away from the vampire hunter, you stumble backwards over an ottoman and into a plush leather armchair. Anne takes this chance to leap at you, her blade aimed at your neck."
    "Laila intercepts Anne, throwing herself into the hunter, causing her to lose her balance momentarily, giving you an opportunity to dive from the chair and onto the floor."
    "This defense has left Laila winded, sending her stumbling across the hall. Anne, not deterred, renews her assault, focusing solely on Laila now."
    "Laila avoids strike after strike, but only barely, Anne’s knife getting closer and closer with each swing."
    "You pull yourself to your feet and move to help Laila, but it is too late."
    "Laila, too focused on Anne, has neglected paying attention to her surroundings, and leaps backwards- crashing into a suit of armor, and impaling herself on the sword it held."

    # sad music
    "Laila lets out a gasp, the air driven from her lungs as the blade embeds itself below her ribcage. She appears unable to move."
    show a frown with dissolve
    a frown "Oh. I wasn’t expecting that."
    a neutral "Fortune smiles on me, I suppose."
    "Anne now turns to face you. Despite her relentless assault, she hardly seems out of breath."
    a neutral "Alright vampire. Surrender now, and I’ll make the deaths of you and your companion swift."
    a "For I will kill you both. It is simply a matter of whether I stake you, or leave you in the sun to burn."
    a "Or perhaps I shall bury you alive in the basement and let you starve to death over decades."
    a neutral "The only difference is the amount of suffering you go through. And the enjoyment I derive."
    hide a with dissolve
    window hide

    # tense music

    menu:
        "\"Why are you doing this?\"":
            window show
            "Anne looks genuinely puzzled at your question."
            show a confused with dissolve
            a confused "Why am I doing this? Surely you jest? The Velsings have always hunted your kind."
            a neutral "I merely aim to be the very best; as I said before, the nonpareil. To go down in history as the greatest Velsing that ever lived."
            a neutral "But if you mean this particular plan, it’s part of that bigger picture. You see, my brother, he was a fool. I lost you the other night because of him. But I anticipated that sort of failure."
            a neutral "I paid off the old woman, Gabrielle. While she is one of you, we are not entirely dissimilar. Her body count of your kind is impressive. I had her direct all those she could here."
            a frown "As for my brother, well. He won’t be getting in my way again."
            a neutral "I hope that answers your question, brat."

        "\"I think you’ve got a problem lady.\"":
            window show
            "Anne is taken aback."
            show a angry with dissolve

            a angry "What impudence! Were I not feeling gracious in my moment of triumph, I would smite you for that."
            "Anne shakes her head."
            a neutral "But it is no matter. You see, I aim to be the very best; as I said before, the nonpareil. To go down in history as the greatest Velsing that ever lived."
            a neutral "And this particular scheme, it’s part of that bigger picture. You see, my brother, he was a fool. I lost you the other night because of him. But I anticipated that sort of failure."
            a neutral "I paid off the old woman, Gabrielle. While she is one of you, we are not entirely dissimilar. Her body count of your kind is impressive. I had her direct all those she could here."
            a frown "As for my brother, well: he won’t be getting in my way again."
            a neutral "So I assure you, there is no problem. Except for you."

    "As Anne monologues, you look over to Laila, who remains slumped against the armor, in obvious pain. She doesn’t look good."
    a neutral "Come now vampire, do not make this harder than it has to be for the both of us."

    hide a with dissolve
    window hide

    menu:
        "\"Surely we can come to some sort of arrangement?\"":
            window show
            "Anne raises an eyebrow at you."
            show a confused with dissolve
            a confused "You are very different from other vampires I have met. Most try to kill me without a thought. Yet you want to make a deal with me? Very curious indeed."
            a neutral "I suppose I’m open to discussing alternatives with you."

        "\"Why would I ever want to make killing me easier for you?\"":
            window show
            "Anne scowls and opens her mouth as if to snap back at you, but pauses."
            show a frown with dissolve
            a frown "You’re right, why would you ever willingly surrender? I never would. And yet, while I will assuredly beat you in a contest of strength, I should not risk life and limb needlessly."
            a "I have won this battle."
            a neutral "So vampire, let us discuss alternatives to needlessly shedding each other’s blood."

    "As she thinks, Anne idly twirls her knife in your direction."
    a confused "What might I do with a vampire brat such as you? I can tell you’re new, so you’d be malleable."
    a neutral "Ooh, perhaps you could be an infiltrator for me, work your way into other vampire clusters. We could eradicate them together. An acceptable evil for the greater good."
    "Laila coughs now as she tries to speak."

    show a at right with ease

    show l away at left with dissolve
    l away "Don’t… help her."
    "Laila’s voice is hoarse, her breathing strained. Still Anne whirls around to look at her."
    a annoyed "Silence, you! Perhaps if you had half the brains as this one here, you wouldn’t be in this position."
    "Anne now returns her attention to you."
    a neutral "Now, where were we? Ah yes, you, joining me."
    a neutral "You have no kindred ties to the other vampires. You’re practically still human. You’d be ridding the world of a plague that sunk its fangs into you."
    "Anne chuckles."
    a neutral "I will admit, that was not an intentional pun. Haha."
    a neutral "Anyway, I suppose it’s worth mentioning that I will protect you from other vampire hunters."
    a "You could live a normal life. Well, close to one."
    a frown "And, should we ever find a cure, you would be amongst the first to get it."

    # sad music
    play music "Monologue.mp3" fadein 1 fadeout 1
    "Laila coughs and attempts speaking again."
    l away "You mean… there’s no… cure?"
    "At this, Laila coughs up blood. Anne glances over her shoulder at her."
    a angry "No you fool, haven’t you picked up on it? It was part of my ruse, my brilliant plan. And you fell for it."
    "Somehow, even battered as she is, Laila looks even more defeated at this definitive confirmation. She closes her eyes."
    a frown "Poor thing. Really killing the mood of my moment of triumph though. Perhaps I shall just end her now."
    "Anne takes a step towards Laila."
    mc "No!"

    "Anne halts her advance."
    a confused "And tell me, why should I spare this one AND you? I do not see how she will be of any use to my goals."
    mc "Well, just leave her until we’re done speaking."
    a frown "I do suppose killing her now would be rather poor form, especially if you are to become my agent. Is agent the right word? Perhaps I shall call you my familiar. What delicious irony that would be."
    "You take a deep breath. Laila is safe for the time being."
    hide l with dissolve
    show a at center with ease

    # tense music
    play music "Ominous Forest.mp3" fadein 1 fadeout 1
    a annoyed "Alright vampire, enough stalling. Time to make up your mind. Are you with me? Or shall I destroy you like so many that have come before?"
    "You have Anne where you want her. You can save Laila, it’s just a matter of choosing your tactics."

    hide a with dissolve
    window hide

    menu:
        "\"Yes Anne, I’ll join you.\"":
            window show
            "Anne gives you a smugly satisfied smile."
            show a neutral with dissolve
            a neutral "I knew you could not resist the temptation of working with a huntress of my skill and power."
            a frown "Of course, we will have to work out the details. After all, there is the matter of how you get fed."
            "She looks you up and down, then sheathes her knife."
            a frown "But I think you will be of great use to me. And think of the joy you will receive, knowing that you are a part of making me a legend."
            a neutral "Yes, there is a bright future ahead of us, my new vampire friend."
            "Anne approaches and clasps your shoulders in a comradely fashion."
            a neutral "Perhaps we shall become friends through this endeavor. And hopefully you prove more competent than my idiot brother."
            "Anne releases you and turns towards Laila now."
            a annoyed "Now, time to finish off the broken one. Then we can clear out the rest of this disgusting backwater of a town."
            "Anne’s attention is away from you. Now is your chance."
            hide a with dissolve
            window hide

            menu:
                "Bite her":
                    window show
                    "Anne has let her guard down, and you take the opportunity to strike."
                    "You lunge forward, and before Anne can react, you’ve sunk your teeth into her jugular vein."
                    "Anne releases a pained gasp, and struggles to shake you off her back, but you remain attached."
                    "You bite down harder, and her blood begins to flow into you. You’re invigorated, strength you’ve never known empowering you all the way to your core."
                    show a angry with dissolve
                    a angry "You… traitor."
                    "Anne’s voice, while weak, is full of fury. She swings her fists over her back and into you, futilely trying to beat you back."
                    "You taste Anne’s feelings in her blood- her overwhelming pride in herself, her self-assuredness, her burning hatred for vampires, and her bewilderment, astonishment at how you’ve outplayed her."
                    a angry "I will not go out like some animal."
                    "As Anne spits these words, she throws her whole body backwards, slamming you into the floor, and you lose your grip on her."
                    "She staggers to her feet and limps away from you, blood gushing from her neck in a torrent. Anne makes no attempt to cover her wound- she knows she’s dead."
                    "She makes it no more than a few steps before she falters, stumbling, then collapsing to the ground, still. Her blood pools around her on the floor."
                    "You rise shakily to your feet. With Anne defeated, you turn your attention to Laila."
                    hide a with dissolve
                    #Jump chap7endcommon

                "Go for her knife":
                    window show
                    "Anne has let her guard down, and you take the opportunity to strike."
                    "You dash forward and pull Anne’s knife. Before she can react, you drive it into her side, between the ribs."
                    "Anne’s breath is forced from her lungs and she faces you, shock and bewilderment in her eyes rapidly replaced by rage."
                    "She tries to swing her fists at you, but she is off balance, and you easily step out of the way, with each attempted blow further winding her."
                    "Anne opens her mouth to speak, and instead only coughs up blood. Evidently your attack has punctured a lung."
                    "Still, Anne manages to recover enough breath to utter a single word."

                    show a frown with dissolve
                    a frown "Why?"
                    "You look pointedly past her at Laila. The huntress shakes her head."
                    a angry "You… fool. My triumph… reduced to nothing."
                    "Her words come slowly and forcefully, each exhalation a battle in a war she is losing."
                    "Anne makes a final desperate attempt to claw at you, but you continue to back out of her reach with ease. She drops to her knees."
                    "You look down on the once-mighty huntress, brought low by her hubris. She glares back, her golden eyes burning with hatred. And then, the fire in her eyes begins to dim."
                    "With a final violent cough of blood, Anne keels over, dead."
                    "Now that the Velsing has been taken care of, you turn your attention towards Laila."
                    hide a with dissolve
                    #chapt7endcommon

        "\"I have a better idea. What if you and I became… lovers?\"":
            window show
            "Anne stares at you, baffled"
            show a confused with dissolve
            a confused "What? Where is this coming from?"
            "She looks as if she is about to shout at you, then relaxes."
            a frown "No, I see where this is coming from. You cannot deny my fabulous looks and regal poise."
            a neutral "I’m so glad that even your kind can appreciate true beauty."
            "Anne cocks her head to examine you from a new angle."
            a frown "And indeed, you are not of an unseemly sort. You’re almost… comely."
            a confused "But to be romantically involved with a vampire? It would be unheard of, it is unprecedented, it-"
            "Anne’s eyes alight with a new realization."
            a neutral "It would be a first of its kind conquest. I, the Velsing to tame the most dangerous of creatures."
            "A change has come about Anne. She re-sheaths her knife and approaches you slowly."
            "You see her eyes gleaming gold over the top of her glasses. They burn with a new intensity, one you have not seen before."
            "Before you know it, she has crossed the room and stands before you."
            "She leans in close to you and you feel her breath, hot, animalistic, on your neck. She smells of woodlands, of vast nature untamed, of life unbridled. You can feel her passion, almost as if it’s your own, a raging fire which cannot be quelled. Still, within you an even greater hunger resides."
            "Anne runs a hand across your cheek- she is warm, and that warmth lingers on your face even after she has withdrawn."
            "She whispers directly in your ear, almost silent, her words carried on the barest vibrations passing her lips. The once-loquacious huntress is now reduced to something much simpler."

            a neutral "Yes. I want you."
            "Indeed, you want her too. You hear her heart pounding with desire, blood flowing through her, more vibrant and full of life than any other you have perceived since you turned."
            "There is no room between the two of you, and Anne closes her eyes to kiss you. Now is your chance."
            hide a with dissolve
            window hide

            menu:
                "Bite her":
                    window show
                    "As Anne lets her guard down, you strike."
                    "The vampire hunter is not expecting your teeth in her jugular vein, and she writhes in panic trying to pull you off of her, but even her athletic skill is no match for your vampiric power."
                    "She wheezes in protest."
                    show a angry with dissolve
                    a angry "Not… like… this."
                    "Still, you bite down harder, and her blood begins to flow into you. You’re invigorated, strength you’ve never known empowering you all the way to your core."
                    "As you feed, Anne’s terror intensifies, the once haughty huntress brought low. Her heart beats faster, only accelerating her demise."
                    "You taste Anne’s feelings in her blood- her overwhelming pride in herself, her self-assuredness, her burning hatred for vampires, and just a hint of begrudging admiration for you. You’ve outplayed her."
                    "Anne’s heartbeat reaches a crescendo now, and the huntress’s struggles cease. The heartbeat now slows to a crawl, and Anne releases one last exhausted breath, before going limp. The heartbeat is gone, and Anne with it."
                    "You detach from Anne, whose lifeless body collapses to the ground in an undignified manner. Now you turn your attention to Laila."
                    hide a with dissolve

                "Go for her knife":
                    window show
                    "As Anne lets her guard down, you strike."
                    "While her lips press against yours, you draw her knife and drive it into her right side, between her ribs."
                    "Anne breaks away from you gasping. You’ve evidently succeeded in puncturing a lung, and now the huntress struggles for breath."
                    "Anne stumbles back, trying to pull the blade from her side, but doubles over in pain. She coughs and blood trickles from her mouth."
                    show a frown with dissolve

                    a frown "...Why?"
                    "You look pointedly in Laila’s direction. Anne scowls."
                    a angry "We could… have been amazing. You… fool."
                    "Her words come slowly and forcefully, each exhalation a battle in a war she is losing."
                    "You approach Anne, who shambles further back."
                    a angry "Stay back, you monster."
                    "She spits these words with venom, and breaks out into a fit of coughing, blood splattering on the floor in front of her."
                    "You look down on the once-mighty huntress, brought low by her vanity. She glares back, her golden eyes burning with hatred. And then, the fire in her eyes begins to dim."
                    "Anne topples over with a death rattle, landing on the ground with a dull thud."
                    "With the Velsing taken care of, you turn your attention to Laila."
                    hide a with dissolve

    "Before you approach Laila, quickly examine Anne’s corpse, finding the reverse echolocator and disabling it. Without the interference you hope to better help Laila."
    "As you step towards Laila, you realize things are worse than you thought. There is a concerning amount of blood pooled on the floor around her, and Laila looks even paler than she normally does. The sword remains lodged in her."
    "You’re not sure how, but you can sense that Laila is dying."

##---CHAPTER 8---

label laila_chapter8:
    scene mansion int
    # sad music
    "Anne Velsing is dead, and Laila could soon be joining her, the vampire bleeding out before your eyes."
    mc "Laila, this shouldn’t be able to kill you!"
    "Laila struggles to open her eyes. She gives you a bleary look."
    show  l away with dissolve
    l away "Well, I’m not a vampire biologist. We need blood to live, and I’ve lost a lot of it, it looks like."
    "She stops for a moment, the pain of speaking evident in her face."
    l away "And I think… there’s something on the sword. It stings, my body can’t heal itself like it normally can."
    "Laila winces now, her speech shifting the sword."
    mc "Okay, well the first thing we need to do is get that sword out of you."

    "Laila shakes her head."
    l away "No, I’m dying [player]. You need to leave. We don’t know if miss bitch over there has friends."
    "She gives an angry look at Anne’s corpse."
    mc "I’m not leaving you after how far we’ve come."
    "Before Laila can protest any further, you hoist her off of the sword. She coughs up a surprising amount of blood."
    "You cradle Laila’s bloody form in your arms, taking her to the chair you fell into earlier and set her down gently."
    l angry "Damn, that hurt. Some warning would be appreciated next time."
    l neutral "Sorry, thank you. But I don’t know what you can do for me."
    "You kneel next to Laila. Though you have only known her a few days, you cannot deny the deep feelings you’ve developed for her."
    "You would be devastated if you were to lose her."

    mc "Surely there’s something we can try!"
    "Laila merely stares at you grimly."
    l away "Even if I were to start healing now, I don’t know if I’d want to."
    mc "What do you mean?"
    l away "There is no cure. And this, the events of the last few days, I cannot bear to go through it again. I’ve run for so long, and for what? To watch more friends die?"
    l away "No, better to go now, knowing you’re safe and Anne is in hell."
    "You gaze into her eyes, and see they are filled with grief. While she is not terribly older than you, the weight of the last decade rests heavily on her."
    mc "What if I got you some of Anne’s blood, she’s not… empty? You could get some of your strength back."
    l away "I told you, I don’t want to go on."
    mc "Please, just try, for me."

    if laila_affection > 14:
        jump lailaTrueEnding

    if laila_affection > 6 and drank_blood == True:
        jump lailaGoodEndingA

    if laila_affection > 6 and drank_blood == False:
        jump lailaGoodEndingB

    if laila_affection < 7 and drank_blood == True:
        jump lailaBadEndingA

    if laila_affection < 7 and drank_blood == False:
        jump lailaBadEndingB

label lailaTrueEnding:
    # romantic music
    "Laila stares into your eyes for a long while before responding."
    l neutral "Okay. Let’s try it. I don’t want my passing to hurt you."
    "You run over to Anne’s corpse and scoop some of the pooling blood into your hands. It’s still warm and consequently rather disgusting."
    "You return to Laila and hold your cupped hands out to her, which she sips from delicately."
    "Once she’s done drinking, Laila makes a face at you."
    l angry "This better work, because that blood was foul, and I refuse to let that be my last meal."
    "Even as she speaks, you notice the wound in Laila’s abdomen beginning to heal- the jagged hole ripped by the sword is growing back into unbroken skin."
    "Laila follows your eyes down."
    l excited "Well, I’ll be damned."
    "Laila is able to sit up straighter now, and takes a deep breath in, no longer in nearly as much pain."
    l neutral "Well, here I am, ready to keep going on living, with nothing to live for."
    "You pointedly frown at her."
    l neutral "What?"
    mc "You have me."
    "Laila falters a moment before speaking."
    l away "I… I suppose you’re right. I didn’t want to admit it. But I don’t think I can deny it."

    l neutral "You’ve done more for me, [player], than anyone else in recent memory. You came with me on this crazy adventure that nearly got us both killed."
    l smile "Without the Velsings to worry about, I don’t have to run anymore. I can settle down, start a life… with you."
    l smile "I’ve got it bad for you, [player]. I want to be with you. You’ve given me something to look forward to."
    "Before Laila can say more, you lean in and kiss her. She seems startled for a moment, perhaps not expecting you to return her feelings quite so suddenly, but any hesitancy is gone quickly."
    "Laila returns the kiss with passion, pulling you close to her. You make no objection."
    "The two of you embrace with the vigor of those who have just escaped a brush with death, seeking to make the most of your time."
    "After a couple minutes pass- during which your kiss almost certainly became a makeout session- Laila stops you, gasping for breath."
    l neutral "You know [player], we’ve been together for every step of your journey, and quite frankly I’m amazed at how well we understand each other."
    l smile "I don’t think it’s chance that we met. I don’t believe in stuff like fate or destiny, but it’s hard to deny what has passed between us."
    l smile "And you know, an eternity like this would have been unbearable without someone who understands me, who understands what I feel about being a vampire."
    l away "And I know this is weird to come in the middle of a heated moment between us, but I felt it needed to be said. I’m sorry."
    l smile "I guess I could have put it more simply- I love you, [player]. I hope you realize that."
    "Laila averts her eyes and gives a shy smile."
    l away "It’s been a while since I’ve said that to anyone."
    hide l with dissolve
    window hide

    menu:
        "\"I love you too, Laila.\"":
            window show
            "You confess your shared feelings to Laila, and her smile widens."
            show l smile with dissolve
            l smile "That means the world to me."

        "Kiss her.":
            window show
            "You take hold of Laila’s hand and pull her close to you, before gently kissing her. She returns the kiss with an intensity unlike any you have experienced thus far. After a moment she breaks away."
            show l smile with dissolve
            l smile "That means the world to me."


    l excited "You know player, let’s leave this all behind. This town, these people. We can go someplace new and be ourselves. Come with me back to New Mexico."
    mc "Really?"
    l excited "Really! So what if we can’t live by day, we’ll be together. Even at night, the desert is beautiful."
    mc "Alright, let’s do it."
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
    "And so it was, you and Laila together, into the future, forever."


label lailaGoodEndingA:
    # romantic music
    "Laila stares into your eyes for a long while before responding."
    l neutral "Okay. Let’s try it. I don’t want my passing to hurt you."
    "You run over to Anne’s corpse and scoop some of the pooling blood into your hands. It’s still warm and consequently rather disgusting."
    "You return to Laila and hold your cupped hands out to her, which she sips from delicately."
    "Once she’s done drinking, Laila makes a face at you."
    l angry "This better work, because that blood was foul, and I refuse to let that be my last meal."
    "Even as she speaks, you notice the wound in Laila’s abdomen beginning to heal- the jagged hole ripped by the sword is growing back into unbroken skin."
    "Laila follows your eyes down."
    l excited "Well, I’ll be damned."
    "Laila is able to sit up straighter now, and takes a deep breath in, no longer in nearly as much pain."
    l neutral "Well, here I am, ready to keep going on living, with nothing to live for."
    "You pointedly frown at her."
    l neutral "What?"
    mc "You have me."
    "Laila falters a moment before speaking."
    l away "I… I suppose you’re right. I didn’t want to admit it. But I don’t think I can deny it."
    l neutral "You’ve done more for me, [player], than anyone else in recent memory. You came with me on this crazy adventure that nearly got us both killed."
    l smile "Without the Velsings to worry about, I don’t have to run anymore. I can settle down, start a life… with you."
    l smile "I’ve got it bad for you, [player]. I want to be with you. You’ve given me something to look forward to."
    "Before Laila can say more, you lean in and kiss her. She seems startled for a moment, perhaps not expecting you to return her feelings quite so suddenly, but any hesitancy is gone quickly."
    "Laila returns the kiss with passion, pulling you close to her. You make no objection."
    "The two of you embrace with the vigor of those who have just escaped a brush with death, seeking to make the most of your time."
    "After a couple minutes pass- during which your kiss almost certainly became a makeout session- Laila stops you, gasping for breath."
    l neutral "Before we go any further, let’s do something about the corpse. Even dead the bitch is spoiling my fun."

    "She casts a somewhat rueful gaze towards Anne’s body."
    "Laila, now fully healed it seems, assists you in dragging the huntress’s corpse out of the grand hall and a remote drawing room- where you also happen to find the levers which deactivate the mansion’s lockdown mechanism."

    scene black with fade

    "Afterwards, you and Laila spend some time discussing your future."
    "This mansion, with all its accouterments and lavish furniture, would make a lovely place to live, provided its exterior sees some renovation. This is where your future will be."
    "You and Laila spend the remainder of the night, and much of the following day, … ‘breaking in’ each of the mansion’s numerous rooms."
    "By the end of it, even with your vampiric enhancements, the two of you are thoroughly exhausted."
    "The following evening, you call up Cass and she assists you and Laila in burying Anne out in the woods. For all the trouble she caused, she deserves at least that much."
    "You and Laila are together almost always in the subsequent nights, splitting your time between repairing the mansion and locating the remaining vampires in town."
    "You let them know the danger has passed and, should they need it, your doors are open to provide a safe haven."
    "As time passes, you find your bond with Laila, formed from drinking her blood, has begun to develop. You can sense each other’s feelings, and sometimes communicate wordlessly."
    "Your relationship only deepens and strengthens because of this newfound connection, with disagreements between the two of you resolving quickly and amicably. Perhaps this should be standard practice for all couples."
    "In a few months, the mansion is repaired, and you and Laila open it for fabulous midnight parties. Vampires and regular humans attend, with the vampires on their very best behavior, and the humans never suspecting a thing."
    "All in town would come to know of the eccentric kind-hearted couple who fixed up the old mansion on the hill, were never seen by day, and were remarkably supportive of town blood drives; a point of pride for all."
    "And so it was, you and Laila together, into the future."

    $ persistent.ending = 2
    return

label lailaGoodEndingB:
    # romantic music
    "Laila stares into your eyes for a long while before responding."
    l neutral "Okay. Let’s try it. I don’t want my passing to hurt you."
    "You run over to Anne’s corpse and scoop some of the pooling blood into your hands. It’s still warm and consequently rather disgusting."
    "You return to Laila and hold your cupped hands out to her, which she sips from delicately."
    "Once she’s done drinking, Laila makes a face at you."
    l angry "This better work, because that blood was foul, and I refuse to let that be my last meal."
    "Even as she speaks, you notice the wound in Laila’s abdomen beginning to heal- the jagged hole ripped by the sword is growing back into unbroken skin."
    "Laila follows your eyes down."
    l excited "Well, I’ll be damned."
    "Laila is able to sit up straighter now, and takes a deep breath in, no longer in nearly as much pain."
    l neutral "Well, here I am, ready to keep going on living, with nothing to live for."
    "You pointedly frown at her."
    l neutral "What?"
    mc "You have me."
    "Laila falters a moment before speaking."
    l away "I… I suppose you’re right. I didn’t want to admit it. But I don’t think I can deny it."
    l neutral "You’ve done more for me, [player], than anyone else in recent memory. You came with me on this crazy adventure that nearly got us both killed."
    l smile "Without the Velsings to worry about, I don’t have to run anymore. I can settle down, start a life… with you."
    l smile "I’ve got it bad for you, [player]. I want to be with you. You’ve given me something to look forward to."
    "Before Laila can say more, you lean in and kiss her. She seems startled for a moment, perhaps not expecting you to return her feelings quite so suddenly, but any hesitancy is gone quickly."
    "Laila returns the kiss with passion, pulling you close to her. You make no objection. The two of you embrace with the vigor of those who have just escaped a brush with death, seeking to make the most of your time."
    "After a couple minutes pass- during which your kiss almost certainly became a makeout session- Laila stops you, gasping for breath."
    l neutral "Before we go any further, let’s do something about the corpse. Even dead the bitch is spoiling my fun."
    "She casts a somewhat rueful gaze towards Anne’s body."
    "Laila, now fully healed it seems, assists you in dragging the huntress’s corpse out of the grand hall and a remote drawing room- where you also happen to find the levers which deactivate the mansion’s lockdown mechanism."

    scene black with fade
    "Afterwards, you and Laila spend some time discussing your future."
    "This mansion, with all its accouterments and lavish furniture, would make a lovely place to live, provided its exterior sees some renovation. This is where your future will be."
    "You and Laila spend the remainder of the night, and much of the following day, … ‘breaking in’ each of the mansion’s numerous rooms."
    "By the end of it, even with your vampiric enhancements, the two of you are thoroughly exhausted."
    "The following evening, you call up Cass and she assists you and Laila in burying Anne out in the woods. For all the trouble she caused, she deserves at least that much."
    "You and Laila are together almost always in the subsequent nights, splitting your time between repairing the mansion and locating the remaining vampires in town."
    "You let them know the danger has passed and, should they need it, your doors are open to provide a safe haven."
    "As time passes, you and Laila find you are not quite a perfect couple. There are occasional squabbles, a tiff here and there. But you two emerge from each conflict stronger and closer."
    "Nothing can break the bond you two have formed."
    "In a few months, the mansion is repaired, and you and Laila open it for fabulous midnight parties. Vampires and regular humans attend, with the vampires on their very best behavior, and the humans never suspecting a thing."
    "All in town would come to know of the eccentric kind-hearted couple who fixed up the old mansion on the hill, were never seen by day, and were remarkably supportive of town blood drives; a point of pride for all."
    "And so it was, you and Laila together, into the future."

    $ persistent.ending = 2
    return

label lailaBadEndingA:
    #sad music
    "Laila looks at you firmly."
    l angry "No [player], I don’t have anything left to live for. I get you might feel deeply for me, but I can’t say I feel the same way. This is it."
    "She lets out a rough cough, and a stream of blood spews forth."
    l away "Please, I don’t have much longer, don’t fight with me in my last moments. Let’s think about the good you’ve done here."
    l smile "So many other vampires are going to be safe because of you. They can live the kind of life I would have wanted."
    l smile "Go out and bring good into the world, okay? And try to avoid turning into a winged rodent, if you can. Do that specifically for me."
    "Though it is very difficult for her, Laila laughs at her final remark."
    "With a deep sigh, Laila closes her eyes, her body takes on a stillness like death, and you know she is gone from the world."

    hide l with dissolve
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
    scene black with fade
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

    $ persistent.ending = 4
    return

label lailaBadEndingB:
    #sad music
    "Laila looks at you firmly."
    l angry "No [player], I don’t have anything left to live for. I get you might feel deeply for me, but I can’t say I feel the same way. This is it."
    "She lets out a rough cough, and a stream of blood spews forth."
    l away "Please, I don’t have much longer, don’t fight with me in my last moments. Let’s think about the good you’ve done here."
    l smile "So many other vampires are going to be safe because of you. They can live the kind of life I would have wanted."
    l smile "Go out and bring good into the world, okay? And try to avoid turning into a winged rodent, if you can. Do that specifically for me."
    "Though it is very difficult for her, Laila laughs at her final remark."
    "With a deep sigh, Laila closes her eyes, her body takes on a stillness like death, and you know she is gone from the world."
    hide l with dissolve

    "You are overcome with overwhelming grief. This beautiful wonderful woman is gone. If only things had been different, had you been closer to her, things might have played out differently."
    "Despite the injuries she suffered before passing, Laila looks serene. She passed from this world to a better place, happy."
    "You leave Laila where she is, and decide to investigate the mansion for a way to disable whatever mechanism locked the doors and barred the windows."
    "After some time searching, you find some levers in a drawing room on the second floor, which seem to lift the security of the place."
    "You phone Cass to let her know what has happened, and she arrives to keep you company, and help you deal with the remains."

    scene forest with fade
    "You sleep in the mansion during the day, and the following evening you and Cass bury Laila in the forest. You leave Anne’s body in the mansion, perhaps as a warning to any future Velsings who might come."

    scene apartment with fade
    "You return to your apartment and begin doing what Laila did- working nights at bars to eke out a living."
    "Afterwards, you and Cass drift apart. You are listless with Laila gone, and Cass has a full human life to live."
    "You seek out what’s left of the vampire community in town, but after the Velsing assault, those who aren’t dead dare not congregate. The current threat may have passed, but few believe it is gone for good."

    scene black with fade
    "Many of those who remain blame you for Laila’s death. She was well-liked, and the troubles started after she took you under her wing, after all."
    "You think often of her- her kindness, her humor and, perhaps most of all, the great sorrow she lived with. The plight of her condition, her desire to return to the world of the living, to the waking world and the sun."
    "You know you will never forget her. And you respect her final wishes. You do what you can to bring some small amount of good into the world- you will sometimes stop petty criminals and miscreants in the night."
    "And, of course, you never turn into a bat, the ‘winged rodent’ Laila so disdained."
    "And so your nights go on, monotonous, alone. The town changes around you, but you do not. You are a fixture stuck in the past."

    $ persistent.ending = 4
    return
