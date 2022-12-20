# A Pico Christmas

This is a christmas-themed project that features flowing LEDs, an LCD display, and a buzzer playing christmas tunes; all done on the Raspberry Pi Pico. Credit for the "buzzer_music.py" code goes to james1236. See the buzzer_music repository for more information. The programs for the LCD can be found at https://www.tomshardware.com/how-to/lcd-display-raspberry-pi-pico

<br>

### Usage
1) Design the circuit based on the breadboard and schematic below:
  
![Pico_Christmas_bb](https://user-images.githubusercontent.com/89809703/208768015-8cb5b147-addb-4401-b849-e5bdfe6131e7.jpg)
![Pico_Christmas_schem](https://user-images.githubusercontent.com/89809703/208768040-d768ec68-15b7-4fa6-9515-3632d005d19a.jpg)

2) Install micropython on your Pico and copy the files in this repository to it.
3) Find some holiday-themed music on onlinesequencer.net, click edit, select all notes with CTRL + A and then copy them with CTRL + C.
4) Paste the string in place of the one in the example file, making sure to remove the "Online Sequencer:120233:" from the start and the ";:" from the end.
