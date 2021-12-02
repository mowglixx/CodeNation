import functions.textutils as t
from functions.assets.dialogue import lines as d, villan_name as meg, player_name as p 

# switches
PLAYER_HAS_NAME, TEXT_SPEED_SET, NEW_GAME_CONFIRM = 0, 0, 0

text_speed = 0.1
screen_width = 60

#t.clear_screen()
t.dialogue_box("blank", meg, d[0])