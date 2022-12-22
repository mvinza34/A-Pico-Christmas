# A Pico Christmas

### Oveview
This is a christmas-themed project that features 18 flowing LEDs, an LCD display, and four buzzers playing three classic christmas tunes; all done on the Raspberry Pi Pico. Credit for the "buzzer_music.py" code goes to james1236 via the "buzzer_music" repository. Check out https://github.com/james1236/buzzer_music for more information. Credit for the lcd_api.py and pico_l2c_lcd.py programs goes to Tom's Hardware and can be found at https://www.tomshardware.com/how-to/lcd-display-raspberry-pi-pico

### Components
1) 1 Raspberry Pi Pico
2) 2 solderless breadboards
3) 1 solderless mini-breadboard
4) 18 LEDs (6 reds, 6 greens, 6 whites)
5) 18 330 Ω resistors
6) 4 buzzers (active or passive)
7) 1 I2C LCD 1602

### Usage
1) Design the circuit based on the provided breadboard and schematic below:
  
![Pico_Christmas_bb](https://user-images.githubusercontent.com/89809703/209020714-17f6809c-ee7f-41de-b96a-2075a4b1517e.jpg)
![Pico_Christmas_schem](https://user-images.githubusercontent.com/89809703/209020722-16d19be7-c813-4b76-9f71-05214e693ade.jpg)

2) Download and install Thonny. (https://thonny.org/)
3) Open Thonny and install Micropython on the Pico. 
4) Copy the files in this repository to the Pico.
5) Open A_Pico_Christmas.py
6) Find some holiday-themed music on onlinesequencer.net, click edit, select all notes with CTRL + A and then copy them with CTRL + C.
7) Paste the string in place of the one in the example file, making sure to remove the "Online Sequencer:120233:" from the start and the ";:" from the end.
8) Run the code.
9) Enjoy the music and lights and have a wonderful Happy Hoildays! 
