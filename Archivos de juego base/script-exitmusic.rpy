label script_exitmusic:
    stop music

    scene black
    $ renpy.pause(delay=2.0, hard=True)
    show flashcard with Dissolve(1.0)
    pause 5

    $ quick_menu = False
    scene black
    show monday
    with dissolve_scene_half
    $ renpy.pause(delay=2.0, hard=True)
    $ quick_menu = True

    scene bg residential_day
    with dissolve_scene_full

    "It's the day of the festival."
    "Of all days, I expected this to be the one where I'd be walking to school with Sayori."
    "But Sayori isn't answering her phone."
    "I consider going to her house to wake her up."
    "It's not a big deal to at least wait for her, or help her wake up."
    "Even the simple gesture of walking her to school makes her really happy."
    "Besides..."
    "I told her yesterday that things will be the same as they always have been."
    "That's all she needs, and what I want to give her."
    "The hell with it. I’ll go get her."
    "I grab the cupcakes Natsuki and I made yesterday, and make my way to Sayori’s."
    scene bg house with wipeleft
    "I reach Sayori's house and knock on the door."
    "I don't expect an answer, since she's not picking up her phone, either."
    "Like yesterday, I open the door and let myself in."
    scene black with wipeleft
    "She really is a heavy sleeper..."
    "I swallow."
    "I can't believe I ended up doing this after all."
    "Waking her up in her own house..."
    "Isn't that more like something a boyfriend would do?"
    "In any case..."
    "It just feels right."
    "Outside Sayori's room, I knock on her door."
    mc "Sayori?"
    mc "Wake up, dummy..."
    "There's no response."
    "I really didn't want to have to enter her room like this..."
    "Isn't it kind of a breach of privacy?"
    "But she really leaves me no choice."
    "I gently open the door."
    mc "Sayo--{nw}"
    scene bg sayori_bedroom
    show sayori 2cm zorder 1 at i11
    play music yawa
    mc "...ri?!"
    s "[player]?!"
    "Sayori stands at the foot of her bed, a long rope in her hand."
    "It’s tied into a hangman’s noose."
    "In the shock of the moment, I release my grip on the cupcakes."
    mc "What the {i}fuck?!{/i}"
    s 2cv "It- it's not what it--"
    mc "Like hell it’s not what it looks like!"
    s 2cw "I-I’m so sorry, [player]!"
    "I can’t believe this."
    "Sayori wouldn’t do something like this..."
    mc "Jesus-... Sayori..."
    mc "I should’ve known it was this bad."
    "Sayori drops the noose to the floor."
    show sayori 1cu zorder 1 at t11
    mc "Sayori..."
    mc "Why haven't you talked to anybody about this?"
    s "I-I don't want to waste people's time..."
    mc "You're not wasting anybody's time."
    mc "We all just want you to be happy, like you've made us."
    mc "You... you really deserve to be happy."
    mc "I know you don't think that now, but..."
    mc "Well, it's the truth."
    mc "And I'm determined to help you every step of the way."
    mc "But to start, you {i}need{/i} to talk about this."
    s 1cv "I..."
    s "I can't."
    s "I just..."
    "There is a short pause."
    "All is silent, aside from Sayori’s sobbing."
    s "I... I was about to do it, [player]..."
    s 1cw "I’d have never seen you again."
    mc "Sayori... could you imagine if I’d found you like that?"
    s 1cv "I-I-I..."
    mc "Sayori, listen. It doesn’t matter what you are going through, you’ll always have a reason to stay with us."
    mc "Even if there’s only one thing worth living for to you, then you need to hold onto that."
    mc "And I know there is."
    mc "You told me yourself yesterday."
    s 1cu "[player]..."
    "She releases her grip on me and backs away."
    mc "We know it'll be tough, but I’ll be there for you."
    mc "We all will."
    mc "No matter what."
    s 4cu "[player], don't..."
    mc "Now, listen to me. You need to talk to somebody professional about this."
    mc "I'm not taking 'no' for an answer, Sayori."
    s "I don't think I-I'm ready..."
    s "W-we can go another time."
    mc "Not a chance."
    mc "You seriously need professional help, as soon as possible."
    mc "We're leaving {i}now{/i}."
    s "I... I don't-... I don't know if I can..."
    mc "Sayori, do it..."
    mc "For me, if not for yourself."
    "She sniffles, wiping her face with her sleeve."
    s 1ck "O-okay.."
    mc "Come on, let’s go."
    mc "To the doctor's."
    mc "We'll take the bus."
    s "[player]..."
    s "The festival..."
    mc "Screw the festival."
    mc "You're more important to me than that."
    s "W-well..."
    s 1ch "I-I need to get changed first."
    mc "Oh!"
    mc "Of course..."
    "I nod, and take a step outside the door, reaching down to pick up the rope first, taking it with me just in case."
    "She gently nods, shutting the door in my face."
    scene black with wipeleft
    "I’m a little anxious, leaving her alone right after... something like {i}this{/i}."
    "Regardless, she needs her privacy."
    "I kneel down, beginning to clean up the cupcake massacre littering the floor with a towel."
    "Natsuki is going to kill me."
    "I return downstairs and untie the noose, dropping the loose rope in the trash."
    "I linger downstairs for a minute or two, before heading back upstairs."
    "{i}She's probably ready by now.{/i}"
    "I knock on Sayori's door, and she answers."
    scene bg sayori_bedroom with wipeleft
    show sayori 3bk zorder 1 at t11
    mc "Ready?"
    "Sayori nods once, her eyes glued to the floor."
    s 1bg "T-this is what’s best for me, right?"
    "She stares at me, expectant of an answer."
    "I feel uneasy, but answer anyway."
    mc "I know it is."
    mc "Come on now, let’s get going."

    scene black
    with Dissolve(1.0)
    stop music fadeout 2.0

    scene bg hospital
    with dissolve_scene_full
    play music tinkertailor

    "I’m sitting down in a waiting room outside of the doctor’s office, patiently waiting for Sayori to return."
    "I’m anxious."
    "My phone buzzes quietly."
    "I remember that today was supposed to be the day of the festival."
    "The text is from Monika."

    m "where are you??"

    "I have to reply."

    mc "I’m busy."
    m "really [player] please don’t tell me you’ve got cold feet about the poems or something"
    mc "It’s a bit more serious than that."
    m "whats going on?"
    mc "I don’t know if I can tell you right now."
    mc "But it’s serious, okay? You gotta believe me."
    m "fine"
    m "just hurry up & bring sayori with you"

    "I look up at the door."
    "Through the small window, I can see Sayori breaking down in her chair, her head resting on the doctor’s desk."
    "I feel terrible, knowing that I let her reach such a point due to my own negligence."
    "Behind me, the door that leads from the entrance to my waiting room swings open, and a couple of nurses walk by."
    "But my phone buzzes again in my hand, and I turn my attention back to it."

    m "its just me and yuri here damnit"
    mc "Why? Where’s Natsuki?"
    m "idk, please get here quick and bring sayori ok??"
    mc "It’s a personal issue. I can’t promise anything but I’ll try to get to the festival before it’s over, okay?"
    m "ok"

    "A couple of minutes of idle waiting pass before I get another message from her."

    m "forget it, everyones here already and theyre waiting"
    m "we have to cancel"

    "I return the phone to my pocket, running my hands through my hair."
    "Why now?"
    "I feel terrible for Sayori, the fact that she’s in such pain right now and how oblivious I was to all of it."
    "But on the other hand, I also feel like I’ve put Monika and Yuri on the spot in front of all of our classmates."
    "Monika and Yuri..."
    "That reminds me of something that Monika told me."
    "Where {i}is{/i} Natsuki?"
    "Suddenly, the door to the waiting room opens again, and another nurse walks by. However, she’s accompanied by somebody familiar..."
    show natsuki 1bba zorder 1 at t11
    n "..."
    mc "Natsuki? Are you... okay?"
    n 1bbb "......{nw}"
    n 1bbc "......{nw}"
    n 1bbd "......{nw}"
    show natsuki at lhide
    hide natsuki
    "She quickly turns and runs back the way she came, exiting the hospital in tears."
    "I jump out of my seat to speak to her, but I notice the nurse staring at me suspiciously."
    "I take a seat once more, anxious now about Natsuki’s wellbeing as well as Sayori’s."
    mc "Uh... excuse me?"
    mc "What... happened to her?"
    "She explains how Natsuki wandered into the hospital, bloody and bruised, looking for help."
    "Poor Natsuki."
    "She then cautiously asks if I had anything to do with Natsuki’s injuries."
    mc "Christ, no!"
    mc "I don’t even know what’s going on!"
    mc "I had to bring my friend here, she tried to-"
    "I stop myself."
    "I doubt Sayori would want me to talk about her struggle so openly."
    "Not now, anyway."
    mc "Well-.. listen, it’s serious, okay?"
    "I bite my lip as the nurse continues on her way."
    "My phone buzzes again."
    m "are u sure u don’t know where sayori or natsuki are?"
    mc "I already told you, I don’t know."
    "I can’t tell her about Natsuki either."
    "Chances are, it’s her own personal issue and she’d deal with it in her own way."
    "Still..."
    "Maybe I should text her."
    m "it doesnt matter anyway"
    m "we had to cancel our performance"
    m "ppl are complaining about the cupcakes not being here"
    m "yuris gone for some fresh air"
    mc "Jesus, I’m sorry, okay?"
    mc "My hands are tied here, I can’t do anything to help right now!"
    m "K. whatever"
    m "thanks a lot [player]"
    "I sigh."
    "Now I’ve pissed Monika off because I couldn’t bring myself to tell her what happened."
    "I decide to text Natsuki quickly about what I just saw."
    "A couple of minutes pass with no response."
    "The message doesn't even mark as read."
    "The office door swings open, and Sayori emerges."
    show sayori 3bg zorder 1 at t11
    s "[player], are you okay?"
    mc "Not really. I’m just stressed out."
    mc "How are you?"
    s 3bh "I... I don’t really want to talk about it."
    mc "Are you sure?"
    mc "Because I’m here for you, I can just-"
    s "[player], please..."
    s 1bf "Can’t we just.. drop this?"
    s "I just don’t want to make a big deal out of it, especially in front of the other club members."
    "I stand up."
    mc "Sayori, I don’t think you understand how big of a deal this really is."
    mc "You nearly f-... you nearly killed yourself."
    mc "I think you should go home and rest for a couple days, okay?"
    s 1by "I guess I’ll have to, right? Ehehe~"
    "Sayori lets out a small bout of almost nervous laughter."
    mc "It’s a good idea, at least. You know that."
    s 2bk "But what about the festival?"
    "I hesitate."
    "I don’t want Sayori to feel like it’s her fault that the performance was cancelled, so I decide to start with Natsuki’s absence."
    mc "Well... Natsuki didn’t actually show up either."
    mc "Monika had to cancel the performance, unfortunately."
    s 2bj "You didn’t.. You didn’t tell her, did you?"
    s 2bi "About-"
    mc "I didn’t."
    mc "Unless you want to talk to her about it yourself, she won't know."
    mc "Okay?"
    "Sayori nods."
    s 1bf "I think I’ll tell her."
    s 3bk "So she knows why.. why her plans for the festival were ruined."
    "I can tell what she’s going to say."
    mc "It wasn’t your fault, Sayori."
    mc "None of this is."
    "Sayori grabs my hand tightly, crushing it in a vice-like grip."
    mc "You can talk to her if you really want to."
    mc "Hell, she’d probably be able to give better advice than me."
    s "Maybe..."
    s 3be "Did you... tell my parents?"
    "I sigh."
    mc "I did, yeah."
    mc "I’m sorry though, I felt like I had to and-"
    s 3bl "Thanks."
    s "I was scared I’d have to tell them myself."
    "Sayori glances downwards to the pristine floor."
    s 1bt "I love you, [player]."
    mc "I..."
    "Despite her condition, I can’t lie to her."
    "It would be unfair on her end to have her hopes disrupted like that."
    "I keep my mouth shut."
    show sayori 1bu zorder 1 at t11
    "A minute or so passes."
    show sayori 1bb zorder 1 at t11
    mc "Anyway, we should get going."
    mc "There’s no point going to school now."
    s 2bc "Why? What time is it?"
    mc "It’s about midday."
    mc "We missed the festival and if we turn up now, Monika’s just gonna get mad at us."
    mc "Come on, I’ll take you home."
    mc "We can talk some more there."
    "She gently nods, following my lead."
    "We exit the hospital and ride a bus back to her house."
    scene black with wipeleft
    "I decide to stay with Sayori in her house, just to make sure she’s feeling better."
    "We have at least a few hours together, but we spend that time talking and watching shows together."
    "Her mother arrives first, thanking me for letting her know of what happened. I tell her that it’s no problem."
    "She tells me that Sayori’s father is on his way, and that I’m free to leave if I want to."
    "After I’m sure she’s safe, I leave her with her mother and head home."
    scene bg kitchen with wipeleft
    "Entering the kitchen, I flick the light on and start to make myself a sandwich, cutting up a tomato."
    "However, I start to wonder about Natsuki."
    "I remember the time I spent with her here, our little scuffle over the cupcake’s icing..."
    "But that bruise, her nosebleed..."
    "What the hell happened to her?"
    "And who in their right mind would do that to her?"
    "Possible reasons for her injuries begin to circulate inside my head."
    "Maybe she just fell over?"
    "She could’ve gotten into a fight with another classmate of ours?"
    "Or maybe..."
    "{i}No.{/i}"
    "Surely not."
    "Maybe I’m just over-reacting to the situation. It’s been a rough day, after all."
    "But something she told me while we were reading manga together sticks in my head..."
    n "I don’t even know what my dad would do if he found this."
    "I shiver at the thought."
    "It’s the only real reason that I can come up with for Natsuki’s terrible injuries."
    "I also notice that while I was distracted, I'd accidentally cut my finger open while slicing the tomato."
    mc "Ah, crap."
    "I wrap my finger in a paper towel, letting the few drops of blood soak into it."
    "Throwing the paper towel in the trash, I think back to Natsuki."
    "I decide that I’ll ask her about her father, next time I see her."
    "Even if she assures me that I’m wrong, at least I’ll know."
    "I eat my sandwich and head upstairs to my room."
    scene bg bedroom with wipeleft
    "I collapse onto my bed, exhausted from the stress that the day had brought me."
    "I drift into unconsciousness within minutes."

    scene black
    with Dissolve(1.0)
    stop music fadeout 2.0

    $ quick_menu = False
    scene black
    show wednesday
    with dissolve_scene_half
    $ renpy.pause(delay=2.0, hard=True)
    $ quick_menu = True

    scene bg club_day
    with dissolve_scene_full
    play music t3

    show yuri 1a zorder 1 at t11
    y "O-oh! Hi, [player]!"
    show yuri at thide
    hide yuri
    "I’m back at the literature club."
    "Craning my neck, I look around the clubroom. It’s empty."
    "Yuri and I are the only people here."
    "I leave the classroom door open, expecting the other members to arrive shortly."
    mc "Hey, Yuri."
    show yuri 1s zorder 1 at t11
    "I sit down on the desk next to her, unpacking my stationery kit as she did with her own."
    mc "Listen, I know that Monika cancelled the club yesterday so I didn’t get a chance to talk to you..."
    mc "So I just wanted to say that I’m sorry that she had to let our little presentations go."
    y "D-don’t worry about it, [player]."
    y 1v "Monika told me that it wasn’t your fault you couldn’t come."
    y "She said it was something serious."
    mc "Yeah. It was a bit of an emergency."
    "I decide to play down the situation, in case Yuri doesn’t know the full story."
    "I don’t want to worry her, after all."
    y 2t "Are you... alright?"
    mc "Me? I’m fine, don’t worry about me."
    mc "It was someone else."
    mc "Someone... close."
    y 2g "I see."
    y 1g "Well, I-I hope everything works out well for you, and your friend."
    mc "I hope so too, Yuri."
    show yuri zorder 1 at thide
    "A moment passes, of complete silence. Yuri is sat down in her desk, still reading."
    "The class is still empty, aside from us."
    mc "So, uh, Yuri..?"
    show yuri 2n zorder 1 at h11
    "Yuri jumps in her chair a little, startled by my interrupting the silence."
    y "Y-yes?"
    mc "You haven’t seen Monika today, have you?"
    y 2o "I-I’m afraid not, [player]. She’s been in a mood since the festival, unfortunately."
    y "N-not that I mean to be so rude about it! I-it did mean a lot to her, after all..."
    mc "I know it did."
    mc "That was why I wanted to speak to her."
    "Maybe if I explained why Sayori and I were absent, then she might forgive me."
    "Well, the both of us."
    "But I promised Sayori I wouldn’t say anything to Monika..."
    mc "Has she..."
    mc "Has Monika said anything about me since the festival?"
    y 1h "N-not really..."
    y 2h "I mean, she did complain that the three of you were gone."
    y "I was kind of thankful that we got to cancel..."
    y 2p "Not to ruin Monika’s plans, though! I-I’d never do such a thing, intentionally!"
    mc "I know you wouldn’t, Yuri. Don’t worry."
    mc "I can tell you’re too good a person to be so mean."
    mc "Besides, you have no reason to want to sabotage her like that."
    mc "Right?"
    "Yuri falters for a moment, lost for words."
    y 3v "N-not at all!"
    y "It’s just that..."
    y 4b "{i}I don’t even know if I should be telling you this...{/i}"
    y 4d "Well, I overheard Monika talking about you and Sayori to one of her friends."
    y 4c "I-I wasn’t eavesdropping, though!"
    mc "What did she say?"
    y 2f "I heard her mention that the only good reason to cancel on her festival was if... somebody died."
    "What?"
    "Monika wouldn’t say something like that, right?"
    "She’s a sweetheart."
    "Besides, not only is it egocentric..."
    "It’s insensitive."
    "Even if she didn’t know about Sayori, it felt like it was too close to reality."
    mc "Wow, that’s harsh."
    y 3t "I doubt she meant it, though!"
    y 2t "What I mean to say is, she was in no position to say that."
    y 2h "I understand that she was frustrated about it, but there's never a good reason to say such horrible things about-"
    show yuri 4c zorder 1 at t11
    "Yuri’s words get caught in her throat, and she retreats to the confines of her book."
    "I turn and see Monika standing in the doorway, giving Yuri an intense glare."
    "She doesn’t dare to meet Monika’s gaze, instead concentrating on the Portrait of Markov."
    "I wish I could do the same."
    "I swallow."
    "She huffs, and starts talking."
    show monika 1i zorder 1 at t21
    show yuri 4c zorder 2 at t22
    m "Where’s Sayori? And Natsuki?"
    "She stares at Yuri intently."
    "Monika’s presence intimidates me."
    mc "I-I don’t know, Monika."
    mc "I haven’t seen them."
    show monika 1h zorder 1 at t21
    "She gives me an acidic stare, her emerald eyes piercing my confident facade."
    "Did Sayori tell her about the hospital?"
    m "Are you sure?"
    mc "I... yeah."
    m "..."
    m 1d "Alright then. How come you weren’t at the festival, [player]?"
    mc "I had a... family emergency."
    "At this point I’m practically lying to her face to keep Sayori’s secret safe until she feels comfortable confiding in Monika."
    "Then again, I’ve known Sayori for so long, she’s pretty much a part of my chosen family at this point."
    "She’s like a sister to me."
    "So it’s more ‘stretching the truth’ than it is lying to her."
    "Well, that’s what I’ll tell myself, anyway."
    m 2h "Right..."
    "Monika is not having any of this."
    "Even if she doesn’t know what’s actually going on, she must know I’m lying to her."
    "But for Sayori's sake I have to keep face for her. I can’t betray her trust. If she finds out I told someone that private information..."
    "Monika’s demeanor suddenly changes, and she looks at the two of us with a wry smile on her face."
    m 2k "Okay, you two!"
    m 2b "Since we’re the only ones here, I’ve decided that we’re going to have to cancel today’s meeting. Hopefully, there won’t be any more {i}emergencies{/i} or {i}absences{/i} tomorrow."
    "The emphasis on those words worry me, due to how aggressively she spoke them."
    m 2i "That’s all. You can leave now."
    "Yuri looks up from her book guiltily and packs up, silently dropping the Portrait of Markov and her stationery kit into her bag."
    "She scurries out of the classroom without a word."
    show yuri zorder 0 at thide
    hide yuri
    show monika zorder 1 at t11
    "Monika turns her attention to me, expecting me to pack up."
    "I nod and pick up my bag, exiting into the hallway without another word."
    stop music fadeout (1.0)
    show monika zorder 0 at thide
    scene bg corridor with wipeleft
    play music t5
    "Walking through the school’s dormant hallways, I reach the door to the courtyard but stop, placing my head in my palm."
    "I forgot my own stationery. I’m an idiot."
    scene bg club_day with wipeleft
    "I return to the clubroom hastily, to find my leather pencil-case opened."
    "As I swipe it into my bag, I realize my pen is missing."
    "A quick glance around, and I conclude that I must have lost it earlier."
    "Returning to the courtyard, I notice Yuri."
    scene bg courtyard with wipeleft
    "She’s moving hurriedly, clutching her bag tightly against her chest and wiping her face with her sleeve."
    mc "Yuri?"
    "She doesn’t notice me at first, so I jog to catch up to her."
    stop music fadeout (1.0)
    show yuri 5c zorder 1 at t11
    mc "Yuri? What’s wrong?"
    play music t9
    y "O-oh h-h-hi, i-it's n-nothing."
    mc "Really?"
    y 5b "Y-yeah. I-I-I’m a-al-alright, really."
    "I don’t believe her."
    "My eyes meet Yuri's for a brief moment before she looks away. I can tell something terrible happened in the few minutes we were separated, but what could have brought her to this state?"
    "I take hold of her shoulder to try and slow her down, so she can face me."
    show yuri 5h zorder 1 at h11
    "She jumps, but complies as she comes to a halt at the school’s entrance."
    mc "Yuri... Whatever’s on your mind, you can tell me."
    mc "I am your friend, after all."
    y 5e "I-it’s not m-m-much... it w-was just some-thing that M-M-Monika said..."
    "Monika..."
    "What could she have said?"
    mc "Well, if you don’t mind my asking..."
    mc "What did she say?"
    y 5a "I... I-I don’t r-really feel c-comfortable... talking about i-it..."
    y "If... you’re okay... with that..."
    "Monika must have said something really hurtful."
    mc "It’s fine, really. I understand."
    y "Well, if you’re s-sure about that."
    mc "You’re always welcome to talk to me, though."
    y 5c "I-I guess... it’d be nice if you... walked w-with me."
    y "M-maybe we c-can talk on th-the way..."
    "Sayori isn’t here, and I’ve got some time to kill."
    "Besides, I feel like I can’t refuse."
    "Not when she’s so emotional."
    mc "Yeah, okay."
    mc "I’m sure that’d be nice."
    scene bg street with wipeleft
    "Following Yuri, I take the opposite turn from my usual walk home."
    "Soon enough, I find myself in a part of our town that I rarely visit."
    "The walk between us is mostly silent."
    "Yuri occasionally sniffles, wiping at her face."
    "What the hell did Monika say to her?"
    "I decide to make some light conversation. Something about writing might be nice. She does take comfort in talking about subjects she’s passionate about, after all."
    show yuri 5b zorder 0 at t11
    y "S-so, [player]... how do you l-like writing poems?"
    "She must have read my mind."
    mc "Well, I usually like to listen to music while I write."
    mc "Even if it’s just quiet, playing softly in the background, you know what I mean?"
    y 5c "R-really?"
    y "Most of the time, I just feel like I can only write in silence."
    y 4b "It leaves me at one with my mind, and lets me express my inner thoughts."
    y "Though sometimes, I do like listening to a soft piano track."
    y 2h "Don’t the lyrics alter the way you write?"
    mc "Well, yeah, but I guess that’s what I’m looking for. Most of the time, anyway."
    mc "I like for the mood of the music to affect the way I write, really."
    mc "Unless it’s something I’m especially passionate about. Then I can write in just about any condition."
    y 2v "That... actually sounds like an effective technique."
    y "I’ll be sure to try it out."
    "At this point, Yuri seems to have perked up, her eyes dried."
    "I decide to continue the conversation, as I still don’t know how much longer it’ll take to reach her house."
    mc "I know Sayori likes to hum a little tune to herself while she writes.."
    mc "I wonder what Natsuki does."
    "Natsuki..."
    "I’ve been trying to contact her since I saw her in the hospital, but she hasn’t responded to my messages."
    "She hasn’t showed up for school at all this week, either."
    "God, what could’ve happened?"
    "Was it really... her father?"
    show yuri zorder 0 at thide
    hide yuri
    stop music fadeout (2.0)
    "I don’t want to believe it, but the pieces fit together."
    "Her absence..."
    "Her inability to contact anybody..."
    "What she said about him..."
    "But most of all..."
    "{i}The bruises.{/i}"
    "I bite my lip, as I feel my breathing growing heavy, and my blood reaching a boiling point."
    "If I find out he laid a finger on her, I’ll..."
    "I’ll..."
    show yuri 2i zorder 0 at t11
    play music t9
    y "...so I’ll be honest, I don’t disrespect her or anything."
    "Yuri’s words derail my train of thought."
    y "Natsuki's poems are just a little too... simple for my liking."
    y 2j "I suppose they lack a certain edge."
    "I spaced out... again."
    mc "Yeah..."
    y 1f "Speaking of Natsuki, however..."
    y "I think we just passed her house, then."
    "We... {i}what?{/i}"
    mc "Wait, which one?!"
    "Yuri looks at me, a little surprised by my urgency."
    "Regardless, she points out the house to me."
    scene bg nhome with wipeleft
    show yuri 3h zorder 1 at t11
    y "It’s... that house, if I recall correctly."
    mc "Right, thanks for that."
    y 3t "Why do you need to know?"
    "I don’t really want to worry Yuri about Natsuki."
    mc "Well, I guess I just wanted.. to..."
    y "Right."
    "The rest of the journey is made in silence."
    "I worry that Yuri got the wrong impression, but there’s not much I can do."
    "Eventually, we arrive, signalling her wave goodbye."
    scene bg street with wipeleft
    show yuri 1y6 zorder 1 at t11
    stop music fadeout (1.0)
    y "You know, [player], you’re quite... different when no one's around."
    play music t10
    y 1y5 "When it’s just... the two of us."
    "Yuri falls silent for a moment, lost in thought."
    mc "Listen, I’d love to stay and talk - I-I really would - but I-"
    y 3p "O-oh!"
    y "I-it’s fine... I get it..."
    y 4b "You have {i}places{/i} to be..."
    "Her head darts towards the direction of Natsuki’s house for a moment."
    y "It’s fine, I’ve got some writing to do anyway."
    "She turns and starts to walk to the door."
    mc "No, please don’t get the wrong idea, Yuri, I’m not really..."
    y 5a "It's fine, [player]. I can take a hint. I'll see you tomorrow."
    show yuri at thide
    hide yuri
    "Before I can finish my explanation, she’s already entered her house."
    "I feel terrible, knowing that Yuri probably blames herself for my rejection."
    "But I leave quickly regardless."
    stop music fadeout (1.0)
    scene bg nhome with wipeleft
    "As I turn the corner and approach Natsuki’s house, my attention is directed upwards."
    "On the second floor balcony, a large, heavily built man leans against the railing, smoking a cigarette."
    "Is that her dad?"
    "{i}Jesus Christ...{/i}"
    "He’s on the phone, and I can’t help but overhear his conversation."
    "The man mutters something about having {i}business{/i} to attend to, but promises to be wherever the caller wants within the hour."
    "My stomach sinks."
    "{i}Business?{/i}"
    "If he means what I think he does..."
    "Back-tracking Yuri's route, I make my way back to school, then to my house from there."
    scene bg house with wipeleft
    "Fumbling with my keys, I unlock the door."
    scene bg bedroom with wipeleft
    "I enter my bedroom and hurriedly get changed out of my uniform, and into some dark clothing."

    scene black
    with dissolve_scene_full
    stop music fadeout 2.0

    scene bg nhomen
    with dissolve_scene_full

    "A short jog brings me back to her house, and I take a seat within a bus stop on the street opposite her, staking out her father."
    "I ponder over if he’s already gone, perhaps, and I missed him leaving."
    "Or maybe he’s still dealing with ‘business’..."
    "After a few minutes, however, I’m proven wrong by the sound of an engine revving up and a new, expensive-looking performance car emerging from the driveway of Natsuki’s house."
    "It speeds away and around the corner within seconds, and once I’m certain that it’s gone, I move over to Natsuki’s house and ring the doorbell."
    "I wait."
    "Nothing."
    "I press down on it again."
    "Once more, no answer."
    "Growing ever-anxious, I knock on the door heavily, aggressively banging my balled fist into the door."
    "A moment of silence."
    "Then from a second floor window, I see a curtain pull back, a flash of pink, and just as quickly, it’s replaced once more."
    "I watch it intensely, waiting for any sign of movement until I hear the sound of the door chain being unhinged and the deadbolt turning."
    "My heart is ready to jump out of my chest. I don’t know what I'll be greeted by, but I await it nervously."
    show natsuki 5bc zorder 1 at t11
    n "[player]?! Wh-what the hell are you d-doing here?"
    "It’s Natsuki."
    "Thank God."
    mc "Natsuki! Are you alright?"
    mc "What happened... to your bruises?"
    n 5bn "Wh... what bruises, [player]?"
    n 5bm "I-I don’t know what you’re talking about, ehehe~"
    "She’s playing dumb, even though I saw her."
    "What could have happened to her, for her to be so devoted to keeping it a secret?"
    "Before I can reply, she grabs me by the collar of my shirt and yanks me into her foyer."
    scene bg hallwayn with wipeleft
    show natsuki 1bq zorder 1 at t11
    n "H-ey..."
    n 1bu "H-how do you ~hic~ know where I live?"
    mc "Now’s not the time for that."
    "Has she been drinking?"
    mc "Better question is, where have you been?"
    n 2bb "I-I haven't been feeling very g-good the past few days..."
    n 2bg "No need to be so... mean... about it..."
    "Does she expect me to believe that, after what I saw?"
    mc "Natsuki, I know something’s wrong."
    mc "I saw you at the hospital, remember?"
    n "Oh, t-that?"
    "She giggles."
    n 1bz "That... that was nothing."
    n 1bt "Don’t worry about... about that, okay?"
    n 1bk "There’s much... worse to be worried about, ~hic~"
    mc "What do you mean?"
    n "C-come with me..."
    n 2bs "{i}I could do with another glass anyway...{/i}"
    "She grips my arm loosely, and tries to move me along with her, through her house."
    "As she moves, she begins erratically wobbling, as though she’s having trouble walking."
    "She holds tighter onto my arm for support."
    "She stumbles and nearly trips. I catch her, wrapping my arm around her chest and pulling her upright."
    n 1bj "Ehehe, thanks..."
    "That’s not like her."
    "Normally if I grabbed her, for whatever reason, she’d freak out and call me ‘gross’ or something of that sort."
    "But here, she didn’t even flinch or say anything about it."
    "Something feels off."
    "I release my grip on her reluctantly, as she’s still staggering her way along."
    "I assist in moving her, now up the stairs, making sure she doesn’t fall and knock us both back onto the steps."
    "We finally make it up the stairs, and Natsuki guides me to her room."
    scene bg nbedroomn with wipeleft
    "Her room is a mess."
    "Her floor is littered with small, ripped up pieces of paper."
    "Picking one up, I recognize one of the protagonists of Parfait Girls."
    "The cover is a heavy laminated card stock, and it’s ripped in two."
    "There is no way Natsuki was able to tear that in half, herself."
    "Not only that, but she had no reason to, either."
    "But I could think of someone who does..."
    "There is a large bottle of red wine, cap opened, lying on its side on her bed."
    "Only a small drip escapes, staining her bedsheet crimson."
    "There can’t be much left of it."
    "I knew she’d been drinking. I could tell from the moment she opened the door."
    show natsuki 4bp zorder 1 at t11
    mc "Natsuki... you haven’t drunk all of that yourself, right?"
    "She looks flustered."
    n 4bp "Of course I have, you dummy."
    mc "That’s a bit much, isn’t it?"
    n 3bq "Ehhh, that... doesn’t matter."
    n "I haven’t even finished, anyway."
    "She retrieves the bottle from the bed."
    "I reach a hand out to take it from her."
    mc "Natsuki-"
    n 5bf "Nuh-uh, it’s mine."
    "She holds the bottle just out of reach, and tries to push me away."
    "She’s too weak, however and I simply move her arm aside."
    mc "Come on, that’s enough."
    n "Ehe, [player], please?"
    n 2be "I need this."
    "Something about the way she said that sent a pang of dread through my body."
    "Before I can reach my arm out to stop her a second time, the remainder of the bottle’s contents are gone."
    "Looking at her bedside drawer, I see Natsuki’s phone."
    "It is overturned, so I can only see her case."
    "The case is glittery and pink."
    n 2ba "This... ~hic~, drink is nice, [player]."
    mc "Natsuki..."
    mc "Talk to me."
    mc "I know something's going on with your dad."
    mc "Please, I just want to help. "
    mc "But I can’t if you won’t tell me what’s going on."
    n 1bj "This is all the help I need..."
    "She collapses onto her bed, and giggles."
    n "I haven't felt this happy... in so... so long..."
    show natsuki zorder 0 at thide
    hide natsuki
    "I grow only more uneasy, hearing that."
    "If this is the length she has to go to in order to escape her demon..."
    "Just how bad is the demon she’s trying to escape from?"
    "As Natsuki begins to snore, her grip on the wine bottle falters, and it rolls off of the bed onto her floor."
    "To my surprise, it doesn’t shatter."
    "Instead, it rolls under her bed."
    "Shaking my head, I bend down to pick up the bottle that rolled under her bed."
    "Reaching my hand underneath the bed, I can feel the wine bottle."
    "And something else."
    mc "What the..?"
    "I pull both from beneath the bed."
    "Placing the wine bottle on her bedside drawer, next to Natsuki’s phone, I take a look at what I recovered."
    "It’s a white container, and made of plastic."
    "Wait, this isn’t right."
    "This is a bottle of pills. Looking for a description, I inhale sharply as I realize that these are ibuprofen tablets."
    "I turn to look at Natsuki. Fast asleep, as I worried."
    mc "Oh my fucking God."
    "I desperately check the label on the back for a date of prescription."
    "Two..."
    "Two days ago."
    play music fulstop
    "She’s trying to overdose."
    "An icy sweat runs down my forehead as I begin to panic, running my hands through my hair."
    "She’s stopped snoring."
    "I violently shake Natsuki's seemingly lifeless body."
    mc "Please, Natsuki..."
    mc "Please wake up..."
    "I grab her hand. It's clammy, and much cooler than it should be."
    "I put my ear next to her mouth, to check and see if she's breathing."
    "Thankfully she is, but it’s faint."
    "I take her by the shoulders, and pull her into a sitting position."
    "I crouch down next to her, supporting her."
    mc "Natsuki..."
    show natsuki 1od zorder 1 at t11
    "I contemplate calling an ambulance, but I'm worried that it'll draw too much attention to her house."
    "The hell with it."
    "I don’t care what happens so long as she lives."
    "I reach into my pocket and..."
    "Fuck."
    "FUCK!"
    "My phone isn’t there."
    show natsuki 2od zorder 1 at t11
    "I reach up onto her bedside table, gripping Natsuki’s phone tightly."
    "I bring it to my face, and press the power button."
    "The screen lights up, but from behind a shattered display."
    show natsuki 1od zorder 1 at t11
    "I try to make an emergency call, but the screen is unresponsive to my touch."
    show natsuki 2od zorder 1 at t11
    "Dropping the phone, I pull Natsuki in close to me, hoping, praying that she wakes up."
    show natsuki 1od zorder 1 at t11
    "I begin to sob, terrified for her life."
    "But Natsuki begins to cough erratically. I’m simultaneously panicked and relieved."
    show natsuki 2od zorder 1 at t11
    "She opens her eyes, and unsteadily rises to her feet, with my assistance."
    mc "N-Natsuki? Please... tell me you’re okay."
    n "I... I..."
    "She falls silent."
    pause 1.0
    show natsuki 2od at h11
    pause 0.75
    show natsuki vomitb at h11
    pause 1.25
    show natsuki at thide
    hide natsuki
    mc "Jesus!"
    "My nose is assaulted by the mixed scent of bile and wine, as it splashes on the floor in front of me."
    "I realize that she got some on my arm."
    "It.. it stings?"
    "Well, at least that would have gotten the deadly mixture out of her body."
    "But she's still in trouble..."
    "Natsuki turns to me, half-conscious, pleading."
    show natsuki 2od zorder 1 at t11
    n "[player]... h-help me..."
    "She stumbles back, landing in a sitting position on her bed."
    n 1od "I... I don’t... wanna d-die..."
    mc "Look at me, okay?"
    mc "You won’t, you hear me?"
    mc "I won’t let you die."
    mc "Natsuki, listen to me, okay?"
    mc "I'll be right back."
    "She nods weakly, barely aware of her surroundings."
    show natsuki at thide
    hide natsuki
    "I need to find her something to eat. Hopefully, it should absorb what’s left of the alcohol."
    "Bolting down the stairs, I reach the kitchen within seconds."
    scene black with wipeleft
    "I swing open every cupboard I can see, along with the refrigerator."
    "Nothing."
    "Not even a slice of bread."
    "When did Natsuki last eat?"
    "Exiting the kitchen, I look all around the house."
    "Hurrying back to Natsuki, I check up on her."
    scene bg nbedroomn with wipeleft
    "She’s as pale as ever, but she’s conscious, at least."
    "She weakly raises her head to look at me. "
    show natsuki 2od zorder 1 at t11
    mc "Hey, hey, Natsuki?"
    mc "I need you to pay attention to me, okay?"
    mc "Just, whatever you do, don’t go to sleep, okay?!"
    mc "Please!"
    n "..."
    "She tries to mutter something, but it’s unintelligible. I have no choice but to leave her again."
    scene bg hallwayn with wipeleft
    "I’ve searched everywhere in the house, besides her father's bedroom."
    "As I approach the door I notice that it’s locked."
    "I ram the door multiple times before the frame gives way."
    mc "Whoa!"
    scene black with wipeleft
    "I tumble onto the floor, now littered with splinters."
    "I rise to my feet and flick the light on."
    "As I search the room for anything that could possibly aid Natsuki, something catches my eye."
    "A few bags from various restaurants around town."
    "I tear them open, to find nothing but empty take-out containers..."
    scene bg nbedroomn with wipeleft
    "I return to Natsuki’s room."
    mc "We have to go. Now..."
    show natsuki 2od zorder 1 at t11
    n "O-okay..."
    "I help her to her feet, wrapping her arm over my shoulder, holding her hand in place."
    show natsuki 1od zorder 1 at t11
    "She’ll make it."
    show natsuki 2od zorder 1 at t11
    "I’ll make sure of it."
    n "W-where are w-we.. going...?"
    mc "Somewhere safe."
    scene bg hallwayn with wipeleft
    show natsuki 2od zorder 1 at t11
    "We make our way down the stairs. I keep Natsuki on her feet, though it is proving to be more difficult as she fades in and out of consciousness."
    "Starvation, mixed with alcohol, and painkillers..."
    show natsuki 1od zorder 1 at t11
    "It’s clearly taken a toll on her."
    "But she isn’t dead."
    "We make it to the front door."
    show natsuki 2od zorder 1 at t11
    "With time feeling like a lost luxury, I shut it behind us, moving through the porch."
    scene bg nhomen with wipeleft
    show natsuki 2od zorder 1 at t11
    "I can feel Natsuki’s tears soak through my shirt."
    "We reach the gate and I set her down while I open it."
    "I scoop Natsuki off the grass and close the gate behind us."
    show natsuki 1od zorder 1 at t11
    "Holding Natsuki close, I move as fast as I can down the street."
    scene bg streetn with wipeleft
    show natsuki 2od zorder 1 at t11
    "As we approach the glow of the street lights I begin to feel relieved."
    "I loosen my grip on Natsuki."
    mc "Can you walk?"
    n 12bh "Y-yes..."
    n "I... I t-think..."
    "I set her down for a moment."
    "Her knees buckle. Again I wrap her arm around me, and mine around her."
    mc "Let’s go."
    n "O-okay..."
    "I end up supporting her the entire way through town."
    show natsuki at thide
    hide natsuki
    "There is nobody about to call me out for looking suspicious."
    "I'm almost glad she has such a small figure. It certainly makes it so much easier to..."
    "That's why she's so small."
    "Her father has been leaving her malnourished, and living on fast food."
    "Jesus Christ."
    "Finally, I recognize the familiar view of my house."
    stop music fadeout 5.0
    scene bg housen with wipeleft
    "I set Natsuki down on my front step."
    "I fumble with my keys for a moment, finally able to unlock the door."
    "I help Natsuki through."
    "She’s safe, from her father at least."
    scene bg kitchen with wipeleft
    play music tinkertailor
    "I bring her to the kitchen and sit her down on one of the chairs."
    show natsuki 12bf zorder 1 at t11
    n "A-ah... [player]...."
    n "Why d-did you... help m-me..?"
    n "H-how did you... know... wh-where I..?"
    mc "Don’t worry about all that now."
    mc "Let's just get you settled in for the night."
    "I’m worried that it’ll be longer than one night."
    "I have a spare bedroom in my house. She’ll be able to sleep there."
    "I search through my pantry, and my fridge for something she may like."
    "I decide to just make some toast, and chicken noodle soup."
    n 12bb "I-is that chicken noodle?..?"
    n "I-I haven’t had that in s-so long..."
    "Her words break my heart."
    "How long?"
    "How long has she lived like this?"
    "I watch the clock as Natsuki eats."
    "It’s late."
    "Now that the immediate panic is over, I realize that poor Natsuki is still drenched in her own stomach acid."
    mc "Natsuki, I’m going to need you to get changed."
    n 1bp "W-what?!"
    mc "Not here, silly."
    show natsuki 1bq zorder 1 at t11
    mc "I mean, you can get changed in the spare bedroom."
    n 1bs "But I don’t... have any of my clothes."
    mc "You’ll have to borrow some of mine."
    n "O-okay..."
    n 5bn "But only because... I have to."
    "Natsuki seems to be in much better shape after her meal. She stands up of her own accord, to return her bowl to the kitchen counter."
    "She moves slowly, but deliberately."
    show natsuki at thide
    hide natsuki
    "Despite the stink of bile clogging up my nose, I’m relatively calm too."
    "Natsuki’s skin tone has returned to normal, mostly. She still looks scarred by the night’s experiences."
    "Once she returns empty-handed, I ask her to follow me to her room."
    mc "Come on, I'll show you where it is."
    "Natsuki timidly complies, wrapping her arms around me."
    "But this time, it hurts."
    "I inhale sharply."
    show natsuki 2bm zorder 1 at t11
    n "A-are you okay, [player]?"
    "My shoulder is in pain."
    "The adrenaline of the situation has settled."
    "Maybe barging through that door was a bad idea..."
    "Not only because of the pain, but the damage it caused, too."
    "When Natsuki's dad returns to the house..."
    mc "Yeah, I’m alright. Don’t worry about me."
    mc "Let's get you cleaned up."
    mc "There’s a shower in the guest room, that you can use."
    "We reach the guest room, located across the hall from my own bedroom."
    scene bg spareroomn with wipeleft
    "I motion towards the edge of the bed."
    mc "Here, sit down for just a minute. I’ll be back with something comfy for you."
    "She sits down."
    scene bg bedroomn with wipeleft
    "I rush into my bedroom, picking out one of my grey tops and a pair of jeans."
    scene bg spareroomn with wipeleft
    "When I bring them back to her room, she’s struggling to take off her socks."
    "I place her fresh clothes on the bed, and kneel down to help her take them off."
    "She opens her mouth like she wants to say something, but reluctantly lets me help."
    "Natsuki has been through too much today. She has next to no strength left."
    show natsuki 1bn zorder 1 at t11
    n "T-thanks, [player]."
    n "I can take it from here."
    mc "Are you sure? I really don’t-"
    "All the blood in my body rushes to my face."
    "She’s going to have a shower."
    "Was I about to indirectly tell her I wanted to help?"
    mc "I-I-I..."
    mc "Nevermind, it’s fine."
    mc "You take your time."
    "I decide that now isn’t the best time to question Natsuki about her family."
    "Instead, she just need a soothing shower and some sleep."
    "Maybe that will take her mind off tonight’s events..."
    "Even if only for a few moments..."
    "Those few moments would do her a lot of good."
    "As I stand to leave the room Natsuki grasps my wrist gently."
    n 1bm "[player]... wait..."
    n 2bm "I-I wanted to thank you again..."
    mc "Don’t mention it, okay?"
    mc "I’m just glad I got there in time."
    "Natsuki stares into my eyes."
    n "M-me too..."
    n 2bc "How did you... know?"
    n "W-where I was?"
    mc "I walked home with Yuri."
    mc "She... she was having a bad day."
    mc "So I went with her."
    mc "She pointed out your place..."
    mc "And ever since I saw you at the hospital..."
    mc "You haven’t left my mind."
    mc "That’s why I decided to go."
    mc "I tried calling you God knows how many times, but you never answered."
    "I cast my mind back to Natsuki’s wreck of a phone."
    mc "I guess I know why."
    n 1bc "I-I saw every one of your calls..."
    n "I couldn’t answer b-because of the stupid screen."
    n 12bg "When all I wanted to do was hear your voice..."
    n 12bh "I couldn’t."
    n "I-I just wanted to go b-back to the club."
    n "And s-sit with you under the w-window..."
    n "To read more together."
    n 12bi "Because when w-we do..."
    n "It’s the only time I really feel... safe."
    n 12bf "Well... not anymore."
    "Of course."
    "Her Parfait Girls manga was torn apart."
    "She looks down at the ground, dejectedly."
    "I leave Natsuki to shower."
    scene bg bedroomn with wipeleft
    "After getting changed myself, I sit on the edge of my bed, gripping the volume of Parfait Girls that I had bought for myself on the weekend."
    "The water stops running, and I hear the en-suite’s door being opened and closed."
    scene black with wipeleft
    "I wait a few moments before knocking on her door."
    mc "Natsuki? I have something else for you."
    scene bg spareroomn with wipeleft
    show natsuki 2ci zorder 1 at t11
    n "Oh.. [player]?"
    "Natsuki opens the door, looking healthy again."
    "She is out of her dirty clothes, and is now wearing my shirt, along with her own pants."
    "The top doesn’t fit her very well, though."
    n 1ck "Huh, this shirt’s massive on me..."
    mc "I-I could get you a smaller top of mine, if you-"
    n 1cs "I like it."
    n "You don’t need to, [player]."
    mc "Are you sure?"
    n "Y-yeah."
    "I present the manga to her."
    mc "I... I saw what happened to your copy of Parfait Girls back at your place, so I thought I’d just drop my own in for you."
    mc "So you can, uh, read it."
    mc "If you want."
    show natsuki 1ca zorder 1 at t11
    "Natsuki gives me a weak, but sincere smile."
    "She reaches out to grab the manga."
    n "I’d love to, [player]."
    "Instead of pulling the manga from my hands as I expected, she grabs my wrist and tries to sit me down on the bed next to her."
    n 3ck "B-but only if we read it together."
    "It’s the least I can do to make her happy. She needs it."
    "So do I, in a way."
    show natsuki at thide
    hide natsuki
    "First having to deal with Sayori attempting suicide..."
    "Now Natsuki?"
    "God, how terrible must her home life have been for her to want to escape it like that?"
    "Well, I can take a guess, considering the complete lack of food in her house..."
    "And her face, when I saw her in the hospital."
    "Christ."
    show natsuki 1cm zorder 1 at t11
    n "Uh, h-hey, [player]?"
    mc "W-what?"
    n 4cn "You just kinda stood there for a second, spacing out."
    n 3cs "God, you’re worse than Sayori sometimes, you know?"
    mc "H-hey!"
    mc "I’m sorry, okay?"
    n 3ca "It’s fine. I was only teasing, dummy."
    "I know that I shouldn’t blame her. She doesn’t know about Sayori’s condition."
    "And as far as I know, she hadn’t seen her at the hospital."
    show natsuki at thide
    hide natsuki
    "Regardless, that hurt me more than it should’ve."
    "I move the duvet to the side, and sit down next to Natsuki."
    "She pulls the covers over the two of us, so we're sitting up with it draped over our laps."
    "We decide to just start the volume over again."
    show natsuki 1cn zorder 1 at t11
    n "[player], you’re so warm..."
    "Natsuki inches closer to me."
    "We're now shoulder-to-shoulder."
    mc "Natsuki, can you see it okay?"
    n "N-not really."
    "I inch myself down into a lying position."
    stop music fadeout(2.0)
    "Natsuki joins me."
    scene n_mod_cg1_base
    show n_mod_cg1_3
    with dissolve_cg
    play music tlwamsp
    n "Much better."
    "My left arm is awkwardly dormant between us."
    "I slide it under the pillow and around her."
    mc "There we go."
    show n_mod_cg1_2 at cgfade
    "We continue to read."
    scene black with dissolve_scene_full
    scene n_mod_cg1_base
    show n_mod_cg1_1
    with dissolve_scene_full
    "Before I know it, she’s fast asleep.."
    mc "N-Natsuki?"
    "I lay there motionless."
    "I dreamed of this moment ever since I really got to know Natsuki."
    "I hate that it had to come due to her circumstances at home, but regardless..."
    "I run my fingers through her silky pink hair. I brush her bangs to the side. "
    "She looks so peaceful in her sleep."
    "What is this feeling?"
    "I feel a lump in my throat."
    "Just the sight of her is enough to make my heart pound."
    "I don’t recognize this."
    "My chest is heavy. It feels like there’s a weight on my ribs. "
    "It’s hard to breathe."
    "This..."
    "This is the happiest moment of my life."
    "As I drop the manga to the side of the bed, not even reading anymore, I drift off to sleep."
    scene black with dissolve_scene_full
    "I’m jerked awake by the sound of crying."
    "Confused, I open my eyes and turn to look at Natsuki."
    scene n_mod_cg1_base
    show n_mod_cg1_4
    with dissolve_cg
    "She’s clutching the sleeve of my shirt, holding me tighter than before."
    "She’s sobbing into my shirt ferociously."
    mc "Natsuki, are you-?"
    "I realize that she’s still asleep."
    "Sighing, I lament over Natsuki’s nightmares."
    "I’m almost certain they’re related to her family, but..."
    "I give her a nudge to wake her up."
    show n_mod_cg1_5 at cgfade
    "As she seemingly begins to stir, I try to calm her."
    mc "Natsuki, it's just a dream."
    mc "You're okay, you're safe."
    show n_mod_cg1_6 at cgfade
    "Natsuki opens her eyes."
    n "[player]..."
    n "That..."
    n "That was more than a dream..."
    n "I watched my dad kill you."
    n "I watched him torture you for saving me..."
    n "He kept telling me this was my punishment for leaving..."
    show n_mod_cg1_8 at cgfade
    n "[player]... you shouldn't have helped me."
    n "This was wrong..."
    n "This is wrong!"
    show n_mod_cg1_9 at cgfade
    n "Why, [player]!?"
    n "Why’d you have to get involved?"
    n "I..."
    n "I can't let you do this..."
    "Natsuki jerks away from me."
    mc "Natsuki..."
    mc "Do you want to know the real reason I showed up at your house?"
    show n_mod_cg1_6 at cgfade
    mc "I missed you."
    mc "I missed reading with you."
    mc "I missed reading your poems."
    mc "And after the hospital, I knew something happened, I had to make sure you were okay."
    mc "I was worried sick for days."
    mc "I felt I had to."
    mc "I’d do anything to ensure your safety."
    mc "I’d gladly be tortured if it meant you would be happy."
    mc "Anything, Natsuki..."
    mc "Do you understand me?"
    mc "I'll do everything in my power to keep you safe."
    mc "If my words right now aren't proving I mean it, maybe this will."
    "I rise to my feet and walk to my room."
    scene bg bedroomn with wipeleft
    "I flick my light on and rifle through my bag."
    "Ah, there it is."
    python:
        if persistent.languague == "spanish":
            poem_me1 = poem_me1_spanish
    call showpoem (poem_me1) from _call_showpoem
    scene bg spareroomn with wipeleft
    "I return to the bed. Natsuki turns to face me."
    "I hand her my poem."
    show natsuki 1cth zorder 1 at t11
    "Natsuki reads, wiping her eyes as she does so."
    n "[player]..."
    n "I..."
    show natsuki 1ctd zorder 1 at t11
    "Natsuki leaps from her bed, and embraces me tightly."
    "I return the gesture, wrapping my arms around her."
    "We stay together for a while, her tears soaking through my shirt once again."
    "After a few minutes, Natsuki eases her grip. "
    "I do as well, resting my hands on her waist, hers hanging from my neck."
    "Natsuki lifts herself up onto her tip toes, and pecks me on the cheek."
    n "I... I want to go back to sleep..."
    n "B-but I want you to stay with me..."
    "I nod wordlessly, and Natsuki gently escorts me to the bed."
    scene n_mod_cg1_base
    show n_mod_cg1_4
    with dissolve_cg
    "Laying my head on the pillow, she keeps her arms wrapped around me."
    "We drift into the void of unconsciousness together."

    stop music fadeout 2.0
    scene black
    with dissolve_scene_full

    $ quick_menu = False
    scene black
    show thursday
    with dissolve_scene_half
    $ renpy.pause(delay=2.0, hard=True)
    $ quick_menu = True

    scene black
    with dissolve_scene_full

    "Drearily stirring, I can tell from the snoring figure next to me that Natsuki is still asleep."
    "I rub my eyes, struggling to open them."
    scene n_mod_cg1_base
    show n_mod_cg1_7 zorder 1
    show n_cg1_dust1 zorder 2
    show n_cg1_dust2 zorder 3
    show n_cg1_dust3 zorder 4
    show n_cg1_dust4 zorder 5
    with dissolve_cg
    "Reaching out to my bedside cabinet, I swipe my phone and check the time."
    "Midday."
    "There’s no point going to school today. We’ve already missed half of the day."
    "Besides, I don’t think Natsuki would be up for it, after last night’s... well..."
    "I sit up and decide to head downstairs, and make breakfast for the two of us."
    "She’ll appreciate the effort."
    "I try to be as quiet as possible, in an attempt to not wake her up while I slip out from under the duvet."
    scene bg kitchen with wipeleft
    play music presenttense
    "I head to the kitchen and decide to make something quick and easy so I can bring it to her."
    "Searching through my fridge, I find some bacon. "
    "I start mixing together some pancake batter after a short search for the ingredients."
    "As I’m cooking, I hear a light knock on the door."
    "Anxious about leaving the cooking food I rush to answer"
    scene bg house with wipeleft
    "It’s Sayori."
    show sayori 1ba zorder 1 at t11
    mc "Hey, Sayori! W-what are you doing here?"
    mc "I thought you’d be back at school."

    "I step outside, closing the door behind me."
    "I don’t want her to know Natsuki is here."

    s "I was planning on it, but I just couldn’t get out of bed this morning."
    s 1bb "Are you cooking? It smells really sweet."

    "Sayori peers through my window, to see what I’m up to in the kitchen. "

    s 4bm "N-Natsuki?!"

    "Taking a look myself, I see Natsuki tending to the breakfast."
    "Crap..."

    s 2bi "I see what’s going on, [player]."
    mc "Y-you do?"
    s 4br "Yes! You two are making cupcakes again!"

    "I can feel the sweat on my forehead begin to bead."
    "I’m so done for."

    mc "Y-yeah! It’s supposed to be a surprise."
    mc "For the club!"
    mc "Neither of us were expecting to see you, though."

    "I give Sayori a weak smile in an attempt to reassure her."

    s 4bq "Don’t worry [player], your secret will be safe with me!"
    s 3bd "Well, since you’re busy I’ll leave you two {i}lovers{/i} be. Ehehe~"
    mc "O-okay Sayori, see you."

    "As she’s about to leave, I stop her momentarily."

    mc "I was just wondering... are you going to the club?"
    s 3bb "I guess, since I’m actually up, I might as well."
    s 1bx "Especially if you're bringing the cupcakes!"
    mc "Yeah..."
    show sayori at thide
    hide sayori
    "Sayori leaves without another word."
    scene bg kitchen with wipeleft
    "I return to the kitchen in a cold sweat, worrying about the false promise I gave to Sayori."
    "Guess I'll have to convince Natsuki that we should cook a batch..."
    "She's nearly finished making our meal."
    show natsuki 2cg zorder 1 at t11
    mc "Ah..."
    mc "The breakfast..."
    mc "It was supposed to be a surprise."
    mc "I was going to wake you and have it all ready for you..."
    mc "Then Sayori knocked and I-"
    n 4ce "You could’ve burned your house down, dummy."
    n "Look!"

    "She points the spatula at a plate of charred pancakes."

    n 3cc "I guess we’re even now, huh?"
    n 3cd "You saved me, and I saved our breakfast."

    "A part of me wants to scold her for her warped perception of what ‘even’ meant, but another doesn’t want to bring up the events of last night with her."
    "I decide that I’ll make a snide remark, at most."

    mc "Heh, not quite."
    mc "Maybe one day."
    n 1cj "Ehehe, maybe~"

    "Natsuki is really something else outside of the clubroom."
    "Maybe it’s because she doesn’t have to put on a show for the other club members."
    "They always call her \"cute\", though I can surely see why."
    "I set the table and sit down with Natsuki."
    "At first she starts eating almost viciously, but quickly snaps out of it remembering I’m in the room."

    mc "How is it?"
    n 2cl "It’s... delicious."

    "She continues to scoff her breakfast down, albeit at a slightly slower pace."
    "Once we’re both finished I take her plate from her and place it in the dishwasher for her."

    n "So..."
    n 2ck "Do you want to do anything today?"
    mc "Well, I, uh, kinda promised Sayori that we'd make a batch of cupcakes for the club later."
    mc "If you want to, then maybe we can set aside a few just for later?"

    "Natsuki immediately jumps from her chair, grabbing the apron draped over the oven handle."

    n 4cd "Let’s do it!"

    "Before I can react she’s tearing through my cupboards and drawers looking for everything she needs, only occasionally stopping to ask where I keep certain utensils and ingredients."

    n 4ca "Ready to help?"
    mc "Of course!"
    mc "Hopefully I’ll be more useful than last time."
    n 4cb "You better be!"

    "Natsuki playfully punches my shoulder."

    mc "Gahk-"
    n 4cy "Don’t tell me that seriously hurt y-"
    stop music fadeout(2.0)
    n 3cn "..."
    n 1cm "The door..."
    n 1cu "[player], I am so sorry... I completely forgot."
    mc "It’s okay."
    mc "It’s only a bruise. You just caught me by surprise is all."

    "I’m having a extremely hard time trying to play it off."
    "That genuinely hurt."
    "I forgot how much power her small frame can deliver."

    mc "What do you want me to do first?"
    n 1cq "Well, uh, I guess you could start pre-heating the oven to 350."
    n 1ck "I’ll deal with the dry ingredients."

    "I do my small part and watch Natsuki get started."
    show natsuki at thide
    hide natsuki
    play music thenumbers
    "She’s so precise with her movements."
    "It’s almost..."
    "Hypnotic."
    "Natsuki catches me staring at her, completely spaced out."
    show natsuki 3cz zorder 1 at t11
    n "Ehehe~"
    n 3ci "Dummy..."
    mc "W-wha?"

    "I shake my head as I’m jerked back into the moment."

    n 4cc "You were staring!"
    mc "Oh, aha... sorry."
    mc "What next?"
    n "I’ve got everything ready to go besides the eggs."
    n 2ck "Could you crack them into this bowl for me while I set the tray liners?"

    "I grab an egg in each hand and crack both simultaneously."
    n 2cs "Show-off..."
    mc "Yeah? So?"
    mc "What’s the matter with me trying to show off for you?"
    n 4ci "U-uh, [player]..."
    n "I-"
    mc "Ha, I finally got you."
    n 4ch "Eh? What do you mean?"
    mc "You get all embarrassed when I try to be sweet."
    n 4co "I-I-I-I..."
    mc "Natsuki, you’re adorable."
    n 4cs "Hmmph..."

    "Natsuki begins to prepare the cake batter."

    n "[player]..."
    n 4cn "Can we talk about last night?"
    mc "As much as I want to fully understand what happened, maybe we should leave that for later."
    n 1cm "Y-yeah... okay."

    "Natsuki nods in agreement, and returns to the batter."
    "She quickly finishes mixing it, and begins to distribute the batter evenly between the cups."
    "I wash the beaters by hand and attach them to the mixer."
    "I start to mix the icing."

    mc "I should've done this last time."
    n 3ch "And what, leave me to mix all that batter by hand?"
    mc "Yeah, well you’re stronger than you think."

    "Natsuki huffs with an arrogant look on her face."

    n 3cw "And don’t you forget it!"

    "The enticing smell of chocolate cupcakes begin to seep from the oven."
    show natsuki at thide
    hide natsuki
    "It’s going to be difficult to not eat any on the way to the club."
    "I drip blue food colouring into the icing."
    "The timer rings and Natsuki opens the oven’s door."
    "Instantly my entire house is filled with the mouth-watering scent of Natsuki’s baking."

    mc "Oh my God."
    mc "These ones smell even better than the last batch!"

    "Natsuki sets them on a rack to cool for a few minutes while I finish the icing."
    show natsuki 2cc zorder 1 at t11
    n "Are you almost done?"
    n 2ck "We have to get going soon."

    "I stop the mixer for a moment and plunge my finger into the cobalt sea of sugar."
    "I raise my finger to my mouth."
    "Natsuki grabs my wrist and pulls my arm away from my face."
    "She scoops the icing off of my finger onto her own and promptly licks it off."

    mc "H-hey!"
    n 1ct "What, you expected me to put your finger in my mouth?"
    n 2cy "That'd be gross."
    mc "E-eh?!"
    mc "You’re only saying that because I did that to you!"
    n 1cz "Ehehe, of course. That makes {i}you{/i} gross."
    mc "I-I’m not gross!"

    show natsuki at thide
    hide natsuki
    "I can’t help but crack a smile as I speak."
    "It would be a lie if I said I didn’t enjoy her teasing."
    "It makes her so happy when she gets a reaction out of me."
    "Even if only a tiny one."
    "Natsuki and I ice the cupcakes and get ready to leave."
    scene bg bedroom with wipeleft
    "Quickly, I head up to my room to get changed into my school uniform."
    "Natsuki, without her uniform, is forced to wear the clothes I gave her."
    "Seeing as most of the teachers will have left by the time we arrive, she shouldn't end up getting into any trouble."
    scene bg kitchen with wipeleft
    "I return to the kitchen for a moment to grab some tin-foil, and cover the cupcakes with it to protect them."
    "Natsuki notices, and heads out of the door. I follow."
    scene bg house with wipeleft
    "As we’re walking down the street, Sayori calls out to us from her door."
    s "Heeeeeeeeey!"

    "Natsuki grabs my arm, signalling for me to stop walking as Sayori catches up."
    show sayori 1n zorder 1 at t21
    show natsuki 1cd zorder 2 at t22
    s "Ooooooooh~"
    s 4s "I could smell those from my house!"
    s 4r "I can't wait, ehehe~"

    scene black with dissolve_scene_full
    stop music fadeout(2.0)
    scene bg courtyard with dissolve_scene_full

    show sayori 3l zorder 1 at t21
    show natsuki 1ct zorder 2 at t22
    "Natsuki, Sayori, and I make our way to the school."
    "Sayori is acting quite normal considering what happened just a few days ago..."
    "Come to think of it, Natsuki is too."
    "Perhaps they wouldn’t like to dwell on dark times."
    "I don’t blame them."
    "I just can’t help but be reminded of their traumatic events."
    "Within a few minutes we arrive at school. Only the last few students trickle out from the doors, as it’s the end of the school day."
    scene bg corridor with wipeleft
    "The three of us make our way to the clubroom, being careful not to drop the cupcakes."
    "I set the cupcakes down on the desk near the door."
    scene bg club_day with wipeleft
    show sayori 1x zorder 1 at t21
    show yuri 1l zorder 2 at t22
    play music t3
    s "Hey Yuri!"

    show sayori 4r zorder 1 at t22
    show yuri 3p zorder 2 at t33
    "Sayori runs up to Yuri and gives her a hug."

    y "A-ah!"
    y "Sayori!"

    show sayori 1q zorder 1 at t21
    show yuri 2q zorder 2 at t22

    y "S-sorry, you startled me..."
    y "Where have you two been?"
    y "Not feeling well?"
    s "Yeah, I wasn’t feeling so good the past few days."
    s "I was really sick."
    show sayori zorder 1 at t31
    show yuri zorder 2 at t33
    show natsuki 4cc zorder 3 at t32
    n "M-me too!"
    y 2s "Well I’m glad you two are back now, and healthy."
    s 1y "Y-yeah..."
    y 2h "But Natsuki... where's your uniform?"
    n 2cq "Oh, uh... it was dirty, and I didn't have time to wash it..."
    y "But you'll get into all sorts of trouble with the teachers if they see you out of uniform..."
    n "W-well, that's why I skipped the rest of the school day."
    show yuri 2g
    "Yuri stares down Natsuki doubtfully."
    "Instead of calling her out though, she changes the subject."
    y 1f "By the way, I have a surprise for you all."
    show natsuki 1cl
    s 2n "Ooooooooh~"
    s "What is it?"
    y 2j "It's a surprise for a reason, Sayori."
    y "Just wait a moment, I’ll show you all when Monika arrives."
    n 3cj "[player] and I decided, since I was feeling better, that we should make some cupcakes."
    n "I’ve already missed the majority of classes this week, so what’s one more day?"
    n 4cz "Especially if it means I get to bake!"

    "Natsuki retrieves the box of cupcakes and lifts up the foil, showing off our handywork."

    y "Such a deep shade of blue..."
    y 3b "They look delectable."
    n "Thanks!"
    s 4r "Eeeeeeeeeeeeeeeh~"
    s 4q "I can’t wait! I’m starving."
    n 2cd "Not me! I'm stuffed!"
    s "What do you mean?"
    n 2cg "I-uh..."
    n 4ck "When I went over to [player]'s house to bake, he’d made me breakfast."
    s 4x "Aww! [player], you’re so sweet."
    mc "Heh... thanks, Sayori."
    s 1c "Hmm... I'm kinda thirsty, actually."
    s "I'll be back in a second~"

    show sayori at thide
    hide sayori
    show natsuki at t21
    show yuri at t22
    "Sayori walks out of the club room turning toward the fountain down the hall."
    "Mere moments later, Monika walks into the clubroom from the other door."
    show monika 1h zorder 3 at t31
    show natsuki zorder 2 at t32
    show yuri 4b zorder 1 at t33
    mc "Hi, Monika."
    m 2i "Wow, looks like everyone bothered to show up today."

    "Natsuki bites her tongue."
    "Yuri buries her head into her novel again."
    "I’m left standing alone fidgeting with my hands."

    mc "Yeah, I guess."
    m "About time."

    "She still seems pretty upset about the festival."
    "I hope maybe our cupcakes will be a sufficient peace offering."
    "Sayori returns, carton of apple juice in hand."
    show monika zorder 4 at t42
    show sayori 1x zorder 3 at t41
    show natsuki zorder 2 at t43
    show yuri zorder 1 at t44
    s "Hey Moni-"
    show sayori 1f
    m 1i "Hi Sayori."
    m "What happened on Monday?"
    m "Were you sick?"
    s 2h "Y-yeah, [player] had to take me to the hospital."
    m 2h "Hmmph. [player], I thought you said it was a family emergency?"
    mc "I-it was, kinda. I’ve known her for ages, she’s basically like family to me at this point."
    mc "Besides, I’ve never seen her like that."
    mc "I felt like I had to make sure she was going to be okay."
    m 2i "And what about you, Natsuki?"
    m 1i "What’s your excuse?"
    n 4cp "I was sick too!"
    n 4cq "And don’t call it an \"excuse\", like you don’t believe us or something."
    m 1h "No, I do."
    m 1i "It just isn’t a good enough reason to have ruined the festival."

    "I should’ve guessed that she was still up in arms about the festival."

    m "Of course, I mean unless you were nearly {i}dying{/i}, then I'd certainly understand."
    m "And since you’re both here, I take it that wasn’t the case."
    m 2i "Whatever. Just don’t miss important days like that again or there will be consequences."
    y 3v "U-Uhm.."

    "In an effort to break the hostile mood that Monika was causing, Yuri clears her throat."

    y 3u "I have something for all of you."

    "Yuri lifts her bag onto her desk and unpacks a new tea set."

    y 2s "I-it’s not much but I thought it’d be nice to share."

    "The new set has five cups."
    "One for each of us, each one has one of our names painted on it in a different colour."

    s 4n "Ooooohh~!"

    "The new teapot has \"Literature Club\" written in script across the middle on each side."

    s 3x "Thanks, Yuri!"
    s 1l "This looks so... elegant!"
    y 2b "Th-thank you."
    n 3cd "And the cups are a little bigger! Thanks, Yuri!"
    mc "This must have taken quite some preparation."
    mc "Thanks."

    show yuri 4a
    "Yuri, clearly uncomfortable with the amount of attention being given to her, turns toward Monika who hasn’t said a word."

    m 4i "Oh, good job, Yuri."

    "Could she have sounded any more monotone?"
    show yuri at thide
    hide yuri
    show sayori at t31
    show monika at t32
    show natsuki at t33
    "Yuri politely nods, and retreats back to her novel."
    show sayori at thide
    hide sayori
    show monika at t21
    show natsuki at t22
    "Sayori is writing something down."
    "I can’t make out what it is but it looks to be a poem."

    n 2ck "Hey [player], come on!"
    scene bg closet with wipeleft
    "Natsuki, dragging me by the arm, pushes me down under the windowsill."
    "She grabs the next volume of Parfait Girls from her set, replacing the volume from last night to its rightful spot."
    "We sit and read this volume in silence, besides the occasional giggle from Natsuki."
    scene black with dissolve_scene_full
    stop music fadeout(2.0)
    scene bg closet with dissolve_scene_full
    "After around twenty minutes, Monika clears her throat to get our attention from across the clubroom."
    scene bg club_day with wipeleft
    show monika 4d zorder 4 at t42
    show sayori 1f zorder 3 at t41
    show natsuki 1cn zorder 2 at t43
    show yuri 4a zorder 1 at t44
    play music t5
    m "{i}*ahem*{/i}"
    m 4b "Okay, everyone!"
    m 4a "It’s time to share poems!"

    "I left my poem for Natsuki at home..."
    "I'm assuming Natsuki was unable to write one, and presumably Sayori too."

    m 4h "Well?"
    m 2i "None of you even tried to..?"

    "We all stay silent."

    y 2o "I-I did, but maybe we should just wait until tomorrow."
    y "Natsuki and Sayori probably couldn’t write because they fell ill."
    y "But I'm not sure about-"
    m 1q "Fine."
    m 1r "Tomorrow it is, then."

    "We all gather around the table."
    "Monika is spacing out."
    "Something else must be bothering her."
    "Either way, still no excuse to be so cold toward all of us."

    y 1g "You know, I’ve been excited to use the new tea set."
    y "I’m going to boil the kettle."
    y 1h "I assume you’ll all be having a cup of tea?"

    "I nod silently."

    n 1cc "I’ll get the cupcakes!"

    "Monika pulls a fresh piece of paper from her notebook and begins writing."
    "Natsuki sets the cupcakes down in the center of the table."
    "Yuri returns with the kettle."
    "Monika seems to be oblivious as to what's going on around her. She’s writing furiously, pressing the pen deep into the paper."
    "Steam begins to flow from the kettle, and Yuri transfers the water into the pot. Yuri pours tea into each of our respective cups."
    "Moments of silence go by as if they were hours."
    "Monika’s really killed the mood with her attitude."
    "Sayori's already pilfered a cupcake from the tray, and bites down into it."

    s 3x "Wow Natsuki, these are the best ones yet!"
    n 4cy "You just haven’t tried this recipe yet!"

    "Sayori, reaching for her cup of tea, accidentally tips it over, spilling its contents all over Monika’s notepad."

    show sayori 1e
    m 2s "Jesus, do you always have to be such a clutz?"
    stop music fadeout(5.0)
    m "Get your act together! You're supposed to be the vice president!"
    show natsuki 1cn
    show yuri 4c
    "Monika’s sudden snap takes us all off guard."
    "Sayori, clearly flustered, knocks the overturned teacup onto the ground, shattering it across the clubroom floor."

    m 2t "For Christ’s sake, Sayori! Do you ever pay attention to what you're doing?"
    s 1u "I-I-I..."
    m 5b "You what?! You're sorry again? Just like how you were sorry about not showing up for the festival?"
    m "And dragging [player] to the hospital with you?"
    show sayori 1v
    m "That was pretty selfish of you."
    show sayori 4w
    m "If [player] was here we could've just continued on without you."
    m 1t "Or Natsuki, considering she probably would’ve weaselled her way out of reading anyway."

    "Everyone besides Monika is in utter shock."

    y 4d "H-hospital..?"

    "Why is she being so hostile?"
    show sayori at lhide
    hide sayori
    show natsuki at lhide
    hide natsuki
    show monika at t21
    show yuri at t22
    "Sayori rushes out of the room crying, quickly followed by Natsuki, who's attempting to comfort her."
    "Yuri has moved from her usual seat to the other side of the room, her face buried in her novel."
    "I stand and Monika glares at me."

    mc "Monika, what the hell are you doing?"
    m 2t "Go take care of her."
    m "She clearly can't take care of herself."
    "I want to scream at her after what she said."
    "I have an urge to slap her."
    "Instead I rush out of the door to console Sayori, and Natsuki."
    scene bg corridor with wipeleft
    play music tinkertailor
    "I can hear them in the hallway upstairs, Sayori's sobbing filling the otherwise silent halls."
    "I run up the stairs to see her crying on a bench, Natsuki alongside her."

    show sayori 1u zorder 1 at t21
    show natsuki 1cu zorder 2 at t22
    mc "H-hey, it's okay..."
    mc "Monika’s just being a..."
    mc "I don’t know what she’s doing, okay? She probably had a really bad day, or something."
    mc "She's just taking it out on you."
    mc "I-I'm not saying it's the right thing to do..."
    mc "What I'm trying to say is..."
    mc "Don't take it to heart."
    mc "She knows that we were all looking forward to the festival."
    mc "Maybe she just takes things like this harder than the rest of us."

    s 3v "I don’t care, [player]."
    s "That’s not how you speak to people."
    s 1u "I'm going home."

    "Sayori stands."
    "Oh, crap."

    s 2u "I'll walk with you tomorrow."
    s 1u "But until Monika stops her campaign to hurt everyone, I’m staying the hell away from the club."

    "Sayori wipes the remainder of her tears from her cheeks."

    s 1f "You two have fun dealing with her. Tell her that if she wants to talk, she knows where I live."
    n 1cu "Wait..."
    n 2cm "Sayori, come back, we'll sort it out together."
    n 2ck "Doesn't that sound better?"
    mc "Yeah, come on, Sayori. It'll be easier this way."

    "Sayori's entire attitude shifts. She's no longer crying..."
    show sayori 1i
    "Her face is completely blank."
    "She turns to me."

    s "[player], I'll see you later."
    s 1j "I'm leaving."
    mc "We can walk home with you. I don't really want to go back there anyway."
    n 2ch "Yeah, me neither."

    "Sayori looks at the two of us and shakes her head."

    s 3j "No."
    s 3i "I just want to be alone right now."
    mc "Okay, well you should join us for dinner tonight!"

    "Natsuki gives me an odd look."

    n "Y-yeah!"
    s 3y "Did you just say join {i}us{/i}?"
    mc "Well, yeah. That's part of the reason why Natsuki was already at my house this morning."
    mc "She... she had a really bad night and-"
    s 3i "No, I'll just stay home."
    s "Maybe my mum’ll order some take out."
    s 1h "Have fun."

    show sayori at thide
    hide sayori
    show natsuki zorder 1 at t11
    "Sayori turns and heads down the stairs."
    "I have never seen her like that."
    "Not even when I caught her trying to..."

    mc "Natsuki, could you give me a second?"
    n 2ck "What’re you doing?"
    mc "I just need to call someone, quickly."

    show natsuki at thide
    hide natsuki
    "Natsuki nods, and takes off to wait at the end of the hallway."
    "Worried, I ring her mother, who’s already at home."
    "I explain what happened and she tells me that there's no reason to be worried."
    "She explains that the doctor had given her some antidepressants during the last trip to the hospital."
    "She tells me that it could just be a side effect of the drugs."
    "I let her know that I'm still concerned, and to please keep an eye on her."
    "Sayori's mum brushes me off and wishes me a good day."
    "Still worried sick about Sayori, I catch up to Natsuki."
    show natsuki 1cg zorder 1 at t11
    mc "Listen..."
    mc "Do you want to go back to the club, or..?"
    n 4cg "Like hell I’m going back..."
    n 4cf "Not while that bitch is there."
    mc "Well, I still need to get my bag and stuff, so I guess I’ll meet you back at the entrance."
    mc "You okay with that?"
    n 3cg "Fine."
    n "I’ll wait."
    mc "Thanks."
    n "Hurry up, though."
    stop music fadeout(2.0)
    "I take off back downstairs to the clubroom."
    scene bg club_day with wipeleft
    "Bursting through the door, Yuri nearly jumps out of her seat and Monika, writing on a new, drier page of her notepad, turns to face me."

    show monika 3i zorder 2 at t21
    show yuri 4b zorder 1 at h22
    m "What do you want?"
    mc "None of your business."

    "Leaning down at my desk, I pick up my backpack and sling it over my shoulders."
    "Moving back towards the exit, Monika tries to get my attention."

    m 1v "Ehehe~"
    m 2u "[player], what’s wrong with you?"

    "I turn, and stare at her in utter disbelief."

    show monika 3s zorder 2 at h21
    show yuri 4c zorder 1 at h22
    play music fulstop
    mc "What the fuck is wrong with {i}you{/i}, Monika?"
    mc "Ever since we accidentally ruined your festival event, you’ve been nothing but pure venom for the club."
    mc "You were needlessly rude to both Sayori and Natsuki, neither of which are in a mental state capable of handling that right now."
    mc "I understand that it was a big day, and it was important to you."
    mc "But you have no right to lose your shit on us."
    mc "And don’t think I didn’t hear about what you said to Yuri."

    "I was only partly telling the truth."
    "I knew that Monika had said something to Yuri, but I didn’t know what."

    m 1h "Oh, is that so, [player]?"
    m 2i "Well, you do know what she’s been doing, don't you?"
    mc "Y-yeah. I do."

    show yuri 4d
    "Yuri's eyes are locked onto me, peering over her book."
    "She's shocked, but won't call my bluff."

    mc "Yeah, she’s been-"
    m 4s "Trying to sabotage the club, we know. She doesn't want any new members."
    m "Not only that, but I caught her rummaging through your stationery yesterday."
    m 4t "I only told her that she was being a selfish bitch."

    "Monika turns and points at Yuri."

    m 2t "You can't fool me, Yuri."
    m "I know exactly what’s been going on here."
    mc "Monika, that's way over the line."
    mc "How paranoid are you to think-"
    m 1s "Shut up, and listen to me."
    m "You're the real reason that the festival was cancelled."
    m "I could give a shit that Sayori is sick. Of course, Yuri just wanted me to let it go. So I'll tell you the same thing I told her."
    m 1t "This is MY club."
    m "We do what I say."
    m 2t "Do I make myself clear?"
    mc "Crystal clear."
    mc "But there’s one thing... Yuri, care to explain-"
    y 3y4 "Fuck you, Monika."
    y "You crazy bitch."
    y 3y7 "Do you not see that this is-"
    m "Hey there."
    m "Don't cut too deep now, Yuri."

    show yuri 3y2 zorder 1 at h22
    "Whatever Monika meant by that, Yuri was affected. Mortified, she drops her novel to the ground and falls back into her chair, stunned."
    show monika 1s zorder 2 at t43
    show yuri zorder 1 at t44
    "Shoving me out of her way, Monika marches over to Yuri."
    "She stumbles out of her desk and backs away into the closet."
    "Monika follows her. I watch from behind all the commotion."
    scene ym_mod_cg_base
    show ym_mod_cg_sleeve zorder 1
    show ym_mod_cg_1 zorder 2
    with dissolve_cg
    "She grabs her by wrist and yanks her sleeve up."
    show ym_mod_cg_2 zorder 3 at cgfade
    hide ym_mod_cg_sleeve
    m "Oh, what a shame..."
    m "You couldn’t just help yourself, could you?"
    m "What did I say, Yuri?"
    "Yuri stays silent, her eyes fearful."
    "Monika moves closer, forcing her to make eye contact."
    m "Maybe I didn’t make myself clear, Yuri."
    m "What."
    m "Did."
    m "I."
    show ym_mod_cg_4 zorder 4 at cgfade
    m "Say?"

    "I can’t believe what I’m seeing."
    show ym_mod_cg_3 zorder 5 at cgfade
    y "I-i-i-i-if I d-d-didn’t s-shut up..."
    y "Y-y-y-ou’d... tell... t-the c-c-club..."
    m "That’s right."
    m "If you dare criticize my ability to lead the club again, Yuri..."
    hide ym_mod_cg_4
    m "Everybody's gonna know about this."
    m "Everyone."
    m "How do you think they'd feel about you, knowing what you do behind closed doors?"

    "My blood is boiling. I’m just about ready to knock her out."

    mc "Monika! What the hell has gotten into you?!"
    mc "You’re crazy!"

    "Monika lets go of Yuri’s arm, pushing Yuri and the desk away from her."
    scene bg closet with dissolve_cg
    show monika 1s zorder 2 at t21
    show yuri cuts zorder 1 at t22
    "Looking at me, she speaks up."
    show yuri 5f
    m "You want to see \"crazy\", [player]?"
    m "I'll show you \"crazy\"."

    "From her school blazer, she pulls a sheet of paper, neatly folded."
    "She thrusts it into my hand."

    python:
        if persistent.language == "spanish":
            poem_s3 = poem_s3_spanish
    call showpoem (poem_s3) from _call_showpoem_1

    m "That is \"crazy\"."
    mc "What the hell is this?"
    m "The poem that Sayori sent me on the morning of the festival."
    m "She told me everything after... it was supposed to be her suicide note."
    y 5b "S-suicide note?"
    y 5a "W-what the h-hell is wrong w-with you?"
    y "S-Sayori, she’d never-"
    mc "Monika..."

    "I shake my head in disbelief."
    "Wordlessly, I storm out of the clubroom."
    scene bg corridor with wipeleft
    "I walk down the vacant halls toward the front doors."
    stop music fadeout(5.0)
    "I can see Natsuki standing outside through the glass."
    scene bg courtyard with wipeleft
    show natsuki 3cn zorder 1 at t11
    n "Are you okay, [player]?"
    n 3cu "You look a little..."
    mc "I’ll be okay."
    mc "It’s just Monika who's not okay..."
    scene black with dissolve_scene_full

    scene bg residential_day with dissolve_scene_full
    play music yawa

    "I show Sayori’s poem to Natsuki on the walk back to my house."
    "She can’t believe what she's looking at either."
    show natsuki 2cm zorder 1 at t11
    n "You know, [player], that’s serious."
    n "You think we should check up on her?"
    mc "After what happened earlier?"
    mc "Yeah, definitely."
    show natsuki at thide
    hide natsuki
    "First we head back to my house, just to drop off our school bags."
    scene bg house with wipeleft
    "We head towards Sayori’s house."
    "I knock on Sayori’s door."
    "She answers the door, but just stares at us."
    show sayori 3ci zorder 2 at t21
    show natsuki 2cu zorder 1 at t22
    mc "Hey Sayori, we just wanted to check in on y-"
    s 1ci "I’m fine."
    s "I told you that already."
    s "I ordered pizza, and was just about to eat it."
    s 1cj "You two enjoy making {i}your{/i} dinner."

    "She edges the door shut."

    mc "Wait, Sayori..."

    "I wedge my foot into the door before she can close it on us."
    "She tries again but harder this time."

    mc "Monika gave me this."

    "I nudge Natsuki, and she nods, giving Sayori the poem."

    s 2ci "Oh yeah."
    s "I forgot I'd sent that to her."
    s 2cj "Whoops."
    n 1ck "Listen, Sayori, if you ever want to hang out or if you need anyone to talk to..."
    n "[player] and I are always happy to listen."
    n 1cl "We are all friends after all!"

    "Sayori forces a laugh."

    s 1cx "Sure, Natsuki."
    s 1cj "Where can I find you? [player]’s place?"
    n 1cs "U-uh..."

    show sayori at thide
    hide sayori
    show natsuki at t11
    "Sayori shuts the door on the two of us."
    "I didn’t think she would care that Natsuki was staying with me."
    "I should really sit down with Sayori and explain the situation."
    "Sooner rather than later."
    "Natsuki and I head back home to eat and get settled in for the night."

    stop music fadeout(2.0)
    scene black with dissolve_scene_full

    scene bg mclivingroom with dissolve_scene_full
    play music presenttense
    show natsuki 2cb zorder 1 at t11

    n "[player]!"
    mc "Yeah?"
    n "You barely have any food left!"
    n 2ck "How are we supposed to make dinner?"
    mc "I... I don’t know."
    mc "Well, we’ll have to go to the shops, but quickly. It won’t be long before they close."

    "I open the closet by the door and grab my jacket."

    mc "You coming?"
    mc "Because I don’t really know what I’m getting..."
    n 2cq "It’s getting pretty cold out there."
    n "And I don’t have a coat..."
    mc "Is it at your place?"
    n 1cu "N-no, [player]."
    n 1cn "I-I don’t... own one."

    "I hand Natsuki my coat for the time being."

    mc "Well, hold onto this for now, then."

    "I can handle the weather until we get to the shopping center."

    n "A-are you sure?"
    n 1cu "Because I really wouldn’t want-"
    mc "It’s fine, believe me."
    mc "Come on, we’re going to have to hurry before the shops close."

    scene bg house with wipeleft
    "As we exit the house, a gust of chilly wind hits us both."
    "Natsuki hurriedly pulls my coat on."
    "I shiver violently."
    scene black with wipeleft
    "We catch the bus, and make our way to the store."
    "On the route, the bus passes Natsuki’s house."
    "She shuffles down in her seat in an attempt to keep it out of her sight."
    "I can understand."
    mc "You okay?"
    "Natsuki wraps her arm around mine."
    n "Y-yeah."
    "Shortly, the bus arrives at our stop, and we make our way to the mall. "

    mc "So, uh... where’d you--"

    "Natsuki is already dragging me into a nearby clothing store before I can finish my sentence. "
    scene bg clothingstore with wipeleft
    "She rips my jacket off and hands it to me."
    show natsuki 3cl zorder 1 at t11
    n "They’re all so cuuuute~!"
    n "Oh! [player]!"
    n "How do you like this one?"

    scene bg clothingstore with dissolve_scene_full
    show natsuki 4dt zorder 1 at t11

    mc "I like it!"
    mc "You know, it fits you perfectly too."
    n 3dk "Oh, and look at this scarf!"
    n "It goes perfectly with it!"

    "Natsuki walks to the cash register to pay."

    mc "Uhm, Natsuki..."
    mc "Where’d you get the money from?"
    n 3dm "Oh, uh..."
    n "I..."
    n 1du "Well, I have to take it from my dad."
    mc "You’re stealing it?"
    n 4dp "It’s not stealing!"
    n 2dq "Well, I don’t like thinking it is..."
    n "It’s usually for fo-{nw}"
    n 2du "It's usually for {fast}baking stuff..."
    n "Sometimes manga."
    n 2dn "I was saving for the Parfait Girls box set, but this is more important."

    "The clerk scans both of her items and the total is a bit steeper than Natsuki expected."
    "Begrudgingly, she brings the scarf back to the rack she found it on."
    show natsuki at thide
    hide natsuki
    "I have an idea."
    "I grab the scarf while she’s paying for her jacket and grab a black beanie for myself."
    show natsuki 1dg zorder 1 at t11
    mc "D’you think this will look good on me?"
    n 4dj "Hmm, maybe."

    "Good enough."
    "I place the two items on the counter and the cashier gives me a sly smile, scanning my things."
    scene black with wipeleft
    "Natsuki is waiting for me outside."
    "During the time we spent indoors, it had begun to snow outside."

    n "Could've done with the scarf after all, huh..."

    "{i}Just you wait...{/i}"
    "Natsuki begins to shiver as we wait."
    "The snow begins to settle as the bus comes to a halt."

    mc "The snow’s beautiful."
    n "Yeah..."

    "We board the bus with our things, and sit at the back."
    "I give Natsuki the window seat."
    "We sit together wordlessly as she becomes more entranced by the snowfall."
    scene black with dissolve_scene_full
    stop music fadeout(2.0)
    scene black with dissolve_scene_full
    n "It’s a shame it’ll be gone in the morning..."
    n "It never really sticks."
    mc "Yeah, I wish it’d stay a bit longer too."

    "Natsuki rests her head on my shoulder, still staring out the window."

    n "This is nice..."

    "I wrap my arm around her."
    "We stay this way for the remainder of the trip back home."
    "As we approach our stop I grab all of our bags."
    "The bus comes to a stop and we get off."
    scene bg residentialsnown
    show n_cg1_dust1 zorder 2
    show n_cg1_dust2 zorder 3
    show n_cg1_dust3 zorder 4
    show n_cg1_dust4 zorder 5
    with wipeleft
    "We're a short walk from the house."
    "Now's probably a good time to-"
    show natsuki 2dj zorder 1 at t11
    n "Hey, [player]..."
    n "How much was the hat after all?"
    mc "Oh! Uhm..."
    mc "I actually don't have a clue, ahaha..."
    mc "I only bought it so I could surprise you with this anyway."

    "I pull the scarf out from inside the hat."

    n 1dm "..."
    play music tlw
    n 1dn "[player]..."
    n 1du "Y-you really didn’t have to buy me the scarf, y’know..."
    mc "I know I didn’t."
    mc "I just wanted to."

    "I hold it out, and she reaches out to grab it."
    show natsuki 1ej
    "Draping it around her neck, she beams at me, speechless."

    n "[player]...."
    n 1el "I..."

    scene n_mod_cg2_base
    show n_mod_cg2_2 zorder 1
    show n_cg1_dust1 zorder 5
    show n_cg1_dust2 zorder 6
    show n_cg1_dust3 zorder 7
    show n_cg1_dust4 zorder 8
    with dissolve_cg
    "Natsuki grabs the sleeves of my jacket."
    "I pull her in close and embrace the moment for as long as possible."
    "Her grip loosens a little."

    show n_mod_cg2_1 zorder 2 at cgfade
    n "S-sorry..."
    mc "You shouldn’t be."
    n "Okay... I just couldn't stop myself..."
    mc "It's fine, Natsuki."
    mc "In fact... this is great."
    show n_mod_cg2_3 zorder 3 at cgfade
    n "Ehehe~"
    n "Thanks, [player]..."
    show n_mod_cg2_2 zorder 4 at cgfade
    n "For everything you've done for me."
    n "I..."
    n "I never want this to end."
    mc "Nor do I."

    "We remain together for a little more."
    "Eventually, our responsibilities get the better of us, and we separate."
    scene black with dissolve_cg
    "I take Natsuki by the hand, and we walk to the grocery store."
    "We grab all the ingredients we’ll need for tonight and head on our way."
    scene black with dissolve_scene_full
    scene bg residentialsnown
    show n_cg1_dust1 zorder 2
    show n_cg1_dust2 zorder 3
    show n_cg1_dust3 zorder 4
    show n_cg1_dust4 zorder 5
    with dissolve_scene_full

    show natsuki 2ec zorder 1 at t11
    n "H-hey, [player]..."
    n 2ek "I can carry some of those for you."
    mc "No need. It’s my turn to do some heavy lifting."
    "The pain in my shoulder slowly returns, leaving it aching."
    "I do my best to ignore it."
    scene bg housesnow
    show n_cg1_dust1 zorder 2
    show n_cg1_dust2 zorder 3
    show n_cg1_dust3 zorder 4
    show n_cg1_dust4 zorder 5
    with wipeleft
    "As we approach my house, I take a peek over to Sayori’s window."
    "Her bedroom light is on."
    "I think back to the hospital."
    "I told her I would be there for her no matter what."
    "Did I break that promise by letting Natsuki stay with me?"
    "No."
    "No, when I explain the situation with Natsuki..."
    "Sayori will understand."
    "I know her."
    "We arrive back at my house."
    "I set the bags onto the ground to unlock the door."
    "Natsuki wanders toward the gate."
    show natsuki 3em zorder 1 at t11
    n "I don’t want to go inside..."
    n 3es "Not just yet."
    n 4es "It sounds childish, but I kinda wanna enjoy the snow."
    n 4et "Only for a little longer."
    mc "Well, wait there and I’ll be right back."
    scene bg kitchen with wipeleft
    "Swinging open the door to the house, I make a beeline for the refrigerator."
    "I hurriedly throw everything inside, not even bothering to take the food out of their bags."
    "I return outside."
    scene bg housesnow
    show n_cg1_dust1 zorder 2
    show n_cg1_dust2 zorder 3
    show n_cg1_dust3 zorder 4
    show n_cg1_dust4 zorder 5
    with wipeleft
    "Natsuki is nowhere to be seen."
    "Now where'd she-{nw}"
    play sound "sfx/slap.ogg"
    stop music
    show white zorder 6:
        alpha 0.6
        linear 0.25 alpha 0.0
    show natsuki 2ed zorder 1 at i32
    "{i}SPLAT!{/i}"
    hide white
    "From what seemed to be thin air, however, a snowball hits me square in the face."
    "I recoil, stunned."

    mc "H-hey!"
    n 2ez "Ehehe~"
    show natsuki at thide
    hide natsuki
    play music thenumbers
    "That's it. If she wants a snowball fight, I'll give her a snowball fight."
    "I duck for cover behind a bush, as she’s already packing another."
    "I begin to collect my own."
    "I hear her footsteps crunch in the snow as she creeps toward me."
    "As I poke my head around, I’m clipped by Natsuki’s next snowball."
    show natsuki 1eb zorder 1 at t11
    mc "Nice try!"
    n 1ed "Aha!"

    "I return fire on her."
    "I hit her in the back as she retreats toward the gate."
    show natsuki 1ex at s11
    stop music fadeout(5.0)
    "Natsuki lets out a yelp, and falls to the ground."
    "Natsuki, now on her hands and knees holds her back in pain."

    mc "Oh God, are you okay?!"

    "I rush over to her side, taking a knee to make sure she’s not injured."
    mc "Natsuki, I’m so sorry-"
    show natsuki 1ed at h11
    "Natsuki scoops a mound of snow up and throws it at my face."
    show natsuki 1ez at lhide
    hide natsuki
    "She hops back onto her feet and runs inside, giggling."
    "Stunned and covered in snow, I sit and process what just happened for a moment."
    "I brush myself off and head back inside."
    scene bg kitchen with wipeleft
    "Natsuki is washing her hands in the kitchen."
    show natsuki 4cj zorder 1 at t11
    play music thenumbers
    mc "You win this time."
    mc "Don’t think I’ll fall for that again."
    n 3cc "Oh yeah?"

    "She leaves the water running for me as I proceed to wash my hands as well."
    "I splash some room-temperature water on my face."

    mc "Ah... "
    mc "That’s nice."
    n 4ct "Oh come on, I could’ve done so much worse!"

    "I dry my hands and face using a flannel."
    "I open the fridge and start unloading the bag of ingredients onto the counter."

    n 4ce "Whadda you think you’re doing, [player]?"
    n 4cb "Sit your ass down, I’m cooking tonight."
    mc "You don’t want my help at all?"
    n 4cd "Nope!"
    n "I can handle it."
    n 3cc "I mean, you did your part by carrying everything for me."
    n 3ck "And it’s the least I can do since you’re letting me stay here."
    "I shrug."
    "Not about to say no to a meal cooked for me, by Natsuki of all people."
    mc "If you insist, aha."
    show natsuki at thide
    hide natsuki
    "I take a seat at the table."

    mc "I’m right here in case you need a hand, ‘kay?"
    show natsuki 1ck zorder 1 at t11
    n "You’re just going to watch me cook?"
    mc "That a bad thing?"
    n 1ca "Well, n-not really."
    n "You might want to pay attention to what I’m doing though."
    n 2cy "Considering you almost set your house on fire making those pancakes."

    "I can feel the blood rush to my face."

    mc "You’re never gonna let me live that down, are you?"
    n "Nope!"
    n 2cz "Ehehe~"

    "Natsuki moves fluidly around my kitchen."

    n 1cl "You really need to learn to manage your time in the kitchen."
    show natsuki at t41
    n "Cooking and baking should be fun, not a pain in the ass."
    show natsuki 1ck at t22
    n "If it’s stressing you out, then you’re probably doing it wrong."
    mc "That’s very poetic of you, Natsuki."
    show natsuki 1cd at t11
    n "Ehehe~"
    n 1ct "I {i}might've{/i} heard it on a cooking show."

    "Natsuki resumes her work as I watch from the table."

    n 3cl "Okay! Now I just need to let this simmer for a few minutes and we’ll be set!"
    mc "Really? That quickly?"
    n "What'd you expect?"
    n 3cy "I’m a pro! I can do it in no time!"

    "Natsuki begins to set the table."

    mc "Wait, let me sort this out."
    mc "I’ve done practically nothing anyway."

    "I position the placemats and the silverware on both sides of the table."
    "Natsuki divides the food onto our plates."
    "The scent of chicken and sauteed vegetables fills the kitchen."

    n 3ck "It’s only a stir fry, [player]."
    n "It’s not {i}that{/i} special."

    "She must have seen the look on my face."

    mc "You sure? It smells great."

    "She talks about it like it’s nothing, but I can tell she’s revelling in the compliment."
    show natsuki at thide
    hide natsuki
    "We sit at the table and eat our dinner."
    "After we’re both finished, I take our dishes and place them in the dishwasher."
    "I fill the sink full of hot, soapy water and let the pan soak for a few moments."
    "Natsuki’s already made her way to the couch and started looking for something to watch."
    "She shouts out to me from the next room over."

    n "[player]!"
    n "Anything you wanna watch?!"
    mc "Unless you got something in mind, not really!"

    "I scrub the pan hastily and toss it in with the rest of the load."
    scene bg mclivingroomn with wipeleft
    "I enter my living room to find Natsuki staring out the window."
    show natsuki 1cm zorder 1 at t11
    n "Aww, it’s stopped snowing..."
    mc "It’ll probably be gone by tomorrow..."
    mc "Hey, at least we got to have our fun with it, right?"

    show natsuki 1cj
    "Natsuki nods in agreement."
    "Natsuki flips through channels."
    "Soap, drama, comedy, comedy, soap, documentary, soap, game show, etcetera, etcetera..."

    n 1cb "Ugh, there’s never anything good on..."
    mc "I know."
    mc "You want to look for a movie instead?"
    n 1ck "Sure!"

    "I open the streaming app I like, and Natsuki begins to browse the selection."
    "She picks a cutesy love story."
    "I didn’t even get a chance to read the title before she hits the play button."

    n 3cj "I love this movie so much."
    n 3cc "I used to watch it all the time because..."
    n 1cm "Because..."
    stop music fadeout(5.0)
    n 1cn "..."
    n "[player], I forgot..."

    "Natsuki pauses the movie and turns to me."

    n 1cu "About everything..."
    play music glasseyes
    n 1cta "M-my father..."

    "I can see the tears forming in her eyes."

    n 1ctg "[player]..."
    n "H-he has a problem..."
    n 1ctd "He’s been like this ever since..."
    n "Ever since m-my mum left us."
    n "I-I... I think I was five..."
    n "Looking back, I can get why she stopped talking to him - he was a terrible person before - but..."
    n 1cte "Why me?"
    n "W-what did I ever do?"
    n 1ctg "I-I think my dad blames me for her leaving."
    n "I think that’s the reason he drinks so much."
    n 1cth "H-he always t-tells me I-I-I r-remind him of... h-her..."
    n 1ctf "A-a-an-and t-that he h-hates it..."
    n "I-I-I..."

    "Natsuki can’t even speak, the sobbing is drowning her voice."

    mc "Natsuki..."
    mc "Just try and breathe, okay?"
    mc "Take your time."
    mc "We don’t have to talk about this right now..."
    mc "We can save this for another day if-"
    n 1cth "N-no, [player]..."
    n "I n-n-need you t-to k-know."
    n "[player], since I was fourteen..."
    n "H-he’s resorted to..."
    n 1ctg "T-to borderline torturing me for existing."
    n "He only brings home food once a week..."
    n "And it’s usually just leftovers from a restaurant..."
    n 1ctd "And when he drinks..."
    n "H-he sees me as my mother..."
    n 1cte "That day you saw me in the hospital..."
    n "T-that wasn’t even the worst."
    n 1ctd "B-b-believe me..."
    n 1cte "I-I’ve tried to run away from him before."
    n 1ctg "A couple years ago, I f-found my mum's address."
    n "I-it’d been s-something like eleven y-years since I’d s-seen her."
    n "I took the train to her city and when I knocked on her door..."
    n "She..."
    n 1cte "[player], she slammed the door in my face..."
    n "Telling me that she left for a reason, and that she ‘didn’t want me’..."
    n "So I came back home because I had nowhere else to go..."
    n 1ctg "H-he found out I went to see my mother."
    n "That’s when he really started to take his anger out on me..."
    n "He... beat me to the point I had to cover it up with make-up just to be able to go to school."
    n 1cte "Of course, no-one noticed."
    n "I secretly hoped that... someone would think something was up."
    n "That I’d have to explain myself."
    n 1ctd "But they never did."
    n 1ctg "I mean, I was trying to cover up, so I can’t really blame them..."

    "She takes a moment, wiping her eyes with her sleeve."

    n 1cta "The other night..."
    n "Y’know, the... the drinks..."
    n "That was the only escape I could think of."
    n "I’d gone back to the doctor’s, a few hours after you saw me."
    n "He gave me painkillers for my ribs..."
    n "So I stole a bottle of wine from Dad’s rack in the basement."
    n 1ctb "I’ve tried everything to get away from him but every time.."
    n 1ctc "Every god damn time, I would always fail..."
    n "And have to go back."
    n "[player]..."
    n 1ctg "I wanted to die."
    n "I really wanted it."
    n "All to get away from him."
    n "I thought the pills would’ve been enough..."
    n 1ctd "But I guess the few that I had left when I was ready to... to go, weren’t."
    n "And I’m glad..."
    n 1cm "Because you came to check on me."
    n "You were worried."
    n "You cared about me."
    n 1cn "I never thought I’d have this, [player]."
    n "I never thought I would feel t-this way."
    n "This..."
    n 1ctg "This... is the f-first time I can remember, w-where I’ve felt truly happy."
    n "All those y-y-years..."
    n "All t-the pain..."
    n 1cth "N-n-nothing can c-ch-change the p-past..."
    n 1ctf "B-but..."

    "I grab Natsuki by the shoulders and hold her tight."
    "Natsuki buries her face into my chest."
    "She’s sobbing uncontrollably."

    mc "I won’t let anything else happen to you, Natsuki."
    mc "I promise."
    mc "You’re here now."
    mc "I’m always here for you..."
    mc "No matter what."
    mc "Do you understand?"

    "She nods her head, keeping it embedded in my chest."
    "I sit there with her for awhile."
    "I don’t know what else to do other than let her cry."
    show natsuki at thide
    hide natsuki
    "She’s held all of this in for so long."
    "She needs to let it all out."
    "After a long time, she sits back upright, wiping the tears from her face."
    "While she’s drying her eyes I glance at the clock."
    "It’s getting really late."
    "If we plan on attending class tomorrow, we should go to bed."
    "Although, there really isn’t much point in going."
    "We’ve already missed a good part of the week anyways."
    show natsuki 1cn zorder 1 at t11
    n "Th-thank you, [player]."
    n "For reading with me at the club..."
    n "For helping me bake for the festival..."
    n 1cta "For saving my life."
    n "For... for everything, really..."
    n 1ctg "I-I..."
    mc "It’s no problem, Natsuki."
    mc "I’ll do it again for you."
    n 1cte "Y-you’re so sweet."
    n "I..."
    mc "Natsuki, from the day I laid eyes on you..."
    mc "I thought you were perfect."
    mc "So I tried to impress you."
    mc "With my trash poems."
    mc "It's why I spent so much time with you."
    show natsuki 1cta
    mc "I really wanted to get to {i}know{/i} you."
    mc "Everything about you was just..."
    show natsuki 1cu
    mc "Wonderful."
    mc "But..."
    mc "There’s one thing, that I can’t stand."
    mc "You hid this pain from me..."
    mc "I could’ve helped sooner..."
    mc "I understand that you had your reasons for not telling me, but..."
    mc "Natsuki..."
    mc "I really don’t know what else to say other than..."
    show natsuki 1cn
    mc "I love you."
    mc "Everything about you makes me feel a way I’ve truly never felt before."

    "Natsuki doesn’t know what to do."
    "She sits there for a moment."

    n 1cm "I-I-I..."
    n 1cu "I love you too, [player]."

    show natsuki 1ctf
    "She’s weeping again. This time, tears of joy, it seems."
    "She wraps her arms around me again, significantly tighter than before."
    "I can’t help but think back to the hospital."
    show natsuki at thide
    hide natsuki
    "When Sayori told me that she loved me."
    "Is this part of the reason I couldn’t say it back?"
    "..."
    "Yes. "
    "It is."
    show natsuki 1ck zorder 1 at t11
    n "D-do you still want to watch the movie, [player]?"
    mc "Of course."

    "We resume the movie from the beginning."
    scene black with dissolve_scene_full
    stop music fadeout(2.0)
    scene bg mclivingroomn with dissolve_scene_full
    "As the movie credits roll, I realize it’s now early morning."
    "I nudge Natsuki to stand and she follows."
    "I head to the kitchen for a drink and Natsuki lingers behind me."
    scene bg kitchen with wipeleft
    show natsuki 1cm zorder 1 at t11
    play music tlwamsp
    n "[player]..."
    n "Can we- u-uh..."
    n 1cn "Can we sleep together again?"
    n "I really..."
    n 1cq "I really liked it, okay?"
    mc "I... sure."
    mc "Come on, then."

    scene black with wipeleft
    "Natsuki and I head upstairs to her bedroom."
    "I let her in to change first."
    "She closes the door on me and I wait patiently outside."

    n "J-just because I said I love you... that doesn’t give you the right to peep!"
    mc "I know, I know."
    mc "I'll stay out, I promise."

    "Of course I won’t invade her privacy."
    "{i}Not without her consent, anyway.{/i}"

    n "Okay, I’m ready."
    n "Come in!"
    scene bg spareroomn with wipeleft
    "I inch the door open, and Natsuki is already in bed."
    "I grab my pyjamas from my drawer and take off my top as-"
    show natsuki 4cp zorder 1 at t11
    n "E-eh?!"
    n 4co "D-did you really just... in front of me?"
    mc "What’s the problem?"

    show natsuki 4cs
    "Natsuki seems tense."
    "As if she wants to say something, but is withholding it."

    n 4cq "Dummy..."
    mc "O-oh, right."

    "I was about to get undressed in front of her."
    "Do I ever stop and think about anything?"
    scene black with wipeleft
    "Moving out into the hall for a moment, I get changed into my pyjamas."
    "I come back in."
    scene n_mod_cg1_base
    show n_mod_cg1_2
    with wipeleft
    "I climb onto bed after turning off the light."
    "Natsuki immediately rolls over and holds me tight as she did the night before."

    n "Night, [player]."

    scene black with dissolve_scene_full
    stop music fadeout(2.0)

    $ quick_menu = False
    scene black
    show friday
    with dissolve_scene_half
    $ renpy.pause(delay=2.0, hard=True)
    $ quick_menu = True

    scene black with dissolve_scene_full
    "{i}BEEP.{/i}"
    "{i}BEEP.{/i}"
    "{i}BEEP.{/i}"
    "{i}BEEP.{/i}"
    "{i}BEEP.{/i}"
    "I jerk awake, waking Natsuki as well."
    scene n_mod_cg1_base
    show n_mod_cg1_10
    with dissolve_cg
    mc "Ah, sorry..."
    mc "I forgot to turn my phone off."

    show n_mod_cg1_7 at cgfade
    "Natsuki lays back down and closes her eyes."

    n "It’s fine, [player]."

    "I check my phone to see who tried to call me."
    "Sayori’s mother?"
    "That can’t be good."
    scene black with dissolve_cg
    play music tinkertailor
    "Climbing out of bed and moving into the hall, I call her back and ask if everything is alright."
    "No, everything is not alright."
    "She explains to me that Sayori had a meltdown last night."
    "She was hysterical."
    "Screaming that she wanted to die, that life is nothing but pain, nothing but seemingly endless suffering."
    "She tells me that Sayori has been admitted to the hospital. Apparently the two of them will be back in a few days."
    "She also instructs me to check my mail."
    "Apparently Sayori came by last night to see us when we got back."
    "Instead of knocking she dropped a letter off."
    "I wish Sayori and her well, and head downstairs."
    scene bg mclivingroom with wipeleft
    "I can’t believe this happened again..."
    "At the foot of the door, there’s an envelope with my name on it."
    "Tearing it open, I begin to read..."

    python:
        if persistent.language == "spanish":
            poem_s4 = poem_s4_spanish
    call showpoem (poem_s4) from _call_showpoem_2

    "I can’t believe what I’m reading..."
    "Not again."
    "I’m glad her mum took her to the hospital."
    "I notice a note written on the back."

    python:
        if persistent.language == "spanish":
            poem_s5 = poem_s5_spanish
    call showpoem (poem_s5) from _call_showpoem_3

    "I feel sick."
    "I can’t believe this."
    "Natsuki walks up behind me."

    show natsuki 3ck zorder 1 at t11
    n "What’s the matter?"

    "I wordlessly hand her the poem."

    n 1cm "Oh, God..."

    "Natsuki is about to hand it back to me, before she notices the scribble on the back."

    n 2cq "Wait, there's more..."

    "It takes her a second to process what it meant."
    "She loosens her grip on the paper, letting it fall out of her hands."

    n 1cu "O-oh..."
    n 1cn "How does she even...?"
    mc "No clue..."

    "We both stand in the doorway for a moment."
    "Eventually we both take a seat on the couch together."

    n 1ch "You should call, maybe ask her mum if she wants you to visit."
    mc "T-that’s a good idea."

    show natsuki at thide
    hide natsuki
    "I ring Sayori’s mother and she answers right away."
    "I ask if Sayori would like me to visit."
    "According to her, she'd love it."
    "I let her know I’ll be there as soon as I can."
    show natsuki 1ci zorder 1 at t11
    mc "Looks like I'm going right now."
    mc "You coming with?"
    n 1cn "No. I don’t really want to get involved."
    mc "So, you’ll be okay here by yourself for a few hours?"
    n 1cq "Yeah. I’ll just watch TV or something."
    n "I think I'll get my clothes washed... I've been wearing your stuff for two days now."
    mc "Alright, sure."

    "I take my phone and my keys off the table."
    show natsuki 1cj
    "I nip her on the cheek as I pass by her seat again."

    mc "Okay, I’ll see you in a bit."

    scene bg house with wipeleft
    "I lock the door behind me, heading to the bus stop."
    "I barely make it to my stop in time."
    scene black with dissolve_scene_full
    stop music fadeout(2.0)
    scene bg hospital with dissolve_scene_full
    play music giveup
    "It’s only a short ride to the hospital."
    "I enter through the emergency doors."
    "Moving as quickly as is allowed, I find the reception desk, and explain that I’m here to visit Sayori."
    "They give me Sayori’s room number."
    "I move quickly to the mental health wing."
    "I find her number and enter the room."
    scene bg nurse with wipeleft
    show sayori 1ci zorder 1 at t11
    mc "Sayori..."
    s "[player]."

    "Sayori’s mother leaves the room to give us privacy."

    mc "I found your... poem.."
    s 1cj "I'd figured."
    mc "Sayori, what’s the matter?"
    mc "I told you, I’m always here for you."
    mc "Speak to me."
    s 1ci "Well, last night I wanted to..."
    s 3cg "But all I could hear through the door was you.."
    s "You and her, laughing."
    s 3ch "It was like the two of you were laughing at me."
    mc "Sayori, you don’t understand..."
    s 3cd "No, I get it. It makes perfect sense."
    mc "Sayori, I-"
    s 1cd "Do you know how much it hurts to see you so happy?"
    s "To know that I’ll never be needed?"
    s 1cl "It feels like a knife being plunged into my chest, [player]. Over and over and over again."
    s 1cy "And I-I can’t stand it anymore."
    mc "Sayori, Natsuki is staying with me because-"
    s 1cd "[player], you don't need to rub it in."
    s "You're happy with her. You don't need me anymore."
    s 2ct "T-there's no point hiding it."
    s "Just go."
    mc "Sayori, please, just let me explain..."
    s 2cu "[player], go away, please!"

    "Having heard the commotion, a nurse peeks her head through the door."
    "She asks if there’s a problem."

    s 2cv "Please, just get him out of here..."
    mc "Sayori, wait. Please..."
    scene bg hospital with wipeleft
    "Complying with the nurse’s requests to leave, I'm forced to make my own way out of the wing."
    "I'm escorted back to the reception area, where I'm instructed to leave."
    scene bg street with wipeleft
    "As I'm walking down the street, Sayori’s words ring in my mind..."
    "I caused this."
    "This is my fault."
    "I can’t believe this is happening, again."
    "Turning the corner to my stop, I watch as the bus speeds off."

    mc "God damn it."

    "I begin my walk back to my house."
    scene black with dissolve_scene_full
    stop music fadeout(2.0)
    scene bg house with dissolve_scene_full
    "It took me a lot longer to get back home than I thought."
    "I open my front door."
    scene bg spareroom
    show black zorder 5
    with wipeleft
    mc "Natsuki? You there?"

    "No answer."
    "I check downstairs, but she’s nowhere to be found."

    mc "Natsuki?"

    "I head upstairs, and hear a rustling coming from the guest room."
    "I gently open the door."

    mc "Natsu-{nw}"
    play sound "sfx/slap.ogg"
    hide black
    show white zorder 6:
        alpha 0.6
        linear 0.25 alpha 0.0
    show natsuki 3hp zorder 1 at i32
    "{i}Urrghhhh!{/i}"
    hide white
    "Natsuki punches me in the stomach, almost dropping her towel in the process."

    n "[player]?!"
    n 3ho "Do you ever knock?!"
    mc "Sorry!"
    n 1hv "Get out, pervert!!"
    mc "S-sorry!"

    scene black with wipeleft
    "I manage to get that out before Natsuki slams the door in my face."
    "Keeling onto my knees, winded, I gasp for air."
    "It takes me a moment to collect myself, but I get back to my feet."
    play music tinkertailor
    "From the hallway, I repeatedly apologize through the door."

    n "[player], you gotta be more careful!"
    n "You could’ve seen me..."
    n "Y’know..."
    mc "I know, I know. It was an accident."
    mc "I’m sorry, okay?"
    mc "You didn’t need to hit me so hard though!"
    n "I-I wasn’t sure it was you until I’d already hit you!"
    n "I... I’m sorry too."
    n "Just... please knock next time, okay?"
    mc "I will, don’t worry."
    n "Now, give me a minute to get ready."
    mc "Sure. I guess I'll just be in my room."

    "I retreat to my room and wait."
    scene bg bedroom with wipeleft
    "While I’m sat at the computer, my phone pings from across the room."
    "Picking it up, I see it’s a text from..."
    "Yuri?"
    "How’d she get my number?"

    y "Is this [player]’s number? It’s Yuri."

    "I have no choice but to reply."

    mc "Yeah, it’s me. What’s up?"
    y "I need to talk to you about what you saw yesterday."
    stop music fadeout(2.0)
    "I stare at it for a minute."
    "She wants to talk about the cuts, or..?"

    mc "Are you talking about your arms?"

    "She takes a moment to respond, sending over a sizeable paragraph."

    play music climbingup
    y "Yes."
    y "I was never given a chance to explain myself."

    "I'm going to have to be careful with how I word my sentences."

    mc "Well, I'm going to ask the questions then."
    y "All right."
    mc "Did you cut yourself because you might be depressed?"
    y "No, I'm not depressed."
    y "In fact, it's quite the contrary. The pain is what motivates me."
    y "It's so exhilerating. It’s almost like a high."
    mc "Then... how did you start?"

    "She takes her time writing out her response."
    "The three pips indicating that she's typing flicker, one by one."
    "Eventually, her explanation comes out as a large paragraph."

    y "Well, I've always had a morbid fasciantion with knives. From when I was young."
    y "Before I started, I'd just collect them. All different styles, engravings, colours..."
    y "They really are beautiful."
    y "And well, while reading a book some time ago, the topic came up..."
    y "I was only going to try it once, to see what it felt like."
    y "But it grew into a fully fledged addiction."
    y "I know, courtesy of Monika, that that's not a good position to be in, but I can’t stop."
    y "There’s just something about the blade effortlessly slicing open my skin that excites me."
    y "It’s such a thrill. I can’t help it anymore. The sensation... it's too powerful."

    "That's not healthy."
    "This is... something else."
    "I don't even know what to do."
    "But there's something nagging at my mind..."

    mc "Speaking of Monika..."
    mc "How'd she find out?"

    "Another few minutes pass."
    "Another paragraph."

    y "It was one day after the club had ended, no more than two weeks ago."
    y "I don't even remember what I was doing at the time..."
    y "But my sleeve slipped up, and Monika saw everything."
    y "We spoke about it for a few hours. She even invited me to her house to talk in private."
    y "She tried to help. I could tell she cared. But nothing she suggested actually worked."
    y "After she had to shut down the Literature Club's festival, she took it out on me."
    y "She assumed that I was going to blame her, even though I really didn't think any less of her when she had no choice but to postpone it."
    y "All I said was that she should have tried to get in contact with everybody before the festival started..."
    y "She didn't really take it well."
    y "She threatened me, telling me not to \"make a scene\" about the festival in front of the rest of you or she'd tell everybody about my arms."
    y "I was very shaken by what she said, not just because of what she was threatening..."
    y "But because I'd never seen that side of her."
    y "And if I'm honest with you, [player]..."
    y "She scares me."

    "Once again, I'm at a loss for words."
    "I don't know the full story. I can't approach it now..."
    "I hesitate."
    "If anything, I just want to convince Yuri to seek professional help for her self-harm."
    "If I have a say in it, that can't go on any longer."

    mc "I see..."
    mc "And have you considered getting help for your arms?"
    y "How can I convince myself to \"get help\" when I’m the best I’ve ever been?"

    "\"The best\" she’s ever been?"
    "I don’t think she understands what she’s getting herself into..."
    "Not to say that I fully do..."

    mc "Right..."

    "I can hear Natsuki moving through the house, humming to herself."

    mc "Well, I've got to go. See you later."
    y "Alright, [player]. I'll speak to you another time. In the club perhaps."
    y "But I just wanted to thank you for trying to help."
    y "Even if it won't change much... it shows that you care."
    y ":)"
    mc "I do care."
    mc "Bye, Yuri."
    stop music fadeout(2.0)
    "I send her a final text, throwing my phone onto my bed."
    "Natsuki knocks on my door."

    mc "Yeah, come in."
    play music tinkertailor
    show natsuki 1bl zorder 1 at t11
    n "See? It’s not that hard, [player]."
    mc "I said I was sorry! What more do you want?"
    n 1ba "Hmm..."
    n 4bl "Ooh! I know!"
    n "You can carry my Parfait Girls collection home for me!"
    mc "So, this is your home now, eh?"
    n 1bs "U-uh, sorry..."
    n "I didn’t mean it like that..."
    n "I just thought I could..."
    n "Y’know..."
    n 1ba "Stay here..?"

    "I'm a little worried I took my teasing too far..."
    "How could I say no to her?"

    mc "Well..."
    mc "Of course, Natsuki."
    mc "I was only trying to tease you..."
    mc "Though now that you mention staying, you might actually need this."

    "Turning to my bedside drawer, I rummage through it for a second, looking for my spare house key."
    "My phone beeps, and Natsuki beats me to checking it."
    show natsuki 1bp at h11
    "Opening the message, Natsuki recoils, dropping my phone to the floor, disgusted."

    mc "Hey, watch it!"

    "As I go to pick up the phone, I see for myself what had sickened Natsuki."
    "It’s a picture of Yuri... "
    "She’s sitting on her bed. Her scarred arm is covering her otherwise bare legs."
    "She’s wearing a purple bra, a small crimson heart drawn on her left breast with a red marker."
    "Or at least I hope it is..."
    "I don’t know how to respond."
    "Closing my messages down, I throw my phone back onto the bed."
    "Natsuki is distraught."

    n 4bo "[player], what the hell was that doing on your phone?"
    mc "I-I-I don’t know."
    n "And her arms..."
    n 4bn "The heart?"
    mc "W-we were talking about her arms, before."
    mc "I told her to get some help, but she wasn’t listening to me."
    mc "Natsuki, I promise you, I didn’t say anything to... encourage her to send something like that to me."

    "I retrieve my phone from my bed and show Natsuki the messages regarding her arms."
    "I purposefully keep the messages regarding Monika hidden, as I don't want Natsuki to jump to conclusions."
    "She’s as confused as I am."

    mc "Yuri... she needs serious help."
    n 4bu "Clearly..."
    n "But why’d she send that to you?"
    n 3bq "And be so open about this with you?"
    mc "Well, I saw her arms yesterday..."

    "As before, I omit Monika from the incident."

    mc "She told me not to tell anyone, so I didn’t, because I didn’t know what the hell else to do."
    n 5bw "[player], you know we’re gonna have to talk to her about... this."
    n 1bw "It... it’s not healthy to be cutting like that."
    n "And it doesn’t help that she clearly gets off doing it."

    n 3bn "There must have been something, something in her head... that made her think that this was okay."
    n "I’ve known Yuri for as long as I’ve been at the club, and yeah, she gets overly attached the moment anyone shows her any attention."
    n 3br "I hate to say that but it’s true..."
    n 1bu "But holy crap..."
    n "I’ve never seen anything like {i}that{/i} before."
    mc "Well, we’ll talk to her the next chance we get, okay?"
    n 1bc "Alright, [player]."
    mc "Oh, and before I forget..."

    "I take the spare house key from my desk drawer, and hand it to Natsuki."
    "To my surprise, Natsuki’s mood seems to completely shift."
    "She pauses for a moment before jumping into my arms."

    n 1bz "[player]!"
    n "Ehehe~"
    n "Thanks!"
    n 2bz "You’re the best boyfriend ever!"

    "As those words escape Natsuki’s mouth she jumps back."
    "That was the first time she’s called me that."
    "I can’t help but smile."
    "Hearing her call me that made the texts with Yuri... Monika's argument... everything... melt away."
    "They didn’t matter."
    "The more time I’ve spent with Natsuki, the more frequently I’ve felt this way."
    "Waking up next to her..."
    "Reading with her..."
    "Hearing her tell me she loves me..."
    "Feeling her arms wrapped around me..."
    "I never thought I could feel this way about someone."

    mc "Natsuki..."
    mc "You’re the best girlfriend I could have asked for."
    n 1bt "You’re just saying that, aren’t you?"
    mc "No, Natsuki."
    mc "I’m not just saying that."
    mc "I love you, more than words can let me describe."
    n 5bq "I..."
    mc "So it’s official then?"
    n 1bl "Y-yeah..."
    n "I guess so."
    n "I love you so much, [player]."

    "I pull Natsuki close to me, holding her tight."
    "She pulls back for a moment and stares at me."
    "I lift her chin up, and kiss her."

    n 5bz "Ehehe~"

    "Natsuki buries her face into my chest again, and squeezes me as tight as she can."

    n 1bz "I never want this to end."

    "The two of us stay locked in this embrace for what feels like an eternity, but in reality probably only lasted a few minutes."
    "Just as we’re separating, the doorbell rings."

    n 1bt "You wanna get that?"

    show natsuki at thide
    hide natsuki

    "I nod."
    scene bg mclivingroom with wipeleft
    "Natsuki heads back to the bathroom, and I head downstairs."
    "I wasn’t expecting any visitors today."
    "I peer through the peephole."
    "It’s Monika, waiting patiently for an answer."
    "{i}How does she know where I live?{/i}"
    "I crack the door open and slip outside."
    scene bg house with wipeleft
    show monika 2d at t11
    m "Hi, [player]."
    mc "Oh, hey."
    mc "Shouldn’t you be at school?"
    m 2i "Shouldn’t you?"
    mc "..."
    mc "What do you want?"
    m 1q "To apologize for the past few days."
    m "I was a..."
    m "Well, I wasn’t very nice to anyone."
    m 1f "I’ve just had a lot going on this past week and..."
    mc "Sorry doesn’t fix everything."
    m "I know..."
    m 1q "I just need to tell you something."
    m "I know this doesn’t excuse my actions..."
    mc "What is it?"
    m 1h "I told my parents about the festival..."
    m "They told me how disappointed they were in me."
    m "They think that I have no control over my club."
    m "The fact I couldn’t get four people to show up on a special day like that..."
    m 1q "[player], they’ve only ever expected the best from me."
    m "There’s a reason I always try to be so perfect all the time."
    m "That’s why I have been so harsh this week..."
    m 2f "I was just trying to control things that I shouldn’t be."
    mc "Monika..."
    mc "What about Sayori?"
    mc "You saw her poem..."

    "I lower my voice a little."

    mc "You {i}knew{/i} it was a suicide note."
    m 4d "For the record, [player]..."
    m "I didn't."
    m "It was worrying, sure, but I'd never interpreted it as that."
    m "She ended up confessing everything to me over text on Wednesday."
    m "But, still..."
    m 4r "It’s okay if you don’t accept my apology, [player]."
    m "I understand."
    m "I was heartless."
    m "I said things I don’t think I’ll {i}ever{/i} be able to take back."
    m "I know that."
    mc "I can’t say that I forgive you for what you’ve said and done to all of us."
    mc "Especially what you did to Yuri."
    m 4d "I-I know..."
    mc "But, seeing your perspective..."
    mc "I think I’m willing to give you a second chance."
    m 1d "That's all I needed."

    "My front door opens."
    show monika 1c at t21
    show natsuki 4bd at t22
    n "Oh, there you a-"
    show natsuki 4bf at h22
    n "..."
    n "What the hell are you doing here?"
    n "[player], why is she here?"
    mc "Natsuki, she’s here to apologize."
    m "Wait...."
    m "What are {i}you{/i} doing here, Natsuki?"
    n 5bo "T-that doesn’t matter!"

    "Oh, you've got to be kidding me."
    "Of all people to find out..."

    m 3p "There’s something going on between you two, isn’t there?"

    "I need to change the subject."

    mc "Monika, we accept your apology."
    n 5bp "Hey, speak for yourself!"
    mc "We’ll see you at the club later, okay?"

    "I slowly inch the door shut, but Monika resists."

    m 1l "Ahaha, not yet."
    m "You didn’t answer my question, [player]."

    "My brain goes blank."
    "I’m panicking internally."
    "I don’t want her to know about Natsuki and I, for fear of her intervening..."
    "But, I also don’t want Natsuki to be offended if I lie..."

    menu:
        "I'm going to..."
        "Lie.":

            $ mc_lie = True
            call mclie_yes from _call_mclie_yes
        "Tell the truth.":
            $ mc_lie = False
            call mclie_no from _call_mclie_no

label mclie_yes:

    show monika 1d
    show natsuki 5bu
    mc "N-nothing’s going on between us..."
    n 1bp "E-eh?"
    n 5bx "Monika, you’re just going to find out anyway..."
    n "[player] and I are dating..."
    m 2c "Well, I can’t say I didn’t see that coming..."
    m "It {i}was{/i} pretty obvious."
    call script_exitmusic2 from _call_script_exitmusic2


label mclie_no:

    show monika 1d at t21
    show natsuki 5bu at t22
    mc "Well..."
    mc "Natsuki and I... we’re dating."
    mc "Don’t worry, we’ll keep it out of the club."
    mc "I promise."
    m 2c "I hope so."
    call script_exitmusic2 from _call_script_exitmusic2_1

label script_exitmusic2:

    "I can’t bring myself to meet Monika’s eyes."
    "This whole situation is so embarrassing."

    m 4k "Ahaha~"
    m "[player], your face is so red."
    m "So is yours, Natsuki."
    m "You two are pretty cute together!"
    n 1bg "I."
    n 1br "Am."
    n 1bf "Not."
    n 4bv "Cute!"
    m 1b "Well, clearly [player] thinks so."
    n 5br "..."
    mc "She's right, y'know?"
    n 4bv "Shut it!"
    mc "Can we please just change the subject?"
    n 5bf "Yeah, I'd love to."
    n "Well, Monika... I’m still mad at you for the horrible things you said to all of us."
    m 1q "Good. I deserve it."
    m "Be mad at me all you want."
    m 1o "I came here to let [player] know how terrible I felt about all of this."
    m "And well, you too now, I guess."
    n 1bh "Do you really mean it?"
    n "Or is this all just a ploy to get us to go to the club again?"
    m 2q "Well, both."
    m "I started the club so everyone can have a nice place to read, and discuss literature."
    m "And to hang out, make friends."
    m "I don’t want that destroyed."
    m "Just like I don’t want our friendship to be destroyed."
    n 4bn "[player], d'you believe her?"

    "I stop for a moment, thinking it over."
    "Could Monika really expect me to forgive her after what she said to Sayori, and did to Yuri?"
    "Could I actually do it?"
    "I mean, considering her explanation, I feel kind of sorry for the pressure she’s being put under..."
    "That doesn’t take away from what her outburst did, and I'm certainly not about to forget it, but..."
    "So long as it doesn’t happen again, I think I can."

    mc "Well yeah, I do."
    mc "Especially after what she told me."
    n 4bg "Okay, well..."
    n "I'm gonna trust [player] on this one."
    n "I guess we’ll see you at the club later, then."
    m 3i "Thank you! I promise, no more outbursts!"
    n "There better not be..."
    show natsuki at thide
    hide natsuki
    show monika at thide
    hide monika

    "Monika turns to leave, but stops herself."

    show monika 1n at t11
    m "Uhm..."
    m "[player], do you know if Sayori’s home?"
    m "I couldn’t find her at school."
    m "She’s the last one of you I need to apologize to, and she isn’t answering her calls."
    mc "U-uh..."
    mc "I’m not sure."
    mc "You can knock if you want. It’s worth a try."
    m 1l "Right! Thank you two again!"
    m "And I’m sorry!"
    m "See you later!"
    show monika at thide
    hide monika

    "As Monika walks away briskly, Natsuki pulls on my sleeve."

    show natsuki 1ba at t11
    n "Let’s go back in."
    "I open the door and head to the kitchen."
    scene bg kitchen with wipeleft
    show natsuki 1bt at t11
    mc "We have some time before we have to go. D'you want something to eat?"
    n "U-uh... sure..."

    "Something about Natsuki seems off."
    "I can’t pin what it is, but something is bothering her."
    "Could it be Monika?"

    mc "What’s wrong, Natsuki?"

    if mc_lie == True:
        call natsuworry from _call_natsuworry
        call script_exitmusic3 from _call_script_exitmusic3
    else:
        call script_exitmusic3 from _call_script_exitmusic3_1

label natsuworry:

    n 1bq "Just wondering..."
    n "Why'd you bother lying to her about us?"
    mc "I-... I was kinda embarrassed, cause I knew she'd make a big deal about it..."
    n 1bs "Eh, I guess..."
    n "But you know she'd have found out anyway."
    mc "Yeah, probably."
    n "Well, there's something else I was wondering as well..."

label script_exitmusic3:

    n 4bm "Do you think the other girls accepted Monika’s apology?"
    mc "I don’t know..."
    n 4bg "Well.."
    n "I hope so."
    n "It’ll be weird if we show up and it’s only Monika and us."
    n "It won’t really be the same."
    show natsuki at thide
    hide natsuki

    "Natsuki’s right. I didn’t think about that."
    "The club would without a doubt be different without Yuri and Sayori.."
    "Hopefully they accept her apology too."
    scene black with dissolve_scene_full
    stop music fadeout(2.0)
    scene bg mclivingroom with dissolve_scene_full
    "After about an hour of lounging around watching TV, I realize how soon the school day was going to end."

    show natsuki 1ba at t11
    mc "We should get going."
    mc "Give me a second..."
    scene bg bedroom with wipeleft
    "I head back to my room, and quickly get changed."
    scene bg mclivingroom with wipeleft
    show natsuki 4bb at t11
    mc "You’re all ready, right?"
    n 4bb "Well, I still don't have my uniform..."
    n "But there isn't much I can do about that."
    n 2bd "Yeah, I'm ready."
    n "Let's get going."
    scene bg house with wipeleft
    "Natsuki locks the door behind us."
    "As we walk down the street I feel her fingers curl around mine."
    "We continue towards the school."
    scene black with dissolve_scene_full
    stop music fadeout(2.0)
    scene bg courtyard with dissolve_scene_full
    "Natsuki, a little more comfortable being affectionate in public, takes my hand in hers."
    "As we enter the gates of the school, I see Yuri walking across the courtyard."

    mc "Yuri!"

    "Yuri drops her books."
    "She must have not seen us."
    "Letting go of Natsuki’s hand, I reach down to help her."

    show yuri 1a at t11
    mc "Sorry, Yuri..."
    y "I-it’s okay."
    y "You just startled me."
    y "I take it you’re here for the club?"
    mc "Yeah, pretty much. You coming?"
    show yuri at t21
    show natsuki 1bc at t22
    n "Yeah, Yuri, are you?"

    "Yuri nods her head in agreement."

    n 2ba "Good, come on then."
    scene black with dissolve_scene_full
    stop music fadeout(2.0)
    scene bg club_day with dissolve_scene_full
    play music t3

    "We all start off the day in the club as we usually do."
    "Natsuki and I head off to the closet to pick out the next volume."
    "Yuri has her head buried in yet another novel."
    "Monika is off in the corner, writing something in her notebook."
    "Sayori is absent as she has been a lot recently."
    "I would be lying if I said I wasn't worried about her, but there isn't much I can do right now."

    show natsuki 4bd at t11
    n "[player], come on!"
    scene bg closet with wipeleft
    "Monika perks her head up and give me a smirk. "
    "I really wish she hadn’t showed up this morning."
    "I join Natsuki under the window, our usual spot."
    "She’s already grabbed the next volume of Parfait Girls."
    scene bg closet with dissolve_scene_full
    show monika 2j zorder 0 at t21
    show natsuki 3bg zorder 1 at t22
    m "Hey, lovebirds."
    m "So much for keeping it out of the club."
    mc "Give it a break, Monika."
    mc "It’s not like that."
    mc "You know the text in this series is tiny."
    m 4d "Yeah, well-"
    n 5bh "Yeah, [player]’s right."
    n "Not only that, we’ve always sat like this."
    mc "Exactly."
    mc "So what’s the problem?"
    m 1h "I was just making a joke..."
    m "Never mind."
    show monika at thide
    hide monika
    show natsuki 1bj zorder 1 at t11
    "Monika walks away without another word."
    "I may be giving her a second chance, but Natsuki isn’t as forgiving as me."
    "I really can’t blame her."
    "I’m not entirely certain why I’m even here."
    "I’d certainly rather be back home, with her."
    "Well, it’d probably end up being worth coming here today if we can take her manga home with us."
    show natsuki 3bd at h11
    n "H-hey!"

    "Natsuki waves her hand in my face, clicking her fingers to get my attention."

    n 1bc "Are you ready to flip the page yet?"
    mc "U-uh, sorry."
    mc "I wasn’t paying attention and-"
    n 4bg "Jeez."
    mc "Sorry, I just get distracted easily."
    n 1bj "It’s fine, [player]."
    n "I’m just glad to have-"
    "Monika clears her throat."
    show natsuki at t21
    show monika 4b at t22
    m "Okay, everyone!"
    "I note the page we left off with."
    scene bg club_day with wipeleft
    "Natsuki and I join Yuri and Monika back in the centre of the clubroom."

    show monika 2e at t31
    show natsuki 4bc at t32
    show yuri 2e at t33
    m 1a "Does anyone have any poems they want to share today?"
    y "But... Sayori isn’t here yet."
    y 1g "Shouldn’t we wait?"
    m 2c "I couldn’t get a hold of Sayori earlier."
    m "I doubt she’ll be joining us."

    "Sayori."
    "I really do hope she’s getting the help she needs."
    "I may not love her the way she loves me..."
    "But that doesn’t mean I don’t love her at all."
    "I’ve known her for the majority of my life."
    "It kills me to see her in such pain."

    y 3f "Well, okay then."
    show yuri at thide
    hide yuri
    show monika at thide
    hide monika
    show natsuki at thide
    hide natsuki
    "Yuri falls back into her novel."
    "Monika sits back at her desk, clearly agitated at everybody’s lack of effort."
    "Natsuki and I head back to the closet to continue reading."
    scene black with dissolve_scene_full
    stop music fadeout(2.0)
    scene bg club_day with dissolve_scene_full
    "Minutes pass by like seconds, and before either of us realize it, the meeting is over."
    play music t5
    show natsuki 4ba at t11
    n "Ready?"
    mc "Yeah, let's go."
    mc "See you guys tomorrow."
    n 1bd "It's the weekend tomorrow, dummy."
    mc "O-oh, my bad-"
    show monika 2b at t22
    show natsuki at t21
    m "Yeah."
    mc "Alright, alright."
    mc "No need to rub it in, guys."

    "As Natsuki and I are walking out the door, Monika halts us."

    m 3k "Wait a second!"
    m 2b "I can walk you home, Natsuki."
    n 5bs "N-no!"
    n "Er-"
    n 4bt "I’m going over to [player]’s."
    mc "Yeah, we wanted to, uh, keep reading."
    m 4l "Well, another time then."
    show monika at thide
    hide monika
    show natsuki at thide
    hide natsuki
    "Monika smiles sweetly."
    "It’s unsettling due to her behaviour the past few days."
    "But if she's trying to give us a reason to forgive her..."
    "Then maybe she's being genuine."
    scene bg corridor with wipeleft
    "Natsuki and I navigate the halls to the front doors."

    show natsuki 1bm at t11
    n "Eh?"
    n 1bf "Crap, my collection!"
    mc "If you want me to get it, I’ll only be a second."
    n 5bq "If you want..."
    mc "I’ll be right back."
    show natsuki at thide
    hide natsuki
    stop music fadeout(2.0)
    "I take off through the vacant halls."
    "I hope Monika hasn’t left yet."
    scene bg club_day with wipeleft
    play music tinkertailor
    "I make it back to the club before she locks the door."

    show monika 1a at t11
    mc "Hey!"
    mc "Sorry, I forgot something."
    m "Oh! No problem."
    m "I wanted to talk to you anyway."
    scene bg closet with wipeleft
    "Monika follows me towards the closet."
    show monika 2c zorder 1 at t11
    "She blocks the door, looking at me expectantly."

    m "Well?"
    mc "What?"
    m 1c "You remember what I said about living near you, right?"
    m "I've seen her going to your place an awful lot."
    m 3d "It looks to me like she hasn’t been home in days."
    m "Or school."
    m "You’ve been skipping as well."
    mc "Monika, that’s none of your business."
    m 4k "Oh, but it is."
    m "I can’t have my club members missing school."
    m "It reflects poorly on the club."
    mc "Yeah, I get that. We’ve just been-"
    m 1h "Been what?"
    m "Been hiding?"
    mc "N-no..."
    m 2f "Are you sure?"
    m "I found it weird you never invited me in."
    m "Are you two ashamed to be together or something?"
    mc "N-no!"
    mc "It’s not like that at all!"
    m 3k "Well that’s how it looks from the outside looking in, [player]."
    m "You two have to attend, Monday."
    m "A full day of school."
    m 2i "This isn’t a discussion."
    mc "O-okay."
    mc "We’ll be here."
    m 1a "Good."

    "Monika moves to the side allowing me access to the closet."
    "I grab Natsuki’s Parfait Girls collection box and leave Monika behind."

    m 3d "Why are you taking that?"
    mc "Natsuki and I read a lot at home."
    scene bg corridor with wipeleft
    "I hear the lock click as I make my way back to the front doors."
    "Natsuki is waiting for me."

    show natsuki 1bc at t11
    mc "Let's go."
    show natsuki at thide
    hide natsuki
    scene black with dissolve_scene_full
    stop music fadeout(2.0)
    scene bg residential_day with dissolve_scene_full
    play music presenttense
    "Monika’s line of questioning made me a little uneasy."
    "Does she know that we've been basically living together?"
    "More importantly, does she know why?"
    "She’s only known that we’re a couple for a few hours."
    "It’s not like Natsuki would tell Monika that she’s living at my place."
    "Or why she is."

    show natsuki 1bd at t11
    n "[player]..."
    n "Snap out of it!"
    n 4bc "Did you even hear a word I said?"
    mc "Natsuki, I’m sorry."
    mc "I’ve just got a lot on my mind right now."
    n "Whatever. I’ll tell you later, okay?"
    show natsuki at thide
    hide natsuki

    scene bg house with wipeleft
    "We walk for a few minutes and we reach our house."
    "Natsuki unlocks the door for me, as I have my hands full."
    scene bg kitchen with wipeleft
    "I rest the collection on the kitchen table."

    show natsuki 4ba at t11
    n "So do you want to read or watch a show?"
    mc "I actually have to go and do something quick."
    mc "I want to try to explain to Sayori what’s going on, again."
    mc "I’ll be back in a few hours at most."
    n 2bb "O-oh..."
    n "Okay [player]."
    mc "Unless you want to come with me?"
    n "Uhm..."

    "She waits for a second, thinking."

    n 4bt "N-not really."
    n "I don’t think she’d want to speak to me right now."
    mc "That's alright."
    mc "Well, speak to you later, yeah?"
    n "Yeah..."
    show natsuki at thide
    hide natsuki

    "I give her a kiss and leave again."
    scene black with wipeleft
    "I wait for a few minutes before the bus arrives."
    "As the bus navigates through the residential area, I see Natsuki’s house."
    "Her father’s car is still absent from the driveway."
    "That reminds me..."
    n "{i}I still don't have my uniform... but there isn't much I can do about that.{/i}"
    stop music fadeout(2.0)
    "I jolt to my feet and signal for a stop."
    scene bg nhome with wipeleft
    "I rush off the bus and walk quickly down the street."
    "My heart is pounding."
    "What am I doing?"
    "Why am I doing this?"
    "I should be going to visit Sayori, but..."
    "I walk around to the alleyway behind Natsuki’s house."
    "I manage to open the gate from my side."
    "I creep to the sliding doors we escaped through."

    mc "Please open..."

    "I reach for the handle."
    "I give it a firm but careful push, and the door slides open."
    scene bg hallway with wipeleft
    "I stand motionless in Natsuki’s house, waiting for any idea as to what I’m doing here."
    "{i}Clothes, toiletries, everything I can carry.{/i}"
    "I quickly head up the stairs and burst into Natsuki’s room."
    scene bg nbedroom with wipeleft
    "Nothing has been touched."
    "The empty wine bottle and pill container lay on Natsuki’s bed."
    "The mess is still all over the floor."
    "A shiver crawls down my spine."
    "Grim."
    "I begin to rifle through her belongings."
    "I clear her closet of all clothes I can see, piling them up on the bed."
    "I notice a large black suitcase in the corner of her room."
    "Perfect."
    "Unzipping the suitcase, I quickly jam her uniform, pyjamas, casual clothes, and underwear into it."
    "The desk is next."
    "I sweep all of her makeup and accessories into my bag."
    "One last look around her room, my eyes lock on the bottle."
    scene bg hallway with wipeleft
    "I lift the over-packed suitcase onto my back, holding the handle over my shoulder, and make my way to the main floor."
    "I set the suitcase down near the door, and make my way down into the basement."
    scene black with wipeleft
    "I flick the light on, to no avail."
    "I clumsily bump around eventually finding my way to the wine rack."
    "I grab four bottles, as many as I can carry."
    "I haven’t a clue as to what I’ve taken."
    "But I hope it was expensive."
    "Feeling the weight of the bottles in my bag, I realize there’s no way I’ll be able to carry this all the way home."
    "I’ll have to take the bus as far as possible."
    "I check my phone for the time."
    "Not too late. If I hurry, I can make it to the next stop."
    scene bg hallway with wipeleft
    "I move as quickly as possible up the stairs."
    "I grab the suitcase and slip through the door."
    "I inch the door closed in hopes of not making any sound."
    scene bg street with wipeleft
    "I turn and make a mad dash for the bus stop."
    "Thank God this thing has wheels."
    "I can see the bus rounding the corner as I exit the alley."
    "Oh crap."
    "Before I know it, it's gone."
    "Great."
    "Now I'll have to walk all the way home with this."
    "And that's the second time today that I've missed the bus..."
    "The adrenaline is tearing through my veins."
    "I can’t believe I did that."
    "And didn’t get caught..."
    "Well, not yet anyway..."
    scene black with dissolve_scene_full
    stop music fadeout(2.0)
    scene bg housen with dissolve_scene_full
    "I ended up having to take multiple breaks."
    "Even one stop at a coffee shop for a drink."
    "But I'm almost home..."
    "As I walk past Sayori’s house guilt begins to surround me."
    "I should have gone and tried to talk with her."
    "I shake the feeling and pick up my pace as much as I can."
    "I get to my front door and Natsuki opens it before I can get my keys out."
    "I bring the suitcase into the house as Natsuki begins to question me."
    scene bg mclivingroomn with wipeleft
    show natsuki 4cp at h11
    n "[player]! I saw you through the window!"
    n "What the hell is all this?"

    "I never thought about how I was going to explain this."

    mc "U-uh..."
    mc "It’s..."
    mc "Your stuff..."
    n 1cs "What do you mean, {i}my{/i} stuff?"

    "I lay the suitcase down in the living room, hanging my jacket over the back of a chair."
    "I lay my bag down near the table. Thankfully the bottles didn’t audibly shift."
    play music tlw
    "Natsuki just stares at me."
    "A few long moments pass."

    mc "Natsuki?"
    n 1cn "I can’t believe this."
    n 1cu "There’s no way you’d..."
    show natsuki at thide
    hide natsuki

    "Natsuki hesitates to reach for the zipper."
    "She finally opens the main pouch, revealing the majority of her wardrobe."
    "She then opens the front pocket, spilling some of her makeup and accessories onto the living room floor."
    "Natsuki is trembling."

    show natsuki 1cm at t11
    mc "I’m sorry..."
    mc "I didn’t think-"
    scene n_mod_cg3_bg
    show n_mod_cg3_1
    with dissolve_cg
    "Natsuki literally jumps into my arms."

    n "[player], I love you so much."
    n "Why'd you..?"
    mc "Well, you would've been stuck with only a couple of pairs of clothes otherwise..."
    mc "And if you're moving in properly, then you needed your stuff moved too."
    mc "Besides, he wasn't there. It was probably my only chance to."

    "She's totally speechless."
    "I'm grinning stupidly."

    n "[player], I..."
    n "I'm yours."
    mc "Ahaha..."
    mc "You mean what I think you mean?"
    n "Absoulutely."
    scene black with dissolve_cg
    "I wrap my arm around Natsuki’s waist, and she pushes me onto the couch on my back as she climbs on top of me."
    "I feel her fingers run through my hair as I kiss her neck...."
    "I can’t help myself."
    "Neither can she..."
    scene black with dissolve_scene_full
    stop music fadeout(2.0)

    $ quick_menu = False
    scene black
    show saturday
    with dissolve_scene_half
    $ renpy.pause(delay=2.0, hard=True)
    $ quick_menu = True

    scene black with dissolve_scene_full
    "As willing as I’d be to stay with Natsuki like this for the rest of my life, my phone’s buzzing beckons me."
    "She’s fast asleep, so I do my best to escape her delicate grip without waking her."
    scene bg bedroom with wipeleft
    play music presenttense
    "Retrieving my phone from my pants, I look out of the window."
    "It must be early morning."
    "I should've disabled my alarm for the weekend."
    "I shrug it off and pull my shirt over my shoulders."
    "I notice a folded piece of paper on my desk as I pull my pants up."
    "My name’s printed on the front, in Natsuki’s writing."
    "I open it."

    python:
        if persistent.language == "spanish":
            poem_n4 = poem_n4_spanish
    call showpoem (poem_n4) from _call_showpoem_4

    "..."
    "The feeling of weightlessness takes hold of me once more."
    "A warmth radiating from my chest pulsates throughout my body."
    "I read the poem multiple times, the feeling grows more intense."
    "I place the poem on my desk next to my computer."
    "Careful not to wake Natsuki as I close the bedroom door, I make my way downstairs."
    scene bg kitchen with wipeleft
    "I make enough coffee for the two of us in case she wants some."
    "I sit at the kitchen table and wait..."
    scene bg kitchen with dissolve_scene_full
    "Natsuki waves her hand in front of my face."

    show natsuki 4cb at t11
    n "Earth to [player]!"
    n "Anyone in there?"

    mc "H-hey, sorry, I didn’t hear you come downstairs."
    n 3cc "Is that for me?"
    mc "Well, both of us, but..."

    "Natsuki takes two mugs from the cupboard, handing me one as I stand up to pour myself a drink."

    mc "Thanks."

    "I return the milk jug to the refrigerator."
    "Natsuki and I take our coffees to the living room."
    scene bg mclivingroom with wipeleft

    show natsuki 3ca zorder 1 at t11
    mc "Hey..."
    n 3ck "Yeah?"
    mc "I, uh, I found your poem."
    n 3cn "E-eh?"
    mc "This."

    "I hand her the folded paper."

    mc "I loved it."
    n 3cl "Oh!"
    n 4cz "Ehehe~"
    mc "Am I really... your hero?"
    n 2ct "What else could you be, dummy?"

    "Natsuki kisses me on the cheek and giggles to herself."
    "I smile warmly back."

    n 1cd "So... whatcha want to do today?"
    mc "No clue..."

    show natsuki 1cj
    "She gives me a playful grin."
    "I beam back at her, only interrupting it to take a sip from my coffee."
    "It’s unusually sweet."

    mc "That’s... strong."
    n 4cy "What’s the matter? Can’t handle a cup of coffee?"

    "She knocks on my right arm jokingly."

    mc "What? No, it’s not that."
    mc "It’s just sweeter than I normally have it."
    n 2cd "Oh yeah, I put a couple teaspoons of sugar into yours while you weren’t looking."
    n "I was just making your cup the same way I make mine."
    n "You like it?"
    mc "It’s a little too sweet for my taste, but I don’t mind all that much."
    mc "Just let me know next time, okay?"
    n 4ca "Yeah, yeah."

    "I beckon for her to come and sit on the couch next to me."
    "She hops over, careful not to spill her own drink."
    show natsuki at thide
    hide natsuki
    "I turn on the TV as I wrap my right arm around Natsuki’s shoulder, holding my mug in my left."
    "She digs her head into my chest and uses her spare hand to flick through channels with the remote."
    "After a while, she settles on something to watch."
    scene black with dissolve_scene_full
    scene bg mclivingroom with dissolve_scene_full
    "We laze about together for hours, watching a film and two TV programmes."
    "After a while, Natsuki speaks up."
    show natsuki 1ck zorder 1 at t11
    n "I-I’ll be right back."
    mc "What’s up?"
    n 1cc "I gotta use the toilet quickly."
    mc "Sure, go ahead."
    mc "I’ll pause this here."
    show natsuki at thide
    hide natsuki
    "As Natsuki leaves the room, I hit the pause button."
    "I’m enjoying Natsuki’s company quite a bit more than the film we’re watching now."
    "And this is one of my favourite films."
    "I hear the toilet flush distantly, and as I wait for her to return, I hear her rush into my room."
    "What’s she up to?"
    "A minute or so later, Natsuki returns with a scowl, my phone in hand."

    show natsuki 2cb at t11
    n "It’s for you."
    stop music fadeout(2.0)
    show natsuki at thide
    hide natsuki

    "She hands me the phone, currently engaged in a call with an unknown number."

    mc "H-hello?"
    m "[player], we need to talk about Yuri."

    "I’m taken aback."
    "Does Monika want to know about what Yuri told me?"
    "Or sent?"

    mc "I- uh, I’m listening."
    m "In person, I mean."
    m "As soon as possible."

    "I sigh."

    mc "Fine."
    mc "Where?"
    m "There's a little café on the other side of town."
    m "It's a couple of blocks down from Natsuki's place."
    m "She'll know where it is."
    m "I’ll pay."
    mc "Alright. I guess I’ll see you there in half an hour?"
    m "Alright, sounds good."

    "She hangs up."
    "I pocket my phone as I get out of my seat and make my way to the hallway."
    "I grab my jacket from the wall-mounted hanger and pull it over me."

    show natsuki 1ca at t11
    mc "You wanna come with?"
    n "Sure."
    mc "Good, because I wasn’t looking forward to having to face Monika alone."
    n 3cb "Yeah, after what she did..."
    n 3cc "Even if she did apologize after, you never know."

    "Throwing my jacket on, I peek out of the door and see that the area is still cold, and it’s raining as if to add insult to injury."
    "The café is too close to warrant getting a bus, which means we’ll have to stomach the weather."

    mc "Ready?"
    n 3ce "Just a second!"
    n "I’ll just get my coat and we can go."
    scene bg mclivingroom with dissolve_scene_full
    show natsuki 1db zorder 1 at t11

    n "Wait, [player], you seen my scarf?"
    mc "Yeah. It should be in the closet as well..."
    n 2dc "I can't see it..."

    "I look in the closet and see it on the shelf, just out of Natsuki's reach."
    "I grab it and hold it over her head."

    mc "It's right here, silly."

    show natsuki 1di zorder 1 at h11
    "Natsuki attempts to snatch it from my hand but fails to jump high enough."
    show natsuki 1dh zorder 1 at h11
    "A couple more times, she{nw}"
    show natsuki 1dw zorder 1 at h11
    "A couple more times, she{fast} hops up in the{nw}"
    show natsuki 1do zorder 1 at h11
    "A couple more times, she hops up in the {fast}air to try and catch it, but to no avail."
    show natsuki 4ds
    "Defeated, she stares me down."

    n 4dq "Pleeeeease..?"
    mc "All right, fine."
    show natsuki at thide
    hide natsuki
    mc "Here."
    mc "Sorry, I couldn't help myself."

    show natsuki 4eg zorder 1 at t11
    n "Yeah, you've proved that a few times now, haven't you?"

    "She punches me jokingly in the arm."

    mc "Hey, that was a little uncalled for, don't you think?"
    n 4ea "Not really."
    n 4ed "You're lucky I didn't just beat the crap out of you while you still had my scarf."
    mc "Oh, would you really?"
    n 3ey "Yeah!"
    mc "Well what if I like it when you play rough?"
    n 1ep "E-eh?"

    "Natsuki goes bright red, stammering."

    n 1eq "U-uh, nice one, [player]."
    n "Way to kill the mood..."
    n 1ek "Now come on, let’s go."
    n 1ec "We shouldn't make Monika wait... unless we want to feel her wrath again."
    show natsuki at thide
    hide natsuki
    "She says that trying to suppress a grin."
    "Natsuki hops out of the door."
    scene bg houserain with wipeleft
    "I follow, with much less enthusiasm."
    scene black with dissolve_scene_full
    stop music fadeout(2.0)
    scene bg streetrain with dissolve_scene_full
    "Turning down side streets, we make our way into town."
    "The café is just in sight, on the corner of the street."
    "We cross the road and get to the door."
    scene bg cafe with wipeleft
    play music thenumbers
    "A refreshing gust of humid air hits us as we enter."
    "There’s a couple of people sat around the place, but Monika is nowhere to be seen."
    show natsuki 1ed zorder 3 at t11
    mc "Looks like we’re early, huh?"
    n 2ed "Yeah."
    show natsuki 2dd
    "Natsuki unwraps the scarf from her neck."
    "She hastily folds it, and stuffs it into her coat pocket."
    n "Well, come on, I’m gonna get a drink-"
    mc "No need. Monika said she’s paying."
    n 4db "Yeah, for you."
    n "I don’t think she’d be happy that I’m even here, let alone be on good enough terms to buy me a drink."
    n 4dc "She still seems really mad at me, you honestly think-"
    mc "Well, if you want to spend your money, that’s fine."
    n "I-I..."
    n 4de "Gah, now you’re just trying to use reverse psychology!"
    mc "Trying to?"
    n 1dq "Fine, I’ll wait."

    "We take a seat at a table in the far corner of the café, and wait."
    "I scroll through my phone while waiting."
    "It bleeps, and I open the notification."
    show natsuki at thide
    hide natsuki
    m "omg im really sorry, listen im only gonna be another 10 mins i promise :0"

    "Once again, the way Monika’s acting has shifted drastically."
    "Why?"

    mc "Why? Has something come up?"
    m "ill tell u all about it when i get there"
    mc "Okay, hopefully you won’t take too long. We’re sat at the back, we’ll keep an eye out."
    m "we??"

    "Ah, crap."
    "Time to bite the bullet."

    mc "Natsuki’s here with me."
    m "ahhh right, got confused there lol"
    m "ill see u 2 there xox"

    "It shouldn’t come as a surprise to me that Monika has softened up to Natsuki, considering we’re together now."
    "But despite that, it still does."
    "Despite Monika’s apology, I, like Natsuki, was hesitant to accept."
    "After showing us the heartless manner in which she emotionally destroyed Sayori and Yuri, I don’t think I can truly forgive her, regardless of her reasoning."
    "Usually, people like that don’t - or can’t - change."
    "{i}Usually.{/i}"
    "That's why I'm giving her a chance to change."
    "However, all I can do right now is see what warranted such an urgent meeting about Yuri, and her habits."
    show natsuki 1dk zorder 1 at t11
    n "What’d she say?"

    "She tries to peek over my shoulder to glimpse the messages."

    mc "Just that she’s running late."
    n "Oh, right."
    n 2dc "Well, how long’s she gonna take?"

    "I shrug."

    mc "No idea. She didn’t really say anything about why she’s-"
    mc "Oh, there you are."

    "Monika arrives, out of breath. She sits between us."

    show natsuki 1da at t21
    show monika 1bb at t22
    m "Hey, [player]."
    m 1ba "And you, Natsuki."
    n 1dc "Hi."
    m 4bm "Sorry I’m so late."
    m "I didn't even have time to grab a coat."
    m 2bn "I was busy chatting to Yuri online."
    m "She’s said some things, that... uhm..."

    "There’s a short silence between us, where nobody knows what to say."

    m 1bo "Well..."
    m 1bq "I'd say they speak for themselves."
    m "..."
    m 1bd "Since I’m getting the drinks, [player], what’d you like?"
    mc "Uhh..."

    "I peer over to the selection of drinks they have written on a sign hanging over the counter."
    "Making my choice, I notice Natsuki also looking over at the sign. Monika doesn’t pick up on it."

    mc "I guess I’ll get... just a regular coffee."
    n 1dl "Ooh, [player], can I get a c-"
    m 1bc "Sorry Natsuki, I don’t think I have enough money to spare for you, and I promised [player] that I’d buy him a drink."
    n 4du "..."
    mc "How much have you got, Natsuki?"
    n 4dq "Uh..."

    "Natsuki fumbles with her change purse for a moment."

    n 4di "I only have like five-"
    mc "I’ve got an idea."
    mc "Why don’t we just pool all our money together?"
    mc "That way, we can all get a drink and maybe a pastry on the side."
    mc "Sound good?"

    "Natsuki beams at me for a moment before snapping her attention back to Monika."

    m 2bd "Yeah, that’ll work."

    "The three of us approach the till, make our orders and sit back down."

    n 1da "I’ll be right back, okay?"
    n "Don’t start without me!"

    show natsuki at thide
    hide natsuki
    show monika 1ba at t11
    "Natsuki heads off to the washroom."
    "Monika leans close towards me."

    m 1bc "I’m gonna be frank."
    m 2bf "There’s something seriously wrong with Yuri."
    mc "Yeah..."
    mc "I've gotta agree."
    m 2bd "You saw the cuts?"
    mc "Yeah... kind of hard to forget."

    "Monika’s reaction to my experience with Yuri’s self-harm was that of... surprise."
    "Like she only just found out I knew, even though she exposed me to it in the first place."
    "Is she trying to pretend that the club’s argument didn’t happen, perhaps for Natsuki’s sake?"

    mc "Well, it’s not just that."
    mc "Look at this."

    "I flash the picture that Yuri sent me to her."

    m 1bo "What the hell..?"
    m "That’s Yuri?"
    m 2bp "Wow..."
    m "You're sure?"
    m "Like, a hundred percent?"
    mc "Yep."
    m 1bg "How’d she react to that?"
    mc "Who, Natsuki?"

    "Monika nods."

    mc "Well, she saw it before me actually."
    mc "We were in the middle of a conversation and she just sent that to me with zero context."

    "I pull up to the messages leading up to the picture to back my point up."

    m 2bh "That’s just bizarre..."
    mc "I know I didn’t respond to it."
    mc "I mean, what the hell {i}am{/i} I supposed to say?"
    m 2bq "Well, that explains a lot..."
    mc "What do you mean?"
    m 2br "Yuri... she’s sent me pictures of her cuts too, [player]."
    m "Nothing like that, mind you."
    m "But, that’s kind of what I wanted to talk about."
    m 2bg "You seriously need to have a word with her."
    m "The things she said to me when I was talking with her online were..."
    stop music fadeout(2.0)
    m 2bo "They were fucked up, [player]."
    m "She told me that I should..."
    m 1bp "Well, you can take a guess."

    "Monika hesitates."
    "She slides her phone over the table with a chat open."
    show monika at thide
    hide monika

    y "It’s none of your business, you preppy bitch."
    y "I’m fine."
    y "In fact, you should try it sometime."
    y "Maybe it’ll take the stick out of your ass."
    y "I’m done talking about this with you."
    m "wait yuri i didnt mean for it to offend u..."

    "I hand the phone back to her."

    show monika 2bg zorder 1 at t11
    mc "Yeah, I’ll speak to her."
    mc "Why me specifically though?"
    m 2bd "Oh, you didn’t see it?"
    m "Here."
    show monika at thide
    hide monika
    "Once again, she hands me her phone, swiping down on the chat."
    "Oh my God."
    "That’s my..."
    "Yuri sliced my initials into her arm..."
    "I feel light-headed."
    "Jesus Christ."

    show monika 1bf zorder 1 at t11
    m "Hey, you okay?"
    mc "I-I’m fine... just..."
    mc "That."
    m 3bg "Do you understand why you have to talk to her?"

    "I swallow audibly."

    mc "Y-yes... I get it."
    m 3bd "I’d suggest bringing up that you’re with Natsuki."
    m "Maybe that'll knock some sense into her."
    mc "Like hell it will."
    m 1bf "[player], I’m worried about her well being."
    m 1bp "I know I've been totally malicious the past week..."
    m "A \"preppy bitch\", as she put it."
    m 1br "But that doesn’t mean I don’t care about her."

    "I’m having trouble believing that..."
    "Though she did actually bother to organize this just to show me..."
    "I don’t even know what Monika’s intentions are anymore."

    mc "I understand. I’ll try my best."

    "Natsuki returns to the table."

    play music thenumbers
    show monika 1bc zorder 1 at t21
    show natsuki 2dk zorder 2 at t22
    n "Is everything okay?"
    mc "Kinda. I just need to have a talk with Yuri."
    mc "She told Monika to cut herself."
    n 2dm "Damn..."
    n "Okay, that’s way over the line."
    n 2dn "I’m sorry, Monika."

    "The barista calls us up to the counter for our drinks and food."
    "I take mine and Natsuki's drinks, while Monika grabs her own drink and the pastry."

    m 2bh "I'm sure you don’t want to tell her about that picture, I get it, but she needs to know."
    n 2dh "What picture?"
    mc "Oh, uh..."
    mc "You know what Yuri said to Monika?"
    mc "Well, she..."
    mc "Monika, can I use your phone for a second?"
    m 2bi "Sure."

    "I hand her the phone, Yuri’s picture already loaded on."
    "She recoils, squealing."
    show natsuki 1dp at h22
    n "EYAH!"
    n "What the hell?!"

    show natsuki 3dr
    "A couple of people turn at the commotion, but resume their activities."

    mc "That’s why I need to talk to her as soon as possible."
    mc "To let her know that I’m with you, and that I don’t plan on leaving you, for anyone."

    "Natsuki takes a sip from her caramel frappe."

    n 3ds "I get it, [player]."
    n 4dh "But if this continues, I’m gonna f-"
    mc "It won’t. I’m going to deal with it on Monday."

    "We sit and eat our food in a heavy silence."
    "I still can’t believe that picture..."
    stop music fadeout(2.0)
    "My phone buzzes in my pocket."
    "Wide-eyed, I look at Natsuki."

    n 2dk "[player]?"

    "Monika turns her attention back to me as I pull my own phone out of my pocket."
    "A text from Yuri."

    y "I can see you."

    "I look around the café and see Yuri near the entrance, novel in hand."
    "She walks over and eventually the others take notice of her."
    "Monika waves awkwardly."
    "Natsuki eyes her down ferociously."
    "Yuri takes a seat next to Monika."
    show natsuki 1ds at t32
    show monika 2bm at t31
    show yuri 2bb zorder 1 at t33
    play music illwind
    y "Good afternoon, everyone!"
    y 2ba "I wasn't expecting to see you all here!"
    m "Y-yeah, Yuri..."
    y 1bh "Monika, I just wanted to apologize for what I said earlier."
    y 1bg "I do hope we can keep it between us."

    "Monika shoots me a worried glance."

    m 2bn "Sure..."
    y 1bs "[player], did you get my message the other day?"
    y 1bt "You never got back to me."
    n 3dr "You know what-"
    mc "N-no, I didn’t."
    mc "My phone was bugging out yesterday..."

    "Natsuki looks as if she could jump over the table and rip Yuri to shreds."
    "I guess it's just lucky that Yuri's not really paying her much attention."
    show natsuki 3di
    "I rest my hand on her knee, signalling for her to keep her cool."

    y 2bj "I’ll be right back. I’m just going to order my drink."
    y 2bb "[player], do you want anything?"
    mc "N-no, Yuri, I’m fine."
    mc "I have my own drink."
    y 3bq "O-oh, that's fine."

    show yuri at thide
    hide yuri
    show monika at t21
    show natsuki at t22
    "Yuri leaves her things at the table and stands in line."

    n 4de "What the hell was that, [player]?"
    n "I thought you were going to bring this-"
    show natsuki 3dg
    mc "Not here and not right now."
    mc "Not with you two here and in a crowded café."
    mc "What if she doesn’t take it well?"
    mc "Well, I don’t even need to say \"what if\" - you and I both know she won’t."
    mc "I’ll deal with this on Monday, as I said."
    mc "For now we need to act as normal as possible."
    mc "That goes for you too, Monika."
    m 1bp "B-but-"
    mc "I know what I’m doing."
    mc "I think..."

    "Yuri joins the table once more, having paid for her drink."

    show monika at t31
    show natsuki 1ds at t32
    show yuri 1bm at t33
    mc "So, what'd you get?"
    y 2ba "I decided on some of their signature blend tea."
    y 2bm "It’s very sweet."
    y 2by6 "[player], we should come here one day."
    mc "Maybe if we had a club meeting here, instead of just the two of us?"
    y 3bn "N-No!"
    y 2bo "Ah, sorry... I didn’t mean to raise my voice."
    mc "Well, maybe..."

    "Natsuki grabs my hand from under the table and squeezes it, hard."

    m 2bm "I’ll be right back, I need to use the washroom."
    n 3dq "Y-yeah, same here."

    "They both look at me like they want me to follow."

    mc "Be right back, Yuri."

    "Yuri nods and opens her book."
    "The three of us head around the corner to the entrance to the bathrooms."
    scene black with wipeleft
    n "[player], I can’t take this."
    m "How are you keeping so cool-headed?"
    n "This is so messed up."
    m "What's your plan anyway?"
    n "Yeah, what’s the plan?"
    mc "Hey hey, one at a time."
    mc "Natsuki, I know this is weird-"
    n "Weird?!"
    n "This is totally crazy!"
    n "Whenever I look at her, all I can see is her arms!"

    "Monika nods in agreement."

    mc "Just hear me out."
    mc "My plan is to talk to her."
    mc "Plain and simple."
    mc "I’ll tell her I’m with you, Natsuki."
    mc "And I’ll bring up her self-harm."
    mc "Ideally, she’ll let me roll up her sleeve to see how bad it really is."
    mc "Hopefully I can talk her into going to a professional."
    mc "Her... feelings... towards me are clearly making her cutting far worse."
    mc "And I don’t want another friend in the hospital."
    n "A-alright, I guess..."
    m "It might work..."
    m "But-"
    mc "Have you got a better idea?"
    m "I- not really..."

    "Monika rushes into the women’s room."

    n "I’m going to go wash my hands and I’ll be back out."
    mc "Okay. I'll just go back."
    scene bg cafe with wipeleft
    "I return to my seat."
    show yuri 2ba zorder 1 at t11
    "Yuri beams at me from over the table."
    "She chuckles to herself as she plays around with her phone."
    "{i}BZZT.{/i}"

    y 2bb "You should read that, [player]."

    "{i}1 message unread: 2 files attached.{/i}"

    "I swipe, dismissing the notification."

    mc "Damn..."
    y 2by5 "Do you like it, [player]?"
    mc "I can’t load it."
    mc "I think I’m out of mobile data."
    y 2bl "Oh, well, you should check it when you get home."
    y 3bj "I’m sure you’ll {i}love{/i} it."

    show yuri zorder 1 at t31
    show monika 1bm zorder 2 at t32
    show natsuki 3ds zorder 3 at t33
    "Natsuki returns to the table, followed by Monika, who takes her handbag."

    m "Y'know, I should get going. I have things to get done for the club tomorrow."
    m 1bl "It was nice seeing you all!"
    show yuri at t21
    show natsuki at t22
    show monika at thide
    hide monika
    "Monika takes off out the door hurriedly."
    mc "Come to think of it, I should probably head out as well."
    mc "Natsuki, I’ll walk you home."
    y 3bf "Wait, [player]."
    y "You don’t need to waste your time."
    y 3bh "I can walk Natsuki home."
    n 1dq "N-no, really, I'm fine to go with [player]."
    y 3br "I-"
    mc "We'll talk to you on Monday, Yuri."
    y 2bw "I- ugh..."

    "Natsuki and I make our way out of the café, leaving Yuri alone at the table."
    scene black with dissolve_scene_full
    stop music fadeout(2.0)
    scene bg houserain with dissolve_scene_full
    "With our house in sight we slow down to a normal pace."

    show natsuki 2eu zorder 1 at t11
    play music tlwamsp
    n "[player]..."
    mc "Yeah?"
    n 2en "Y-you’re really good at handling these kinds of things."
    mc "Whadda you mean?"
    n "Well first talking to Sayori, now Yuri?"
    n 1em "You {i}do{/i} know Sayori’s in love with you, right?"
    mc "Yeah..."
    mc "She told me."
    n 1ek "R-really?"
    mc "Yeah... I'll tell you what I told her."
    mc "It’s not like I don’t love her..."
    mc "It’s just that it's purely as friends..."
    mc "Especially considering I was already falling for you."

    "Natsuki stops walking."

    n 1eq "Y-you really mean that?"
    mc "Yeah. I love {i}you{/i}."

    "Natsuki wraps her arm around mine as we continue walking."

    n 3et "I love you too, [player]."
    scene bg mclivingroom with wipeleft
    "After a short walk we enter our house."
    "Natsuki makes her way upstairs, leaving me in the foyer."
    scene black with dissolve_scene_full
    stop music fadeout(2.0)
    scene bg bathroom with dissolve_scene_full
    "I stare idly into the mirror."
    "The figure boxed within stares idly back."
    show natsuki 3bb zorder 2 at t11
    play music tlw
    n "[player]!"
    n "Anyone there?"

    show natsuki 1bb
    "Natsuki wags her arm in front of my face."

    mc "Sorry, Natsuki."
    mc "I’ve just been thinking..."
    n 1bk "It’s fine, [player]."
    n "I can’t really blame you."
    n 1bc "Today was nuts."
    n "..."

    n 2ba "Y’know, we look really good together."

    show natsuki 1ba
    "I wrap my arm around Natsuki."
    "We stare at the mirror for a few moments."

    n "Do you have your phone on you?"
    mc "Yeah. Why?"
    n 1bd "You should take a picture of us."
    n "We really do look nice together."
    n 1bl "Cute, even."
    mc "Cute, huh?"
    mc "What happened to \"I’m not cute\"?"
    n 2bq "I... uh..."
    n "That doesn't count!"
    n 2bt "I was talking about both of us together, dummy."

    "Digging into my pocket, I grab my phone to take a quick photo."
    "Natsuki is already posing."

    n 1bb "Take your time."
    mc "Just a second, sorry..."
    mc "Ready?"

    show natsuki 1bd
    "Natsuki faces me, nodding enthusiastically."
    scene black with dissolve_cg

    show white zorder 6:
        alpha 0.6
        linear 0.25 alpha 0.0
    pause 0.5
    hide white
    pause 1

    show white zorder 6:
        alpha 0.6
        linear 0.25 alpha 0.0
    pause 0.5
    hide white
    pause 1

    show white zorder 6:
        alpha 0.6
        linear 0.25 alpha 0.0
    pause 0.5
    hide white
    pause 1

    scene bg bathroom with dissolve_cg
    "Immediately after she snatches the phone from me, to see how they turned out."

    show natsuki 1bg zorder 1 at t11
    n "This one’s really blurry. I’m getting rid of it."
    n "But..."
    n 3bk "I really like this one."

    "She turns the phone to me."
    "I can’t help but agree. It’s perfect."

    mc "Actually, yeah, that one’s great."

    "Natsuki takes my hand and leads me out of the bathroom."
    scene bg mclivingroom with wipeleft
    "She hops onto the couch, and I follow."
    "I pluck the phone out of her hand, turning it off."

    show natsuki 2bl zorder 1 at t11
    n "Did you want to watch something?"
    n 2bt "Or maybe..."
    mc "What you got in mind?"

    "I give her a suggestive grin."
    "She ignores it."

    n 4bd "We could bake some cookies!"
    mc "Oh, that sounds good, actually..."
    n 3be "[player]!"
    n "Get your mind outta the gutter!"
    n 3bg "Dummy..."

    "Natsuki stands and heads to the kitchen."
    "Her voice echoes back through to the living room."

    n "[player], did we run out of eggs?!"
    mc "Uhm, I’m not sure..!"
    mc "You checked right at the back of the fridge?!"
    n "Yeah... I don’t see them..!"

    "Natsuki huffs, returning to the couch."

    n 5bh "So much for baking..."
    mc "Well, I got a better idea."
    n 5bo "Don’t even-"
    show natsuki 5bi
    mc "I was going to suggest going out to the park, Natsuki."
    mc "Come on, you really thought I was gonna keep-"
    n 5bs "Well, you meant it the first time."
    mc "I-yeah, but it was just a suggestion."
    n "U-uh..."

    "Natsuki pauses for a moment, unsure of how to come back."

    n 5bq "A-alright, I get it."
    mc "Well, I tell you what..."
    mc "Why don’t we just order in?"
    n 2bt "Y-yeah. I guess we could do that."
    mc "So, where do you wanna order from?"
    n 2bk "I dunno, really. I'm guessing you have something in mind?"
    mc "I don't actually, ahaha..."
    mc "It was just a suggestion."
    n 1bc "You choose."
    mc "Pizza?"
    n 1bk "Sure, but only if you order a dessert for us too."
    mc "Alright."

    "Using my phone, I quickly place the order online and turn the television on."

    mc "Im gonna use the bathroom. I’ll be right back."
    n 3bk "Okay."

    "I pick my phone up off the coffee table and head upstairs."
    scene bg bathroom with wipeleft
    "I enter the bathroom and lock the door behind me."
    "I have to know what else Yuri sent me."
    stop music fadeout(2.0)
    "Curiosity takes its course."
    "Natsuki was already so upset at the café..."
    "I can’t let her see these ones too."
    "I open the conversation with Yuri."
    "There are a total of seven images from her."
    "The one of her with the blood drawn heart on her chest."
    "My initials carved into her arm."
    "Wait..."
    "What?"
    "So that’s why Yuri went through my bag."
    "It’s bloody..."
    "I cautiously continue to scroll through the pictures."
    "In the next one she’s wearing an unbuttoned shirt."
    "She’s sitting on her bed with my pen in her mouth."
    "I can’t help myself now, I keep scrolling."
    scene black with dissolve_scene_full
    scene bg bathroom with dissolve_scene_full
    "I think I’m going to be sick."
    "My face is completely red."
    "Crap."
    "I flush the toilet, splash some water on my face and head back downstairs."
    scene bg mclivingroom with wipeleft
    "As I enter the living room I shut my phone off completely."
    "Just as I sit down there’s a knock at the door."
    play music tinkertailor
    show natsuki 1bl zorder 1 at t11
    n "Yay!"
    show natsuki at thide
    hide natsuki
    "I answer the door, pay for our food, and return to the couch."
    "I set out our meal on the table."
    "It's a large pepperoni pizza, with a side of fries, and some onion and garlic dipping sauce."
    "Natsuki's already tucking in, having dipped the edge of her first slice in the sauce and taken a bite."
    show natsuki 1bz zorder 1 at t11
    n "Thanks, [player]!"

    "She gives me a kiss on the cheek, accompanied by a speck of sauce."

    n 1bt "Ehehe~"
    n "Sorry..."

    "Natsuki leans over and licks my cheek."

    mc "Hey-"
    n 5bt "Ehehe~"
    n 5by "Now we’re even."
    mc "Cheeky..."

    "I feel the blood rush to my face once more."

    n 3ba "You’re so easy to fluster."
    mc "Hey!"
    mc "So are you!"
    n 3by "Oh, am I now?"

    "I place my hand on her thigh, sliding up ever so slightly."

    mc "There you go."
    show natsuki 3bi
    "Natsuki's cheeks light up like a Christmas decoration, and she moves my hand from her leg by shoving a cushion between us. "

    n 5bi "T-that doesn’t prove anything!"
    n 5bs "Dummy..."
    mc "You shouldn't throw stones if you're living in a glass house."

    "I take a bite of my pizza, suppressing the urge to chuckle."
    "Natsuki subtly retakes her original spot beside me."
    "We sit for a while, exchanging slices of pizza while watching the TV."

    n 5bh "You don’t {i}always{/i} have to be right, y’know..."

    "I can’t help but crack a smile."

    mc "Well, you make it easy sometimes."
    n 4bq "What’s that supposed to mean?"
    n 4bw "I’m a pro, don’t forget."
    mc "All right, Natsuki. Whatever you say."

    "I shoot her a cheeky wink."
    show natsuki 4bs
    "She looks like she wants to say something, but she bites her tongue."
    "Instead, we turn our attention back to the TV while we eat..."
    scene black with dissolve_scene_full
    stop music fadeout(2.0)
    scene bg mclivingroomn with dissolve_scene_full
    show natsuki 2bj zorder 1 at t11
    mc "Are you done with that?"
    n 2bl "Yeah, I’m stuffed."

    scene bg kitchen with wipeleft
    "I take Natsuki’s plate with mine to the kitchen."
    "I almost forgot..."
    "I lean down and open up my bag, revealing the bottles of wine."
    "I take one and set it on the counter, putting the rest in the fridge."
    "{i}That’s what you do with wine, right?{/i}"
    "Eh, whatever..."
    "I peer over into the living room for a moment."
    "Natsuki is focused on the show."
    "I rummage through my drawers, trying to find something to open it with."

    n "Is everything okay in there?"
    mc "Y-yeah, just give me a second!"

    "At the back of the cutlery drawer, I find a corkscrew."
    "I look for a way to open the bottle as quietly as I possibly can."
    "To make sure the cork doesn’t make the loud \"pop\", I wrap a towel around the mouth of the bottle as I wriggle the cork free."
    "Success."
    "I take two glasses from my cupboard, hiding the bottle behind my back."

    scene bg mclivingroomn with wipeleft
    show natsuki 3bj zorder 1 at t11
    mc "Hey, Natsuki."
    mc "I have a little something for you."
    n 3bk "Huh?"

    "I reveal the bottle, and her eyes light up."
    play music presenttense
    n 3bd "[player], you must know your wine."
    n "I remember when my, uh-..."
    n 1bk "When he bought that, it had to be imported."
    mc "Expensive, was it?"

    "Natsuki nods her head furiously."

    mc "Oh well, isn’t that a shame?"

    "I sit myself down on the couch again and pour each of us a glass."

    n 1bb "Gimme that!"

    "I wrap my arm around Natsuki as we enjoy the wine."
    "Personally, I really don’t like it as much as I expected to."
    "It just tastes kinda sour..."
    "Either way, Natsuki seems to really be enjoying it."
    "I'm sure the taste will grow on me..."

    n 5bl "How exactly did you get this?"
    mc "I was going past your house and well... I..."
    mc "Just got off the bus, and went inside."
    mc "After I got your stuff, I decided I should check the basement."
    mc "Not entirely sure why, but it worked out, I guess."
    n 5bu "I know I’ve already said it, [player], but..."
    n 5bn "Thank you so much."
    n "For everything."

    show natsuki 5bn
    "Natsuki places her glass down on the coffee table and embraces me tightly."

    n 5bj "You make everything better."
    mc "So do you, Natsuki."

    "We stay like this for a few moments."
    "Natsuki pulls back and finishes her glass, as do I."

    n "Mind if I have another?"
    mc "Sure."

    "I pour ourselves another glass."
    "I lean back into the couch once more."
    stop music
    show natsuki 1bp at h11
    play sound smack
    pause(0.3)
    show natsuki 1bn at h11
    play sound smack
    pause(0.3)
    show natsuki 12bd at h11
    play sound smack
    "Someone's pounding heavily on the door."
    "Natsuki flinches, spilling her wine on the table."
    "She curls into a fetal position on the sofa."
    "The knock startled even me, but her reaction is out of sheer terror."
    "{i}I wonder why.{/i}"
    "The knuckle prints on her bedroom door..."
    "No wonder."

    mc "Natsuki, you’re okay."
    mc "It’s okay."
    mc "I get it."

    show natsuki 12bg
    "Natsuki doesn’t meet my eyes."
    "She looks embarrassed, and I can’t help but feel bad."

    mc "I’ll be right back, okay?"

    scene black with wipeleft
    "I leave Natsuki on the couch, heading to the doorway."
    "I peer through the peephole. "
    "Who is that?"
    "It’s late. I can’t make out who it is."
    "Another few hard pounds ring though my house."
    "I can hear Natsuki whimper."
    "I turn the deadbolt, but leave the chain on."
    "Just in case."

    scene bg housen with wipeleft
    play music yawa
    show sayori 2bi zorder 0 at t11
    mc "H-hello?"
    s 2bi "Hi, [player]."
    mc "S-Sayori?"
    s 2bh "What’s that smell?"
    mc "What smell?"
    s "It’s your breath."
    s 2bg "It smells like wine..."
    s 1bj "I know you have {i}her{/i} here, so I'll make it quick, but..."
    s 3bk "I just wanted to let you know that I’ve been prescribed some medication that should help me with my..."
    s "My rainclouds."
    s "So you don’t need to worry about me anymore, [player]."
    s 3bl "I know that's what you wanted."
    mc "Sayori, it’s not like that."

    "Natsuki peeks around the corner to the door."

    show sayori 3bf zorder 0 at t22
    show natsuki 3bj zorder 1 at t21
    n "S-Sayori?!"
    n 3bl "Hey!"
    n "I’m glad you’re okay!"
    n 3bk "How're you d-"
    s 1bi "Natsuki..."
    s "I just came over to talk to [player] about something serious."
    s 2bj "Can we have some privacy, please?"
    n 1bn "Oh..."
    n 1bu "Well, okay..."
    n 1bq "I guess I’ll just clean up this mess while you two talk then."
    show natsuki at thide
    hide natsuki
    show sayori 2bi at t11
    "Natsuki retrieves a towel from the kitchen and disappears to the living room once again."
    "I’m surprised she took Sayori’s attitude so well..."
    "Maybe she just doesn’t want to upset her."

    mc "So, what is it?"
    s 2bk "[player], since I've been put on this medication..."
    s "I've been thinking a lot more clearly than usual."
    s "And, well..."
    s "..."
    s 1bh "I think you should break things off with Natsuki."
    mc "What? Why?"
    s 1bg "Because I loved you first, and you threw me to the side."
    s 3bf "It’s not fair."
    s "All I need is to see you happy."
    s 3bh "And now that things are getting better, I think I can do that."
    mc "Sayori, you know I can’t just-"
    s 3bj "Why not?"
    s 3bi "What does she have that I don’t?"
    s 3bj "Is it because you found me with a noose in my hand, ready to die?"
    s "Is it because you really do hate me, like I'd always thought?"
    s 1bj "Give me a reason, [player]!"
    s 1bi "Because I’m not leaving until you do."

    "God damn it..."

    mc "Sayori, you’ve been my best friend for years."
    show sayori 1bu
    mc "I know this is going to hurt, but that’s all we’ve ever been."
    mc "Don’t you think that if we brought feelings into this that we would ruin what we have?"
    mc "I don’t... I don't want to ruin the longest friendship I have over a relationship with someone else."
    mc "Y-you have to understand where I’m coming from, right?"

    "Sayori wipes the tears from her cheeks."
    "My chest feels as if it’s in a vice."

    mc "Sayori, you mean the world to me."
    mc "But I’m just not willing to risk losing you over this."
    s 1bv "..."
    mc "Sayori, please say something."

    "Sayori turns away from me, taking a step off the porch."

    mc "Wait..."

    "I grab her arm and pull her back."

    s 4bw "Let me go!"
    mc "Not yet."
    s 4bv "Just let me go, [player]!"
    s "I got my answer..."
    mc "Well, I wasn't finished."

    "Sayori resists for a few more moments, eventually giving in."

    mc "Sayori, you’re my best friend."
    mc "You’ve changed my life so much since we met."
    mc "Every one of my memories involve you."
    mc "Every birthday, every Christmas, every summer, the club, {i}everything{/i}."
    mc "Sayori, I don’t want to lie to you."
    mc "That’s why I’m gonna tell you this now."
    mc "I need to put this to rest."
    mc "I love you, but..."
    mc "N-not in the way you love me."
    mc "It’s just... platonic."

    "Why has this got to be so difficult?"

    s 2bk "I..."

    "She reaches into her pocket with her hand, and gulps two small capsules."

    mc "Uhm... you’re supposed to be taking them now, right?"
    s 3bl "Y-yeah, yeah..."
    s "I was meant to a couple of hours ago."
    s "..."
    s "I-I’m sorry, I really can’t think straight..."

    "She leans her other hand against the door, to support herself."

    mc "Sayori?"
    mc "You alright?"
    s 4bj "No, I’m not fucking alright!!"
    s 3bg "[player], I love you, so much... but..."
    s "But..."

    "She takes a deep breath."

    s 1bh "You make me sick."
    s 1bf "I’m going home..."

    "I don’t protest."
    show sayori at thide
    hide sayori
    "Instead, I silently watch as she storms down the street to her house and closes her front door behind her."
    "Wordlessly, I let myself back into the house."
    scene bg mclivingroomn with wipeleft
    "Natsuki’s waiting for me."
    show natsuki 4be zorder 1 at t11
    n "So, what was that?"
    n 4bg "I could hear her shouting something."
    mc "She was just... upset that I didn’t love her."
    mc "She wanted me to break up with you."

    "Natsuki shakes her head, glass of wine in hand."

    n 3bu "I feel kinda bad, because it isn't her fault, but..."
    n 3bq "She can’t just demand you \"break it off\" with me because she wants you."
    n 3bh "It’s not fair to try and ruin our relationship like that."
    mc "I know."
    mc "Well, there's some good news... at least..."
    n 1bm "What was it?"
    mc "Well, she got let outta hospital yesterday."
    mc "She’s been prescribed some pills."
    n 1bk "Well, that’s good."
    n "I just hope they’ll help her."
    n "I... I know I was rude about Sayori earlier, but I do care about her, y’know?"
    mc "There wasn’t a doubt in my mind, Nat."
    mc "I just guessed you were p-probably a little shocked by it."
    stop music fadeout(2.0)
    n 2bm "W-wait..."
    n "D-did you just call me Nat?"
    mc "Uhm..."
    mc "Y-yeah..."

    "I give her a weak smile."
    "My head is swimming..."
    "The drink is really starting to kick in..."
    play music tlwamsp
    n 2bj "I... *hic*"
    n "I like it."
    n 2bz "Ehehe~"
    mc "You... do?"
    n 1bt "Y-yeah."

    "She giggles some more."
    "I can't help but join in."
    "I can barely stand."
    "I feel like I could pass out at any moment."
    "I don't even know if it's that late."
    "Either way, I need sleep."

    mc "Uhm..."
    mc "Do you... wanna... go to bed now?"
    n "W-well, it is kinda late..."
    n 2bt "But I'd be happy to... y'know..."
    mc "Oh, I meant go to bed literally, silly."

    "She keeps her eyes locked on me."

    n 4by "I didn't."
    mc "O-oh, right..!"
    mc "Well, if you meant it like that..."
    mc "I’d love to..."

    "Dropping the empty glass to the floor - mercifully, it didn’t smash - she grabs me by the hand and practically drags me upstairs."
    scene bg bedroomn with wipeleft
    "Once we're in my room, she embraces me tightly, and brings her lips to mine."
    "I can hardly see her, but that doesn't matter."
    "We break apart for a moment only to discard my shirt."
    scene n_mod_cg4 with dissolve_cg
    "We collapse onto the bed together, still fiercely making out."

    scene black with dissolve_scene_full
    stop music fadeout(2.0)

    $ quick_menu = False
    scene black
    show sunday
    with dissolve_scene_half
    $ renpy.pause(delay=2.0, hard=True)
    $ quick_menu = True

    scene bg bedroom with dissolve_scene_full

    "The sunlight, creeping through the blinds, forces me awake."
    "The light burns my eyes."
    "Groggily, I gently release myself from Natsuki’s arms."
    "Peering at the clock, I realize it’s almost midday."
    "I stand at the foot of the bed, pulling my boxers and a fresh pair of jeans on."
    "I leave our room as quietly as possible."
    scene bg kitchen with wipeleft
    play music thenumbers
    "Heading downstairs, I hear a faint knock on the door."
    "I head over, taking a glance through the peephole."
    "I see a courier walking back to his van."
    "I don’t remember ordering anything..."
    "I open the door and see the small box he delivered."
    "I take it back to the kitchen, inspecting the label."
    "It’s from... my mother."
    "I haven’t had anything sent from her in ages."
    "She's hardly been able to respond to my texts or calls."
    "Although having the house to myself is quite nice, I wish she hadn’t moved across the country for work."
    "Moving to the counter, I start boiling a pot of coffee."
    "I take my box-cutter knife from the drawer and slice along the taped edge."
    "I cut the tape holding the bubble wrap closed, revealing a new expensive-looking watch."
    "Discarding the box-cutter, I see there’s a note alongside the box."

    python:
        if persistent.language == "spanish":
            poem_mum = poem_mum_spanish
    call showpoem (poem_mum) from _call_showpoem_5

    "I wonder how they’ll react when I tell them Natsuki’s living with me."
    "..."
    "Who am I kidding? They’ll just be happy I finally have a girlfriend."
    "I remove the off white box from its packaging."
    "I'm faced with a smaller, green package."
    "That must have been quite the promotion."
    "I delicately flip open the lid."
    "The watch’s glare is nearly blinding."
    "I lean back in my chair, staring at the glimmering timepiece."

    show natsuki 2ck zorder 1 at t11

    n "O-oh, wow, [player]."
    mc "H-huh?!"
    n "Who’s that from?"
    mc "My parents."
    n 1cq "W-whoa..."

    "Natsuki can’t take her eyes off the box."
    "I can’t blame her, the golden face and band are enough to entrance anyone."
    "I close the box carefully, Natsuki pours us both a coffee."
    "She joins me at the table, gently placing my mug in front of me."

    mc "Thanks, Natsuki."

    "She nods and takes a sip from the mug."

    n 3cj "So do your parents usually send you such fancy gifts?"
    mc "Not like this, but they got promotions... I guess."
    n 3ck "Where are they, anyway?"
    mc "Well, they both had to move ‘cause of their jobs last year."
    mc "They’re fine with letting me stay here until I’m done with high school..."
    mc "After that, I’ve basically gotta get a job ASAP."
    mc "For now though, they've set up a weekly allowance that gets transferred to me."
    mc "Just for groceries and other stuff."
    mc "It’s nothing too crazy, but it’s enough to not go hungry, I guess."
    show natsuki 3cu
    "As those words exit my mouth I realize what I’ve said."
    "Crap."
    "Natsuki squirms a bit in her seat, but doesn’t seem all that bothered."

    n 3cn "Y-yeah, I figured..."
    n 3cs "I don’t really know what my d-... what {i}he{/i} does."
    n 3cq "He’d usually be gone by the time I woke up for school."
    n 3cc "K-kinda weird, huh?"
    n "Not even knowing where the money comes from..."

    "I don’t want to have to dwell on this subject for much longer."
    "After all, I don’t want to taint our day alone together with the thoughts of that abusive piece of..."

    mc "Mhm."
    mc "Listen, did you want to do something special today?"

    "Not exactly the smoothest subject change, but Natsuki’s eyes widen with my words."

    n 2ck "Like what?"
    mc "I was thinking we could go on a proper date."
    n "Whadda you mean?"
    mc "I want to take you out to do something."
    mc "Just the two of us."
    mc "How’s that sound?"
    n 2cl "O-oh!"
    n 2cj "Well, that sounds great, [player]."
    n "What’d you have in mind?"
    mc "Well..."

    "There was the café. It’s not too far from here, and the pastries were delicious."

    mc "I was thinking we could go back to the café."
    mc "I really liked the place. Looked like you did as well."
    n 1ck "Yeah, it was really nice, if you forget about the whole... thing... with Yuri."
    mc "Wanna go get ready then?"
    n 1cz "Ehehe~"
    n 1cl "Sure."

    show natsuki at thide
    hide natsuki
    "Natsuki immediately slides out of her chair and books it upstairs."
    "I can’t help but laugh. She’s genuinely adorable."
    "I take our mugs to the sink, and await Natsuki's return.."
    scene bg bedroom with wipeleft
    "She’s in the bathroom, probably fixing her hair or something."
    "I put on fresh pants and a shirt."
    scene black with dissolve_scene_full
    stop music fadeout(2.0)
    scene bg street with dissolve_scene_full
    "The streets are noticeably empty, even for a Sunday."
    "I pull open the glass door to the café, letting Natsuki hop into the building, with an expression of utter glee painted across her face."
    mc "Ladies f--{nw}"

    "I'm interrupted by a hard slug into my shoulder."

    mc "O-ow!"
    mc "What the hell?"

    "Natsuki flashes a quick grin, winking at me from inside the building."
    "I shake my head as I step inside."
    scene bg cafe with wipeleft
    play music presenttense
    show natsuki 1ca zorder 1 at t11
    n "If I go find a table for us, you can go order."
    mc "Yeah, yeah..."
    n "Ooh, [player]..."
    n 2ck "Could you get me... a couple of the pastries I had last time?"
    n 2cl "I really liked them."
    mc "Okay, sure."
    mc "Anything else?"
    n "Maybe a drink too?"
    n 2cj "Something sweet."

    show natsuki at thide
    hide natsuki
    "Natsuki sits herself at a booth near the back of the café."
    "I order both of us the same pastry, getting Natsuki a glass of orange juice."
    "After I place our order, I head to the booth Natsuki chose for us."
    "As I walk towards her, I can't help but notice that the café is rather empty for this time of day."
    "Must be because it’s a Sunday..."
    "Regardless, I take a seat opposite her."
    show natsuki 1cc zorder 1 at t11
    n "So..."
    n 3cj "Didn’t you say, a couple nights ago you were gonna head out and buy us the new volume of Parfait Girls?"
    mc "The latest one?"
    mc "It’s a bit pricey, don’t you think?"
    n 3ck "Well, yeah, I guess..."
    n 3cc "I just assumed you had enough to get it."
    n 3cq "Y’know... with the watch..."
    n 1cs "Your parents..."
    mc "I do have enough, you know."
    mc "I’m just a bit cautious about how I-"

    "Natsuki scoffs sarcastically."

    n 1cw "Pfft~"
    n 1cy "You're just putting off reading it with me, aren't you?"
    mc "Wha- no!"
    mc "I’m just a little bit wary of how I actually spend my money is all."
    mc "You never know when you might need it..."
    mc "Besides, we haven’t even gotten through half of the set we have yet."
    mc "I’m not really in a rush to buy it now anyway. It’ll probably be another week before we even finish off this volume..."
    n 2ct "Mmm, I guess..."
    mc "I will get around to it though."
    n 2cc "Promise?"
    show natsuki 2cd
    mc "I promise."

    "The barista calls out our order."

    mc "Give me a second."
    show natsuki at thide
    hide natsuki
    "Exiting the booth, I make my way to the counter, where the barista is busy taking someone else’s order."
    "They’ve left two small plates, with a pastry each, on the counter. The glass of juice is next to it."
    "Seeing as I haven’t yet paid, I leave a note covering the bill in place of our order."
    "I pick up the plates in one hand, and the glass in the other."
    "As I return to the table, Natsuki immediately snatches her pastry."
    show natsuki 1cy zorder 1 at t11
    n "Mmmft-"
    n 1cz "I love these things."
    mc "I’d have guessed."

    "Natsuki has already wolfed down the whole thing in only a few quick bites."
    "She seemed completely oblivious to how quickly she was eating."
    "I glance her a quick grin, before taking a bite from my own pastry."
    "It’s delicious."
    show natsuki 1cl
    "Natsuki, her eyes wild with excitement, leans over the table and attempts to take a bite from my pastry."
    "I instinctively pull back, holding the pastry out of reach."

    mc "Hey hey! Leave mine alone!"
    n 3ct "Fine, fine..."

    "She returns to her seat. I return to mine."
    "Hurriedly, I munch down on the rest of my pastry quickly."
    "As I do so, Natsuki snaps to her right for a moment at the sound of the door swinging open."
    "Just another guest."
    "She turns back to me, bringing the orange juice to her mouth and taking a sip."

    n 1cj "Mmm..."
    n 1cl "Thanks, [player]."
    mc "It’s no problem."
    mc "Anything for you."

    show natsuki 1cz
    "She grins at me."
    "A few awkward moments pass, as she gulps down her orange juice in silence."

    mc "Ready to go?"
    n 3ca "Just about, yeah."

    "We both slip out of the booth simultaneously, and I neatly stack the plates and the glass for the barista."
    "I hold open the door for her, and we make our way back out into the street, hand in hand."
    scene black with dissolve_scene_full
    stop music fadeout(2.0)
    scene bg house with dissolve_scene_full
    play music tinkertailor
    "As we approach the door, Natsuki stops me."
    show natsuki 1cc zorder 1 at t11
    n "[player], thanks for taking me out."
    n 1cq "It... really means a lot to me."
    n 1ct "I... I love you."
    mc "I love you too."
    scene bg mclivingroom with wipeleft
    "The two of us enter the house and head to the living room."
    "Natsuki takes the remote and finds us a show to watch."
    scene black with dissolve_scene_full
    stop music fadeout(2.0)
    scene bg mclivingroomn with dissolve_scene_full
    play music giveup
    show natsuki 3cb zorder 1 at t11
    n "Hey!"
    n 3cc "Are you hungry yet?"

    "I look at the clock, somehow hours have passed without my knowledge."

    mc "Not really, are you?"
    n 3cd "Nah, I ate way too much at the café..."
    n 3cz "Ehehe~"
    mc "I am a little thirsty though. You want me to fix us a drink?"

    "Natsuki nudges her leg, and removes her head from my shoulder."

    n 1cj "Yeah, thanks."
    scene bg kitchen with wipeleft
    "I head to the fridge, take one of the remaining bottles of wine, and pour the both of us a healthy glass."
    "I struggle to fit the cork back into the bottle before returning it to the fridge."
    scene bg mclivingroomn with wipeleft
    show natsuki 2ck zorder 1 at t11
    n "No bottle service today?"
    mc "No, we have school tomorrow."
    mc "If we hadn’t missed the majority of last week, I’d be more than happy to drink the whole thing."
    mc "I can’t imagine tomorrow will be an easy day."
    n 2cc "You’re right..."
    n 2cd "It’s too bad we can’t just keep bunking off."
    mc "I know, it’ll be hard to get used to attending classes again."
    n 2ca "Mhm."

    "We finish our glasses of wine, watch a few more shows, and head upstairs."

    n 1cj "I think I’m just gonna shower now, it should save a bit of time in the morning."
    show natsuki at thide
    hide natsuki
    "Natsuki heads to the ensuite bathroom while I head to the main."
    scene black with dissolve_scene_full
    stop music fadeout(2.0)
    scene bg bedroomn with dissolve_scene_full
    "I flop down onto my bed and stare at the ceiling, hearing the water cut out from the en-suite."
    "I decide to wait for Natsuki before I pull the covers over."

    show natsuki sexy1 zorder 1 at t11
    n "[player]..."

    "I stand up and see Natsuki in her towel."
    "I can hardly see her in the moonlight."
    show natsuki sexy2
    "Natsuki throws her towel to the floor, pushing me back onto the bed."
    scene black with dissolve_scene_full

    $ quick_menu = False
    scene black
    show monday
    with dissolve_scene_half
    $ renpy.pause(delay=2.0, hard=True)
    $ quick_menu = True

    scene black with dissolve_scene_full

    n "Ohh, crap."
    mc "Mmm… wh…"

    "I can feel Natsuki stirring beside me. Her outstretched arms brush along my shoulder."
    "I yawn, mouth open wide."

    mc "Wh… what’s up?"
    n "We’re gonna be late, dummy. We gotta get going."

    "She clambers out of bed, and I hear my bedroom door slam shut."
    scene bg bedroom with wipeleft
    play music tinkertailor
    "I wrench my eyes open, and rise from my bed."

    mc "Mm… go where?"
    n "School!"
    mc "Oh, yeah..."
    mc "Crap..."

    "I begin hastily ransacking my drawers in an effort to find my uniform."
    "I quickly throw on my pants and shirt, followed by my tie."
    "Natsuki emerges, tying the ribbon on her uniform."

    show natsuki 3fc zorder 1 at t11
    n "[player]..."
    n 3fm "D’you know where my jacket is?"
    mc "Not a clue, love."
    n 3fn "Ugh…"
    n 4fs "Damn it."

    "I pull the jumper over my head, followed by my own blazer."

    mc "You want mine?"
    n "It’d be {i}massive{/i} on me."
    n 4fq "Thanks, but not really."
    mc "All right."
    n 2fu "I just hope I don’t get told off..."
    mc "I doubt it."
    mc "Just don’t worry about it, okay?"

    "I rush downstairs, Natsuki right behind me."
    scene bg mclivingroom with wipeleft
    "Putting my shoes on, I swing the front door open."

    show natsuki 1fc zorder 1 at t11
    mc "Come on!"
    n "Yeah, yeah, I’m coming…"

    "Slamming the door behind us, we rush to school."
    scene black with dissolve_scene_full
    stop music fadeout(2.0)
    scene bg courtyard with dissolve_scene_full
    "We made it on time, thank God."
    "Walking through the courtyard, we part ways with a light kiss as we depart to our separate lessons."
    show natsuki 2fk zorder 1 at t11
    n "See you later!"
    n 2fl "Love you!"
    mc "Love you too!"
    show natsuki at thide
    hide natsuki
    "I notice a couple of students whispering and pointing in our direction."
    "I have to assume they’re just jealous they don’t have what we do."
    "I turn and flip them off, before hastily making my way into the school building."
    scene bg corridor with wipeleft
    "I hurry through the corridor towards my first lesson."
    "As I turn a corner, I bump into someone, nearly knocking them backwards."
    "The flash of purple I saw as they fell tells me that it was Yuri."
    show yuri 3o zorder 1 at t11
    mc "Oh, sorry."
    y 3n "O-oh! [player]!"
    y "It’s fine..."
    y 2q "I was hoping to see you, actually."
    y 2t "You see, we need to talk."
    mc "I-I don’t think now’s the time, Yuri."
    mc "I’ve got a lesson to get to…"
    mc "So do you… right?"
    y "I suppose..."
    y 2v "B-but I wouldn’t mind {i}too much{/i} if I missed it."
    y 1f "Besides, this is important."
    mc "We’ll talk later, okay?"
    mc "At the club?"

    "I try to walk away, and she grabs my arm to stop me."

    mc "H-hey!"
    y 2g "This needs to be private."
    y 2h "Just the two of us."

    "Seeing that there’s not much chance of me escaping this, I accept it."

    mc "Fine."
    mc "But make it quick."

    "She beckons me along to a vacant classroom."
    scene bg class_day with wipeleft
    "She practically barges down the door with excitement, dragging me inside."
    "She locks it behind us."
    show yuri 1h zorder 1 at t11
    mc "Why are you..?"
    y "Sit, there."

    "I reluctantly take a seat at one of the desks."
    "What the hell is she playing at?"

    y 1f "You see, [player]..."
    y "I needed you alone because..."
    y 4b "{i}I-I don’t know how else to say it…{/i}"
    y 3y6 "I'm…"
    y "I'm…"
    play music climbingup
    y 3y5 "I'm madly in love with you."
    y 3q "There… I said it."
    y "I just… need you to know."
    y 3r "I don't care if that immature child is listening!"
    y "[player], you don’t want to be with her."
    y "Believe me."
    y 1y4 "She’s a bitch."
    y "She doesn’t really love you… not like I do."
    y "What happens to her is entirely her fault."
    y 2y7 "She doesn’t deserve somebody as brilliant as you."
    y "You know that you can do better..."
    y "And I’m right here."
    y 2y1 "[player], I want you to be with me, and only me."
    mc "N-no..."
    mc "I’m with Natsuki."
    mc "I love her."
    mc "That isn’t going to change."
    y 2y3 "[player], I want you inside me."
    y "You know you want to."
    y 3y1 "So just let me--{nw}"

    "Yuri reaches out to grab my tie, pulling me towards her."

    mc "H-hey!!"
    mc "Get off me!"

    "The feeling of helplessness is inescapable."
    show yuri 3y2 zorder 1 at h11
    "Shocked, I shove her back, knocking her into a desk."
    "Her momentum slides it back a little, but it comes to a halt quickly."

    y 3t "Oh, [player]..."
    y 2y4 "Why would you prefer a little {i}girl{/i} when a woman is standing right in front of you?"
    y "Trust me [player], I could treat you much better than she ever could."
    y 2y6 "All I’m asking for is a chance to show you what I can do."
    y "Can you at least give me that?"
    mc "No, Yuri. I can’t."
    mc "Just… leave me alone."
    y 3y6 "I know you saw my pictures, [player]."
    y "I know you liked them."
    y "That’s why you said that your phone was malfunctioning."
    y 3y1 "You wanted me to take more for you."
    y 3y4 "So, why are you turning me down right now?"

    "She edges forward."
    "Yuri’s getting a little too close."

    y "Which one was your favourite?"
    y "I bet it was the one with the heart."
    y 2y3 "I saw that in your eyes, [player]."
    y "At the café."
    y 2y4 "I know you want me."
    y "There’s no need to hide it anymore."
    y 2y1 "So come on, {i}take what’s yours{/i}."

    show yuri 2dy1
    "Yuri reaches out to her shirt, and begins to unbutton it in an attempt to seduce me."

    mc "Yuri, that’s enough."
    mc "Really."
    mc "Cut it out, now."

    "I reach out and grab her hands to stop her from unbuttoning her shirt any further."

    y 1dy4 "Why, [player]? Afraid you’ll give in?"

    "Yuri inches toward the wall, still unbuttoning her shirt."

    mc "Yuri! I told you to stop!"

    "I grab her arms and shove her up against the classroom wall."

    y 1dy1 "Wow, [player]."
    y "I didn’t know you liked to be so rough."

    "Turning for a second, I see a blurred face in the window disappear."
    "I’m absolutely sick of her attitude."
    "I’m not going to bother being polite anymore."

    show yuri 1dy2 at h11
    mc "Fuck you."
    mc "You’re an obsessive, bullying, narcissistic bitch."
    mc "And you’re lucky I won’t tell anyone about {i}this{/i}..."
    mc "Just… stay the hell away from me, you hear?!"
    mc "And stay away from Natsuki, too."
    mc "Because if you don’t…"
    mc "They’re gonna know about {i}these{/i}."

    "I motion towards my arms."

    mc "You understand?"
    y "I-I-I…"
    y 1do "Why, [player]?"

    "I let go of her, and make a break for the other door, suspiciously wide open."

    y 3dp "[player], wait!"
    scene bg corridor with wipeleft
    "I sprint though, running as fast as I can towards my classroom without looking back."
    scene black with dissolve_scene_full
    stop music fadeout(2.0)
    scene bg class_day with dissolve_scene_full
    play music tinkertailor
    "As pushy and psychotic as Yuri was being, I feel terrible for lashing out at her like that."
    "That wasn’t like me..."
    "But if it keeps her away from us, then I’m glad it worked, at least."
    "And I {i}will{/i} have to maintain my threat."
    "Regardless, I turn back to my mountain of school work."
    "How could I have missed this much in a week?"
    "It’s almost a blessing that I have two weeks worth of detention to catch up."
    "I doubt I’d be able to get anything done at home."
    "The school’s bell rings, signalling the end of the day."
    "I consider skipping the detention, and just going to the club instead."
    "Hopefully I can find Monika, and tell her to keep Yuri away from me."
    "Packing the piles of unfinished worksheets into my bag, I leave for the club."

    scene bg corridor with wipeleft

    "Sayori and Monika are both waiting outside, seemingly scared to enter."
    "Sayori doesn't meet my gaze."
    show sayori 2k zorder 1 at t21
    show monika 1o zorder 2 at t22
    mc "H-hey, what’s going on?"
    m 1f "Oh, [player]..."
    m 2g "They’re throwing names at each other."

    "My stomach twists into a knot."

    mc "Right..."
    mc "You know what they’re arguing over?"
    m 2r "Yuri told Natsuki to \"ditch you, because you’d already devoted yourself to her\"."
    mc "That's a load of bullsh-"
    m "We tried to stop the fighting, but they’re both so angry..."
    show sayori at h21
    show monika at h22
    n "{i}You total bitch!{/i}"




    mc "I need to end this right now."
    stop music fadeout(2.0)
    "I feel the doorknob twist in my hand as I enter the clubroom."
    scene bg club_day with wipeleft
    show natsuki 1fth zorder 1 at t11
    mc "Natsuki, are you--{nw}"
    n "N-no…"
    n 1ftf "I-I…"

    "She mutters something, but I don’t catch it."
    show natsuki at lhide
    hide natsuki
    "She shoves past me, tearing down the hall."
    scene bg corridor with wipeleft
    play music tinkertailor
    "I follow out of the room, only to be stopped by Monika."
    show sayori 2k zorder 1 at t21
    show monika 1o zorder 2 at t22
    mc "What’d she say?"
    s 2h "She said she wanted to be alone."
    s 2j "For once, she’s not desperately clinging to you."
    mc "Shut it. There’s no need to be so rude."
    s 1i "Sorry."
    s "I was just a little surprised, considering--"
    show sayori 1k at h21
    mc "Sayori, shut your fucking mouth for a minute."
    mc "Just..."
    mc "I shouldn't have snapped..."
    mc "S-sorry... I just... I gotta go see if she’s okay."
    show monika at thide
    hide monika
    show sayori at thide
    hide sayori
    "I follow in Natsuki's footsteps, sprinting out of the school to get home."
    scene black with dissolve_scene_full
    stop music fadeout(2.0)
    scene bg mclivingroom with dissolve_scene_full
    "Slamming the front door behind me, I make my way upstairs."
    scene black with wipeleft
    mc "Natsuki?!"
    n "I-I’m in the b-b-bathroom, [player]. I told you to leave m-me alone..."
    mc "Are you okay? What did Yuri say to you?"
    n "She…"
    n "I-it was nothing."

    "I grit my teeth together."
    "I don’t think she’s going to tell me anything right now."
    "If she’s feeling better later on, then maybe…"
    "But I can hear her sobbing through the door."
    "I’ll give her some space."

    mc "Okay…"
    mc "I’ll just be in my room if you need anything, alright?"
    n "O-okay."

    scene bg kitchen with wipeleft
    "I reluctantly leave her be, heading downstairs for a drink."
    "I check the fridge to see what we have."
    "It still baffles me how much food is in here."
    "Since Natsuki moved in with me, it’s always stocked with ingredients."
    "The longer I stare into the fridge I feel as if something is missing…"
    "{i}The wine.{/i}"
    "I don’t want her drinking when she’s so emotional…"
    "I’ll talk to her."
    scene black with wipeleft
    "I head upstairs again, and knock on the bathroom again."

    mc "Natsuki, have you got the bottle of wine?"
    n "Y-yeah…"
    n "J-j-just.. please g-go away…"
    mc "I’m just worried about you."
    mc "Please, don’t drink it… or any more if you have."
    n "[player]... I t-told you to go…"

    "I sigh."

    mc "I’m sorry, but I’m coming in to take it."
    mc "I just… can’t bear to see you like this."
    n "N-no… [player]... don’t…"

    "I fiddle with the handle for a second."

    mc "Look, if you’re getting changed or something, I’ll just close my eyes."
    mc "Just hand me the bottle and I’ll leave you alone, okay?"
    n "F-fine…"

    "I open the door, eyes clenched shut."
    "I hold my arm out, hand outstretched and waiting for the wine bottle."
    "It reaches my hand, and I close my hand around it."
    "It’s wet around the sides, and I start to lose my grip."
    "The bottle slips out of my hand, and I can hear it shatter against the tiles."

    mc "Shit!"

    "I open my eyes to look at the remains."
    scene bg bathroom with wipeleft
    "And in the corner of my eye, I see Natsuki."


    show natsuki 1gcry zorder 1 at t11
    play music glasseyes
    mc "O-oh god…"
    mc "No, no, no, no no no… please…"
    mc "Natsuki… please…"
    n 1gth "I’m s-so s-s-sorry, [player]..."
    n 1gti "S-s-she told me to..."
    mc "Wh-what… why..?"
    n "I-I’ve been feeling s-so… so bad…"
    n 1gth "Th-those kids… they f-followed me to my class, a-a-and they were…"
    n "They were…"
    n "Just…"
    n 1gtf "H-horrible."
    n "I r-ran out of the class…"
    n "I saw y-you with Yuri…"
    n 1gth "I… I didn’t w-want to believe that s-something was… going on, between y-you…"
    n "B-but she t-told me…"
    n 1gti "You wanted to b-be with her…"
    mc "Natsuki... I’d never--"
    n "Th-they were right…"
    n 1gtf "W-why would anyone w-want me..?"
    n "Yuri’s right… s-she’s so much more m-mature than me, [player]."
    n 1gth "Everyone sees me as the… \"cute girl\"..."
    n 1gti "S-some arrogant k-kid…"
    n 1gth "I m-made that name for myself…"
    n "It’s my fault…"
    n 1gti "This i-is all my f-f-fault."
    mc "No, you just don’t--"
    n 1gtf "I don’t want to h-hear it."

    show natsuki 1gtf at h11
    "I grab Natsuki by her shoulders in an attempt to force her to listen to me."

    mc "I… I can’t…"
    mc "Natsuki, please... just hear me out."
    n "F-fine..."
    mc "This morning, Yuri threw herself at me. She was overly aggressive…"
    mc "The only reason I got out of there when I did, was because I threatened her…"
    mc "Threatened to expose what she’s been doing if she didn’t stay away from us."
    mc "I didn’t want to, but I was desperate."
    mc "And she’s crossed that line now…"
    mc "I love you, and only you, Natsuki."
    mc "I don’t know why you’d believe what she said."

    play sound "sfx/slap.ogg"
    show white zorder 6:
        alpha 0.6
        linear 0.25 alpha 0.0
    show natsuki 1gth
    "I recoil back, holding my cheek."
    hide white

    "What did I say that was so wrong, I deserved that?"

    n 1gcry "D-don’t lie to me!"
    n "You would’ve deleted the pictures she sent you otherwise!"
    mc "Nat, you aren’t listening to me. Nothing happened."
    show natsuki 1gth
    mc "Yuri was acting like a psycho… she tried to force herself on me."
    mc "That’s all there was…"
    mc "I swear to you."

    "Natsuki says nothing."
    "And she’s still bleeding… "
    "Shit…"

    mc "Come on, let’s go."
    n 1gcry "What? I’m not going anywhere."
    mc "For fuck’s sake, Natsuki! I’m taking you to the god damn hospital before you bleed out in my bathroom!"
    n 1gth "M-make me."

    "Natsuki sits down on the rim of the bathtub, hands buried in her hair, her locks beginning to match her ribbons. "
    "I grab her arms, careful not to touch her wounds."
    "I pull her to her feet."

    mc "We’re going. Now."
    n 1gcry "No! I-I don’t want to!"

    "Natsuki’s knees buckle, and she begins to fall forward."
    "I catch her on the way down."

    mc "This isn’t negotiable, we’re going."
    n 1gtf "N-no…"

    show natsuki at thide
    hide natsuki
    "Reaching into my pocket for my phone, I speed-dial the emergency number and press my phone to the side of my head."
    "I explain the situation. The operator assures me that an ambulance is on it’s way."
    "I gently lift Natsuki from the bloody tiles, carrying her downstairs."
    scene bg mclivingroomn with wipeleft
    "I lay her down on the couch, and rush to the kitchen for a towel."
    "I kneel beside her trying to minimize the bleeding, staring out the window waiting for the flashing lights to appear."
    scene black with dissolve_scene_full
    scene bg mclivingroomn with dissolve_scene_full
    "After what feels like hours, the ambulance arrives, two paramedics hop out and wheel the gurney to my door."
    "As I pick Natsuki up once more, I notice she’s unconscious."
    "The paramedics roll the gurney into the living room, I lay her down onto it."
    "Immediately they begin to rush her back to their vehicle."
    "I follow."
    scene bg housen with wipeleft
    mc "Wait! Can I stay with her?"

    "The attendant nods, motioning for me to get in."
    scene black with wipeleft
    "I jump into the ambulance, and immediately we speed off to the hospital."
    "I can’t do anything but watch as the paramedic does everything he can to stop the bleeding."
    "I’ve answered all the questions I could, of course mentioning that she's probably gotten through a whole bottle of wine."
    "I overhear the driver speaking on the radio, mentioning that Natsuki’s wounds are \"fairly deep\"."
    "The ambulance comes to a sudden halt."
    "The back doors immediately swing open, and Natsuki is rolled out."
    "I try to follow with her into the A&E ward, to no avail."
    "Instead, a nurse intercepts me, and leads me to the waiting area."
    scene bg hospital with wipeleft
    "She also mentions that they will keep me updated."
    "Reluctantly, I take a seat and wait."
    scene black with dissolve_scene_full
    stop music fadeout(2.0)
    $ quick_menu = False
    scene black
    show tuesday
    with dissolve_scene_half
    $ renpy.pause(delay=2.0, hard=True)
    $ quick_menu = True

    scene bg hospital with dissolve_scene_full
    play music giveup
    "I feel something nudge my shoulder."

    mc "N-Natsuki..?"

    "I rub my eyes and see the same nurse from earlier..."
    "Must've been yesterday, even."
    "She explains that Natsuki was discharged an hour ago, and her emergency contact was called to pick her up."
    "{i}Emergency contact?{/i}"
    "My chest feels as if it has collapsed on itself."
    stop music fadeout(2.0)
    "That...that has to be her dad."
    "I jump from my chair, rushing out of the hospital without another word."
    scene bg street with wipeleft
    "Making my way to the nearest bus stop, I glance at the schedule posted on the stop."
    "I don’t have ten minutes to spare..."
    "The hell with it."
    "I depart from the stop, sprinting down the street to get to her house."
    "I need to get her out of there."
    "God knows what he’ll do to her in the state she’s in..."
    "Not to mention the property damage, and the fact that we've stolen from him."
    "I didn’t even have a chance to fully explain to her what Yuri was doing..."
    "That I was totally against it, and even had to threaten Yuri just to get her to stop."
    scene bg nhome with wipeleft
    "I can see her street sign as I slow down into a jog."
    "As I round the corner, I see him."
    "Her father is planted on the balcony, where I first overheard his conversation."
    "He’s smoking a cigarette, taking a deep puff from it."
    "I can’t tell if it's the running or the stress, but I feel as if my heart is going to leap from my chest any moment."
    "I can’t go to confront him about this directly, not now. He’d kill me."
    "I need to wait for him to leave."
    "I hang a left, deciding to head back home."
    scene black with dissolve_scene_full
    scene bg house with dissolve_scene_full
    "After a short while, I return to the familiar view of my house."
    scene bg mclivingroom with wipeleft
    "I head up to my bedroom."
    scene bg bedroom with wipeleft
    "I undress, noticing the blood stains on the sleeves of my blazer."
    "She tried again..."
    "Everything in me feels as if my life is tearing apart, all because she's been taken from me."
    "I launch my jacket as far away from me as I can."
    "With nowhere else to vent my rage, I drive my fist into my desk, causing the contents of the shelves above to topple over."
    "An issue of Parait Girls and some papers fall to the floor."
    "Looking down at the manga, I notice a word on one of the papers."
    "{i}\"Hero.\"{/i}"
    "I place the poem back onto my desk carefully, and get dressed as quickly as possible."
    scene bg kitchen with wipeleft
    "I search through my house for anything I can use to protect myself, just in case I do have a run-in with her father."
    "Nothing other than kitchen knives."
    "If I'm caught in public with one of those, I'm dead."
    "I guess I’m going empty handed."
    scene bg mclivingroom with wipeleft
    "I head toward the front door, noticing the closet in the foyer was left open."
    "Out of habit I close it, not before seeing Natsuki’s jacket and the scarf I bought her."
    "I can’t tell what’s driving me anymore."
    "Is the rage directed toward her father?"
    "Is it the anxiety caused by her actions last night?"
    "Or is it the void she’s left by being taken from me?"
    "I slam the closet door, running out of my house."
    scene black with dissolve_scene_full
    scene bg nhome with dissolve_scene_full
    "I can see Natsuki’s house."
    "I stop running and walk instead."
    "I’m not wearing running clothing, and I figure that someone in a long sleeve shirt and jeans may seem out of the ordinary."
    "I’m steps away from the gates of her home."
    "I can see her father's car, parked in the driveway."
    "I continue down her street and round the block."
    "I see a bus stop with a bench across the street."
    "I’m going to sit here until I hear his car leave."
    "The car is a performance vehicle."
    "I'd be able to hear the obnoxiously loud engine from a mile away."
    scene black with dissolve_scene_full
    scene bg nhome with dissolve_scene_full
    "I check my phone for the time."
    "I’ve been sitting here for an hour and a half."
    "And she’s still in there."
    "I need a drink."
    "My tongue feels like sandpaper."
    "I stretch out and stand up, heading quickly to the store nearby for a can of cola."
    scene black with dissolve_scene_full
    scene bg nhome with dissolve_scene_full
    "Back and refreshed, I pass by Natsuki’s house."
    "The car is still parked in the driveway."
    "I'm coming for you, Natsuki."
    "I promise."
    scene black with dissolve_scene_full
    scene bg nhome with dissolve_scene_full
    "Again I round the block, this time walking around and sitting down at the bus stop on her street."
    "I stay there, motionless, fixated on the house’s gate."
    "A hand on my shoulder breaks my concentration, and makes me jolt to my feet."

    show monika 1bd zorder 1 at t11

    m "[player]... what are you doing here?"
    mc "I-uh…"
    mc "It’s private, Monika. Sorry."
    mc "What're {i}you{/i} doing here?"
    m 1bc "I was going to check in on Natsuki. Yuri told Sayori and I that you two broke up."
    m "I stopped by your house as well, but you weren’t home."
    mc "We didn’t break up, Monika."
    mc "Her dad took her back after I took her to the hospital."
    m 2bh "So what, you’re just going to sit here and stake out her house?"
    m 2bi "And why was she at the hospital?"
    mc "She-"

    "I choke on my words, but by the look on Monika’s face, she can tell what I’m trying to say."

    m 2bg "Was it because of Yuri?"

    "I nod."

    m 1bp "I didn’t think she’d take it seriously..."
    m 1bg "Why don’t you just go knock on her door and ask to see her?"
    mc "I can’t do that, and neither can you."
    mc "It’s not for me to explain..."
    mc "But if you knock on that door, Natsuki might get hurt again."
    m 1bp "What do you mean, {i}again?{/i}"
    mc "Her father, he..."
    mc "He..."
    m 1bo "..."
    m "Oh..."
    m 1bo "Jesus."
    m 2bq "I understand, [player]."
    m 4br "Do you want me to keep you company while you wait?"
    mc "I don’t think that’s a good idea, Monika."
    mc "You should probably get wherever you’re going… it’s getting late."
    m 3bf "Okay, [player]. Let me know if there’s anything you need, okay?"
    m 1bg "Just call me."

    "I nod and give her a weak smile, as she stands and walks away."
    scene black with dissolve_scene_full
    stop music fadeout(2.0)
    scene bg nhomen with dissolve_scene_full
    "Finally, I hear the engine start and the headlights illuminate the driveway."
    "This is my chance."
    "The gate opens, allowing the car to burst from the driveway."
    "I didn’t see anyone in the passengers seats, she must still be inside."
    "I sprint toward her house."
    "I need to act fast, I’m not sure how long he’ll be gone for."
    "I’m banking on her being holed up inside her room, like last time."
    "So, it shouldn’t take long to pick her up, and take her to the police station."
    "This can’t go on any longer. I won’t let it."
    "Seeing as the knocks provided no response, and I’m not taking no for an answer, I brace myself for impact as I swing a small rock into the glass window on the door."
    "The glass shatters."
    "I know exactly what the consequences would be if her father caught me trespassing like this."
    "But I don’t care."
    "I jam my right hand through the window and unlock the door from the outside."
    "It creaks open, and I slip through, slamming it behind me."
    scene bg hallwayn with wipeleft
    "Peeking through the downstairs of the house, she’s nowhere to be seen."
    "Definitely her room then."
    scene black with wipeleft
    "I nearly find myself sprinting up the stairs, shouting her name."

    mc "Natsuki!"
    mc "It’s me!"

    "I notice that the remains of the doorframe I’d left behind have been cleaned up, leaving a vacant entrance to her father’s room."
    "Curiosity washing over me, I take a quick look."
    "Her father’s room is even bigger a mess than hers was all that time ago."
    "The cupboard is gaping open, clothing littering the floor."
    "Desk drawers torn open, their contents spilled."
    "A fast-food wrapper litters the bed. I reach out and feel it."
    "Still warm."
    "That must’ve been from before he left, then."
    "Backtracking to Natsuki’s door, I nearly trip over on what appears to be her shoes, strewn out neatly in the hall."
    "I remember what she told me about knocking."
    "And what happened when I didn’t."
    "For my own safety, I rap on the door a couple times."

    mc "Natsuki?"
    mc "It’s me..."

    "Nothing."
    "Ah, the hell with it."
    "{cps=30}Swinging open the door, I{/cps=30}{nw}"

    $ quick_menu = False
    $ _windows_hidden = True

    window hide(None)
    window auto
    play music daydreaming
    play background natsuki
    show n_kill_bg2
    show n_kill2
    show n_kill_bg as n_kill_bg at n_kill_bg_start
    show n_kill as n_kill at n_kill_start
    $ renpy.pause(delay=4.0, hard=True)
    show n_kill_bg2 as n_kill_bg
    show n_kill2 as n_kill
    show black zorder 5
    $ renpy.pause(delay=0.0001, hard=True)
    hide black
    hide n_kill_bg
    hide n_kill
    show n_kill_bg_zoom zorder 1
    show n_kill_bg2_zoom zorder 1
    show n_kill_zoom zorder 3
    show n_kill2_zoom zorder 3
    show n_kill as n_kill_zoom_trans zorder 3:
        truecenter
        alpha 0.5
        zoom 2.0 xalign 0.5 yalign 0.05
        pause 0.5
        dizzy(1, 1.0)
    show vignette zorder 3:
        alpha 0.0
        linear 3.0 alpha 0.75
    $ renpy.pause(delay=6.0, hard=True)

    $ quick_menu = True
    $ _windows_hidden = False

    mc "N-Natsuki...?"
    "No…"
    "No."
    "This…"
    "I’m not…"
    "I’m not here."
    "This isn’t happening."
    "That..."
    "What the fuck..?"
    "My entire body feels cold."
    "I can't even feel my heart beating anymore."
    "I drop to my knees."
    "She… she can’t be..."
    "Natsuki..."
    "She's gone."
    "The only girl that I've loved like this..."
    "She's been taken from me..."
    "I want to scream, but I can't make a sound."
    "The overwhelming urge to vomit nearly overcomes me..."
    "But my sobbing suppresses the bile in my throat."
    "I can hardly breathe."
    "I can't even see properly, my tears fogging my vision to a blur..."

    mc "N-N-N..."

    "I can't even speak her name without it getting caught in my throat."
    "I reach out, and gently wrap my hand around hers."
    "It’s limp. Lifeless. Cold."
    "I take my hand back."
    "I loved her."
    "But I couldn't save her."
    "I've never felt so weak in my entire life."
    "Try as I might, I can't even bring myself to stand."
    "All sensation other than absolute dread has left me."
    "I can’t bear to look at her like this anymore…"

    scene black with dissolve_cg

    "I jam my eyes shut, and try to fill my mind with memories of her."
    "Happy thoughts."
    "Happy thoughts."
    "Happy thoughts..."

    $ quick_menu = False
    $ _windows_hidden = True

    scene black with dissolve_scene_full
    $ quick_menu = False
    window hide(None)
    scene bg nhomen with dissolve_cg
    $ renpy.pause(delay=2.0, hard=True)
    scene bg streetn with dissolve_cg
    $ renpy.pause(delay=3.0, hard=True)
    scene bg housen with dissolve_cg
    $ renpy.pause(delay=3.0, hard=True)
    show sayori 1ci zorder 1 at t11
    $ renpy.pause(delay=2.0, hard=True)
    show sayori 1cv
    $ renpy.pause(delay=1.0, hard=True)
    show sayori 4cw
    $ renpy.pause(delay=2.0, hard=True)
    scene bg housen with dissolve_cg
    $ renpy.pause(delay=2.0, hard=True)
    scene bg bedroomn with dissolve_cg
    $ renpy.pause(delay=3.0, hard=True)
    scene bg bedroom with dissolve_cg
    $ renpy.pause(delay=5.0, hard=True)
    scene bg bedrooms with dissolve_cg
    $ renpy.pause(delay=2.0, hard=True)
    scene bg bedroomn with dissolve_cg
    $ renpy.pause(delay=3.0, hard=True)
    scene bg bedroom with dissolve_cg
    $ renpy.pause(delay=3.0, hard=True)
    scene bg bedrooms with dissolve_cg
    $ renpy.pause(delay=2.0, hard=True)
    scene bg bedroomn with dissolve_cg
    $ renpy.pause(delay=3.0, hard=True)
    scene bg bedroom with dissolve_cg
    $ renpy.pause(delay=5.0, hard=True)
    scene bg bedrooms with dissolve_cg
    $ renpy.pause(delay=2.0, hard=True)
    scene bg bedroomn with dissolve_cg
    $ renpy.pause(delay=3.0, hard=True)
    scene bg bedroom with dissolve_cg
    $ renpy.pause(delay=5.0, hard=True)
    scene bg bedrooms with dissolve_cg
    $ renpy.pause(delay=2.0, hard=True)
    scene bg bedroomn with dissolve_cg
    $ renpy.pause(delay=3.0, hard=True)
    scene bg bedroom with dissolve_cg
    $ renpy.pause(delay=2.0, hard=True)
    scene black with dissolve_scene_full
    stop music fadeout(2.0)
    scene black
    show sunday
    with dissolve_scene_half
    $ renpy.pause(delay=2.0, hard=True)
    $ quick_menu = True

    window auto
    scene bg bedroom with dissolve_scene_full

    $ quick_menu = True
    $ _windows_hidden = False

    play music glasseyes
    "{i}KNOCK.{/i}"
    "{i}KNOCK.{/i}"
    "{i}KNOCK.{/i}"
    "{i}KNOCK.{/i}"
    "{i}KNOCK.{/i}"
    "They're not gonna shut up if I don't answer."
    "Ugh."
    "I slowly rise from my bed and make my way downstairs."
    scene black with wipeleft
    "Reaching the door, I open it."
    scene bg houserain with wipeleft
    "Monika’s stood outside, Yuri and Sayori in tow."
    show monika 2co zorder 2 at t31
    show sayori 1dk zorder 1 at t32
    show yuri 2cg zorder 0 at t33
    "They’re all looking solemnly at me."

    m "[player]..."
    mc "Don’t even bother."
    mc "I don’t want to know."
    m 1cq "You missed it..."
    m "The funeral, [player]..."
    m 1cr "It was today."
    mc "I..."

    "What?"
    "I had no idea…"
    "Natsuki’s funeral..."
    "My one chance to see her, to say my goodbyes..."
    "Gone."

    mc "I-I-I... need a m-minute."

    scene bg kitchen with wipeleft
    "I drag myself into the kitchen just in time to vomit into the trash can."
    "I’m fucking pathetic."
    "I couldn’t even make it to the funeral of the girl I loved."
    "I couldn’t even get out of bed."
    "I couldn’t even save her."

    show monika 1cf zorder 1 at t11

    m "[player]..?"

    "I wipe my mouth with my sleeve, slamming the can's lid shut."

    m "[player]..."
    m 2cg "I’m so sorry."
    mc "What for?"
    m "You, having to go through this…"
    m 2cp "Everything you saw..."

    "I brush past her on the way back upstairs, to my room."
    scene bg bedroom with wipeleft
    "I can hear the other girls rushing up the stairs."
    show monika 1cf zorder 2 at t31
    show yuri 2cv zorder 0 at t32
    show sayori 1dk zorder 1 at t33
    m 1ce "You know we’ll always be there for you."
    m "At the club."
    m 3cd "Are you... coming?"

    "I need to go back there."
    "I know I do."
    "Natsuki would’ve wanted me to…"
    "And I can’t fail her again."

    mc "I-I guess."
    m 4cd "Well, we’ve suspended club activities for now. It’ll just be a place to talk for a few days."
    m 2cg "You... okay with that?"

    "I nod."
    show sayori 1du
    "Sayori fidgets uncomfortably, tears welling up in her eyes."
    "I can tell she wants to say something."

    mc "Sayori…"
    show sayori 4dw zorder 3 at t11
    show monika zorder 2 at t41
    show yuri zorder 1 at t21
    "Sayori rushes towards me, pulling me into a deep embrace."
    "I stumble back, nearly tripping over."
    "She begins crying into my shoulder."

    s "[player], I’m so sorry!"

    "I awkwardly pat her on the back to comfort her, but it does nothing."
    "A long silence ensues, broken only by Sayori’s stifled sobs."
    show monika zorder 2 at t31
    show yuri zorder 0 at t32
    show sayori 1dv zorder 1 at t33
    "Eventually, she breaks away, wiping her face."

    m 2cq "He's been arrested..."
    m 2cr "Apparently for more than what he did to her..."
    m "It wasn’t your fault."
    m 1cg "There was nothing you could’ve done."

    mc "Nothing I could have done..?"

    "{i}Nothing I could have fucking done?!{/i}"
    show monika at thide
    hide monika
    show yuri at thide
    hide yuri
    show sayori at thide
    hide sayori
    "I could’ve done so much more."
    "I could’ve stayed with her at the doctor’s."
    "I could’ve been there to comfort her."
    "I could’ve told her I loved her more."
    "I could’ve convinced her to go to the cops."
    "That if she did, she’d be free of him."
    "She’d be safe."
    "She’d be happy."
    "But now..."
    "She never will be."
    "And nor will I."
    "I can feel the tears welling up in my eyes again."
    "I..."
    "I need to get away from this."
    "I need help."
    "I need sleep."
    "I need..."
    "I need Natsuki."
    "I need to be with her."
    "I need to k{nw}"

    show monika 1co zorder 2 at t21
    show yuri 2ct zorder 0 at t22

    y "[player]..."
    mc "Don’t."
    mc "All of you… please."
    mc "Just, leave."
    mc "Get out."
    mc "I’ll be at the club tomorrow..."
    mc "I need some time alone."
    stop music fadeout(2.0)

    "Yuri wants to protest, but I glare at her, glassy-eyed."
    "She doesn’t back down."

    play music climbingup
    y "Well..."
    y 2cv "I’m sorry, [player]..."
    y 2cf "But-"
    m 1ch "Yuri, come on."
    m "[player] needs some space."
    y 1ch "Monika, you can’t tell me what to do."
    y "H-he clearly needs somebody to speak to, and I know how to help him!"
    m 1ci "Yuri, he just wants to be alone."
    m 2ci "Why is that so hard to understand?"
    y 3cr "He doesn’t know what he wants!"
    m 2cs "And you do?!"

    "Yuri rushes Monika, but Sayori jams herself between them, trying to retain the long-lost peace."
    show sayori 4dv at t32
    show yuri at t33
    show monika at t31
    s "Stop it!"
    y 2cy7 "I know exactly what he needs!"
    m 1cs "You don’t know anything, Yuri!"
    m 1ct "Now that Natsuki’s gone, you just want to swoop in and take him while he’s vulnerable!"
    s 4dw "Guys. stop!"
    m 2cs "I saw the pictures you sent him."
    m 2ct "You’re disgusting!"

    "My head is spinning."
    "I can’t focus."
    "Stumbling back against the wall, I slide down to the floor, watching the fight wearily."

    y 2cy4 "How dare you."
    show sayori 1dw zorder 0 at t31
    show monika 3ct zorder 2 at t32
    show yuri 3cy4 zorder 1 at t33
    y "How much must you hate yourself to{nw}"
    show yuri zorder 1 at t44
    show monika zorder 2 at t22
    y "How much must you hate yourself to{fast} be such a self-righteous-{nw}"

    play sound "sfx/slap.ogg"
    stop music
    show white zorder 6:
        alpha 0.6
        linear 0.25 alpha 0.0
    show yuri 1cy1b zorder 1 at h44
    show monika 1cu zorder 2 at t22
    "Yuri stumbles to her knees, dazed and confused."
    hide white
    show monika 1co zorder 2 at t32
    show yuri zorder 1 at t33
    "Monika, fist still raised in the air, freezes on the spot as everybody’s eyes lock onto her."

    m "O-oh, God..."
    show yuri 1cy2b
    m 1cp "Yuri... I’m sorry..."

    show yuri 1cy3b
    "Yuri pulls herself to her feet, eyeing Monika scathingly, and starts striding towards her."
    show yuri at lhide
    hide yuri
    show sayori 1du at t21
    show monika at t22
    "Instead of making a move, she shoves past her, and straight out of the door."
    "I have no words."
    show sayori at lhide
    hide sayori
    show monika zorder 1 at t11
    "Sayori, weeping, rushes out too. To catch up or to leave, I don’t know."
    "Monika, left alone with me, begins muttering to herself."

    m 1cq "I shouldn’t have…"
    m 1cr "I-I’m sorry, [player]."

    show monika at thide
    hide monika
    "Being the last girl to leave, Monika slams the door behind her."
    "And I’m alone with my thoughts once again."
    "May as well put this time to good use."
    "From my drawer, I pull out a sheet of paper and a pen, and I start to write."

    scene black with dissolve_scene_full

    $ quick_menu = False
    scene black
    show monday
    with dissolve_scene_half
    $ renpy.pause(delay=2.0, hard=True)
    $ quick_menu = True

    scene bg bedroom with dissolve_scene_full

    "Morning."
    "This is it… my first day back at the club."
    "Hopefully my l{nw}"
    "I make my way to the bathroom…"
    scene bg bathroom with wipeleft
    "Oh god…"
    "I haven’t cleaned up."
    "Her dried blood still specks the tiles, broken glass spread along the floor."
    "I can hear it crunch beneath my shoes as I make my way to the sink, and splash my face with water from the tap."
    "Facing the mirror, I take a good long look at myself."
    "{i}Look at you.{/i}"
    "{i}You’re disgusting.{/i}"
    "{i}This is your fault.{/i}"
    "{i}You should’ve done more.{/i}"
    "{i}You should’ve called the police as soon as she confirmed your suspicions.{/i}"
    "{i}But you didn’t, because he was out of town and things were going well between the two of you.{/i}"
    "{i}You were lazy, and didn't want to deal with the hassle.{/i}"
    "{i}You disgust me.{/i}"
    "{i}You fucking idiot.{/i}"
    "{i}It’s your fault she’s dead.{/i}"
    "{i}It’s your fault.{/i}"
    "{i}It’s your fucking fault.{/i}"
    "I can’t take it anymore."
    "I leave the bathroom, the tap still running."
    scene bg bedroom with wipeleft
    "Back in my room, my uniform lays waiting for me."
    "I get changed quickly, ready to go."
    "Taking one last look around, I make my way downstairs and out the door."

    scene black with dissolve_scene_full
    scene bg corridorrain with dissolve_scene_full

    "School was hell."
    "Of course, I had teachers and students alike reaching out, offering me someone to talk to should I need it."
    "{i}False sympathy.{/i}"
    "{i}That’s what it is.{/i}"
    "{i}And I hate it.{/i}"
    "Regardless, I think going to school was worth it."
    "I can go back to the \"literature\" club."
    "It’s strayed a long way from literature at this point..."
    "I open the clubroom door."
    scene bg clubrain with wipeleft
    "This..."
    "This isn't right."
    show monika 1f zorder 1 at t11
    m "Oh, [player]..?"
    m "How are you doing?"
    mc "..."
    m 2e "We're all here for you, y'know."

    "Monika gives me a weak smile."
    "I understand where she's coming from..."
    "But false sympathy is the last thing I want."
    show monika at thide
    hide monika
    "I can't help but feel drawn to the closet."
    "Knowing full and well that if I step foot in there..."
    "I'll break down entirely."
    "I sit near the corner of the room, next to the entrance of the club."

    scene black with dissolve_scene_full
    scene bg clubrain with dissolve_scene_full
    show sayori 2f zorder 1 at t11
    s "[player]?"
    s 2g "A-are you okay?"

    "I nod at Sayori, trying to politely get her away from me."
    "I don't want anyone’s sympathy."
    "I can feel my vision being blurred by tears."
    "I hang my head down to avoid anyone noticing, jamming my eyes shut."
    scene black with dissolve_cg
    s "[player]..."
    s "A-are you sure?"
    mc "..."
    s "[player], please say something..."
    mc "I-I'm fine."

    "My fucking voice broke."
    "I feel a hand on my shoulder."
    "I want to jerk away, but what's the point?"
    "Her hand lifts my chin."
    scene bg clubrain with dissolve_cg
    show sayori 2g zorder 1 at t21
    show monika 2o zorder 2 at t22

    s "You'll be okay, [player]."
    m 2m "Time heals all wounds."

    "I can't hide my disgust in their words."
    "Do they honestly believe what they're saying?"
    "The love of my life has been ripped from me."
    "I can feel the tears falling over my cheeks."

    show sayori 1k at h21
    show monika 1q at h22
    mc "Things aren't fucking okay!"
    mc "She's gone!"
    mc "Don’t you get that!?"
    mc "Or was she so disposable to you, you just don't give a shit?!"

    "I lay my head down onto my arm, supported by the desk."
    "I didn't mean to snap..."
    "I can't help but feel even worse..."

    s 1i "Fine then."
    s "I'll leave you alone."
    s 1j "Jerk."
    m 1f "Sayori, you realize what he’s going through, right?"
    s 1i "Yeah, I know. But that doesn’t mean-"
    m 2h "That's enough."
    mc "It's okay, Sayori."
    mc "I-I understand."

    show monika at thide
    hide monika
    show sayori at thide
    hide sayori
    "I can't handle this."
    "I need to see the closet."
    "One last time."
    scene bg closetrain with wipeleft
    "I enter, dropping my bag to the floor."
    "The rest of her manga collections are still here..."
    "I never did take them back to our house..."
    "I close the door behind me, looking out at the clubroom."
    "Under that windowsill..."
    "I met the true Natsuki."
    "The one I fell in love with..."
    scene bg windowsill with wipeleft
    "I crumple to the floor near the window."
    "I can't control the tears any longer."
    "I..."
    "I just want her back…"
    scene black with dissolve_scene_full
    scene black with dissolve_scene_full
    m "Um, [player]..."
    m "It’s nearly the end of the day... we need to go soon."
    scene bg windowsill with wipeleft
    "Monika’s stood above me, trying to talk to me."
    "I’m pretty much unresponsive."
    "Sighing, she outstretches her arm in my direction, offering to pull me up."
    "I reluctantly stand up of my own accord, ignoring her helping hand."
    scene bg closetrain with wipeleft
    show monika 2o zorder 1 at t11
    m "Sayori’s already gone home."
    mc "Oh."
    m 2f "If you want, I’ll take you home."
    m 2g "I just want to make sure you recover, [player]."
    m "This… it’s horrible... and we all hate seeing you go through this."
    m "It’s why we’re trying our best to help."
    mc "You don’t need to…"
    m 1o "[player], please don’t tell me you’re considering…"
    m 1p "Y’know…"
    m 1r "I’ll have to let the school know."
    mc "I’m not…"
    mc "I’m fine living with this…"
    mc "I deserve it."
    m 1g "[player]..."
    m "Why?"
    m 1p "Why’re you blaming yourself..?"
    mc "Because it {i}was{/i} my fault."
    mc "I… I should’ve called the cops as soon as I knew for sure what was going on."
    mc "I didn’t, because h-he was away or something…"
    mc "And we were enjoying the time we had…"
    mc "I had the perfect opportunity to give her a better life, and I fucking blew it."
    mc "N-now… Natsuki’s dead... "
    mc "And I’m rotting in the worst hell I could possibly think of."
    m 1o "[player]..."
    m 1q "This isn’t okay."
    m "You can’t live like this…"
    m 1r "Come on, let’s go."
    m "I’ll walk home with you."
    mc "I… I need to use the bathroom first."
    m 2f "F-fine…"
    m 2e "I’ll be waiting outside, okay?"

    "We exit the clubroom together, without another word."
    scene bg corridorrain with wipeleft
    "She takes a seat on one of the benches in the hallway."
    scene black with wipeleft
    "In the bathroom, I move into one of the stalls."
    "I drop my bag to the floor inside, and unzip it."
    "I look for my poem, buried deep within it."

    python:
        if persistent.language == "spanish":
            poem_me2 = poem_me2_spanish
    call showpoem (poem_me2) from _call_showpoem_6

    "I swallow."
    "I’m going to have to make this quick."
    "I exit the bathroom, note in hand."
    scene bg corridorrain with wipeleft
    "Monika must know something’s up, because she stands up at once, and approaches me."
    show monika 1f zorder 1 at t11
    m "[player], what’s that?"
    mc "It’s... it’s something I wrote, last night…"
    m 2g "Y-you… mind letting me read it?"
    mc "Sure… go ahead."

    "I let go of the note, letting it drift to the floor towards her."
    "She bends down to pick it up, and returns to her seat on the bench to read."
    "A couple of minutes pass, her eyes fixated on the paper."
    show monika 1w
    "By the time she’s finished reading, she stares up at me with glassy eyes, like she’s on the verge of tears."
    "But she doesn’t even have time to mutter my name like I’m sure she would have, because I’m already out the door, bolting out of the school."
    scene bg courtyardrain with wipeleft
    m "[player]!!"

    "I hear that echo from behind me as I sprint out into the street, and out of her sight."
    scene black with dissolve_scene_full
    scene bg street with dissolve_scene_full
    "It's stopped raining."
    "At this point, it’s the adrenaline that’s carrying me to my destination."
    "I know where I’m going, but I need to make sure I don’t run into anyone."
    "Not far now..."
    "I hear a siren blare out from a couple of blocks away. Sounds like Monika’s let them know about me."
    "It doesn’t matter anyway."
    "I’m here."
    scene bg bridge with wipeleft
    play music mps
    "I stand in the middle of the bridge and stare out over the water."
    "I try to control my breathing and sobbing but it's no use."
    "I failed her."
    "If I could have done things different I would have..."
    "But I can’t, and now the girl I loved is gone."
    "Forever…"
    "I drop to my knees, gripping the railing with one hand."
    "I lift my head, looking out at the vast body of water."
    "I bring myself to my feet."
    "An intense wave of clarity stops my sobbing."
    "I hold my breath for a moment, letting out a shaky sigh."
    "I step up onto the ledge."
    "This is what has to happen."
    "I was doomed from the start."
    "There’s not much else I can do now but..."

    m "[player]!"

    "My eyes lock on Monika, rushing toward me."
    "Looks like she found me..."
    "I inch my heel closer to the edge."
    show monika 1g zorder 1 at t11
    m "[player], don't!!"

    "She reaches out to grab me."
    "Monika desperately holds onto the lapels of my jacket, while I give feeble resistance."
    "I’m tugged forward, collapsing onto the concrete."

    m 1f "[player], listen to me."
    m "I'm not letting you go."
    m "Not for a second."
    m "Just, please..."
    m 1h "Don't do this. Let us talk it out."
    mc "..."
    m "[player]..."
    m "This..."
    m 1o "This isn’t a solution to what happened, [player]."
    m "This is only going to make everything worse..."
    m 1q "Do you understand?"
    mc "I..."
    m 1r "[player]... This isn’t how your story ends."
    m 1w "Please..."

    "I wipe the remaining tears from my cheeks."
    "I manage to rise to my feet, gripping the railing for support."
    "My entire body is trembling."
    "I... I feel completely numb..."

    m "Look at me, [player]..."
    m 1x "Please, you can't do this..."

    "I meet Monika’s gaze for a moment."
    "Seeing the tears welling in the corners of her eyes sends a sharp pain through my chest."

    m 1w "[player], you're not thinking of the bigger picture."
    m "Sayori? You know what'll happen to her if she loses you?"
    mc "..."
    m 1x "I know you know, [player]."
    m "You really want that?"
    m "You can't."
    m "And Yuri?"
    m 1y "God only knows what she'd do..."
    mc "Why should I care?"
    mc "She's a good chunk of the reason..."

    show memory2 zorder 1000
    hide monika
    window hide(None)
    pause(0.001)
    show monika 1y at i11
    hide memory2
    window auto

    mc "Monika…"
    m 1w "Let’s go back."
    m "Please..."

    "Monika takes hold of my hand, pulling us away from the rail."

    m 1x "We all love you, [player]."
    m "We’ll always be here for you."
    m 1w "No matter what."

    "I release my grip from the railing, following Monika’s lead."
    show memory2 zorder 1000
    hide monika
    window hide(None)
    pause(0.001)
    show monika 1w at i11
    hide memory2
    window auto

    mc "N-..."
    mc "No..."

    "Pushing with all the energy I have, I take Monika by the shoulders and shove her back as hard as I can."
    show monika 1y at thide
    hide monika
    "She loses her grip on me, stumbling and nearly falling onto the concrete."
    "As Monika realizes what's happening, she lets out a scream and scrabbles to her feet."
    "This must be done."
    "This is the only escape from everything."
    "I can’t control my actions anymore."
    "I’m coming, Natsuki."
    "I sprint toward the rail, vaulting myself over."
    scene bg sky with wipeleft
    "As I begin the journey down, I remember the times Natsuki and I had spent together."
    "Our first time reading together..."
    "When she first told me she liked my poems..."
    "Baking together…"
    "When she told me she loved me…"
    "All of it."
    "Being able to tell her the same, see the look on her face…"
    "Of pure happiness…"
    "I’m reminded of the sensation of weightlessness."
    "Almost like right now..."
    "Now I’m going to see her again."
    "Natsuki… if you can hear me…"
    "I will see you in the next life."
    "..."
    "This was the right choice."
    "I did what I{nw}"
    $ quick_menu = False
    $ _windows_hidden = True
    window hide(None)

    show black zorder 5
    stop music
    stop background
    pause(5.0)

    $ renpy.movie_cutscene("mod_assets/video/credits.webm")
    scene black
    with dissolve_scene_full
    scene bg creditnote
    play audio page_turn
    with dissolve_cg
    $ renpy.pause(delay=300.0, hard=True)

    $ _windows_hidden = False
    $ quick_menu = True

    call restart from _call_restart
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
