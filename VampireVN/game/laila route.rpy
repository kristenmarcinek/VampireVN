label LailaRoute:
    label laila_chapter4:
        scene forest
        # tense music
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

        menu:
            "\"Oh thank god, you’re alright!\"":
            	"Laila’s countenance, somewhat grim, now lightens."
                show l excited with dissolve
                l excited "I’m glad to see you’re okay too, [player]."
            	$ laila_affection+=2

            "\"Don’t sneak up on me like that!\"":
            	"Laila lets out a soft chuckle."
                show l excited with dissolve
                l excited "I didn’t know you were such a fraidy cat. Are you sure you’re qualified to be a creature of the night?"
            	$ laila_affection+=1

            "\"Took you long enough.\"":
            	"Laila gives you a withering stare."
                show l angry with dissolve
                l angry "Perhaps had you not made such a racket in your escape, I would not have had to run quite so far to hide."
                $ laila_affection-=1

            "Remain silent.":
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
        "She lets out a little laugh."
        hide l with dissolve

        menu:
            "Stay quiet.":
            	"You remain silent and Laila’s laugh peters out."
                L away "Sorry, wrong time, yeah."
            	$ laila_affection-=1

            "Give a little laugh.":
            	"You release a little giggle at Laila’s joke, and she gives you a broad smile."
                L excited "I’m glad you found it funny."
            	$ laila_affection+=1

            "Make a quip back.":
            	mc "Yeah, I expected you to buy me a drink first."
                "Laila chuckles at your remark."
                l excited "Next time, [player]."
            	$ laila_affection+=1


        l neutral "Well, we’re going to be here for a while. I guess I can answer any questions you might have."
        #romantic music
        hide l with dissolve

    #CHANGE: make sure that the game doesn't break bc there's no option to pass the questions, hopefully it just returns

    label laila_pit:
        menu:
        "Ask about Laila’s past." if not lq1:
        	mc "If you don’t mind, could I know some more about your past?"
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
        	mc "Can you tell me what things have been like for you recently?"
            l neutral "I mean, I’ve been living here for something like 9 months? After Grand Rapids, I needed to find a new place to settle down. My ex, some of her friends were out here. Felt like it could be safe. And it has been."
            l away "But there’s not a whole lot to life here beyond subsisting. I take shifts at some of the local bars a few nights a week. It’s enough to get by here."
            mc "You’re a bartender?"
            l neutral "Yeah. Not what I imagined spending my life doing, but there’s not a whole lot of employment options for people in our position. It’s not awful."
            l away "But it’s not great, either."
            $lq2 = True

            jump laila_pit

        "Ask about the other vampires in town." if not lq3:
        	mc "Can you tell me about the other vampires living in town?"
            l neutral "The ones that are left you mean? There’s something like 20ish of us? I knew a couple of them through my ex and they’re good enough folks."
            l away "It’s pretty tough to find vampires who aren’t into the whole live feeding thing. The New York City vamps are living it up, they disguise their kills as regular murders, they never have to worry about getting caught."
            l away "Vampire hunters always go after us- they look for blood banks with mysteriously missing blood. This is why I split with my ex. She didn’t share my objections about killing, and wanted to protect herself."
            l neutral "I’d rather not discuss it further."
            $lq3 = True

            jump laila_pit

        "Ask what Laila thinks of you." if not lq4:
        	mc "Well, what do you think of me?"
            "Laila’s eyes widen briefly at your question, then she looks away."
            l away "Look, I think you’re nice enough. But I don’t really know you all that well yet. And things aren’t great, you know?"
            $lq4 = True

            jump laila_pit

        "From everything Laila’s said, you’re picking up on something."
        mc "Do you like being a vampire?"
        "At this, Laila lets out a deep sigh."
        l away "No."
        "She is silent for a long while."
        L neutral "Okay, I probably owe you more of an explanation than that."
        L neutral "I tried very hard to adapt. But the sort of existence I have to live- the things we have to do just to survive- is miserable. The speed and the strength is neat, but it’s not worth never getting to feel the sun on my skin again."
        L away "Living this way forever? I see it as a curse."
        L neutral "I’m sorry, I’m sure you’re enjoying the experience. I don’t mean to upset you."
        "It’s all for her to share, and a great deal for you to process."
        Menu:
        "\"It’s okay, I get where you’re coming from, I feel that a bit too."":
        	Jump pitInquiry2a
        	$ laila_affection+=2
        "\"I’m loving it, but your feelings are totally valid."":
        	Jump pitInquiry2b
        	$ laila_affection+=1
        "\"Yeah, how could anyone not love this?"":
        	Jump pitInquiry2c
        	$ laila_affection-=2

        Label pitInquiry2a
        "Laila cheers up a bit at your response."
        L smile "Thank you [player]. I appreciate your empathy. And I’m glad someone else feels the way I do."
        "Laila stares into your eyes, raising a hand and allowing her fingers to brush lightly against your cheek, before she quickly pulls away."
        L away "Sorry, I’m going through a lot right now."
        	Jump pitInquiry2common

        Label pitInquiry2b
        "Laila takes a deep breath and nods at your response."
        L neutral "That’s more understanding than I get from most others, so I appreciate it."
        	Jump pitInquiry2common

        Label pitInquiry2c
        "Laila goes from quiet and contemplative to furious in an instant."
        L angry "Yeah, of course, your feelings are the only ones that matter. Sorry I bothered to open up to you. You’re just like all the others."
        "The two of you sit in the silence uncomfortably."
        	Jump pitInquiry2common

        Label pitInquiry2common
        "After several minutes of quiet, Laila speaks up again."
        L neutral "Well, I think we should at least try to get some sleep. I can only imagine tomorrow night will be busy. Sleep tight, [player]."
        "With this, Laila closes her eyes and, still standing, settles into a slumber like death."
        "You decide to follow suit, and rapidly fall into a deep and dreamless abyss."
        Jump laila_chapter5
