# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

init:
   $renpy.music.register_channel("default","music",True)

image bg beerout = "beerhunterext.png"
image bg beerint = "beerhunterint.png"
image bg berlin = "berlin.png"
image bg blur = "broadcastnewsdeskblur.png"
image bg broadgreen = "broadcastgreenroom.png"
image bg broadnews = "broadcastnewsdesk.png"
image bg broadoff = "broadcastoffice.png"
image bg broadstud = "broadcaststudio.png"
image bg carl = "carloffice.png"
image bg elvis = "elvis.png"

image bg resout = "restaurantext.png"
image bg resint = "restaurantint.png"

image bg safe = "safe.png"
image bg scandal1 = "lewinsky.png"
image bg scandal2 = "manning.png"
image bg scandal3 = "robford.png"
image bg scandal4 = "sandusky.png"
image bg side1 = "sidewalk01.png"
image bg side2 = "sidewalk02.png"
image bg side3 = "sidewalk03.png"
image bg sink1 = "sinkholeext.png"
image bg sink2 = "sinkholeside.png"
image bg sexy = "sextape.png"
image bg street1 = "street01.png"
image bg street2 = "street02.png"
image bg street3 = "street03.png"
image bg ussr = "ussr.png"

image andrea = "andrea.png"
image carl = "carl.png"
image jimmy = "jimmy.png"
image julian = "julian.png"
image sandra = "sandra.png"
image seung = "witness-full-bod.png"
image seung2 = "witness-full-bod.png"
image phone = "phone.png"

# Declare characters used by this game.
define an = Character('Andrea', color="#ffffff")
define ca = Character('Carl',color="#ffffff")
define ji = Character('Jimmy',color="#ffffff")
define ju = Character('Julian',color="#ffffff")
define sa = Character('Sandra',color="#ffffff")
define cm = Character('Cameraman', color="#ffffff")
define di = Character('Director', color="#ffffff")
define m = Character('Man', color="#ffffff")
define sf = Character('The Storm Of Pale Lightning', color="#ffffff")
define sf2 = Character('Mason', color="#ffffff")
define sf3 = Character('Storm of Pale Lightning', color="#ffffff")
define jiva = Character('Jimmy (onscreen)', color="#ffffff")
define sava = Character('Sandra (onscreen)', color="#ffffff")
define txt = Character('Text Message', color="#ffffff")
define jtxt = Character('Jimmy (text)', color="#ffffff")
define stxt = Character('Sandra (text)', color="#ffffff")
define apho = Character('Andrea (on phone)', color="#ffffff")

# The game starts here.
label start:
    $ renpy.music.play("Pamgaea.mp3")
    $ blackmail = False
    $ flag2 = False

   

    scene bg broadnews
    with fade
    show jimmy at center with dissolve

    ji "Ow. Owwww. Owwwwww."
    cm "We're live in five,{w} four,{w}three..."
    ji "Tell me again, whose goddamn idea was it to not do this shit live--"
    cm "and action!"

    scene black

    $renpy.pause(1.0)

    $ renpy.movie_cutscene("OP.avi")

    $renpy.pause(1.0)

    scene bg broadnews
    with fade
    show jimmy at center with dissolve

    "Jimmy suddenly snaps back into action."
    ji "G-good morning, Flor-"

    scene bg blur
    with fade

    show jimmy at center with dissolve

    ji "Wh-whoa. Whooooa. Um..."
    ji "Um... Flor-ami-mami! G'morning Futami-ami...? Futanari... mami? Th-that can't be right."
    cm "(Pssst. It's 'Miami.')"
    ji "Right, um. Good morning My-amy. Miami? That's a fucking stupid name. Right, that's... that's the one!"
    ji "Uh, I don't suppose you could bleep that one out? Eheh. Heh heh."
    "The cameraman's eyes roll."

    hide jimmy

    scene bg broadstud
    with fade

    cm "Um, Mr. Producer, sir? Should we cut here?"

    show julian at topright with dissolve

    ju "Haha, no, keep it rolling! This stuff is hilarious."

    scene bg blur
    with fade

    show jimmy at center with dissolve

    ji "Yeah, it's... it's me, your faithful newsanchor, J- James-- Jimmy McKay, here with you at Action News Six!"

    scene bg broadnews
    with fade

    show jimmy at center with dissolve

    ji "Seven? Was it seven? Was it se-- no, it's six. Oh god, my head. Ow."

    scene bg blur
    with fade

    ji "(Oh. Oh. God damn. This is not good.)"

    cm "*whispers* Psst! Get with the news!"

    ji "Oh, right, those! Er, um... breaking news!! (Think, Jimmy, think!)"

    menu:
       "Talk about an international incident regarding the sovereignty of several European states":
          jump ussr
       "No, there was that revolution, or other in Germany. Talk about that":
          jump berlin
       "No, people like celebrities. Talk about a recent death.":
          jump elvis

label ussr:

    scene bg ussr
    with fade

    show jimmy at center with dissolve

    ji "The United States of Soviet Russia has formally announced its dissolution..."
    ji "Wait, is that what 'USSR' stands for...?"
    ji "That... that doesn't..."
    ji "Oh, sorry, the, uh... Union of Soviet Socialist Republics was dissolved today, marking the end of ---"

    jump start2

label berlin:
    scene bg berlin
    with fade

    show jimmy at center with dissolve
    ji "Ladies and gentlemen, the Berlin Wall is crumbling down!"
    ji "At last, families are together, and a country is reunited once again."
    ji "...wait, wasn't Germany already one country? Why was the wall there? Hell if I know, but--"

    jump start2

label elvis:
    scene bg elvis
    with fade

    show jimmy at center with dissolve
    ji "Uh, beloved... beloved rock n' roll icon Elvis Presley has, unfortunately, left the building."
    ji "Our thoughts go out to his family ...wait, no, that's not right."
    ji "Was that joke too soon? No? How old was this guy?"

    jump start2

label start2:

    scene bg broadnews
    with fade

    cm "*whispers* Psst! Cut to weather!"

    show jimmy at topleft with dissolve

    ji "Right! Here's our lovely weather reporter man person... Walter Cronk--"

    $renpy.pause(1.5)

    show sandra at topright with dissolve
    hide jimmy with dissolve

    sa "Thanks, Jimmy! Now today's forecast involves..."
    hide sandra
    scene black

    $renpy.pause(1.5)

    jump openingcrawl
 
label openingcrawl:
    #TODO: background CG
    scene black
    "Action News Six is Miami's number one source for entertainment and information."
    "Or, at least, it would be... if people took it seriously."
    show carl at topleft with dissolve
    "Meet Carl Johnson McKay, president of Action News Six. He purchased the network at a very low sum, and turned it into an empire."
    show jimmy at center with dissolve
    "This is James Patrick McKay, President McKay's only child, and the network's only newsanchor."
    show sandra at topright with dissolve
    "This is Sandra Locke-McKay, President McKay's new trophy wife... and the network's resident weather-lady."
    hide carl with dissolve
    show julian at topleft with dissolve
    "This is Julian César, the young executive producer, who's always aiming for higher ratings... and profits."
    hide sandra with dissolve
    show andrea at topright with dissolve
    "This is Andrea Locke, Sandra's older sister, and star newsanchor for Channel Six's rival, Channel Eleven."
    #todo: black screen
    "It's an awful mess in the city of Miami, a land of wasted minds and plastic bodies..."
    "Where the truth is never what it actually is, and the facts are never straight."
    "That's right, this is a city, most assuredly... on the air."
    jump caughtontape

label caughtontape:
    scene bg broadgreen
    with fade
    show jimmy at center with dissolve
    ji "That was... that was terrible. Oh my god, that was really bad. How did we not do a retake of that?"
    cm "Dunno. Mr. Cesar thought you did pretty good."
    ji "If by 'pretty good' you mean 'really really terribly.' I embarrassed myself out there, and he knows it!"
    cm "Even then, it's not like we have the time to do it in more than one take. Or the budget."
    ji "...wait, don't you just delete the footage? Can't you do that?"
    cm "Well, sure, if the President felt like getting us digital equipment. You know. Film."
    ji "Right, just... oh god, my head."
    cm "Relax. I'll see if we can just air... iunno, a nature documentary. It's not like anyone ever watches this channel."
    ji "For once in my life, I am thankful."
    # TODO: knocking at the door
    ji "Ugh. Who is it?"
    show julian at topright with dissolve
    ju "Hey, hey, J-Town, it's ya boy, Julie-C! What's shakin'."
    ji "Oh, can I... can I not deal with you right now? Please? My head..."
    ju "Haha, excellent performance earlier today, might I add! Bravura. Incroyables. Merveilleuses."
    ji "Do... do you actually understand what those words--"
    ji "Never mind! Just... can you please not? I can't deal with you right now, I'm off shift, I'm..."
    ju "Yes, you can! You're all about the dealing, isn't that right, J-Town? Dealin' the boss's new squeeze a some of that Jimmy Jr., if you catch my drift."
    ji "A, uh... what?"
    ju "A little bird tells me you got a little frisky with your own stepmom, J-Town!"
    ji "Wait, wait... what bird? What?"
    ju "Meet me in my office in five if you wanna talk out the deets. And believe you me, these are some spicy deets. Deets by Dr. J. Heh."
    hide julian with dissolve
    ju "Catch you on the flipside, if you wanna keep your job! Laters, J-Town."
    # SOME SOUND EFFECT MAYBE 
    ji "I... what the hell was that?"
    cm "Whatever goes on between you and the producer, man, I want no part of that."
    ji "Sigh. I guess I've got no choice, then, do I?"

    # TODO: HALLWAY CG w/ footsteps

    scene bg broadoff
    with fade

    show julian at topright with dissolve
    #TODO: knocking at door

    ju "Door's open, my good man!"

    #TODO: door opens

    show jimmy at center with dissolve

    ji "I'm here. What is it...?"
    ju "Oh, good, good! Have a seat."
    ji "So what is this about?"
    ju "So, tell me... how do you feel about the sex tape to END all sex tapes?"
    ji "With all due respect, sir..."
    ju "Please! Call me Julian."
    ji "You forget that we feed off of sex tapes. Those are like, a dime a dozen in this town."
    ju "That's right, but this right here? This ain't no ordinary sex tape, no sir!"

    #TODO: show vhs cg

    ju "In fact, I might even go so far as to say that this sex tape will CHANGE YOUR LIFE, J-Town."
    ju "You hear that? This thing right here is a life-changer! Haha, I love it!"

    "Jimmy sighs."

    ji "Who's on it? Let me guess, it's that politician, Mayor Ross, isn't it? He was killed, and suddenly..."
    ji "And suddenly, the whole world wants to see him doin' ekkies off of a broad's tits. Right."

    ju "Whoa, whoa, whoa. Who said any dang thing about some senator?"
    ji "Mayor."
    ju "May not. Settle down, kiddo."
    ji "What?"
    ju "Ths right here, J-Town, is a sex tape featuring everyone's favorite McKay..."

    scene bg sexy
    with fade

    jiva "Oh, yes! Yes!"

    scene bg broadoff
    with fade

    show julian at topright with dissolve
    ju "You. And hey, your dad's new wife makes a guest appearance, too!"
    ju "That'd make two of our favorite members of the McKay family. If you count her."

    show jimmy at center with dissolve
    ji "Wait, no, that's me, but... that can't be my goddamn step-mom, that'd be... weir-"

    sava "Oh, more!"

    ji "Oh, fuck me."
    ju "Exactly!"
    ji "Shut up."
    ju "Ooh, harsh words, Eddy-pus."
    ji "That's... it's 'Oedipus.'"
    ju "Whatever. This tape's gonna make for a memorable prime-time variety show, that's for dang sure."
    ji "N- Don't you goddamn dare!"
    ju "Oh, I'm not going to. Yet. Let's talk this through, J-Town."
    ji "Shit."
    ju "So... give me one good reason why I shouldn't-- or wait, what do YOU think? What should I do with this tape?"

    menu:
         "You can't! I'll do ANYTHING! ANYTHING, I tell you!":
              ju "Anything, you say?"
              ji "Yes. Yes, anything."
              jump beg
         "Um, could you give me some time to think about this?":
              ji "...yeah, I'm gonna need some time. This is a hard decision to make."
              jump stall
         "(Say nothing, just lunge at him and take the tape)":
              ji "(What, are you kidding? This guy's a trained boxer! I'll be killed!)"
              menu:
                    "You can't! I'll do ANYTHING! ANYTHING, I tell you!":
                        ju "Anything, you say?"
                        ji "Yes. Yes, anything."
                        jump beg
                    "Um, could you give me some time to think about this?":
                        ji "...yeah, I'm gonna need some time. This is a hard decision to make."
                        jump stall

label beg:
    scene bg broadoff
    with fade

    show julian at topright with dissolve
    show jimmy at center with dissolve
    $ blackmail = True
    ji "So, um... Mr. Cesar."
    ju "Please, I told you! Call me Julian. I feel weird when older people call me 'mister."
    ji "Well, you see... my dad's the president, right? With that in mind, couldn't you look the other way? Just this once?"
    ju "No can do, bud. Ratings are in the gutter, and I have a good feeling that the tentatively-titled 'The Real McKay' is gonna shoot them through the roof!"
    ji "That's... that's a really fucking terrible name for a porno."
    ju "Whatever. This right here's the juice. And I'm the juicer. Or rather, he who operates the juicer. The juicer-er."
    ji "Juicy."
    ju "See? You get it, J-Town. You get it exactly."
    ju "So let me tell you what. If you can tell me what Action News Eleven has going on, I'd be more than happy to trade juices."
    ji "That's gross, man."
    ju "Hey, don't knock it 'til you've tried it, J-Town."
    ji "So I just need to steal Channel Eleven's scoop, and that'll be that, right? Wait, what makes you think I can even do this?"
    ju "Don't be coy. I know for a fact you've been slipping that Andrea chick some of the little Miami steam, am I right or am I right?"
    ji "It's not little, but--"
    ju "Oh man, that chica is Sandra's older sister, right? I just remembered! You dog, J-Town, barking up every branch of that sweet, sweet tree."
    ji "Look, this conversation's becoming really uncomfortable, and I--"
    ju "Irregardless."
    "Jimmy rolls his eyes."
    ji "Okay, what if I refuse?"
    ju "See, if you don't give me some of THAT juice, then some of THIS juice..."

    scene bg sexy
    with fade
    jiva "You're crushing me, baby!"

    ju "Is gonna leak all over national television. Primetime, baby."

    scene bg broadoff
    with fade

    show julian at topright with dissolve
    show jimmy at center with dissolve

    ji "You're bluffing."
    ju "Am I? Am I, really?"
    # DEAD SILENCE
    ji "Ugh, fine! Fine, I'll do it!"
    ju "Sweet! I knew you'd understand the sitch, J-Town. I'll meet you at the Beer Hunter later, and I expect some development! Who knows, I might persuade your dad into giving you the late-night slot..."
    ju "I mean, Jay Leno? Make way for JIMMY Leno, am I right? Up top!"

    menu:
         "Give the guy a high five":
             ji "Here."
             ju "Excelente. Great things, J-Town! GREAT THINGS!"
             jump andreasidewalk
         "Leave the sucker hanging":
             ji "Look, uh... Julian? I'd hate to interrupt, but I'd better get moving. Carpe diem, right?"
             hide jimmy with dissolve
             ju "J-TOWN! NOT cool, bro! Don't leave a brother hanging!"
             ji "Bye!"
             ju "Hello? J-Town? Anybody? Slap me some skin? Please?"
             ju "Help a brother out?"
             jump andreasidewalk

label stall:
    scene bg broadoff
    with fade

    show julian at topright with dissolve
    show jimmy at center with dissolve

    ji "So, um... Mr. Cesar."
    ju "Please! Call me Julian. It feels weird when someone older calls me 'Mister.'"
    ji "Right, right. So, uh... how about I get back to you on this? Maybe later. I'll give you a heads-up."
    ju "I dunno, J-Town. This feels pretty pressing."
    ji "Great! Great. See you in... an hour. Or two. I'll let you know!"

    hide jimmy with dissolve
    ju "Whatever. I'm in no rush."

    scene bg sexy
    with fade

    sava "Tell me, who's your daddy? Who's YOUR daddy?"

    ju "Haha! This dang thing is hilarious."

    jump rendezvous

label andreasidewalk:

    scene bg side1
    with fade

    show andrea at topright with dissolve
    show jimmy at topleft with dissolve

    an "So, how's work going? You holding up on the Good Morning show?"
    ji "Don't remind me. I'm still weary from last night."
    an "I'm really sorry I couldn't come! I was busy with work..."
    ji "Hey, don't... don't worry about it! You didn't have to. Missed you, but I still had fun."
    an "Oh, no doubt. I wouldn't be much fun, anyway... my sister's the party animal, not me."
    ji "Yeah. Haha, your sister. Funny you should mention her."
    "Jimmy laughs nervously."
    an "I still think it's kinda weird that she's sleeping with your dad. Then again, who am I to judge?"
    ji "It's just... it's weird, you know. She's your younger sister, and he's my seventy-three year old dad."
    an "That's nothing new. She'll sleep with anyone if it means getting her face on TV."
    ji "Yeah... anyone. Haha."

    scene bg side2
    with fade

    show andrea at topright with dissolve
    show jimmy at topleft with dissolve

    if blackmail:
        ji "By the way, you wouldn't happen to be privy to anything juicy going on, would you?"
        an "'Juicy'?"
        ji "Oh, sorry, I've... been hanging around the producer for way too long."
    else:
        ji "So what's been going on with you, lately?"

    an "Well, I suppose the only thing going on lately was that murder case. I mean, that senator was found with the murder weapon. I'm covering that..."
    ji "He's gonna get away with it. I know he will."

    scene bg side3
    with fade

    show andrea at topright with dissolve
    show jimmy at topleft with dissolve

    an "What makes you say that?"
    ji "It's... it's all politics. The political scene is this huge clusterfuck. Murder and madness is what passes for law."
    an "That's... I prefer to believe in the truth. Justice. The right thing prevails at the end of the day."
    ji "Truth? I'll tell you what the truth is."

    scene bg scandal1
    with fade

    $renpy.pause(0.5)

    ji "People don't want to see justice prevailing. People want to see heroes and icons dragged through the dirt."
    ji "Everyone loves a good scandal. Why else is gossip so prevalent in the media? This stuff is our lifeblood."

    scene bg scandal2
    with fade

    $renpy.pause(0.5)

    ji "They don't want the truth! They want to know who's gay! Who's fucking who! Who's gained ten pounds, who's lost twenty!"
    ji "Oh, no, the prime minister is a racist! People eat that shit up!"

    scene bg scandal3
    with fade

    $renpy.pause(0.5)

    ji "Presidents, lawyers, doctors, superstars... people love to see them brought down to their level. And they laugh, and laugh, and laugh."

    scene bg scandal4
    with fade

    $renpy.pause(0.5)

    ji "See, the truth is... everyone is filled with filth. And people want to see that the world is as filthy a place as they are!"
    ji "They want trash... and we give them trash."

    an "But... isn't that why no one takes your channel seriously?"

    scene bg resout
    with fade

    show andrea at topright with dissolve
    show jimmy at topleft with dissolve

    an "I mean, that's why I do what I do. I try to make the world a better place. If I'm drowned out by all the shit and filth, so be it."
    an "At the end of the day, the only one I'll have to face is me. If I can do that with a smile... then I've done good."

    jump date

label date:

    scene bg resint
    with fade

    show andrea at topright with dissolve
    show jimmy at topleft with dissolve

    ji "I'm... y'know, back there, I... I kind of said some things. Things that I regret. And I'm sorry."

    an "Oh, don't worry about it. You're having a rough time adjusting."

    ji "It's just... it's a dead-end job, you know? I'm the only reporter at Channel Six that's worth a damn, but..."
    ji "Management is terrible. Pay is next to nothing. Everything sucks."
    "Jimmy sighs."

    an "Oh, well. Channel Eleven's not much better. People are just hard to work with."
    ji "But at least people take you guys seriously! With us, well... it's all pointless human interest stories, half of which are staged."
    an "Oh... even the one about the high schooler being forced to coach an all-girls elementary school basketball team? I liked that one."
    ji "Ugh, don't remind me. Their second season didn't go so well."
    ji "It's just... it's all a sick joke, you know? It's so dumb. I hate it."

    if blackmail:
        an "Hey, I... I'd hate to interrupt, but I need to go to the ladies' room. Watch my stuff for me?"
        ji "Sure thing."
        an "Thanks, babe. You're the best."
        hide andrea with dissolve
        # RINGTONE
        play sound "SMS.wav"

        show phone at topright with dissolve
        ji "Huh, her phone's ringing..."
        txt "hi andrea- jus wanted 2 let u know that witness wil meet u @ sinkhole in 15m. kthx! -boss"
        ji "Oh. Oh shit, this could be what Julian wants. I'll... uh..."
        menu:
             "Reply":
                menu:
                     "Legible Reply":
                         ji "Um... How about..."
                         jtxt "Cool! I'll be right there, ETA 10 minutes."
                         ji "That sounds good. Whatever. Let's go."
                     "Illegible Reply":
                         ji "Uh... maybe this?"
                         jtxt "cool!!!! meet u then lolllll xDDDD"
                         ji "Ow, my head. That hurt to write."
                     "Just send a bunch of smilies":
                         ji "You know what, here goes nothing:"
                         jtxt "*^____^* ~!! <3 <3 <3 xD"
                         ji "I... I don't know what any of that is even supposed to mean."
                hide phone with dissolve
                ji "Sorry, Andrea, but... that's the way the cookie crumbles!"
                jump witness
             "Don't reply":
                hide phone with dissolve
                ji "No. No, I couldn't. Too much risk."
                ji "I'll... I'll work something out with Sandra. Maybe we can come up with a plan."
                an "Thanks for waiting!"
                show andrea at topright with dissolve
                ji "Oh, you got an important text. From your boss, I think."
                an "I did? Oh no, that means I'll have to cut today short! I'm so sorry!"
                ji "Don't be. Knock 'em dead, hon. I'm rooting for you."
                jump rendezvous
    else:
        an "Well, I mean it'd be a *little* unethical, but... what if I could get you an interview?"
        ji "Huh? You mean, over at Channel Eleven?"
        an "I could introduce you to our chairman, Teej Viola Icystorm!"
        ji "What the hell kind of a name is that?"
        an "A total sweetheart who'll totally be willing to do you a solid, that's who! This could be your big break."
        ji "Aw, no. I couldn't! I'd hate to impose."
        an "Please, I insist. Think of it as an early Christmas present."
        ji "Thanks, hon. You're the best."
        an "Don't mention it! Now, I have to go to the ladies' room. Be right back!"
        ji "Okay!"
        hide andrea with dissolve
        ji "Haha! YES! FINALLY!"
        # RINGTONE
        play sound "SMS.wav"

        show phone at topright with dissolve
        ji "Uh-oh."
        stxt "problem. tape not in safe. -s"
        ji "Oh. Oh no."
        jump burnbabyburn


label witness:

    #IGNITION
    scene bg resout
    with fade

    $renpy.pause(1.5)

    #VROOM VROOM VROOOOOOM

    play sound "car_LP.wav"

    scene bg street1
    with fade

    play sound "car_LP.wav"

    $renpy.pause(1.5)

    scene bg street2
    with fade

    play sound "car_LP.wav"

    $renpy.pause(1.5)

    scene bg street3
    with fade

    play sound "car_LP.wav"

    $renpy.pause(1.5)

    scene bg sink1
    with fade

    show jimmy at center with dissolve
    ji "Okay, I'm here. Now... where's that witness?"

    m "Shh. Over here. In the alley."

    ji "That doesn't sound very safe. But since it's my ass on the line... whatever."



    scene bg sink2
    with fade

    show jimmy at center with dissolve
    show seung at topright with dissolve

    ji "Whoa, what are we going to do in the alley?"

    m "Psst. Are you Andrea?"

    ji "Am I? Well, uh."

    menu:
        "I'm Andrea!":
            ji "Why yes, that'd be me."
            m "Shh. You keep quiet, understand? There are wolves in the walls, and the walls have ears..."
            ji "I'm pretty sure you mixed two different phrases, but okay...?"
        "No...":
            ji "Actually, I'm James."
            m "Ah, an alias. Very good, Andrea. Very, very good. Exquisite."

    ji "Right, right. And YOU are?"
    m "My name? It is in a tongue that no mortal was meant to enunciate."
    m "For in the time it would have taken you to express even a fragment of my name, a million million stars would have fallen from the sky..."
    ji "So, uh... what do I CALL you?"
    m "For the time being, you may call me The Storm Of Pale Lightning. It is a poor translation of my true name."
    ji "Riiiight. And what, pray tell, does The Storm Of Pale Lightning do for a living?"
    sf "Behold!"
    sf "The Storm Of Pale Lightning manufactures only the finest artisan mason jars on this side of Lemuria!"
    ji "Actually... Mason is easier to say. Can I call you that? I think I'll call you that."
    sf "The Storm of Pale Lightning cares little for your petty trivialities!"
    ji "So, Mason..."
    sf2 "Bah!"
    ji "What's this about an eyewitness testimony, or whatever?"
    sf2 "The Storm of Pale Lightning will not respond to anything save for his true name!"
    ji "Really?"
    sf2 "Yes."
    "Jimmy sighs."
    ji "Oh, Storm of Pale Lightning!"
    sf3 "THE Storm of Pale Lightning."
    ji "Do I have to?"
    sf3 "Yes."
    ji "Oh, the Storm of Pale Lightning, answer this humble mortal's query, that mine soul might be granted release at last from the cruel uncertainties of this earth!"
    sf "Yes! The Storm of Pale Lightning likes this very much, Andrea the mortal. We are amused."
    ji "So, will you tell me now-"
    sf "Continue by praising our eldest son, he who is named The Caress of Spring's Flowers..."
    ji "Answer the fucking question."
    sf "Yes, it was the senator. Big Wolfy J did it."
    ji "See, was that so ha--"
    sf "FOOL! Was that perhaps what you were expecting The Storm of Pale Lightning to say?"
    ji "Seriously? Fuck you, dude."
    sf "Because in that case you would be correct, Andrea the Mortal. It was truly the senator, the Lone Wolf Of Winter's Peak."
    ji "The... what?"
    sf "You see, The Storm of Pale Lightning can verify this, for the eyes of the wind do not falter!"
    ji "Prove it."
    sf "BEHOLD!"
    "The Storm of... Whatever. He pulls out a VHS tape from his jacket."
    ji "And what's this supposed to be?"
    sf "Surveillance footage, taken on the day of the murder! It shows The Lone Wolf Of Winter's Peak entering the victim's abode, armed with an axe!"
    ji "Huh. That... that adds up, I think. That's actually really soli-- wait a minute, why do you have this?"
    sf "FOOL! When the wind of providence blows, does the sailor question it?"
    ji "Uh... no, but... you know what, never mind. Thank you, The Storm of Pale Lightning. Thank you for your time."
    hide jimmy with dissolve
    sf "Run fast, Andrea the mortal. For when the wind blows, it is the lightning that swiftly descends on the unprepared!"

    jump beerhunter

label beerhunter:
    scene bg street3
    with fade

    play sound "car_LP.wav"

    $renpy.pause(1.5)
    scene bg street2
    with fade

    play sound "car_LP.wav"

    $renpy.pause(1.5)


    scene bg beerout
    with fade

    $renpy.pause(1.5)
    scene bg beerint
    with fade

    show julian at topright with dissolve
    show carl at center with dissolve

    ji "Dad! Dad dad dad!"

    show jimmy at topleft with dissolve

    ca "Oh, look what the cat dragged in."

    ji "I... I've got it! A scoop, a... an honest-to-goodness scoop!"

    ca "Well, what are you standing around there for, let's hear it."

    ji "I've got evidence that proves that Senator Wolfman killed Mayor Ross!"

    ca "Well, we always knew that it was definitely a wolfjob. But who does that surprise, exactly?"

    ji "No, no, I mean conclusive evidence! Something that the Big Wolfy J can't talk out of, this time! Evidence that has him seen entering the area with the weapon!"
    ca "Huh. I've gotta admit, that's pretty hard to deny..."

    ji "Exactly! It's... it's actual news! News that doesn't involve an alien abduction, or conjoined twins, or a pair of twin angels that have a third in the group!"

    ca "Yeah, but... is it interesting?"

    ji "Interesting enough for Action News Eleven, at any rate."
    ca "Ho-ho! You sly dog, I knew you were my son! "

    "Jimmy hands Carl the tape."

    ji "So can I... can I have a better shift, now?"

    ca "What, are you kidding? Who else is gonna do Good Morning, Miami?"

    ji "But I... that scoop!"

    ca "And I'm glad that you're showing some initiative. But let's be honest, we're short on hands, and we need all the help we can get. Everyone has a place here at Channel Six, and, well... yours is with Good Morning, Miami."

    ca "I'm glad we had this talk, son! See you tomorrow morning!"

    hide carl with dissolve

    ji "But I...! But I! Julian, you son of a bitch!"

    ju "Sorry, dude, that's the way the cookie crumbles, yeah?"

    ji "Don't... don't screw with me, you greasy fuck! The tape, where is it!?"

    ju "Fine, fine, here it is. "

    "Julian hands Jimmy the tape."

    ji "And this is it, right? No duplicates, triplicates... or any other funny stuff?"

    ju "Honestly, dude, that tape's the funniest shit. I don't need extra copies, the best of it's in my head."

    hide julian with dissolve

    ju "Have fun, J-Town! Catch you on the flipside, duder."

    ji "Ah, fuck!"

    # RINGTONE

    play sound "SMS.wav"

    ji "Yeah, what?"
    apho "I knew it. I was wondering who took my phone, and something told me it was gonna be you."
    ji "Ah-- Oh fuck, this was your phone! Listen, I can explain, I can..."
    apho "I didn't sign up to date a thief! We're through!"

    #CLICK

    ji "FUCK!"

    scene black

    $renpy.pause(5.0)

    scene bg broadstud
    with fade

    ji "Nowhere left to go..."

    scene black

    "...but on the air."

    "~FIN~"
    return



label rendezvous:

    scene bg broadgreen
    with fade

    show sandra at topright with dissolve

    ji "Okay, okay, we're fucked. We are rightly, completely, totally fucked. Shit!"

    show jimmy at center with dissolve

    sa "Huh? What was that? Who's fucking who?"

    ji "No, not you! Well, okay, fine, maybe you. And me. That happened."

    sa "Is this about last night...?"

    ji "Yes it is. Yes it really is. Goddamn it."
    sa "What about? Didn't we agree not to speak of it again?"

    ji "Yes, but... but! That tanned piece of shit Julian has it on tape! I don't know how, or why, but... he's got footage."

    sa "Oh no! How?"

    ji "I don't know, but... I've seen the tape, he isn't bluffing. He's caught us, red in the face, doing the nasty."

    sa "I'm sure your dad'll understand--"

    ji " No, no, no, a thousand times, no. You know how he gets. He's already moved me to the shit-shift that is Good Morning, Miami, so who knows how he'll react when he finds out his own son has been caught banging his smokin' piece of arm candy?"

    sa "Who?"

    ji "Me and you."

    sa "Ohh. Oh. Oh, I know! My sister's smart, she'll know what to do. I'll go call her up..."

    ji "No! No, no, no, don't. Just... don't. I'm sure she could help, but I'd rather keep things simple. Less complicated."

    sa "Then, um... what are we going to do? I'm not sure what we can do."

    ji "Um... hmm. Well, the way I see it, we have two options."

    scene black

    $renpy.pause(3.0)


    show julian at center with dissolve
    ji "Option one- I go back, and beg Julian for the tape. On the upside, this might get me into his good graces, but on the downside, do I really want to do that smug-ass snake a favor?"
    
    if blackmail:
        ji "Thing is, I've already tried this. It's not happening."
        sa "Well, that's a shame..."
    else:
        sa "Well, probably not..."

    hide julian with dissolve
    show carl at center with dissolve
    ji "Option two- you handle it. ...Admittedly, I have no real clue what you can do, but hey, you might be able to get my idiot dad in on it. Tell him he's on the tape. I mean, you two have been fucking like rabbits everywhere in this goddamn studio, so it stands to reason that there'd have been at least one recording that'd have gotten out somehow, right?"
    sa "We do not--"
    ji "We're not deaf."
    sa "Wait, why can't you ask your dad? He's your dad."
    ji "See, I have no credibility with that senile asshole."

    scene black

    $renpy.pause(3.0)

    scene bg broadgreen
    with fade
    show jimmy at center with dissolve
    show sandra at topright with dissolve

    ji "So... those are our options. No matter how you slice it, the best course of action has got to be..."

    menu:
        "Beg Julian":
            if blackmail:
                ji "No, we can't do that, remember? We have to ask Carl..."
            else:
                ji "I'll... beg Julian. I mean, it sucks that I'll owe the guy a favor, but... I know for sure he has the tape."
                sa "You sure you don't need me for anything?"
                ji "Well, the thing is...  if you did anything, then Julian would know that I told you. And that's bad."
                jump beg

        "Beg Carl":
            ji "Yeah, you're... you're gonna have to field this one."
    ji "While I could easily just... swallow my pride and do the guy a solid, my Dad is still president of the company, right? Which means, he'd own the keys to the joint. Which means, that if Julian's got the tape locked up in a safe, he'd be able to crank it open somehow."
    sa "But that doesn't make sense... if it's Julian's safe, why would your dad have a key?"
    ji "You underestimate how sneaky Carl Johnson McKay can be. He'd have a key. He'd have duplicates. He'd have triplicates."
    sa "Wow! I don't know what those words mean, but darn, that sounds impressive."
    ji "Exactly! Go nuts."

    jump askcarl

label askcarl:
    scene bg carl
    with fade

    show carl at topright with dissolve

    sa "Hey, huggie-bear, I kinda need your help!"

    show sandra at center with dissolve
    ca "What's wrong, darling?"

    sa "Oh, sweetie, it's just... you know that time we hid in Studio Number 3, and um... I gave you 'The Octopus?'"

    ca "Oh, heheh, I remember the Octopus quite well. What about it, honey-bunch?"

    sa "See, um, one of the cameramen... kind of filmed us doing it."

    ca "Oh, that won't do at all! Which one was it? I'll put the fear of God into 'em, I will! They won't be able to find work from here to Tinseltown when I'm through!"

    sa "That's the thing, honey, I don't know! All I know is that Julian's got his hand on the tape, and--"

    ca "Why, that snake! I'll get 'im, I'll shove my foot so far up his ass that his breath'll smell like old socks for weeks!"

    sa "Oh, no! Don't do that, I mean, won't he just release the tape?"

    ca "Right, right. Julian's a smart sonuvabitch, he'd have multiples."

    sa "Duplicates! Triplicates!"

    ca "Exactly right! Quadruplicates! Octublicates!"

    sa "Making up words is fun!"

    ca "Don't worry, hon, I'll get in there, I'll take all those copies, and I'll... I'll keep 'em for our... private-time."

    sa "Aaaactually, maybe it'd be safer to just... y'know, destroy them. That'd work, too. Like, just give 'em a good stamping."

    scene black

    if blackmail:
       scene bg beerint
       with fade

       play sound "SMS.wav"

       show phone at topright with dissolve

       ji "Uh-oh, what's this...?"
       stxt "problem. tape not in safe - s."
       ji "FUCK."
       jump burnbabyburn
    else:
       jump andreasidewalk


label burnbabyburn:

    scene bg broadoff
    with fade

    scene bg safe
    with fade

    show sandra at center with dissolve
    show carl at topright with dissolve

    sa "Well, wh-what if that wasn't the only safe? What if there's a secret safe?"

    ca "Aw, son of a bitch. I durn knew Julian'd be one step ahead of us."

    hide carl with dissolve

    play sound "SMS.wav"

    show phone at topright with dissolve

    jtxt "wait wtf do u mean its not in safe"
    stxt "not in safe! safes empty!"

    play sound "SMS.wav"

    jtxt "well maybe its not in safe keep looking"

    sa "Hey, um, maybe it's not in the safe! Maybe we should just keep looking through the studio...?"

    hide phone with dissolve

    show carl at topright with dissolve
    ca "Are you crazy? I know for damn sure that Julian's a crazy enough sumbitch to air that shit, so if we don't find it soon, who knows what's gonna happen!"
    sa "Okay, okay!"

    play sound "SMS.wav"

    hide carl with dissolve

    show phone at topright with dissolve

    jtxt "look i dont care if u set the whole studio on fire, just find the goddamn tape! LOOK DAMMIT!!!!"

    sa "Hey, um, huggie-bear?"

    ca "Yeah? What is it, darling?"

    hide sandra with dissolve
    hide phone with dissolve
    scene black

    sa "How's our fire insurance?"

    play sound "Match_lit.wav"

    "THE END"



    return





