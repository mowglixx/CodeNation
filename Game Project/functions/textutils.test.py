import textutils as t

text_speed = 0.03
screen_width = 40

t.clear_screen()
print("clear_screen Done")

# t.typewriter("This is the typewritter function")

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

formatted_dialogue = t.format_lines("Lorem ipsum, dolor sit amet consectetur adipisicing elit. Sequi nulla repellendus iusto voluptas quasi esse id magnam dolore sunt ullam deserunt dicta alias, aliquid, ea quis inventore nisi nobis soluta? Iusto dolorem, quod mollitia vero suscipit maxime quidem explicabo similique quo dolorum eligendi autem ratione, quaerat in! Velit aspernatur voluptatibus perspiciatis rerum vel fugit asperiores a. Enim veniam a ullam? Voluptatibus laboriosam ipsa delectus! Provident laboriosam nesciunt id, dolores facilis mollitia impedit consequatur, tenetur atque iste dicta sapiente corporis numquam repellendus dolorum autem vel veritatis odio minima aperiam temporibus similique. Exercitationem corporis sit, ab incidunt voluptatem earum consectetur inventore eius accusantium nisi maxime explicabo necessitatibus, optio suscipit. Quos consequatur velit, eius, porro fuga cum mollitia molestiae iure eum quisquam modi? Tempore quaerat aspernatur hic ducimus aut veniam distinctio aliquid at est deserunt et similique temporibus ea nemo voluptatem dolor sint enim vel, numquam vero nobis rem cumque eos inventore. Quas!")
# print(formatted_dialogue)

# for line in formatted_dialogue:
#     t.typewritter(line)


t.dialogue_box(ascii_art, "Jimmy Testerman", formatted_dialogue)
print("dialogue_box Working")
