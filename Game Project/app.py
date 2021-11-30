import functions.textutils as t

# switches
PLAYER_HAS_NAME, TEXT_SPEED_SET, NEW_GAME_CONFIRM = 0, 0, 0

text_speed = 0.1
screen_width = 60

player_name = ""

if __name__ == "__main__":
    t.clear_screen()
    while (PLAYER_HAS_NAME == 0
           and TEXT_SPEED_SET == 0
           and NEW_GAME_CONFIRM == 0):
        player_name = input("What is your name, hero?\n")
        dialogue_1 = "It reads… \“Hello {}, you little bum head. Thought you could get away with stealing from me\? You thought wrong. Until you bring me what is rightfully mine, I’ll keep hold of something very dear to you. Or should that be… Someone\? Mwahahaha! You have until midnight to do the right thing. And no, I don’t mean go on a quest in a bid to be the hero. What do you think this is, a game\? Bring me what you stole from me, or else, the Princess will die. Try and be smart with me, you will both die. Is that understood\? Lots of love, \nBastard #3. \nP.S. Bring milk.".format(
            player_name)
        text_speed = float("0." + input(
            "How fast would you like to read? (number of miliseconds)\n"))
        t.clear_screen()
        if(player_name and text_speed):
            t.dialogue_box("", player_name, t.format_lines(dialogue_1))
