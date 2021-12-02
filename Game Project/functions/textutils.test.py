import textutils as t
from assets.dialogue import player_name

text_speed = 0.03
screen_width = 40

t.clear_screen()
print("clear_screen Done")

t.typewriter("This is the typewritter function")

ascii_art = """           .          .           .     .                .       .
  .      .      *           .       .          .                       .
                 .       .   . *            "Go where you will...
  .       ____     .      . .            .    I'll always love you, Tammy."
         >>         .        .               .
 .   .  /WWWI; \  .       .    .  ____               .         .     .         
  *    /WWWWII; \=====;    .     /WI; \   *    .        /\_             .
  .   /WWWWWII;..      \_  . ___/WI;:. \     .        _/M; \    .   .         .
     /WWWWWIIIIi;..      \__/WWWIIII:.. \____ .   .  /MMI:  \   * .
 . _/WWWWWIIIi;;;:...:   ;\WWWWWWIIIII;.     \     /MMWII;   \    .  .     .
  /WWWWWIWIiii;;;.:.. :   ;\WWWWWIII;;;::     \___/MMWIIII;   \              .
 /WWWWWIIIIiii;;::.... :   ;|WWWWWWII;;::.:      :;IMWIIIII;:   \___     *
/WWWWWWWWWIIIIIWIIii;;::;..;\WWWWWWIII;;;:::...    ;IMIII;;     ::  \     .
WWWWWWWWWIIIIIIIIIii;;::.;..;\WWWWWWWWIIIII;;..  :;IMIII;:::     :    \   
WWWWWWWWWWWWWIIIIIIii;;::..;..;\WWWWWWWWIIII;::; :::::::::.....::      \\
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%XXXXXXX
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%XXXXXXXXXX
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%XXXXXXXXXXXXX
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%XXXXXXXXXXXXXXXXX
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%XXXXXXXXXXXXXXXXXXXX
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%XXXXXXXXXXXXXXXXXXXXXXXXXX"""

formatted_dialogue = "Lorem ipsum, dolor sit amet consectetur adipisicing elit. Sequi nulla repellendus iusto voluptas quasi esse id magnam dolore sunt ullam deserunt dicta alias, aliquid, ea quis inventore nisi nobis soluta? Iusto dolorem, quod mollitia vero suscipit maxime quidem explicabo similique quo dolorum eligendi autem ratione, quaerat in! Velit aspernatur voluptatibus perspiciatis rerum vel fugit asperiores a. Enim veniam a ullam? Voluptatibus laboriosam ipsa delectus!"
print("formatted_dialogue: \n==================")
print(formatted_dialogue)

for line in formatted_dialogue:
    t.typewriter(line)


t.dialogue_box("castle", player_name, formatted_dialogue)
print("dialogue_box Working")
print("This is a choice")
if t.choice():
  print('yes answer')
else:
  print('no answer')