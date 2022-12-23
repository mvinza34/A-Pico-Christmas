from machine import Pin, PWM, I2C
from buzzer_music import music
from time import sleep
import machine
import utime
from pico_i2c_lcd import I2cLcd

# LCD
i2c = I2C(1, sda=Pin(26), scl=Pin(27), freq=400000) 
I2C_ADDR = i2c.scan()[0]
lcd = I2cLcd(i2c, I2C_ADDR, 2 ,16)

# Flowing LEDs
leds = [Pin(i,Pin.OUT) for i in range(0,18)]

"""
Find a piece of holiday-themed music on onlinesequencer.net, click edit,
then select all notes with CTRL+A and copy them with CTRL+C.

Paste the string as shown below after removing ";:" from
the end and "Online Sequencer:120233:" from the start.
"""

# Songs
##    https://onlinesequencer.net/1725035 - We Wish You A Merry Christmas
song1 = '0 A#4 1 8;2 D#5 1 8;4 D#5 1 8;5 F5 1 8;6 D#5 1 8;7 D5 1 8;8 C5 1 8;2 D#4 1 8;8 C4 1 8;10 C5 1 8;12 C5 1 8;14 F5 1 8;14 G#3 1 8;16 F5 1 8;17 G5 1 8;18 F5 1 8;19 D#5 1 8;20 D5 1 8;22 A#4 1 8;24 A#4 1 8;26 B3 1 8;20 A#3 1 8;26 G5 1 8;28 G5 1 8;29 G#5 1 8;30 G5 1 8;31 F5 1 8;32 D#5 1 8;34 C5 1 8;32 C4 1 8;36 A#4 1 8;37 A#4 1 8;38 C5 1 8;40 F5 1 8;42 D5 1 8;44 D#5 1 8;36 A#3 1 8;37 A#3 1 8;38 G#3 1 8;40 A#3 1 8;42 D4 1 8;44 D#4 1 8;42 F4 1 8;44 G4 1 8;48 A#4 1 8;50 D#5 1 8;52 D#5 1 8;54 D#5 1 8;56 D5 1 8;60 D5 1 8;61 D5 1 8;62 D#5 1 8;64 D5 1 8;66 C5 1 8;68 A#4 1 8;48 F5 1 8;50 G5 1 8;52 G5 1 8;54 G5 1 8;56 F5 1 8;60 G#5 1 8;61 F5 1 8;62 G5 1 8;66 D#5 1 8;68 A#4 1 8;64 F5 1 8;68 D5 1 8;72 F5 1 8;73 F5 1 8;74 G5 1 8;76 F5 1 8;78 D#5 1 8;80 A#5 1 8;82 A#4 1 8;84 A#4 1 8;85 A#4 1 8;86 C5 1 8;88 F5 1 8;90 D5 1 8;92 D#5 1 8;84 G4 1 8;85 G4 1 8;86 G#4 1 8;88 A#4 1 8;90 D5 1 8;92 D#5 1 8;90 G#4 1 8;92 G4 1 8;96 A#4 1 8;98 D#5 1 8;100 D#5 1 8;101 F5 1 8;102 D#5 1 8;103 D5 1 8;104 C5 1 8;98 D#4 1 8;104 C4 1 8;106 C5 1 8;108 C5 1 8;110 F5 1 8;110 G#3 1 8;112 F5 1 8;113 G5 1 8;114 F5 1 8;115 D#5 1 8;118 A#4 1 8;120 A#4 1 8;122 B3 1 8;116 A#3 1 8;122 G5 1 8;124 G5 1 8;125 G#5 1 8;126 G5 1 8;127 F5 1 8;128 D#5 1 8;130 C5 1 8;128 C4 1 8;132 A#4 1 8;133 A#4 1 8;134 C5 1 8;136 F5 1 8;138 D5 1 8;140 D#5 1 8;132 A#3 1 8;133 A#3 1 8;134 G#3 1 8;136 A#3 1 8;138 D4 1 8;140 D#4 1 8;138 F4 1 8;140 G4 1 8;96 A#4 1 8;98 D#5 1 8;100 D#5 1 8;102 D#5 1 8;104 D5 1 8;108 D5 1 8;109 D5 1 8;110 D#5 1 8;112 D5 1 8;114 C5 1 8;116 A#4 1 8;116 A#4 1 8;121 F5 1 8;122 G5 1 8;124 F5 1 8;126 D#5 1 8;128 A#5 1 8;130 A#4 1 8;132 A#4 1 8;133 A#4 1 8;134 C5 1 8;136 F5 1 8;138 D5 1 8;140 D#5 1 8;132 G4 1 8;133 G4 1 8;134 G#4 1 8;136 A#4 1 8;138 D5 1 8;140 D#5 1 8;138 G#4 1 8;140 G4 1 8;120 F5 1 8;0 A#3 1 8;6 G3 1 8;7 A#3 1 8;12 G3 1 8;13 A#3 1 8;18 F3 1 8;19 G#3 1 8;24 G3 1 8;25 A#3 1 8;30 G3 1 8;31 A#3 1 8;48 A#3 1 8;50 D#4 1 8;52 D#4 1 8;53 F4 1 8;54 D#4 1 8;55 D4 1 8;56 C4 1 8;58 C4 1 8;60 C4 1 8;62 F4 1 8;64 F4 1 8;65 G4 1 8;66 F4 1 8;67 D#4 1 8;68 D4 1 8;70 A#3 1 8;72 A#3 1 8;74 G4 1 8;76 G4 1 8;77 G#4 1 8;78 G4 1 8;79 F4 1 8;80 D#4 1 8;82 C4 1 8;84 A#3 1 8;85 A#3 1 8;86 C4 1 8;88 F4 1 8;90 D4 1 8;92 D#4 1 8;144 A#4 1 8;146 D#5 1 8;148 D#5 1 8;149 F5 1 8;150 D#5 1 8;151 D5 1 8;152 C5 1 8;154 C5 1 8;156 C5 1 8;158 F5 1 8;160 F5 1 8;161 G5 1 8;162 F5 1 8;163 D#5 1 8;164 D5 1 8;166 A#4 1 8;168 A#4 1 8;170 G5 1 8;172 G5 1 8;173 G#5 1 8;174 G5 1 8;175 F5 1 8;176 D#5 1 8;178 C5 1 8;180 A#4 1 8;181 A#4 1 8;182 C5 1 8;184 F5 1 8;188 D5 1 8;195 D#5 1 8;144.25 A#5 1 8;146.25 D#6 1 8;148.25 D#6 1 8;149.25 F6 1 8;150.25 D#6 1 8;151.25 D6 1 8;152.25 C6 1 8;154.25 C6 1 8;156.25 C6 1 8;158.25 F6 1 8;160.25 F6 1 8;161.25 G6 1 8;162.25 F6 1 8;163.25 D#6 1 8;164.25 D6 1 8;166.25 A#5 1 8;168.25 A#5 1 8;170.25 G6 1 8;172.25 G6 1 8;173.25 G#6 1 8;174.25 G6 1 8;175.25 F6 1 8;176.25 D#6 1 8;178.25 C6 1 8;180.25 A#5 1 8;181.25 A#5 1 8;182.25 C6 1 8;184.25 F6 1 8;188.25 D6 1 8;195.25 D#6 1 8'
mySong1 = music(song1, pins=[Pin(19),Pin(20),Pin(21),Pin(22)]) # Four buzzers will make the song sound better

##    https://onlinesequencer.net/2017946 - Jingle Bells
song2 = '0 G4 1 8;1 E5 1 8;2 D5 1 8;3 C5 1 8;8 G4 1 8;9 E5 1 8;10 D5 1 8;11 C5 1 8;4 G4 3 8;12 A4 4 8;7 G4 0.5 8;7.5 G4 0.5 8;16 A4 1 8;17 F5 1 8;18 E5 1 8;19 D5 1 8;20 B4 4 8;24 G5 1 8;25 G5 1 8;26 F5 1 8;27 D5 1 8;28 E5 4 8;28 C5 4 8;32 G4 1 8;33 E5 1 8;34 D5 1 8;35 C5 1 8;36 G4 4 8;40 G4 1 8;41 E5 1 8;42 D5 1 8;43 C5 1 8;44 A4 3 8;47 A4 1 8;48 A4 1 8;49 F5 1 8;50 E5 1 8;51 D5 1 8;52 G5 1 8;53 G5 1 8;54 G5 1 8;55 G5 1 8;56 A5 1 8;57 G5 1 8;58 F5 1 8;59 D5 1 8;60 C5 1 8;62 G5 2 8;64 E5 1 8;65 E5 1 8;66 E5 2 8;64 G4 1 8;64 C4 1 8;65 G4 1 8;65 C4 1 8;66 G4 2 8;66 C4 2 8;68 E5 1 8;69 E5 1 8;70 E5 2 8;68 G4 1 8;68 C4 1 8;69 G4 1 8;69 C4 1 8;70 G4 2 8;70 C4 2 8;96 E5 1 8;97 E5 1 8;98 E5 2 8;96 G4 1 8;96 C4 1 8;97 G4 1 8;97 C4 1 8;98 G4 2 8;98 C4 2 8;100 E5 1 8;101 E5 1 8;102 E5 2 8;100 G4 1 8;100 C4 1 8;101 G4 1 8;101 C4 1 8;102 G4 2 8;102 C4 2 8;72 E5 1 8;73 G5 1 8;74 C5 1 8;75 D5 1 8;76 C5 4 8;76 E5 4 8;80 F5 1 8;81 F5 1 8;82 F5 1 8;83 F5 1 8;84 F5 1 8;85 E5 1 8;86 E5 1 8;87 E5 1 8;88 E5 1 8;89 D5 1 8;90 D5 1 8;91 E5 1 8;92 D5 2 8;94 G5 2 8;104 E5 1 8;105 G5 1 8;106 C5 1 8;107 D5 1 8;108 C5 4 8;108 E5 4 8;112 F5 1 8;113 F5 1 8;114 F5 1 8;115 F5 1 8;116 F5 1 8;117 E5 1 8;118 E5 1 8;119 E5 1 8;120 G5 1 8;121 G5 1 8;122 F5 1 8;123 D5 1 8;124 C5 2 8;126 C5 1 8;126 G4 1 8;126 E4 1 8;126 C4 1 8;128 G3 4 8;128 D4 4 8;132 D4 4 8;132 G3 4 8;140 D4 4 8;140 G3 4 8;136 D4 2 8;138 D4 2 8;136 G3 2 8;138 G3 2 8;146 G3 2 8;146 D4 2 8;150 G3 2 8;150 D4 2 8;144 D4 1 8;145 D4 1 8;144 G3 1 8;145 G3 1 8;148 D4 1 8;149 D4 1 8;148 G3 1 8;149 G3 1 8;144 B5 1 8;145 B5 1 8;146 B5 2 8;148 B5 1 8;149 B5 1 8;150 B5 2 8;152 B5 1 8;153 D6 1 8;154 G5 1 8;155 A5 1 8;156 G5 4 8;156 B5 4 8;160 C6 1 8;161 C6 1 8;162 C6 1 8;163 C6 1 8;164 C6 1 8;165 B5 1 8;166 B5 1 8;167 B5 1 8;168 B5 1 8;169 A5 1 8;170 A5 1 8;171 B5 1 8;172 A5 2 8;174 D6 2 8;178 B5 2 8;182 B5 2 8;176 B5 1 8;177 B5 1 8;180 B5 1 8;181 B5 1 8;184 B5 1 8;185 D6 1 8;186 G5 1 8;187 A5 1 8;192 C6 1 8;193 C6 1 8;194 C6 1 8;195 C6 1 8;196 C6 1 8;197 B5 1 8;198 B5 1 8;199 B5 1 8;200 D6 1 8;201 D6 1 8;202 C6 1 8;203 A5 1 8;208 D6 1 8;209 D6 1 8;210 C6 1 8;211 A5 1 8;212 G5 2 8;214 G6 1 8;172 D4 4 8;178 G3 2 8;178 D4 2 8;182 G3 2 8;182 D4 2 8;176 D4 1 8;177 D4 1 8;176 G3 1 8;177 G3 1 8;180 D4 1 8;181 D4 1 8;180 G3 1 8;181 G3 1 8;204 D4 1 8;205 D4 1 8;206 C4 1 8;207 B3 1 8;212 G3 3 8;212 D4 3 8;188 B5 4 8;188 G5 4 8'
mySong2 = music(song2, pins=[Pin(19),Pin(20),Pin(21),Pin(22)])

##    https://onlinesequencer.net/3107063#t0 - Silent Night
song3 = '0 E5 3 23 0.32283464074134827;0 G5 3 23 0.32283464074134827;3 F5 1 23 0.3858267664909363;3 A5 1 23 0.3858267664909363;0 C5 4 23 0.3385826647281647;4 E5 2 23 0.3779527544975281;4 G5 2 23 0.3779527544975281;0 C4 6 23 0.35433071851730347;6 C5 0 23 0.36220473051071167;6 G4 3 23 0.3700787425041199;9 A4 1 23 0.3937007784843445;6 C5 6 23 0.36220473051071167;6 E5 6 23 0.36220473051071167;6 C4 6 23 0.3779527544975281;10 G4 2 23 0.3700787425041199;12 E5 3 23 0.4015747904777527;12 G5 3 23 0.4015747904777527;15 F5 1 23 0.3937007784843445;15 A5 1 23 0.3937007784843445;12 C5 4 23 0.3937007784843445;16 E5 2 23 0.35433071851730347;16 G5 2 23 0.35433071851730347;12 C4 6 23 0.3937007784843445;18 C5 0 23 0.36220473051071167;18 G4 3 23 0.36220473051071167;21 A4 1 23 0.3937007784843445;18 C5 6 23 0.36220473051071167;18 E5 6 23 0.36220473051071167;18 C4 6 23 0.3700787425041199;22 G4 2 23 0.3779527544975281;24 F5 4 23 0.4409448802471161;24 D6 4 23 0.4409448802471161;24 B4 4 23 0.3937007784843445;28 F5 2 23 0.3779527544975281;28 D6 2 23 0.3779527544975281;24 G4 6 23 0.3700787425041199;28 B4 2 23 0.3937007784843445;30 D5 3 23 0.3937007784843445;33 E5 1 23 0.3937007784843445;30 F5 6 23 0.3700787425041199;30 B5 6 23 0.3700787425041199;30 G4 6 23 0.3700787425041199;34 D5 2 23 0.36220473051071167;36 E5 4 23 0.4015747904777527;36 C6 4 23 0.4015747904777527;36 C5 4 23 0.36220473051071167;40 E5 2 23 0.3779527544975281;40 C6 2 23 0.3779527544975281;36 G4 6 23 0.3700787425041199;40 C5 2 23 0.35433071851730347;42 E5 3 23 0.31496062874794006;45 D5 1 23 0.35433071851730347;42 G5 6 23 0.36220473051071167;46 C5 2 23 0.3700787425041199;42 G4 6 23 0.3858267664909363;42 C4 6 23 0.3937007784843445;48 F5 4 23 0.3700787425041199;48 A5 4 23 0.3700787425041199;48 F4 4 23 0.4015747904777527;48 C5 4 23 0.4015747904777527;52 F5 2 23 0.3937007784843445;52 A5 2 23 0.3937007784843445;52 F4 2 23 0.3700787425041199;52 A4 2 23 0.3700787425041199;54 A5 3 23 0.3937007784843445;54 C6 3 23 0.3937007784843445;57 G5 1 23 0.3779527544975281;57 B5 1 23 0.3779527544975281;58 F5 2 23 0.3700787425041199;58 A5 2 23 0.3700787425041199;54 F4 6 23 0.3937007784843445;54 C5 6 23 0.3937007784843445;60 E5 3 23 0.35433071851730347;60 G5 3 23 0.35433071851730347;63 F5 1 23 0.4015747904777527;63 A5 1 23 0.4015747904777527;60 C5 4 23 0.3700787425041199;64 E5 2 23 0.3858267664909363;64 G5 2 23 0.3858267664909363;60 E4 6 23 0.3779527544975281;66 C5 0 23 0.3700787425041199;66 G4 3 23 0.36220473051071167;69 A4 1 23 0.3937007784843445;66 C5 6 23 0.3700787425041199;66 E5 6 23 0.3700787425041199;66 C4 6 23 0.36220473051071167;70 G4 2 23 0.36220473051071167;72 F5 4 23 0.3858267664909363;72 A5 4 23 0.3858267664909363;72 F4 4 23 0.3937007784843445;72 C5 4 23 0.3937007784843445;76 F5 2 23 0.3937007784843445;76 A5 2 23 0.3937007784843445;76 F4 2 23 0.3700787425041199;76 A4 2 23 0.3700787425041199;78 A5 3 23 0.3779527544975281;78 C6 3 23 0.3779527544975281;81 G5 1 23 0.3779527544975281;81 B5 1 23 0.3779527544975281;82 F5 2 23 0.3700787425041199;82 A5 2 23 0.3700787425041199;78 F4 6 23 0.3700787425041199;78 C5 6 23 0.3700787425041199;84 E5 3 23 0.3700787425041199;84 G5 3 23 0.3700787425041199;87 F5 1 23 0.4015747904777527;87 A5 1 23 0.4015747904777527;84 C5 4 23 0.3858267664909363;88 E5 2 23 0.3700787425041199;88 G5 2 23 0.3700787425041199;84 E4 6 23 0.4015747904777527;90 C5 0 23 0.3700787425041199;90 G4 3 23 0.36220473051071167;93 A4 1 23 0.4015747904777527;90 C5 6 23 0.3700787425041199;90 E5 6 23 0.3700787425041199;90 C4 6 23 0.35433071851730347;94 G4 2 23 0.3779527544975281;96 F5 4 23 0.4330708682537079;96 D6 4 23 0.4330708682537079;96 G4 4 23 0.3858267664909363;96 B4 4 23 0.3858267664909363;100 F5 2 23 0.3779527544975281;100 D6 2 23 0.3779527544975281;100 G4 2 23 0.3858267664909363;100 B4 2 23 0.3858267664909363;102 A5 3 23 0.3937007784843445;102 F6 3 23 0.3937007784843445;105 F5 1 23 0.36220473051071167;105 D6 1 23 0.36220473051071167;102 D4 4 23 0.3700787425041199;106 G5 2 23 0.35433071851730347;106 B5 2 23 0.35433071851730347;102 D5 6 23 0.4015747904777527;106 G4 2 23 0.4015747904777527;108 E4 3 23 0.3700787425041199;111 F4 1 23 0.3779527544975281;108 E5 6 23 0.3858267664909363;108 C6 6 23 0.3858267664909363;108 C5 6 23 0.3779527544975281;112 E4 2 23 0.3700787425041199;114 G5 6 23 0.4094488322734833;114 E6 6 23 0.4094488322734833;114 C5 6 23 0.3700787425041199;114 C4 6 23 0.3779527544975281;120 E5 3 23 0.3700787425041199;120 C6 3 23 0.3700787425041199;123 E5 1 23 0.35433071851730347;123 G5 1 23 0.35433071851730347;120 E4 4 23 0.36220473051071167;120 G4 4 23 0.36220473051071167;124 C5 2 23 0.35433071851730347;124 E5 2 23 0.35433071851730347;124 C4 2 23 0.3937007784843445;124 G4 2 23 0.3937007784843445;126 B4 3 23 0.4015747904777527;126 G5 3 23 0.4015747904777527;129 A4 1 23 0.35433071851730347;129 F5 1 23 0.35433071851730347;126 G3 4 23 0.3779527544975281;126 F4 4 23 0.3779527544975281;130 B4 2 23 0.36220473051071167;130 D5 2 23 0.36220473051071167;130 G3 2 23 0.3779527544975281;130 D4 2 23 0.3779527544975281;132 G4 12 23 0.36220473051071167;132 C5 12 23 0.36220473051071167;132 C4 12 23 0.3937007784843445;132 E4 12 23 0.3937007784843445;144 E5 3 23 0.4173228442668915;144 G5 3 23 0.4173228442668915;147 F5 1 23 0.3937007784843445;147 A5 1 23 0.3937007784843445;144 C5 4 23 0.4173228442668915;148 E5 2 23 0.3779527544975281;148 G5 2 23 0.3779527544975281;144 C4 6 23 0.3779527544975281;150 C5 0 23 0.35433071851730347;150 G4 3 23 0.3700787425041199;153 A4 1 23 0.3937007784843445;150 C5 6 23 0.35433071851730347;150 E5 6 23 0.35433071851730347;150 C4 6 23 0.36220473051071167;154 G4 2 23 0.3700787425041199;156 E5 3 23 0.4015747904777527;156 G5 3 23 0.4015747904777527;159 F5 1 23 0.4015747904777527;159 A5 1 23 0.4015747904777527;156 C5 4 23 0.3937007784843445;160 E5 2 23 0.36220473051071167;160 G5 2 23 0.36220473051071167;156 C4 6 23 0.3937007784843445;162 C5 0 23 0.3700787425041199;162 G4 3 23 0.36220473051071167;165 A4 1 23 0.3779527544975281;162 C5 6 23 0.3700787425041199;162 E5 6 23 0.3700787425041199;162 C4 6 23 0.3779527544975281;166 G4 2 23 0.3858267664909363;168 F5 4 23 0.4251968562602997;168 D6 4 23 0.4251968562602997;168 B4 4 23 0.3858267664909363;172 F5 2 23 0.3779527544975281;172 D6 2 23 0.3779527544975281;168 G4 6 23 0.3858267664909363;172 B4 2 23 0.3937007784843445;174 D5 3 23 0.3858267664909363;177 E5 1 23 0.3937007784843445;174 F5 6 23 0.34645670652389526;174 B5 6 23 0.34645670652389526;174 G4 6 23 0.3858267664909363;178 D5 2 23 0.3779527544975281;180 E5 4 23 0.4015747904777527;180 C6 4 23 0.4015747904777527;180 C5 4 23 0.36220473051071167;184 E5 2 23 0.3858267664909363;184 C6 2 23 0.3858267664909363;180 G4 6 23 0.3779527544975281;184 C5 2 23 0.3779527544975281;186 E5 3 23 0.4015747904777527;189 D5 1 23 0.3700787425041199;186 G5 6 23 0.35433071851730347;190 C5 2 23 0.34645670652389526;186 G4 6 23 0.3858267664909363;186 C4 6 23 0.3700787425041199;192 F5 4 23 0.3937007784843445;192 A5 4 23 0.3937007784843445;192 F4 4 23 0.4094488322734833;192 C5 4 23 0.4094488322734833;196 F5 2 23 0.3779527544975281;196 A5 2 23 0.3779527544975281;196 F4 2 23 0.36220473051071167;196 A4 2 23 0.36220473051071167;198 A5 3 23 0.4094488322734833;198 C6 3 23 0.4094488322734833;201 G5 1 23 0.3700787425041199;201 B5 1 23 0.3700787425041199;202 F5 2 23 0.36220473051071167;202 A5 2 23 0.36220473051071167;198 F4 6 23 0.3858267664909363;198 C5 6 23 0.3858267664909363;204 E5 3 23 0.3858267664909363;204 G5 3 23 0.3858267664909363;207 F5 1 23 0.3858267664909363;207 A5 1 23 0.3858267664909363;204 C5 4 23 0.3858267664909363;208 E5 2 23 0.3700787425041199;208 G5 2 23 0.3700787425041199;204 E4 6 23 0.3937007784843445;210 C5 0 23 0.3700787425041199;210 G4 3 23 0.3779527544975281;213 A4 1 23 0.3779527544975281;210 C5 6 23 0.3700787425041199;210 E5 6 23 0.3700787425041199;210 C4 6 23 0.36220473051071167;214 G4 2 23 0.36220473051071167;216 F5 4 23 0.4094488322734833;216 A5 4 23 0.4094488322734833;216 F4 4 23 0.3937007784843445;216 C5 4 23 0.3937007784843445;220 F5 2 23 0.3779527544975281;220 A5 2 23 0.3779527544975281;220 F4 2 23 0.3779527544975281;220 A4 2 23 0.3779527544975281;222 A5 3 23 0.4173228442668915;222 C6 3 23 0.4173228442668915;225 G5 1 23 0.3700787425041199;225 B5 1 23 0.3700787425041199;226 F5 2 23 0.3700787425041199;226 A5 2 23 0.3700787425041199;222 F4 6 23 0.4015747904777527;222 C5 6 23 0.4015747904777527;228 E5 3 23 0.3858267664909363;228 G5 3 23 0.3858267664909363;231 F5 1 23 0.3779527544975281;231 A5 1 23 0.3779527544975281;228 C5 4 23 0.4015747904777527;232 E5 2 23 0.36220473051071167;232 G5 2 23 0.36220473051071167;228 E4 6 23 0.3937007784843445;234 C5 0 23 0.35433071851730347;234 G4 3 23 0.35433071851730347;237 A4 1 23 0.3937007784843445;234 C5 6 23 0.35433071851730347;234 E5 6 23 0.35433071851730347;234 C4 6 23 0.3700787425041199;238 G4 2 23 0.35433071851730347;240 F5 4 23 0.4094488322734833;240 D6 4 23 0.4094488322734833;240 G4 4 23 0.3858267664909363;240 B4 4 23 0.3858267664909363;244 F5 2 23 0.36220473051071167;244 D6 2 23 0.36220473051071167;244 G4 2 23 0.3858267664909363;244 B4 2 23 0.3858267664909363;246 A5 3 23 0.4015747904777527;246 F6 3 23 0.4015747904777527;249 F5 1 23 0.3700787425041199;249 D6 1 23 0.3700787425041199;246 D4 4 23 0.3779527544975281;250 G5 2 23 0.3700787425041199;250 B5 2 23 0.3700787425041199;246 D5 6 23 0.4173228442668915;250 G4 2 23 0.4015747904777527;252 E4 3 23 0.3779527544975281;255 F4 1 23 0.3779527544975281;252 E5 6 23 0.3937007784843445;252 C6 6 23 0.3937007784843445;252 C5 6 23 0.36220473051071167;256 E4 2 23 0.3779527544975281;258 G5 6 23 0.4015747904777527;258 E6 6 23 0.4015747904777527;258 C5 6 23 0.3937007784843445;258 C4 6 23 0.3700787425041199;264 E5 3 23 0.35433071851730347;264 C6 3 23 0.35433071851730347;267 E5 1 23 0.34645670652389526;267 G5 1 23 0.34645670652389526;264 E4 4 23 0.3700787425041199;264 G4 4 23 0.3700787425041199;268 C5 2 23 0.35433071851730347;268 E5 2 23 0.35433071851730347;268 C4 2 23 0.3779527544975281;268 G4 2 23 0.3779527544975281;270 B4 3 23 0.3937007784843445;270 G5 3 23 0.3937007784843445;273 A4 1 23 0.3700787425041199;273 F5 1 23 0.3700787425041199;270 G3 4 23 0.3858267664909363;270 F4 4 23 0.3858267664909363;274 B4 2 23 0.35433071851730347;274 D5 2 23 0.35433071851730347;274 G3 2 23 0.3700787425041199;274 D4 2 23 0.3700787425041199;276 G4 12 23 0.3700787425041199;276 C5 12 23 0.3700787425041199;276 C4 12 23 0.3937007784843445;276 E4 12 23 0.3937007784843445'
mySong3 = music(song3, pins=[Pin(19),Pin(20),Pin(21),Pin(22)])

def lights_on():
    for x in range(0,18):
        leds[x].value(1)
        utime.sleep_ms(75) # controls how fast the LEDs flow when turning on and vice versa

def lights_off():
    for x in range(0,18):
        leds[x].value(0)
        utime.sleep_ms(75)

def play():
    # time limits for each of the 3 songs
    song1_time = len(song1)
    song2_time = len(song2)
    song3_time = len(song3)
    
    lights_on()
    lcd.putstr("We Wish You A"+"\n"+"Merry Christmas") # adds a message to the LCD
    while song1_time >= 0: # counts down the time it takes for the song to play 
        mySong1.tick()
        sleep(0.05)
        song1_time -= 5  # countdown rate (varies depending on the song) (figured out through trial and error)
           
    mySong1.stop() # stops the buzzers once the countdown is finished
    lights_off()
    lcd.clear()
    sleep(1) 
    
    lights_on()
    lcd.putstr("     Jingle "+"\n"+"     Bells")   
    while song2_time >= 0:
        mySong2.tick()
        sleep(0.08)
        song2_time -= 3.65 # countdown rate  
    mySong2.stop()   
    lights_off()
    lcd.clear()
    sleep(1)
    
    lights_on()
    lcd.putstr("     Silent "+"\n"+"     Night")  
    while song3_time >= 0:
        mySong3.tick()
        sleep(0.1)
        song3_time -= 12.25 # countdown rate  
    mySong3.stop()
    lcd.clear()
    sleep(1)
    
    lcd.putstr("     Merry  "+"\n"+"   Christmas!")
    sleep(3)
    lights_off()
    lcd.clear()   

if __name__ == '__main__':
    play()
