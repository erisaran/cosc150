def water_state(temp):
    if 0<temp<100:
        return liquid
    elif temp>=100:
        return steam
    elif 0>=temp:
        return ice

x=raw_input("Water temperature? ")
steam="steam"
liquid="liquid"
ice="ice"
print water_state(x)

