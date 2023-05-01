# 2023-05-01
# Michael Gries

# tested with:
# MicroPython v1.19.1-993-g283c1ba07 on 2023-03-29; 
# Raspberry Pi Pico W with RP2040 

print("µP_RP2040_Onboard-LED")

# Onboard-LED pin WL_GPIO of Infineon Chip
# add '[ "pico:GP1", "pico:TP5", "", [ "v0" ] ],' within diagram.json
## pin_onboard_led = machine.Pin("LED", machine.Pin.OUT) 
pin_gpio1 = machine.Pin(1, machine.Pin.OUT) # equals Pin 2 of PICO W board

pulse_length = 500 # msec
intervall = 1000 # msec

# Timer-Handler 
def timer_handler(timer):
    global pulse_length
    ## pin_onboard_led.on()
    pin_gpio1.on()
    timer_pulse = machine.Timer(-1)
    timer_pulse.init(period=pulse_length, mode=machine.Timer.ONE_SHOT, callback=timer_callback)

# Timer-Callback 
def timer_callback(timer):
    ## pin_onboard_led.off()
    pin_gpio1.off()

# Timer konfigurieren
timer_intervall = machine.Timer(-1) # default für RP2 board
timer_intervall.init(period=intervall, mode=machine.Timer.PERIODIC, callback=timer_handler)
