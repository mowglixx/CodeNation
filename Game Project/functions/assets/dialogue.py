# ask for player name

player_name = input("\n\nBefore we begin... What is your name Hero? ")
villan_name = "Septic Meg"

affirmative_words = [
    "yes",
    "yeah",
    "yeh",
    "ye",
    "y",
    "yup",
    "sure",
    "ok",
    "affirmative",
    "affirmative",
    "amen",
    "fine",
    "good",
    "okay",
    "true",
    "yea",
    "all\ right",
    "aye",
    "beyond\ a\ doubt",
    "by\ all\ means",
    "certainly",
    "definitely",
    "gladly",
    "good\ enough",
    "granted",
    "indubitably",
    "just\ so",
    "most\ assuredly",
    "naturally",
    "of\ course",
    "positively",
    "precisely",
    "sure\ thing",
    "sure",
    "undoubtedly",
    "unquestionably",
    "very\ well",
    "willingly",
    "without\ fail",
    "yep",
]

negative_words = [
    "no",
    "na",
    "nah",
    "nope",
    "n",
    "nada",
    "negative",
    "nay",
    "nix",
    "never",
]


lines = [

    f"""Hello {player_name}, you little bum head. Thought you could get away with stealing from me? You thought wrong. Until you bring me what is rightfully mine, I'll keep hold of something very dear to you. Or should that be... Someone? Mwahahaha! You have until midnight to do the right thing. And no, I don't mean go on a quest in a bid to be the hero. What do you think this is, a game? Bring me what you stole from me, or else, the Princess will die. Try and be smart with me, you will both die. \nIs that understood? \nHugs and Kisses,\n{villan_name}\nP.S. Bring milk.""",

    f"Oh no! {villan_name} has kidnapped her highness, Princess Footstool! {player_name}, you'll have to go and rescue her! Quick! You leap out of bed, still in your pyjamas, and run out the door. You look around and see an old lady...",

    # (YES/NO)

    "What's the matter, dear? You look like you've seen a ghost! Can I help you with anything? ...Oh, I see. That Princess Footstool is one clumsy tart. I did see her run off with a rather imposing figure. I could tell you where they went... But my short-term memory only works when people can finish Christmas song lyrics for me. I know, it sounds insane. Just go with it.",

    # (MISSING WORD CHALLENGE)

    f"Bingo! Now I remember! She went towards the village! Run! Save her! Please! She owes me fifty quid. I don't care if she is the princess, I'm not letting her get away with that. Have a safe trip {player_name}!",

    "You make your way towards the village. Hopefully, the old woman wasn't completely insane! ...wait! ...what is that? There's something on the floor...",

    # (YES/NO)

    "Oh, it's just dog poo. Now your hands smell of dog poo. Let's carry on, Dog Poo Hands.",

    f"WAIT!!! WHO GOES THERE!?",

    "You stop dead in your tracks and look behind you. A Black Knight approaches you.",
    
    f"What are you doing here? Who are you? Where are you going?",
    
    "...",
    
    f"Your name is {player_name}? I see. And you want to rescue the Princess? Hahahahahahahahaha! Only knights can rescue Princesses! Why, your puny little arms are no match for my strength, my stamina, And my phenomenal good looks. I'm going to put you in your place... I challenge you to Rock, Paper, Scissors!",

    # (ROCK PAPER SCISSORS CHALLENGE)

    "What?",
    
    "No!",
    
    "How?",
    
    "My whole purpose in life. Crumbling in front of me. I am Not strong, I am weak. I am pathetic. I am no knight. I am worthless...",
    f"Take my sword {player_name}, and do what you need to do... I'm going to become an estate agent.",

    f"Congratulations {player_name}! You won a sword! You can use this to fight enemies... or steal from off licences!",

    "You make your way towards the village. But it's eerily quiet. Nobody is around. A cold wind blows through your hair, and you feel something is amiss. You look around to see what's wrong. Is it the bitter chill in the air? Maybe it's the empty shops. Could it be the stone-cold silence? Oh! it's just a lion sitting on a bench. He signals you to come and sit with him.",

    # (YES/NO)

    f"Take a seat, mon amis. My super lion senses tell me you're looking for someone. You may have already assumed I'm quite the hunter, and you'd be right. The fact you've come and sat next to me Makes me think you'd appreciate my assistance. Would you like my help?",

    # (YES/NO)

    f"Marvellous. Of course, I would ask for you to scratch my back before I scratch yours. You see, us lions are losing faith in you humans, as you call yourselves. Primarily because too many of you lot keep trying to stick our heads on walls, but also, we don't think you humans are very good at riddles unlike us furry bois. I'm going to give you a riddle. Correctly answer the riddle and I will give you the guidance you so require.",

    # (RIDDLE CHALLENGE)

    f"You're not as stupid as you look. Colour me impressed, {player_name}. I guess you could say, I have pride in you... heh heh heh. Head into that phone box over there, and you will be transported to {villan_name}'S castle. You're on your own from there, my friend. Now, go away. Farewell, {player_name}.",

    f"You go to the phonebox and step inside. The phonebox starts to shake! The light from outside is blinding! You close your eyes until the shaking and rattling finally stops. Everything settles down. Your eyes slowly open, and there it is – {villan_name}'s castle. Princess Footstool must be inside! Let's go! ...well? Open the door then! ...oh no. It's locked. Balderdash! Maybe a code unlocks the door. Wait... not all those business cards are phone numbers... They're sums!",

    # (MATHS CHALLENGE)

    "Carol Vorderman would be proud! The door is unlocked. Now get out there and save the Princess! Just look out for that tranquiliser... Oops... You start to black out. Soz...",

    "Where... Where are you? Everything's all blurry...",

    f"{player_name} Help me!",

    f"Princess Footstool! It's her! But where is she? Curse this blurry vision! Wait... Why can't you move your arms? You're tied up! Oh no! And so is your beloved Princess! And is that... Oh no... It's {villan_name}!",

    "Look at you, you pathetic worm. I told you you'd have no chance against me. And now, I'm going to have to kill you both. Do you have any last requests?",

    # (YES/NO)

    "And what might that be? A game of Hangman? Hahahahaha... Oh, it is? Oh, well... My developers haven't got time to do anything like that. Besides, Hangman is old and stale. I'll set you a fresh challenge you've never seen before. You'll have no chance! I challenge you to... Rock, Paper, Scissors!",

    # ROCK PAPER SCISSORS CHALLENGE 2

    "Curses! It's almost as if you've played this before! Alright, fine. I'll let the Princess go. As long as you give back what you took... Why are you giving me a blank look? Have you forgotten? You stole my precious antique sword! Do you have it, yes or no?"

    # (YES/NO)

    "Hand it over! ...yes, that's the one. Looks practically unused. Did you even bother killing someone with it? ",
    
    "Never mind.",
    
    "Take your princess and Get out of my sight. Go on. Shoo.",

    "You grab the Princess' hand and you both sprint to freedom! You're free! You saved the day! Now, here comes your hero's reward! A big kiss from Princess... wait... You're not Princess Footstool. Who are you?",

    f"I'm Princess Satsuma. I'm sorry {player_name}, but your princess Is in another castle.",

    "You must be nuts if you want to do all that again! Let's go home.",

    # THE END
    f"Congratulations {player_name}! \nyou made it to the end!\nYou may not have saved the 'CORRECT' princess but I suppose one will do, Well Done!"
]
