import machine # Základní knihovna pro práci s rapbbery pi pico W
import time # Importování knihovny time pro zpomalení chodu programu

# Ukládání do proměné odkazy na pin
# název proměné   volání knihovny   Voláme třídu Pin  Pin s číslem 1    volání knohovny  Pin - výstup
led1           =   machine.          Pin              (1,               machine.         Pin.OUT)
led2 = machine.Pin(2, machine.Pin.OUT) # Stejný zápis
led3 = machine.Pin(3, machine.Pin.OUT)
led4 = machine.Pin(4, machine.Pin.OUT)

# Vytvoříme si list (pole), kde si uložíme proměné s led
leds = [led1, led2, led3, led4]

# Funkce pro zapínání nebo vypínání Led
def LightOption(Pin, option, delay):
    # Pin - Odkážete, jaký pin bude odesílat signál
    # option - Boolean hodnota 1- zaponout, 0 - vypnout
    # delay - Zpomalení chodu programu v sekundách
    time.sleep(delay)
    return Pin.value(option)

# Nekončicí smyčka programu
# Efektivní kod, je kratší
while True:
    # Vnořená for pro postupné zapínání ledek
    for led in leds:
        LightOption(led, 1, 1)
    time.sleep(1)
    for led in leds:
        LightOption(led, 0, 0)

# Můžete kod zapínat i tímto dlouhým způsobem
#machine.Pin(1, machine.Pin.OUT).value(1)

#while True:
    # Ledku zapneme pomocí proměné, nemusím psát zdlouhavě kod
#   led1.value(1)
#    led2.value(1)
    # Zpomalíme chod programu
#    time.sleep(1)

#    led3.value(1)
#    time.sleep(1)

#    led4.value(1)
#    time.sleep(1)

    # Vypneme ledky - 0
#    led1.value(0)
#    led2.value(0)
#    led3.value(0)
#    led4.value(0)
#    time.sleep(1)


