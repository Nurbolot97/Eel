import eel
from back.converter import get_bishkek_weather



@eel.expose
def give_bishkek_weather():
    return get_bishkek_weather()






