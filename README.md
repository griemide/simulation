# Simulation
Various simulation tools and projects

## Tools
- [WOKWI](https://wokwi.com/) by [Uri Shaked](https://hackaday.io/urishaked)  - Simulate IoT Projects (Arduino / MicroPython) within a Browser - [GitHub](https://github.com/wokwi) / [Blog](https://blog.wokwi.com/)

## Projects

https://wokwi.com/dashboard/projects

 - Simulating [Micropython on a Raspberry PICO W](https://github.com/griemide/MicroPython/tree/master/RP2040)
 
## Available Board Definitions
https://github.com/wokwi/wokwi-boards/tree/main/boards

## Specials

add additional connection to diagam.json file: e.g. ```[ "pico:GP0", "pico:TP5", "", [ ] ], ```  
in this case following code can be applied:
``` micropython
# Pins konfigurieren
pin_gpio0 = machine.Pin(0, machine.Pin.OUT) # entspricht dem Pin 1 des RP2-boards
pin_onboard_led = machine.Pin("LED", machine.Pin.OUT) # entspricht WL_GPIO es Infineon Chip
...
# Pin auf high setzen und Impulslänge warten
pin_gpio0.on()
pin_onboard_led.on()
```

## Examples

- https://wokwi.com/projects/363282075914340353
- https://wokwi.com/projects/363352758307109889

![2](https://github.com/griemide/simulation/blob/main/%C2%B5P_RP2040_Pulse-Generator-2/%C2%B5P_RP2040_Pulse-Generator-2.gif)


## References

- [RP2040](https://hackaday.io/course/178733-raspberry-pi-pico-and-rp2040-the-deep-dive) 
- https://www.hackster.io/news/uri-shaked-is-developing-a-javascript-raspberry-pi-pico-emulator-in-a-live-coding-video-series-e2905e44023f

- Coding with help of ChattGPT: https://blog.wokwi.com/learn-arduino-using-ai-chatgpt/
