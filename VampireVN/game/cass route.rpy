##---CHAPTER 4---

label cass_chapter4:
    # Tense Music
    hide c
    hide l
    
    "You lose sight of Cass after a while, but for some reason you can still tell where she is."
    "It’s as if you can sense her, hear her heartbeat in the air"
    "You hear the Velsings gaining on you, and you remember the powers Cassandra mentioned earlier."
    show a angry with dissolve
    "You see Anne Velsing chasing after you with ferocity."
    a "Come here bloodsucker!"

    #CHANGE: listen to radha for further clarification, you're confused about whether or not the choices are supposed to be eliminated and if hypnosis is the "canon" option

label anne4fight:
    hide a with dissolve
    window hide

    menu:
        "Turn into a bat" if not a1:
            window show
            "You try to picture yourself as a bat but you can’t focus."
            "Anne is gaining on you."
            show a neutral with dissolve
            a "I’m screaming! You can’t even turn into a bat! Pathetic."

            $ a1 = True
            jump anne4fight

        "Try hypnosis":
            window show
            pass

        "Try floating" if not a2:
            window show
            "You jump as high as you can but you can’t get yourself to float"
            "You trip and fall, causing Anne to gain on you."

            show a neutral with dissolve
            a "Are you trying to fly? How long have you been a Vampire, a day!"
            "She doesn’t know that she’s more or less right…"
            $ a2 = True
            jump anne4fight


    "This is a gambit you can’t afford to fail on."
    "You stare into Anne’s eyes, trying desperately to get her to stop chasing you."
    "It doesn’t seem to be working, but then…"
    "You both freeze in your tracks."
    "She can’t move, but you can’t move either."
    "You stare at each other, both powerless."
    "Even though her mouth isn’t moving, you can almost hear Anne say:"

    show a angry with dissolve
    a "You vermin! I should have known you’d be a E-vamp!"
    "E-Vamp? What the hell is an E- Vamp?"
    show a confused
    a "Emphatic Vampire? E Vamp? Hypnotiser? Oh my god, you are one day old. Can’t let Han hear about this."
    "How did she hear your thoughts?"

    show a angry
    a "Oh for crying out… ARE YOU STUPID? You are hypnotizing me! You’ve made a perverse psychic link between us!"
    a "You’re freshly stolen blood, so you don't know how to do any actual hypnosis stuff, but as long as you don't move, I don’t move."
    a "BUT! Before you gloat, keep in mind that as soon as you move or break concentration even a little, I’ll slit your pretty little throat!"

    "You see. You're both in a stalemate. If you move, she kills you. But if you don’t, she’s trapped."
    "You hear a rustling in the wood, and as if in sync, you both think–"
    show a confused
    a "Oh shit."

    "Han Velsing appears, lugging an barely conscious Cassandra behind him."
    show a at left with ease
    show h neutral at center
    show c doubt at right
    with dissolve

    "You take the moment to let Anne go and dash into the bushes."
    #Batbashers are just like standin name
    h "The heir to the Velsing bloodline, head of the Batbashers, and you couldn’t even kill a day old vamp?"

    show a annoyed
    a " I got caught off guard ok! Don’t tell the others."
    show h unsure
    h "Like you didn’t tell dad about Ren? Oh wait…"
    show a frown
    a "We were young Ok! It was ages ago! Why are you still fixated on that!"
    show h sigh
    h "Why am I still… WHY AM I STILL FIXATED ON THAT?"
    h "Are you for real?"

    hide a
    hide h
    hide c
    with dissolve

    "As they bicker, you have time to focus."
    "You finally turn into a bat and sneakily fly into the trees and hide"

    show a angry at left
    show h sigh at right
    #show c doubt at right
    with dissolve

    a "Look, I’ve said I’m sorry for outing you a million times. It’s in the past! Dad’s gone!"
    h "So you betray me, exploit my weakness, stab me in the back… and now that it’s all over-"
    h "You get to be all \"We’re all in this together! We’re family!\""

    show h unsure
    h "In case you forgot, I was supposed to be the successor!"
    h " And it wasn’t until you exploited my weakness that you got in charge!"
    h "So yes, I am gonna tell the others."

    show a annoyed
    a "Oh COME ON!"
    a "You never know when to give up!"
    a "I’m being magnanimous! I’m winning with grace!"
    a "If I were a worse person, you wouldn’t even be a vampire hunter anymore!"
    show h neutral
    h "Forget it."

    #Maybe this oscillates with some angry and disgusted faces for the Velsings
    "You feel powerless."
    "These aren’t just some vampire hunters, they’re the heads of the whole organization."
    "You need to figure out how to get Cassandra out of there!"

    #CHANGE: where the fuck are we
    # also this entire menu choice confuses me

    menu:
        "Attack the Velsings":

            "You decide that an all out brawl is the only way to allow Cassandra to escape."
            " You aren’t much of a fighter, but you could maybe turn back into a human and fall on someone?"

            menu:
                "Fall on Han":
                    pass
                "Fall on Anne":
                    pass
                    
            "You miss both and fall on the ground next to them."
            "Your whole body hurts like hell, but you seem to have created a cloud of dust."
            "Both Velsings are coughing as you grab Cassandra and run as far away as possible."



        "Get the Velsings to chase you":

            "You fly in front of the Velsing’s and dash away."
            #both objective
            a "You won't be able to tell the others anything once I catch [pronoun]!"
            h "Sigh… not if i’m the one who catches [pronoun]."
            "You fly as fast as you can as the Vellsings fire stakes and bullets at you."

            hide h
            hide a
            with dissolve
            "Once you zoom far enough that you don’t hear them, you transform back, tumbling into the grass."
            "Turning to a bat has you beyond exhausted. You luckily still have your phone on you, so you text  Cassandra your location and pass out."

            scene forest with fade
            show c neutral with dissolve
            c neutral "Hey, you. You’re finally awake."

            menu:
                "What.. happened..":
                    pass
                "Are you ok?":
                    $ cass_affection+=1
                "I’m in deep, deep pain.":
                    pass

            c neutral "Let’s get you up, we need to head home."
            #"You walk as fast as you can until you get out of the woods and reenter the town"
            scene street

        "Wait in the tree":

            "You wait in the tree hoping for an opening."
            a "Anyways, who’s the girl?"
            h "She’s a human. She seems to be close to some of the vampires, but…"
            h "... she’s not a vampire yet. I’ve been cooking up a plan for her."
            h "For tonight though, I just wanted to get her to safety."
            c "Wha… Whats going on?"
            a "Ahh, she’s awake! Now what?"
            h "Now we find the other vamps. She can find her way back home."

            hide h
            hide a
            with dissolve
            "Once you made sure the Velsings were far enough away, you followed Cassandra as she ran home."
            "What was Han talking about? What did he have planned for her?"
            scene street with fade
            "As you both finally get back in town, you turn back into a human."
            mc "Cassandra! It's me."
            c "[player]! I’m so happy you’re ok! That was terrifying!"


    # Neutral Music

    #CHANGE: i don't know where this line of dialogue goes, it was originally after the last line of dialogue in the attack option but also after the jump to the main script
    #---resolved

    "You walk as fast as you can until you get out of the woods and re-enter the town."
    scene street with fade
    "You both walk down the street, catching your breath after the trauma you just experienced."
    "It all slowly starts to sink in."
    "You’re being hunted. Hunted by trained professionals."
    "Laila hasn’t been returning your calls, she might be dead."
    "Who knows what could have happened to Cassandra?"
    "You look at her, thinking about everything that happened so far"

    #Want to have a couple variables here, need help.
    #If you chose kiss:
    if cass_kiss:
        "The fall, the almost kiss."

    "The adrenaline of it all, the danger."
    "You feel like you can’t let anything go unsaid."
    "You don’t want to regret not telling her how you feel."
    "But you also worry about bringing her closer into your life."
    "Closer to danger."
    c "Look, I know you have something on your mind, please tell me!"

    menu:
        "\"Cassandra, I don’t think you should be around me anymore.\"":
            show c doubt with dissolve
            c "What… Look. I knew you being a vampire was dangerous from the get go, ok?"
            c "I’m not going to let you die, just so I can be safe!"
            c "You know me. You know I’d never give up on you. Because I care about you!"
            c "Because I lo-"
            c "Because I like you!"
            "You heard that. You heard what she wanted to say."
            "But why is she holding back?"
            "Is it fear of losing a friendship?"
            "Or something else?"


        "\"Cassandra, I need to tell you something\"":
            mc "Cassandra, what if I turned you into a vampire?"
            mc "With these hunters after us… with the danger I'm putting you in…"
            mc "Maybe you could have powers too?"
            show c smile with dissolve
            c "Really? Wow, I need a minute to think about this…"
            c "I've been dreaming of being a vampire since I was a kid…"
            "She was right. You remember nights in middle school where you played vampires and werewolves together."
            "Reading the Moonlight trilogy… watching Nosferatu…"
            c "But…"
            "Cassandra seems conflicted, lost in thought..."
            "Clearly something is holding her back… but what?"
            "You decide not to press her on it. It's been a long night."

    scene apartment with fade
    "You finally make it home and the exhaustion starts to hit."
    "You let Cassandra stay over, knowing she wouldn’t leave you alone after all this."
    "In exhaustion you fall asleep in each other’s arms."
    "You drift away, anxious for what comes next."

##---CHAPTER 5---

label cass_chapter5:

    #CHANGE: where the fuck are we
    # Tense Music
    "You feel it. The hunger."
    "It grows every day, tormenting you, torturing you."
    "You haven’t heard from Laila since the night of the attack, and you have no idea how to get blood otherwise."
    "Well… except for the obvious."
    "But you wouldn’t do that…Would you?"
    "Cassandra’s been bringing you raw meat, and it's been keeping you alive."
    "But the hunger is getting worse."
    "You get a text from Cassandra, inviting you to the library."

    scene street with fade
    "You strut through the night streets, hunger pounding through you."
    "A strange figure approaches you, pushing you down."
    "Stranger""This is for the Bloodbashers!"
    "As you get back, the stranger trips and falls."
    "They knock themselves unconscious."
    "They attacked you first… would it really be so bad if you drank their blood?"

    menu:
        "Drink their blood":

            "You bite into their neck and suck their blood."
            "After all of your hunger, you feel a sense of relief."
            "You let go before you kill them, and rush to the library."
            scene library with fade
            show c smile with dissolve
            c "Hi [player]!"
            show c doubt
            c"Is that fresh blood on your mouth?"
            mc "Umm… No?"
            $ cass_affection-=3
            mc "Anyway… Why did you call me here?"


        "Leave them alone":
            "You leave them knocked out and rush to the library."
            scene library with fade
            show c smile with dissolve
            c "Hi [player]!"
            show c confident
            c "I’ve got something important to show you!"

    # Romantic Music
    show c neutral
    c "You know the book I told you about? The diary of Bran Velcant?"
    c " I finished it, and well.."
    c doubt "It does not end well…"
    c "Bran Velcant’s brother, Abram, always had a contentious relationship with him."
    c neutral "They used to be a part of this group of vampire hunters called Batbashers."
    c "But when Bran turned, Abram was unwilling to sell out his own brother."
    c "I was kind of hoping that Abram would learn to accept Bran…"
    c doubt "But he didn’t."
    c neutral "The diary stops abruptly, it was never finished."
    c "But in this book..."

    "Cassandra pushes another huge book titled {b}{i}A Historie of the Order of the Batbasher{/i}{/b} towards you."
    c " Someone named Abram kills his own vampire brother to found this order."
    c "And look at his last name..."
    "You open the book and see Abram’s full name."
    c "Abram Van Velsing."
    c "Abram killed Bran, and coined the motto \"firmitas voluntatis in fraudem.\""

    c smile "It’s been a while since I took Latin, so it’s a little rusty…"
    c "But it translates to \"strength of will over the deceit of the heart.\""
    c "Basically, Abram founded this organization on betrayal, on hurting even those you care about the most for \"justice.\""
    mc "And that organization became the Batbashers, led by the Velsing siblings.."

    c wink "You’re so sharp, [player]!"
    c smile "So, I grabbed every book I could find with any relevance."
    "You eye Cassandra’s mountain of books…"
    "This is going to be a really long day isn’t it..."
    c "Let’s get researching!"
    "You toil through the mountain of books, hoping to find more information about the Batbashers."

    "After a while, you start to get into a groove."
    "It reminds you of when you and Cassandra studied together before a big test."
    "Cassandra would be dealing with transitioning and family stuff, but still made time to study with you."
    "Just like back then, Cass brought a bunch of cans of Demon Energy Drinks to fuel the study sesh."
    "She had gone through the \"Big Blue Betrayal\", \"Red Anguish\", and \"Emerald Elation\" flavors."
    "You were getting tired, so you decided to drink the…"
    hide c with dissolve
    window hide

    menu:
        "Green Apple Envy":
            pass

        "Ultra Sour Ushy Gushy":
            pass

        "Brorple Smorp":
            pass
        "That one trans flavor you forget the name of, but it has baby blue and hot pink on it":
            $ cass_affection+=1

    window show
    show c wink with dissolve
    c "Nice choice, [player]."
    show c smile

    "You both take a break and chat for a while."
    "You talk about the bizarre things you only discuss during a long study sesh on 3 cans of monster."
    "Would you be my friend if you were a worm, would you rather bend fire or water, etc."
    "And eventually, as the day goes on, the conversation steers towards…"
    c smile "You know, Pet Names! Like fun little names people call their partner!"
    c doubt "My awful chaser ex Darryl called me honey bun, and at the time I liked it…"
    c smile "But now I can’t even look at a honey bun without gagging."
    c "I feel like I’d love to be called something like Sand Pie, or Cutums, or something cool like C-sharp!"

    #Save this as $casspetname variable except honeybun
    "You feel like what suits you the most is…"

    #CHANGE: you need to review this later bc while i'm 99% sure text works with variables i'm not 100% sure... so... look at that.

label cass_petchoice:
    hide c with dissolve
    window hide

    menu:
        "Sand Pie":

            $ casspetname = "Sand Pie"

        "Cutesandra":
            $ casspetname = "Cutesandra"

        "C-Sharp":
            $ casspetname = "C-Sharp"

        "Honey Bun":
            window show
            show c doubt with dissolve
            c "Haha, very funny. What’s your real choice?"
            jump cass_petchoice

    window show
    show c smile with dissolve

    c smile "[casspetname], huh."
    c wink "I love it!"
    c smile " I’d love for my next partner to call me that some day."
    c confident "Wait, now I HAVE to figure out one for you!"
    c smile "You’ll find a cool person someday, and they have to call you a cool name too!"
    c "Something like Red, you know, cause of the blood?"
    c neutral "Or Echo, cause of echolocation, cause… you can turn into a bat?"
    c wink "Or Cutasaur! You know… cause you’re cute?"
    c smile "What do you think?"
    mc "Hmm, I really like…"

    #Save this as $petname variable
    hide c with dissolve
    window hide

    menu:
        "Red":
            $ petname = "Red"

        "Echo":
            $ petname = "Echo"

        "Cutasaur":
            $ petname = "Cutasaur"

        "\"Actually, I feel like I just like being called by my first name.\"":
            $ petname = player

    window show
    show c smile with dissolve

    c smile "[petname] suits you best of all, for sure."
    c "I’m sure your next partner would love calling you that, it really suits you."
    c doubt "I know your last relationship didn’t go so well…"
    c smile "But you’ll get someone you deserve soon! I feel it in my bones!"
    "You casually hold each other's hands."
    "It’s something you’ve always done, as friends…"
    "But there’s something about the conversation you just had, and the events since you turned…"
    "And you both start blushing."
    c neutral "Let’s get back to studying!"

    hide c with dissolve
    "Cass buries herself in her book, but doesn’t let go of your hand."
    "It feels nice and comforting."
    "You go back to reading the huge pile of books."
    "Hours go by and you don’t find anything really useful until Cassandra pushes an open book towards you."
    "You read the chapter heading…"

    "\"The Church at Stephan Lane\""
    "\"In the early 1800’s, the old church had a bat infestation…\""
    "\"Shutting it down permanently…\""
    "\"But it was restored partially in the 80’s\""
    "\" By Logan \"Gan\" Velsing, hunting gear mogul.\""
    mc "VELSING!"

    "Cassandra beams at you."
    mc "This has to be their hideout!"
    mc "We should go check it out tonight!"
    show c smile with dissolve
    c "Yeah, we definitely.. *yawn*... definitely should…"
    "Cassandra looks absolutely exhausted…"
    "You kind of forgot that vampires needed a lot less rest than humans did."

    mc "Hey, I can scout it out tonight on my own. You get some rest."
    c doubt "You sure, [player]?"
    mc "Yeah, don’t worry. I’ll just turn into a bat and watch from afar."
    mc "It’ll be fine!"
    c "Ok… If you.. *yawn*... insist."
    hide c with dissolve
    "Cassandra rests her head on the table and takes a nap."
    "The library is 24/7, so she should be fine."
    "Plus, If all goes well, you’ll be back before you know it!"
    "You leave the library, curious about what the Batbashers are up to."

##---CHAPTER 6---

label cass_chapter6:
    scene forest with fade
    # Tense Music
    "You fly as a bat through the thick forest trees."
    "Thanks to training with Cassandra, you’ve gotten pretty good at flying."
    "It’s a lot easier than you may have imagined."
    "It’s as if the wind wants you to float, to zoom."
    "And you just need to let it carry you forward."
    "You see the abandoned church before you."
    "You must have passed by it a couple of times on walks before."
    "An old, rusty, haggard building, abandoned decades ago."
    "It was only notable now as a spot for teens to smoke weed…"
    "And, apparently, for vampire hunters to plot their hunts."

    scene church with fade
    "You perch at the very height of the church, getting a good vantage point on the meeting."
    show a neutral at left
    show h smile at right
    with dissolve

    "Sure enough, you see Anne and Han at the front, and a crowd of masked vampire hunters watching them."
    a "Glad to see you all here. Plenty of unfamiliar faces, I assume, beneath the mask."
    "The crowd chuckles. Damn, they must be easy to please."
    a "For those of you who were at the culling of the vampire hideout, a toast!"
    "Thunderous applause"
    h "Our organization has a proud history, and a success rate beyond any other."
    h "Looking today, you may not know that this town used to be a huge center for vampire activity!"
    h "There were shops, schools, communities…more than anywhere else in the south "
    "This stuns you. Cassandra theorized that there was an old vampire community here, but a hub?"

    h sigh " And then came my ancestor. He killed the monstrous Bran Velcant, founded the ______, and brought the vampire community to its knees."
    #CHANGE: i'm going to assume this isn't meant to be blank

    h neutral "And now, here we are. Us an organization sprawling across Georgia, Alabama, Mississippi, Tennessee, The Virginias…"
    a "Even Kentucky starting next spring!"
    h sigh "And the vampires are all but stamped out. But now is not the time for complacency!"

    "Crowd Member" "Yeah, you’d know about complacency."
    "The crowd starts giggling."
    "This must be about the relationship Anne mentioned earlier? The nosy in you needs more information."
    h neutral "Yeah I was complacent. I let myself be manipulated. But so have we all."
    h sigh "We’ve grown complacent. We’ve let vampires not a day old slip through our fingers."
    "The crown murmurs. It seems the news of you escaping Anne has gone out."
    h neutral "We cannot rest until every last one of them is stamped out."
    h smile "The escapees have a camp in the deep woods. Tomorrow, we strike, and kill them all."
    "Relief and fear twirl into you. Laila and the others might be safe… But…"
    "You thought a few dozen people raiding you last time was bad…"
    "There’s over a hundred vampire hunters in this room right now."
    "If they weren’t wiped out now, after another attack they very well might be."

    a neutral "Anyway, enough speeches. One of our proudest sponsors, Fish-Fil-A, has graciously given us free sandwiches for this meeting!"
    a "Chow down!"
    "The meeting adjourns as ravenous vampire hunters descend upon the catering."

    hide a with dissolve
    show h at center with ease

    "Anne joins them, but Han wanders off , bringing one of the hunters with him."
    "You fly closer to Han, still out of sight."
    h sigh "We need to talk."
    # reveal thing
    "???" "Look, I'm only here because of the initiation spell. I don’t support what you're doing."
    "That voice seems familiar…"
    h "Doubt is something every initiate goes through. I know this more than anyone."
    "???" "Why single me out then? There are dozens of other initiates here."
    h smile "Because you live here. Because you know a vampire. Because you remind me of me."
    h "C'mon, take off your mask. We’re all family here."

    show h at left with ease
    show c doubt at right with dissolve
    "The figure takes off her mask to reveal Cassandra."
    # Sad Music
    "Cassandra?!?"
    "What is she… Why is she…"

    #obj pronoun
    #CHANGE: there's a whole lot of pronoun fuckery going on here in the comments ask abt it later

    c "We aren’t family. The person I love, [player], has been there for me since forever. I’m not going to betray [pronoun] for you!"
    h smile "Let me tell you a story."
    h sigh "I was in love once. Adrian Lansberry. He was handsome, devoted, kind."
    h smile "We did everything together. I hid it from my dad, but my sis knew."
    h sigh "It was just lovely… until he got bit."
    h unsure "At first, i loved him so much, I betrayed the whole organization for him. Covered for him."
    h "My father disowned me. I was meant to take over as head but Anne seized the opportunity. I was alone and scared and we only had each other."
    h "But i noticed he was different. He wasn’t the man I fell in love with anymore."
    h "He grew violent. His bloodlust grew and grew. He… tried to bite me."
    h neutral "That’s what vampirism is, Kalluri. A disease."

    #contraction
    h "Your friend isn’t the same one you fell in love with. That vampire is different, a monster, a killer now."

    # subject pronoun
    c "That’s not true, [player]... "
    #Code in depending on affinity level either $ cass_affection >5 jump highcassaffection
    # or if  $ cass_affection <=5 jump lowcassaffection

    if cass_affection > 5:
        # pronoun obj
        c "They’ve been acting the exact same as long as i’ve known [pronoun]!"
        h "That’s how it starts. Pretty soon the bloodsucker will be.."
        c "Pretty soon what? Don’t think I don’t see you trying to worm your way back to the top!"
        C"You killed your boyfriend to get your old job back!"
        h surprise " Kalluri, Kalluri, I get you’re upset but no need to get emotional!"
        h unsure "You’re going through a lot right now, I get it. I’ve helped dozens of people like you. Like me."
        h "take your time. You’ll realize sooner or later."

    if cass_affection <= 5:

        c "Well, they have been acting a bit different… but.. "
        h surprise "How different?"
        #pronoun obj
        c "A little more aggressive, but that’s not [pronoun] fault! There has to be a better way!"
        h unsure "I’ve been where you are! I’ve said what you’ve said, I’ve done what you’ve done."
        h "You’re going through a lot right now, I get it. I’ve helped dozens of people like you. Like me."
        h "Take your time. You’ll realize sooner or later."
        #then
        h "Look, my sister, Anne, lusts for the kill. She doesn’t know vampires like we do. How dangerous they are, how human they are."
        h neutral "I have plans. Restructure the organization. More strategic hunts. Protect people like your friend before they get bit. A cure."
        h "That means I need allies. I see potential in you. Something to consider."
        "You sense worry and conflict in Cassandra's face."
        c "I need some air…"
        h smile "Whatever you need, friend."
        "Cassandra runs out, leaving the church."
        "You don’t know how to feel."
        "The situation is difficult to process."
        "You zoom out of a window to follow her and confront her."

#---CHAPTER 7---

label cass_chapter7:

    # Sad Music
    scene forest
    show c doubt
    with fade
    "Once you are both far enough away, you poof back to confront her."
    c smile "[player]! I’m so happy to see you!"

    hide c with dissolve
    window hide

    menu:

        "\"What the hell! How could you join the vampire hunters!\"":
            pass

        "\" I heard everything… I promise I’m not dangerous Cassandra.\"":
            pass

        "\"You betrayed me!\"":
            pass

    window show
    show c doubt with dissolve

    c "Please, let me explain, I…"
    "Cassandra freezes. It’s as if she’s trying to say something, but she can’t."
    "You remember what Cassandra was saying earlier about the initiation ritual."
    "Maybe that was stopping her from being able to talk?"
    "To tell you the truth?"
    "You think back to the library. She never actually told you where the hideout was, you found it out yourself…"
    "She guided you to the answer without saying anything…"

    hide c with dissolve
    window hide

    menu:
        "\"Are you under a spell?\"":
            pass

        "\"What can you tell me?\"":
            pass

    window show
    show c doubt with dissolve

    c "I am prohibited from discussing the organization… I would get hurt if I did."
    c "I want to help you as best as I could, but I can't tell you anything."
    "Cassandra seems to be struggling, but her precise words seem to be mostly avoiding the curse."
    c "If I disobey, If i reveal a secret, if I do anything… "
    "She doesn’t finish, but you get the implication. She would die."
    c "I didn’t think it was real. I’ve joined larps and role plays and conventions all the time…"
    c neutral "So I took the oath no problem."
    c doubt"That night in the woods… I realized it was real."
    "When she met Han… When Han dragged her unconscious…"
    c "I wanted to tell you… they told me that you were some kind of monster, that you weren’t yourself…"

    #CHANGE: cass' expression doesn't change much. look into this

    #ANother affinity check, if enough affinity jump 5cfriend, else jump 5cfoe
    #Code in depending on affinity level either $ cass_affection >5 jump highcassaffection
    # or if  $ cass_affection <=5 jump lowcassaffection

    if cass_affection > 5:
        pass

    if cass_affection <= 5:
        jump cass_bad

    c smile"But I know you! You’re still the sweet beautiful person I've known forever!"
    c "Vampire’s aren’t a danger!"
    c "You aren’t a danger!"
    c doubt "You’re…"
    "She hesitates again, but this time it doesn’t seem like the curse."
    c "You're my rock, [player]. When was bullied, when I came out, when I transitioned, you were always there for me."
    c neutral"And i tried so hard to repay that, repay everything you’ve done for me but in the end i keep hurting you."
    c doubt"I don’t deserve your friendship… so why do I…"
    "She pauses again."
    c "I love you, [player]."
    c neutral "I wanted to tell you before this whole thing, but now it's too late."
    c "Now we’re on opposite sides of this war."
    c doubt "And I can’t fight them without dying… But I can’t fight you without wishing I was dead."
    "You stare into Cassandra’s eyes, the gravity of the situation sinking in."
    "That’s why she was acting distant recently."

    # Romantic Music
    "She loves you?"
    "This whole time, she’s been holding back because of this big secret."
    "She loves you?"
    "She feels so close to you now, in the cold night wind."
    "Quick, say something smooth!"
    hide c with dissolve
    window hide

    menu:
        "Well… That just happened…":
            pass
        "Erm… What the Scallop?":
            pass
        "Stare at the floor awkwardly":
            pass

    window show
    show c neutral with dissolve
    c "*giggles*"
    $ cass_affection+=1
    "Cassandra’s smile is infectious as always. Despite everything, you both giggle together."
    "Cassandra holds her hand in yours."
    "You look into each others eyes."

    menu:
        "Kiss":
            pass

    "You close your eyes as Cassandra presses her lips against yours."
    $ cass_affection+=10
    "It’s like a decade of emotions have flowed through you both, left with a peaceful bliss."
    "As you hold her close, and she holds you close.."
    "All the fear and anguish melts away."
    "You stay like this for a while, kissing and kissing and.."

    #hear voice without seeing person?
    # Tense Music
    h "Oh Kalluri… I’m disappointed."
    show c at left with ease
    show h neutral at right with dissolve

    h "After all my precautions, you led the bloodsucker right to us."
    "A net falls over you, barely missing Cassandra."
    h sigh "I guess I need to tighten the spell a little more for the next batch."
    h "Well, at least this should work."
    h "Kalluri, kill the bloodsucker."
    "Cassandra stays back from you, aghast."
    c doubt "I’m not going to do that, you freak!"
    h surprise "Freak?"
    c "No matter what you say I’ll never hu-"
    "Pain courses through Cassandra as she resists."
    h sigh "Look Kalluri, this is going to be good for you."
    h "In a year or so, when you’ll be head of a raid up north, you’ll thank me."
    "Cassandra looks like she wants to rebut, but the pain is preventing her."
    mc "Stop it!"
    "Han moves next to her and puts a stake in her hand."
    h "Come on, Kalluri. It’ll be quick."

    hide c with dissolve
    show h at center with ease

    "Cassandra resists and collapses to the ground."
    "It seems like the pain is intensifying."
    "You struggle against the net, trying to escape."
    "Cassandra passes out, still writhing."
    "Eventually the writhing stops and she lies still."
    h neutral "A pity. So much potential."
    "Rage boils in you. You burst through the net to attack Han."
    "A stake grazes your side and you fall down again."

    show h at left with ease
    show a neutral at right with dissolve
    a "Heh.. I got you! Finally! Wait till the Batbashers hear about this!"
    h "Step aside Anne, this is my business."
    a "That bloodsucker was going to kill you, idiot!"
    "As they bicker, you stumble to grab Cassandra and crawl away."
    "Anne points a shotgun at you."
    a "Hannn, he’s getting away."

    "Han walks behind Anne."
    #pronoun obj
    h neutral "Then shoot [pronoun]."
    "Anne pulls the trigger. Pain shoots through your arm as you look behind you to see Han shoot Anne with a net gun."
    #Hide A with dissolve.

    a annoyed "What the hell, Han?"
    h " Vampire, you’re weak, you need blood… kill her."
    a "What?"
    h "Kill her, and you’ll heal enough to escape."
    h "You wrestled the net gun from her, killed her, and I found her dead."
    h "Catch my drift?"
    "You hate to admit it, but he’s right about you needing blood."
    "You wouldn’t make it a few feet without healing, much less to a hospital."
    "But you don’t like being a pawn in Han’s game."
    "He’d blame you for Anne’s death, he’d use you as a tool to gain power."
    "Maybe you're through being a tool.."
    "But you don’t want Anne to die…"

    hide h
    hide a
    with dissolve
    window hide

    menu:
        "Kill Anne":
            window show
            "You barrel towards Anne. Her death is swift. It's the first time you’ve really drank someone's blood."
            "You feel like the numbness you’ve felt for a while has gone away."
            "You’re alert, like you’ve drunk four matcha’s all at once."
            "You grab Cassandra and run into the night."
            $ anne_dead = True
        "Fight Han":
            window show
            # Tense Music
            "You reject Han’s order and attack him."
            "You feel a stake dig into your back."
            "You bite into him as the pain sinks in."
            "It's the first time you’ve really drank someone's blood."
            "You try to drink more but he pulls you off of him."
            "He lets go and you scurry away with Cassandra, deeply wounded."
            "You hear Anne escape her net."
            show a angry with dissolve
            a "Really dude? After all I did for you?"
            show a at left with ease
            show h sigh at right with dissolve
            h "You took away my birthright! I’m the eldest boy!"
            a neutral "Aww, look at you grumble! You're turning into a bloodsucker just like your little boyfriend!"
            a "And you know what I do to bloodsuckers.."
            show h unsure
            h " I HATE YOU!"

            hide h
            hide a
            with dissolve
            "As you escape, you hear the two tussle."
            "You run as far away as you can, hoping to sense the other vampires and find safety."
            $ han_kill = True

    jump cass_chapter8

label cass_bad:
    # Tense Music
    c doubt "And I wanted to say you were the same person as always, but.."
    c "You’ve been acting so different lately."

    #Have a section listing all the evil things m/c did
    #CHANGE: this is more up to radha than me but don't forget it

    c "There's so many violent mean things you’ve done that the old you wouldn’t have done…"
    c "I didn’t want to believe it, but you’ve changed."
    c " I was selfish. I thought I was living my fun vampire dream, and I didn’t consider that I would lose my best friend."
    "You have been acting more aggressive lately."
    "Was Cassandra right? Were you not the same person you were before the bite?"
    "You have the same memories, but.."
    c "I’m sure there’s a way to bring you back, I just know it."
    c "A lot of the people in the Batbashers are just bloodthirsty violent people, but…"
    c "Some of them were researching a cure. Han was saying…"
    mc "A cure?"
    "Regardless of how you feel about your vampirism, you don’t really trust a cure made by Han.."

    "You may have been a jerk to Cassandra recently…"
    # if you picked bite "And you did almost kill her that one time…"

    #CHANGE: i didn't see a part in the script where you were given an option to bite cass, but there is a part where you bite a stranger. is this about that?

    "But Cassandra was the one who showed you that there’s beauty in vampirism…"
    "Maybe you can convince her that you aren’t dangerous…"
    show c at left with ease
    show h neutral at right with dissolve
    h "Ahh, what have we here…"

    #pronoun obj
    c "Han… please don’t hurt [pronoun]..."
    h "This is the one you wanted to cure, huh…"
    "Han shoots you with a net."
    c "You said you needed me right? Leave [player] alone, and I’ll help you take over."
    h "Glad to see you change your mind Kalluri."
    h "I promise, I’ll keep [player] safe."
    "You feel the sharp prick of a tranquilizer and pass out."

    scene dungeon
    show h smile
    with fade

    h "Hey buddy."
    h "Your girlfriend is safe right now, don’t worry."
    mc "What do you want with me?"
    h "I told Cassandra I would humanely give you a cure."
    h sigh "I lied."
    h neutral "I tend to do that."
    h smile "But I get away with it cause I'm such a charming little fella."
    h surprise "I’m such a little goof sometimes!"
    h neutral "Anyway… Yeah, i’m gonna kill you."
    h "Sorry! It’s just that I’m a vampire hunter, and you’re, you know."
    "You feel your strength returning. It’s now or never…"

    hide h with dissolve
    window hide

    menu:
        "Break free and Attack Han":

            window show
            "You  burst free from your net and maul Han."
            show h surprise with dissolve

            h "Woah, quit it!"
            "You hear a creak from the door just as you're about to finish Han off."
            hide h with dissolve
            "You bite your teeth into him, sucking his blood."

            show c doubt with dissolve
            c "Han, I can’t let you do this… What…"
            c "[player], no…"

            $ cass_affection-=10
            "It's the first time you’ve really drank someone's blood."
            "You feel like the numbness you’ve felt for a while has gone away."
            "You’re alert, like you’ve drunk four latte’s all at once."
            c "This isn’t you, please, I know [player] would never murder someone…"
            "You run away, out of the cellar, away from Cassandra."

            scene church with fade
            "Your bloodlust  fuels you as you maul as many members as you can."
            show a annoyed with dissolve

            #CHANGE: is anne supposed to be saying this or nah???

            "Hey, isn’t that–"
            "You pounce on Anne and suck her blood too."
            "Your emotions flow through you, your anguish."
            hide a with dissolve
            "Until you feel a bullet go through your arm."
            show c doubt with dissolve
            c "[player], please. Don’t make me do this."
            "You look in Cassandra’s eyes and see fear."
            "Your best friend, your… maybe more, in another life.."
            "Looks at you with fear as you look back, covered in the blood of others."
            "You run, in fear, in shame."
            scene forest with fade
            "Away from everything. "
            "Away from her."
            $ evil_cass = True

        "Stay in the net and yell.":

            window show
            show h neutral with dissolve
            h "You remind me a lot of my old partner, Adrian Lansberry."
            h smile "He was a great, wonderful person…"
            h neutral "But in the end, vampirism twisted him into a monster."
            h "I’m saving Kalluri a lot of trouble, a lot of heartbreak."
            h "Loving a creature like you, it never ends well."
            h " This is going to hurt, but you need to remember…"
            h " You’re already dead."
            h "I’m just sending you where you were meant to go."
            "You hear a creak at the door."

            show h at left with ease
            show c doubt at right with dissolve
            c "Han, I can’t let you do this.. What?"
            h surprise "Oh, Hey Kalluri! Ummm…. Yeah I can’t think of an excuse. Sorry?"
            c "You said you were going to cure [player]! That was the promise you made!"
            #obj
            c "I won’t let you hurt [pronoun]!"
            "Cassandra wrestles with Han, but pain shoots through her."
            "It must be the initiation spell…"

            hide h
            hide c
            with dissolve

            "Cass struggles through it and punches Han to the ground before passing out."
            "You bust through the net and grab Cassandra’s passed out body, rushing out."
            "You climb through the cellar and…"

            scene church with fade
            "You rush through the convention, still wounded from the net."
            "The stakes and bullets of the Batbashers pierce your skin.."
            scene forest with fade
            "You escape, wounded, tired, on the brink of death, but safe…"
            "At least for now."
            "You totter towards where the Batbashers said the other vampires would be…"
            "But you collapse halfway there, tired out of your mind."
            "You pass out…"

            scene forest day
            #CHANGE: we don't have an image for this. lol

            "And wake up, the sun in your eyes."
            "You feel the sharp pain of the sun as you witness one last sunrise."
            "Cass wakes up just as you start to fade out."
            show c doubt with dissolve
            c "[player], please… no. Please, please."
            c "I need you, please don’t go."
            "You die in Cassandra’s arms."

            return

            #CHANGE: so is this a bad ending? like specifically when you spare han?


##---CHAPTER 8---

label cass_chapter8:

    if evil_cass:
        jump evilCass

    #if $dyingMc jump wakeup8
    scene forest with fade
    # Tense Music

    if $ dying_mc:
        pass

    else:
        "You drag Cassandra’s unconscious body into the vampire hideout."
        mc "I need a doctor! Please!"
        "It’s all a blur. Someone takes Cassandra away and you collapse from exhaustion."
        "You fall asleep, the long run sinking in…"
        scene forest with fade

    show l smile with dissolve
    "You wake up to see Laila, at long last."
    # Neutral Music
    hide l with dissolve
    window hide

    menu:
        "\"Laila? Oh my god you’re alive!\"":
            pass

        "\"Where’s Cassandra? Is she safe? Is she alright?\"":
            pass

        "\"What’s happening? Where am I?\"":
            pass

    window show
    show l neutral with dissolve
    l neutral "Calm down, you’re in a safe place. Well, as safe as any place can get for a vampire."
    "You look around and find that you’re still in the forest, albeit surrounded by a cluster of tents."
    l away "After the destruction at the Blood Bank, we were scattered for a bit. I had to hide in this root cellar, it was a whole thing."
    l neutral "I was able to find a few others and we’ve decided to set up here. The town’s almost certainly not safe."
    l neutral "In fact, we were planning on moving on to some other town when we found you. I thought you were dead!"

    mc "I almost was…"
    "You tell Laila about everything that happened, and that the Batbashers are on their way to attack the hideout."
    l angry "Damn, okay. I need to speak with the others and figure out what we’re going to do. Are you going to be okay on your own?"
    mc "Well, I’ve managed this far…"
    mc "Also, where’s Cassandra? Is she ok?"
    l neutral "She’s at the clinic. But, she’s not been responsive since you arrived."
    "As Laila goes to figure out the plan, you beeline to the clinic to see if Cassandra is ok."


    scene clinic with fade
    show c doubt with dissolve
    # Tense Music
    "You see her, awake but tired."

    hide c with dissolve
    window hide

    menu:
        "\"Cassandra!!!\"":
            pass
        "\"Are you ok?\"":
            pass

    window show
    show c doubt with dissolve
    c "I’m ok, thanks to Dr. Fang. She’s been researching the spell and… there may be a way to undo the damage."
    c "The spell wounded me deeply. Doc says my internal organs are bleeding."
    c "I’m dying. And the spell is going to keep hurting me until… until…"
    c "Han told me that  being bit would trigger the curse and kill me, but the doctor says that vampire healing may be the only way I live."
    c "Maybe Han lied. Maybe he didn’t, I don't know. But it’s my only shot."
    "You didn’t truly expect the vampires to have a 100% solution."
    "Turning Cassandra into a vampire could kill her…"
    "But what other option was there?"
    "Maybe you could beat the solution out of Han.."
    "But that’s a risk too."

    c neutral "I’m so sorry about all of this, [player]."
    c "I want you to know, no matter what you choose, no matter what happens to me."
    c "I still feel the same way I did when we kissed…"
    c "I love you, [player]."
    "You kiss again, this time a somberness pervading the whole thing. "
    $ cass_affection+=1
    c "You’re the only one I trust to turn me, [player]."
    c "But I understand if you don’t want to."
    "You have to make a decision…"

    hide c with dissolve
    window hide

    menu:
        "Bite Cassandra":
            "You kiss her again."
            $ cass_affection+=1
            "But this time you slowly extend your fangs into her lips."
            "You let the blood flow through you."
            "After a while, you feel her go limp."
            "You let go and she collapses onto the bed."
            mc "What’s happening! Is she ok?"
            "The doctor assures you that everyone passes out after getting bitten."
            "It happened to you too, so it makes sense."
            "Still, you can’t help but worry if you made the wrong decision."
            $ cass_vamp = True

        "Try to find a cure":
            "You kiss her one more time"
            $ cass_affection+=1
            mc "I’m sorry Cassandra, I don’t want to risk you dying by my hand."
            mc "I’ll find Han and get him to stop the spell somehow."
            mc "Cassandra… Cassandra?"
            "She’s passed out again."
            "You stay at her side for a bit before running out."
            "You hope you made the right choice."
            $ cass_human = True


    scene forest with fade
    show l away with dissolve
    "You leave the clinic, emotional, and run into Laila."
    l neutral "[player], are you ok?"

    hide l with dissolve
    window hide

    menu:
        "\"I’m fine!\" (lie)":
            window show
            show l away with dissolve
            l "[player], it’s okay to be upset. It’s not easy being like this, and that comes with difficulties that you normally would never have to face."

        "\"No, I’m not doing well right now.\"":
            window show
            show l neutral with dissolve
            l neutral "I’m sorry. I hope Cynthia will be ok."
            mc "It’s Cassandra."
            l neutral "Oh, uh, yeah. Sorry. Long night."

    #CHANGE: the original script to this had the second choice jump to 8c2, but the label for 8c2 doesn't exist. I'm giong to assume that 8c2 was the label that started with laila saying 'i'm sorry,' but i need to make this note just to check in

    # Exciting Music
    l angry "We are in general agreement that we should leave this place, sooner rather than later."
    l neutral "This camp was always meant to be temporary, and we’re just going to leave ahead of schedule."
    l excited "However, we have a plan to make our exit… memorable."
    l neutral "This camp is in a valley."
    l neutral "If we set some traps here before we leave, we can take a bunch of these hunters out, maybe scare them away, make it harder for them to follow us."
    l neutral "After what happened at the Blood Bank, I had an idea."
    L smile "If we set a bunch of kegs on fire, we could give the Velsings a taste of their own medicine for once."
    l away "We just need someone to stay put and trigger the trap."
    # if( $cassvamp) jump Cassfight
    # if( !$cassvamp) jump MCfight
    #CHANGE: this was the original variable jump, but i'm going to assume the mc is fighting if cass isn't a vampire. check in later.

    if cass_vamp:
        show c confident with dissolve
        c "I’ve got this."
        "You see Cassandra, fit as a fiddle, awake and filled with vampiric energy."
        mc "Cassandra!"
        show c at left with ease
        show l neutral at right with dissolve
        "You rush to give her a hug before kissing her. Her lips feel different now, colder, but still lovely as ever."
        l neutral "Don’t let me interrupt you love birds."
        "You pull apart, acutely aware of your surroundings."
        c smile "Look, after everything the Vellsings did, everything I was complicit in, I can’t let them get away with it. I need to fight them."
        "You feel the same way. After all the Vellsings put you through, you can’t just turn and run."
        l smile "I would stay, but I’ve lived through this kind of thing too many times already. I can’t bear to witness it again. I wish you luck, [player]. Your nobility is touching."
        "You say goodbye to Laila and prepare for the fight. With Cassandra at your side, you feel ready for anything."
        hide l with dissolve
        # Label fightalongCass
        "As the town evacuates, you and Cassandra stand next to the empty clinic."
        # Romantic Music
        c smile "You know, It's really sinking in how, this might be our last day.."
        "Cassandra moves closer to you."
        c smile "And I’m so glad I get to spend it with you."
        "Cassandra gives you a little kiss on the neck."
        c "You know, the clinic is empty…"
        c "Nobody would bother us if we wanted to.. You know…"

        hide c with dissolve
        window hide

        menu:
            "\"I know…\"":
                label sex_time:
                    window show
                    "Cassandra giggles."
                    c smile "Well, what are we waiting for, [petname]?"
                    "You follow Cassandra into the clinic and lock the door behind you."
                    $ cass_affection+=1

                    scene clinic with fade
                    show c smile with dissolve
                    c "How about here in this empty bed? No one's used it, and noone is going to use it any more…"
                    "You nod and turn off the lights."
                    scene black with fade
                    c "Come here, you!"
                    $ cass_affection+=11
                    scene woods with fade
                    show c smile with dissolve
                    "After a few hours of fun, you stumble out of the clinic with Cassandra."
                    c "That was fun… I feel so energized! Let's train before those dickheads show up!"
                    # Jump to finalbattleCass

            "\"Wait what?\"":
                window show
                "Cassandra giggles."
                show c smile with dissolve
                c "You know… spend some… quality time together… of a risque variety.."
                window hide

                menu:
                    "\"Oh, I see! Yeah, I’m down\"":
                        $ cass_affection+=1
                        jump sex_time

                    "\"I’d rather not right now.\"":
                        label no_sex:
                            window show
                            show c smile with dissolve
                            c smile "That’s ok! How about we train for tonight instead!"
                            $ cass_affection+=1


                    "\"I’m still confused.\"":
                        window show
                        show c neutral with dissolve
                        c "You know, have sex… bang… fuck…etcetera…"
                        hide c with dissolve
                        window hide

                        menu:
                            "Oh, I see! Yeah,  I’m down":
                                $ cass_affection+=1
                                jump sex_time

                            "I’d rather not right now.":
                                jump no_sex

                            "I’m still confused.":
                                window show
                                show c doubt with dissolve
                                c doubt "Ummm, oh boy,  You know, like… when two birds love each other very much…"
                                window hide

                                menu:
                                    "Oh, I see! Yeah, I’m down":
                                        $ cass_affection+=1
                                        jump sex_time

                                    "I’d rather not right now.":
                                        jump no_sex

                                    "I’m a proud virgin, I don’t want to sully myself with such things until marriage.":

                                        window show
                                        show c doubt with dissolve
                                        c doubt "Oh. Umm… I didn’t know that about you… Let’s discuss this later ok?"
                                        c smile "For now, lets train for tonight!"

                                    "I’m still confused.":
                                        window show
                                        show c doubt with dissolve
                                        c doubt "Nevermind, I’m not feeling it anymore. Lets just train for battle, ok?"
                                        $ cass_affection-=1


        # Label final battleCass
        # Exciting Music

        scene forest with fade
        "After a while, the battle begins."
        "You stand in the center of the hideout."
        "You watch as dozens of Batbashers rush towards you."
        "You gesture to  Cassandra at the right moment."
        "She uses a lighter to set a string near a blood moonshine keg on fire"
        "She speeds towards you, pushing you to the ground as…"
        scene fire with fade
        "BOOOM"
        "The kegs explode, lighting most of the batbashers on fire."
        "As the survivors rush to fight you, you and Cass go on a rampage."
        "Cassandra has gotten used to being a vampire a lot faster than you did."
        "She floats and zooms, knocking out a bunch of the Batbashers."
        "You zoom past towards Han, bloody bruised and angry."
        scene forest with fade
        show h neutral with dissolve

        if anne_dead:
            h "Ah, [player]. Thanks for the help with the coup. Couldn’t have done it without you."
        else:
            h "I took care of my own sister for this, I’m not going to let a punk like you stop my dominion."

        #Can we have this many options?
        #CHANGE: we can, but it's going to clog up the screen

        hide h with dissolve
        window hide

        menu:
            "Looks like it's going to be a short reign.":
                pass
            "I am going to kill you.":
                pass
            "I am going to unalive you.":
                pass
            "I genuinely hate you on a deep level.":
                pass
            "You’re kinda hot, but I have to kill you.":
                pass
            "Sorry for this, babygirl.":
                pass
            "Yeah, I’m thinking you're gonna die.":
                pass

        window show
        "You and Cassandra beat the crap out of Han."
        show h surprise with dissolve
        "He gets off a few shots of his gun, but the two of you easily take him down."

        show h at left with ease
        show c confident at right with dissolve
        c confident "So, what should we do with him?"

        hide c
        hide h
        with dissolve
        window hide
        menu:
            "Give him a quick death.":
                window show
                "Cassandra snaps Han’s neck."
                "He collapses to the ground, instantly dead."
                "You toss his corpse into the raging fire that has started around the moonshine kegs."
                "You and Cassandra leave, heading back home."
                # Jump cassgoodending

            "Make him a vampire.":
                window show
                "You bite down on Han’s neck, sucking his blood."
                "You let go, and he collapses."
                "You tie his leg to a root and leave him there."
                "Han wakes up."
                show h surprise with dissolve
                h "Please, don’t leave me here! Kill me! I’d rather die than be one of you, please!"
                "You and Cassandra leave, heading back home."
                # Jump cassgoodending

            "Let Cass decide.":
                window show
                show c neutral with dissolve
                c "I think we should flip the spell on him."
                "Cassandra grabs the book of names from Han’s pocket and starts chanting."
                c "You will protect all vampires from harm till your dying breath."
                c "If you disobey, the spell will torture and kill you."
                show c at left with ease
                show h surprise at right with dissolve
                h "Nooo! Not the consequences of my own actions!"
                "Han tries to attack you, but gets hurt in every attempt."
                "You and Cassandra giggle and walk away calmly."
                show h sigh
                h "Damn you, Kalluri! And you too, Bloodsucker!"
                # Jump cassgoodending




    else:
        # Label mcfight
        "You realize what you have to do."
        "\I need to fight Han and figure out how to cure Cass."
        "\I need to be the one to stay here and trigger the explosion."
        "Laila nods grimly."
        l smile "I would stay, but I’ve lived through this kind of thing too many times already. I can’t bear to witness it again. I wish you luck, [player]. Your nobility is touching."
        "You say goodbye to Laila and prepare for the fight. Without Cassandra at your side, you feel uneasy."
        hide l with dissolve
        "You hope you can handle Han alone…"
        jump fightalone



    #CHANGE: i'm going to assume that this is label cassgoodending, but i'm not sure.
    scene diner with fade
    # Romantic Music
    "ONE MONTh LATER"
    "You rush into the town Waffle Home."
    "You hope you aren’t too late for your date with…"
    show c wink with dissolve
    c "[player]!!!"
    "Cassandra pulls you into an embrace"
    c "Oh my god it's been so long!"
    mc "[Casspetname], it's been two days."
    "Cassandra giggles."
    c "I’m so happy to see you though!"
    c smile "We’ve been so busy helping rebuild the local vampire community, we’ve haven’t had time for a date like this!"

    mc "I guess this is technically our first real date as a couple, huh"
    c smile "What are you gonna have, [petname]? I’m thinking strawberry pancakes and some whisky."

    hide c with dissolve
    window hide

    menu:
        "Chicken and waffles":
            pass

        "Pancakes and syrup":
            pass

        "Eggs, hot sauce and hashbrowns":
            pass

    window show
    mc "And I’ll drink:"
    window hide

    menu:
        "Whisky":
            pass
        "Moonshine":
            pass
        "A fruity cocktail":
            pass

    window show
    show c wink with dissolve
    c wink "Nice choice, [petname]!"
    "You smile. With the Vellsings and the Batbashers dealt with, the town has become a new safe haven for the vampire community."
    "More and more new vampires have come into town to help rebuild the hideout."
    "The world finally feels safe."
    "You and Cassandra talk and eat for a while, giggling and laughing and smiling."
    c "I’m so happy with you, [player]."
    mc "Me too."
    "You both lean in for a kiss."
    $ cass_affection+=1
    # END OF PART 8 GOOD ENDING

label fightalone:
    #exciting music
    "After a while, the battle begins."
    "You stand in the center of the hideout."
    "You watch as dozens of Batbashers rush towards you."
    "As the get close, you use a lighter to set a string near a blood moonshine keg on fire."
    "You run away as fast as you can."
    scene fire with fade
    "BOOOM"
    "The kegs explode, lighting most of the Batbashers on fire."
    "As the survivors rush to fight you, you fly away."
    "Their bullets graze you, but you have one focus."

    # "Fighting Han"

    "You zoom past the fire, grab Han, and drag him deeper into the woods."
    scene forest with fade
    show h smile with dissolve
    h smile "Ahh, bloodsucker. There you are."
    h "Let me guess, you want to get me to let Kalluri free from the spell."
    h "That’s not going to happen."
    "Han stabs you, and you fall to the side."
    "You see a book strapped to his pants."
    "Maybe the book has something to save Cass."
    hide h with dissolve
    window hide

    menu:
        "Fight Han":
            window show
            # Tense Music
            "You tackle Han, wrestling him to the ground."
            "You’re pretty strong with your vampire powers…"
            "But Han is a trained fighter."
            "He pins you down and stabs you in the chest with a stake."
            "As you lie, bleeding out, you see Han get up and brush himself off."
            show h surprise with dissolve
            h surprise "Damn, that’s crazy."
            "Han scratches his head."
            h smile "Anyways… let's go slaughter these vamps!"
            "You lie in deep pain, dying."
            "Staring as Han descends to go off and murder other vampires."
            "As Cassandra dies away from you, unable to break the curse."
            "The light leaves your eyes as you lay defeated, conquered, slain."
            return
            # END OF GAME BAD ENDING

        "Grab the book":
            window show
            # Tense Music
            "You swipe the book and dash as far as you can from Han."
            "He chases after you, shooting bullets that graze you."
            "You need to get this book to Cassandra and the Doctor fast."
            "But if you go on the shorter path to where Cass and the vampires were, you may lead Han right to them."
            "If you take the long way, you may not make it in time."
            window hide

            menu:
                "Take the shortcut":
                    window show
                    pass
                "Take the long way":
                    window show
                    "You sprint as fast as you can and lose Han in the woods."
                    "You dash through hedges and around logs, desperate to get to Cassandra."
                    "But to your horror…"
                    "The sun starts to rise."
                    #CHANGE: still no graphic for this
                    scene forest day
                    "You start to feel sharp, agonizing pain throughout your body."
                    "You duck under the shade of a lone tree."
                    "Trapped."
                    "Waiting, knowing you have the very thing that can save Cassandra and can’t get it to her."
                    "As the sun rises, your future falls."
                    return
                    # END OF GAME BAD ENDING


    # Tense Music
    "You zoom through the shortcut until you can’t see Han behind you anymore."
    "You sense where the new vampire hideout is and dash towards it."
    "Just as you make it, you feel a stake puncture your foot."
    show h sigh with dissolve
    h sigh "looks like you led me right to them."
    "Han cocks his shotgun at you."
    h "Say your prayers, bloodsucker."
    "Suddenly, bats swarm all around Han."
    h suprise "GET OFF ME GET OFF ME GET OFF ME!"
    "As the bats bite and peck at Han, you feel yourself slipping from consciousness."
    "Quick, say something cool before you die!"
    hide h with dissolve
    window hide

    menu:
        "Looks like it's… Bats out, for you!":
            pass
        "I genuinely hate you on a deep level.":
            pass
        "You’re kinda hot, but I have to kill you. Sowwy.":
            pass
        "Sorry for this, babygirl.":
            pass
        "Yeah, I’m thinking you're gonna die.":
            pass

    window show
    "You pass out, watching Han die."
    scene diner with fade
    "THREE MONTHS LATER"
    # Romantic Music
    "You stumble into the town Waffle Home."
    "You hope you aren’t too late for your date with…"

    show c wink with dissolve
    c "[player]!!!"
    "Cassandra pulls you into an embrace."
    c smile "Oh my god it's been so long!"
    "You’ve both been in recovery for the last couple months, but you’ve both finally healed enough to go on a real date!"
    "You smile. With the Vellsings and the Batbashers dealt with, [townname] has become a new safe haven for the vampire community."

    #CHANGE: i'm 99% sure we don't have a townname variable

    c "What are you gonna have, $petname? I’m thinking strawberry pancakes and some whisky."
    mc "Hmm, I’ll have…"
    hide c with dissolve
    window hide

    menu:
        "Chicken and Waffles":
            pass
        "Pancakes and syrup":
            pass
        "Eggs, hot sauce and hashbrowns":
            pass

    window show
    mc "And I’ll drink:"
    window hide

    menu:
        "Whisky":
            pass
        "Moonshine":
            pass
        "A fruity cocktail":
            pass

    window show
    show c wink with dissolve

    c wink "Nice choice, [petname]!"
    "You and Cassandra talk and eat for a while, giggling and laughing and smiling."
    c smile "More and more new vampires have come into town to help rebuild the hideout!"
    "You nod, smiling."
    mc "The world feels safe for once."
    "As you finish your meal, you hold Cassandra’s hand."
    "She looks lovely in the fluorescent lights of the waffle home."
    c "I’m so happy with you, [player]."
    mc "Me too."
    "You both lean in for a kiss."
    $ cass_affection+=1
    return

label evilCass:

    # Sad Music
    scene forest with fade
    "You crawl into the vampire camp, wounded beyond belief."
    "Exhausted, you pass out."
    scene clinic with fade
    # Tense Music
    "You wake up in a clinic, but noone is there…"
    "How strange…"
    scene fire with fade
    "You walk outside the clinic and see fire."
    "Raging fire."
    "The moonshine kegs must have exploded again."
    "The town is abandoned, vampire corpses everywhere."
    "You look to the end of the camp and see in the smoke…"
    "A long line of Batbashers."
    "And at the front of it all… "

    show c doubt with dissolve
    "It’s Cassandra."
    "You stand in shock. She sees you, and motions for the Batbashers to kill you."
    " You turn into a bat and fly, the smoke masking your escape."
    "Tears in your eyes, you fly as far as you can."
    "Alone, afraid."
    "Lost."

    scene street with fade
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

    show h smile w dissolve
    #Neutral Music or Goofy music
    h "Howdy, bloodsucker."
    mc "HAN?"
    h surprise "Woah, not so loud!"
    h unsure "Sorry for all the uh… Murdering and stuff."
    h "No hard feelings?"
    mc "NO HARD FEELINGS?"
    h surprise "Calm down! You’ll get us both killed…"
    h unsure "look, you turned me into a vampire, and, well.."
    h "I kinda lied to Cassandra, and the others."
    h sigh "You are the same person when you turn."
    h unsure "Adrian was the same person."

    h "I just wanted to make killing him easier, you know?"
    h "Anyway, now Cassandra thinks you aren’t you."
    h "That you are the reason why her best friend/crush is dead."
    "\" Crush?"
    h smile"Yeah, it’s really obvious."
    h "The will they won’t they of it all was getting deeply annoying."
    h "Like, make out already! You know?"
    h unsure "Anyway…"
    h "Now that I'm a vampire, I feel really guilty about everything."
    h "Kalluri, I hate to admit, is much better at vampire hunting than I ever was."
    h "She’s like, fueled by her grief about you."
    h "I want to stop her from running the Batbashers…"
    h "You want her to realize you're the same person."
    h smile "Let’s team up! Enemies to lovers except without the lovers!"
    "You don’t really have any other options…"
    "This is a real sad state of affairs."

    mc "Okay, I guess i don’t have another choice…"
    h surprised "Really? Wow, honestly expected you to tell me to fuck off or something…"
    h smile "Don’t worry, I won’t let you down."
    "Filled with new found confidence, you both head towards the church."

    scene church with fade
    # Tense Music
    show h smile with dissolve
    "You feel anxious and afraid."
    h "Cassandra Kalluri, I challenge you to a Velsing Valorian for the title of head of the Batbashers!"
    show c doubt with dissolve
    "Cassandra appears from the shadows."
    "She looks depressed, broken."
    c "You can’t do that as a vampire, as you well know, Han."
    c "Or should I say, Hankiller."
    h "Well, the first one  was between  a Vellsing and a Vampire Velsing! It’s my birthright!"
    c "I… suppose you're right."
    c "And that’s why you’ve brought [player]’s corpse here right! To taunt me, to phase me."
    h unsure "Well, not exactly."
    h smile "This bloodsucker is my champion!"

    "Han looks at you."
    h "You’re going to fight for me, friend!"
    "Wait what?"
    mc "That was never part of the plan!"

    h smile"Oh my god, are you naive? It’s me!"
    h smile "Of course I’m going to betray you."
    c "Well, at least I’ll be able to put [player] to rest."
    h "Look, you’ve got this bloodsucker! Pull some Stephen Universe redemption shit on her!"
    mc "Screw you…"

    hide h with dissolve
    "Soon enough, you face off against Cassandra."
    "You don’t want to hurt her…"
    "Maybe you can convince her somehow…"
    window hide

    menu:
        "\"You can make it different…\"":

            window show
            mc "You can make it right,"
            mc "You can make it better!"
            mc "We don’t have to fi-"

            "Cassandra stabs you in the chest with a stake."
            "She starts crying."
            show c doubt with dissolve
            c "I know this isn’t you, [player]."
            c "But I don't know who to say this to…"
            c "Now that [player] is gone…"
            c "[player] made my life worth living."

            # all obj
            show c smile
            c "Made me smile every time I saw [pronoun]."
            c "I loved [pronoun]."
            #sing
            show c neutral
            c "And when [player] turned, I was so excited."
            #obj
            c "I didn’t even realize that I lost [pronoun]."
            c "I’ll always feel guilty for that."
            c "I just hope now, [player]’s soul will finally rest."
            "You fade into death, Cassandra’s tears the last thing you see before you die."
            # END OF GAME BAD ENDING

        "\"I am the same as [player]! I can prove it!\"":
            window show
            pass

        "\"Screw it, it's on!\"":
            window show
            "You brawl with Cassandra."
            "She fights with a deep sorrow and anger."
            "It seems like she’s spent the last several months studying how to be a great fighter."
            "She pins you to the ground."
            "You see a weak point in her defense."
            "But taking it might kill her…"
            window hide

            menu:
                "Use the weak point.":
                    window show
                    "You take advantage of the weak point and punch Cassandra."
                    "But you don’t know your own vampiric strength."
                    "You kill her."

                    "As she dies, you hold her in your arms."
                    "You didn’t mean for this to happen."
                    show h surprise with dissolve
                    h surprise "Damn, that’s crazy…"
                    h "Anyways…"
                    h smile "I guess that makes me the head of the Batbashers!"
                    h "Everyone, kill that vamp!"
                    "What feels like a hundred stakes pierce through you as you hold Cassandra."

                    scene black with fade
                    #CHANGE: this is just for me, i think i could make a little bloody graphic. probably.
                    "You feel the guilt carry you to the other side."
                    "Maybe in another life, things would be different."
                    "Or maybe, this tragic end was fate."
                    "Your last sight is Han, a bright smile on his face."
                    "He really did win it all."
                    return

                    "Don’t use the weak point."
                    window show
                    "You miss the chance to hurt Cass."
                    "You tussle for a bit…"
                    "You try your best…"
                    "But in the end, Cassandra stabs you in the chest with a stake."
                    "She starts crying."
                    c "I know this isn’t you, [player]."
                    c "But I don't know who to say this to…"
                    c "Now that [player] is gone…"
                    c "[player] made my life worth living."
                    # all obj
                    c "Made me smile every time I saw [pronoun]."
                    c "I loved [pronoun]."
                    #sing
                    c "And when [player] turned, I was so excited."
                    #obj
                    c "I didn’t even realize that I lost [pronoun]"
                    c "I’ll always feel guilty for that."
                    c "I just hope now, [player]’s soul will finally rest."
                    c "You fade into death, Cassandra’s tears the last thing you see before you die."
                    return



    show c doubt with dissolve
    c "Prove it? Prove it how?"
    mc "Ask me anything. Anything you think the real [player] would know."
    c "Fine… what’s my favorite color?"

    #CHANGE: THERE IS NO SUCH THING AS QUIZDEATH. THIS IS HUGE.

    hide c with dissolve
    window hide

    menu:
        "Orange":
            jump quiz_death

        "Blue":
            jump quiz_deathh

        "Pink":
            pass

        "Green":
            jump quiz_death

    window show
    show c smile with dissolve
    c "Ok, that was easy. I mean, look at me."
    c "How about… What’s my favorite book?"
    hide c with dissolve
    window hide

    menu:
        "What They do in the Shade":
            jump quiz_death

        "The Werewolf Diaries":
            jump quiz_death

        "The Moonlight Trilogy":
            pass

        "Nosferatu":
            jump quiz_death

    window show
    show c neutral with dissolve
    c "Ok, Ok. Who was my crush in elementary school?"
    hide c with dissolve
    window hide

    menu:
        "Michelle":
            jump quiz_death
        "Gwen":
            jump quiz_death
        "I don’t know":
            pass

    window show
    show c doubt with dissolve
    c"Right, you wouldn’t know. Because we only met in middle school."
    c "Sorry, I had to do a trick question."
    c "You have all of [player]’s memories…"
    #obj
    show c neutral
    c "You look just like [pronoun]…"
    c "But you have to be different somehow!"
    "You explain that Han lied, and that vampires remained the same after turning."

    show c doubt
    c "So you mean… All this time…"
    "It all hit her like a pile of bricks. She was on the wrong side of history. She was fighting her best friend."
    "Cassandra screamed in anguish and ran away from the church."
    hide c with easeoutleft
    "You try to run after her, but…"

    show h smile with dissolve
    h "What do you think of that, Batbashers?"
    h "This is my perfect victory!"
    h sigh "That’s right, I win!"
    h smile "By the rules of the Batbashers, with no other legitimate heir in sight, I’m in charge now!"
    h sigh "And by the rules of the initiation spell…"
    h smile "You all have to listen to me!"
    h "It’s the Han Dynasty, baby!"
    h "As my first order of business…"
    h sigh "Kill that vamp!"
    "You scamper out of the church."

    scene forest with fade
    "You try to find Cassandra, but she’s gone, long gone."
    "You hear the marching of the Batbashers as they hunt you down, and you run. "
    "Back into hiding again."
    "Alone once more."
    "ONE YEAR LATER"

    #sad music
    scene street with fade
    "After a year of searching, you finally find her."
    show c doubt with dissolve
    mc "Cassandra."
    "You’ve tried confronting her before, but she’s always slipped away."
    "But now, in the light of the moon, she finally says."
    c "[player]."
    "You look at each other, tears in both of your eyes."
    c "I… I’m sorry for running."
    c "I didn’t know what else to do."
    c "After everything I did to you, to the other vampires…"
    c "I couldn’t live with myself."
    c "I’ve been fighting off Batbashers, hoping to atone in someway…"
    c "But after everything we’ve been through, I couldn’t look you in the eyes."
    c "I’m so so sorry, for everything."
    "The guilt on her face is heartbreaking."

    hide c with dissolve
    window hide

    menu:
        "I forgive you.":
            window show

            show c doubt with dissolve
            c "But i can’t forgive myself."
            c "All the horrible things i did."
            c "I’m a monster."
            c "You deserve better."
            c "You deserve a better friend."

            menu:
                "You’re right.":
                    jump no_forgiveness

                "You were manipulated, misled":
                    window show
                    mc "Han tricked you."
                    mc "If I were in your place, I may have been tricked too."
                    mc "Please, I need you."
                    mc "I’ve lost so much already, I can’t lose you too."
                    mc "You mean so much to me."
                    mc "I miss meeting you in the library"
                    mc "I miss seeing you smile after geeking out about something."
                    mc "I miss being with you."
                    mc "I… "
                    window hide

                    menu:
                        "I like you platonically.":
                            jump cass_med
                        "I love you. Most ardently.":
                            jump cass_best



        "I can’t forgive you.":
            label no_forgiveness:
                window show
                # Sad Music
                show c doubt with dissolve
                c "I know. That’s why I can’t see you anymore."
                c "Goodbye, [player]."
                c "I’ll always remember you, and treasure what we had, and mourn what we lost."
                "Cassandra leaves, and you let her."
                hide c with dissolve
                "You stand alone for a while, letting it all sink in."
                "Imagining what could have been."
                "Before you too walk away in the night."
                return

label cass_med:
    window show
    show c smile with dissolve
    c smile "Wow…"
    "Cassandra giggles"
    $ cass_affection+=1
    # Neutral Music
    c smile "I haven’t laughed in so long…"
    c "I like you platonically too, [player]."
    c "Let’s be friends again."
    "You and Cassandra laugh and catch up as the sun rises."
    "You walk to Cassandra’s new place in the shade."
    "Han Velsing might still be out there…"
    "But at least you have your best friend back."
    return

label cass_best:
    window show
    show c neutral with dissolve
    c neutral "Pride and Predjudice?"
    c smile "You’re really using Pride and Prejudice on me?"
    $ cass_affection+=1
    "Cassandra breaks out into laughter."
    # Romantic Music
    c "Oh my god, It’s like Sophomore Lit when Mr. Stoker.."
    c "Wait, I’m going off on a tangent… I love you too."
    c confident "I love you most ardently."
    c "You mean the world to me."
    c doubt "When I thought you were gone… It broke my heart."
    c smile "If you really mean it, that you forgive me…"
    c wink "I’d love to be your girlfriend."
    c smile "I’d love to brave this messed up world with you."
    c "What do you say, [player]?"

    hide c with dissolve
    window hide

    menu:
        "Yes.":
            pass
        "I love you, Cassandra Kalluri.":
            pass
        "I don’t know If i really forgive you…":
            jump no_forgiveness

    "Cassandra gives you a kiss."
    $ cass_affection+=1
    "The moonlight shines bright as you embrace her."
    "Even though Han is still out there somewhere…"
    "You feel like the world is perfect right now."

    return

label quiz_death:
    window show
    # Sad Music
    show c doubt with dissolve
    c "Damn it. I really, really hoped it was you in there."
    "Cassandra shifts back into attacking you."
    "You tussle for a bit…"
    "You try your best…"
    "But in the end, Cassandra stabs you in the chest with a stake."
    "She starts crying."
    c "I know this isn’t you, [player]."
    c "But I don't know who to say this to…"
    c "Now that [player] is gone…"
    c "[player] made my life worth living."
    # all obj
    c "Made me smile every time I saw [pronoun]."
    c "I loved [pronoun]."
    #sing
    c "And when [player] turned, I was so excited."
    #obj
    c "I didn’t even realize that I lost [pronoun]"
    c "I’ll always feel guilty for that."
    c "I just hope now, [player]’s soul will finally rest."
    c "You fade into death, Cassandra’s tears the last thing you see before you die."
    return
