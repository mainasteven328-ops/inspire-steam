from machine import Pin, I2C
import utime

# ================= LCD DRIVER =================
class I2cLcd:
    def __init__(self, i2c, addr, rows, cols):
        self.i2c = i2c
        self.addr = addr
        self.rows = rows
        self.cols = cols

        utime.sleep_ms(20)
        self._write_cmd(0x33)
        self._write_cmd(0x32)
        self._write_cmd(0x28)
        self._write_cmd(0x0C)
        self._write_cmd(0x06)
        self.clear()

    def _write_cmd(self, cmd):
        self._write4(cmd & 0xF0)
        self._write4((cmd << 4) & 0xF0)

    def _write_data(self, data):
        self._write4(data & 0xF0, True)
        self._write4((data << 4) & 0xF0, True)

    def _write4(self, data, char_mode=False):
        control = 0x01 if char_mode else 0x00
        self.i2c.writeto(self.addr, bytes([data | control | 0x04]))
        self.i2c.writeto(self.addr, bytes([data | control]))

    def clear(self):
        self._write_cmd(0x01)
        utime.sleep_ms(2)

    def move_to(self, col, row):
        addr = col + (0x40 if row else 0x00)
        self._write_cmd(0x80 | addr)

    def putstr(self, string):
        for char in string:
            self._write_data(ord(char))

# ================= HARDWARE SETUP =================
# LCD I2C (GP0 SDA, GP1 SCL)
i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=400000)
lcd = I2cLcd(i2c, 0x27, 2, 16)

# Buzzer (GP15)
from machine import PWM

buzzer = PWM(Pin(15))
buzzer.duty_u16(0)  # Start silent

# Keypad Pins
rows = [Pin(2, Pin.OUT), Pin(3, Pin.OUT), Pin(4, Pin.OUT), Pin(5, Pin.OUT)]
cols = [
    Pin(6, Pin.IN, Pin.PULL_DOWN),
    Pin(7, Pin.IN, Pin.PULL_DOWN),
    Pin(8, Pin.IN, Pin.PULL_DOWN),
    Pin(9, Pin.IN, Pin.PULL_DOWN)
]

keys = [
    ["1","2","3","A"],
    ["4","5","6","B"],
    ["7","8","9","C"],
    ["*","0","#","D"]
]

PASSWORD = "123456"
entered = ""

# ================= FUNCTIONS =================
def beep(duration=0.1, freq=1000):
    buzzer.freq(freq)
    buzzer.duty_u16(30000)  # Volume
    utime.sleep(duration)
    buzzer.duty_u16(0)

def wrong_alarm():
    for _ in range(5):
        buzzer.freq(800)
        buzzer.duty_u16(40000)
        utime.sleep(0.15)
        buzzer.duty_u16(0)
        utime.sleep(0.1)

def read_key():
    for i, row in enumerate(rows):
        row.high()
        for j, col in enumerate(cols):
            if col.value():
                utime.sleep(0.2)  # debounce
                row.low()
                return keys[i][j]
        row.low()
    return None

# ================= MAIN PROGRAM =================
lcd.putstr("Enter Password:")
lcd.move_to(0, 1)

while True:
    key = read_key()
    if key:
        beep(0.05)
        entered += key
        lcd.putstr("*")

        if len(entered) == len(PASSWORD):
            utime.sleep(0.5)
            lcd.clear()

            if entered == PASSWORD:
                lcd.putstr("Access Granted")
                beep(0.3)
            else:
                lcd.putstr("Wrong Password")
                wrong_alarm()

            utime.sleep(2)
            lcd.clear()
            lcd.putstr("Enter Password:")
            lcd.move_to(0, 1)
            entered = ""


# SECOND FILE IN WOKWI HOME ALARM SYSTEM
{
  "version": 1,
  "author": "sir lance",
  "editor": "wokwi",
  "parts": [
    {
      "type": "wokwi-pi-pico",
      "id": "pico",
      "top": 0,
      "left": 0,
      "attrs": { "env": "micropython-20241129-v1.24.1" }
    },
    {
      "type": "wokwi-membrane-keypad",
      "id": "keypad1",
      "top": -107.6,
      "left": -455.2,
      "attrs": {}
    },
    {
      "type": "wokwi-lcd1602",
      "id": "lcd1",
      "top": -176,
      "left": 82.4,
      "attrs": { "pins": "i2c" }
    },
    {
      "type": "wokwi-buzzer",
      "id": "bz1",
      "top": 21.6,
      "left": 251.4,
      "attrs": { "volume": "0.1" }
    }
  ],
  "connections": [
    [ "pico:GP2", "keypad1:R1", "green", [ "h-111.6", "v169.65", "h-249.6" ] ],
    [ "keypad1:R2", "pico:GP3", "green", [ "v-9.6", "h230", "v-169.65" ] ],
    [ "keypad1:R3", "pico:GP4", "green", [ "v19.2", "h239.7", "v-188.85" ] ],
    [ "keypad1:C1", "pico:GP6", "green", [ "v57.6", "h239.9", "v-198.45" ] ],
    [ "keypad1:C2", "pico:GP7", "green", [ "v48", "h268.8", "v-179.25" ] ],
    [ "keypad1:C3", "pico:GP8", "green", [ "v28.8", "h249.45", "v-150.45" ] ],
    [ "keypad1:C4", "pico:GP9", "green", [ "v38.4", "h258.9", "v-150.45" ] ],
    [ "pico:GND.4", "bz1:1", "black", [ "h0" ] ],
    [ "lcd1:GND", "pico:GND.8", "black", [ "h0" ] ],
    [ "lcd1:VCC", "pico:VBUS", "red", [ "h0" ] ],
    [ "lcd1:SDA", "pico:GP0", "black", [ "h-105.6", "v137.75" ] ],
    [ "lcd1:SCL", "pico:GP1", "green", [ "h-124.8", "v137.85" ] ],
    [ "keypad1:R4", "pico:GP5", "green", [ "h268.6", "v-160.05" ] ],
    [ "pico:GP15", "bz1:2", "red", [ "h0" ] ]
  ],
  "dependencies": {}
}