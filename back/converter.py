import eel
from pyowm import OWM

def get_bishkek_weather():
    city = "Bishkek, KG"

    owm = OWM('83fb857ad999187748b6eeea5df78703')
    mgr = owm.weather_manager()

    observation = mgr.weather_at_place(city)
    w = observation.weather

    print(w.temperature('celsius')['temp'])

















