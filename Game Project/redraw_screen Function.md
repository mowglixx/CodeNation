# redraw_screen Function

## Globals
- bg_ascii_art
- player
  - ascii_art
  - position
    - x
    - y
- dialogue
  - [
      'line_1',
      'line_2',
      'line_3',
      'line_4']

## functionality/logic
```
when player_pos / dialogue changes:
    clear_screen()
    redraw(bg, player_char)
        if dialogue lines == 4
            typewritter(next_dialogue_lines, 0.3s/char)
```


