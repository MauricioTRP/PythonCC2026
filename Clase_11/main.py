from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps

owm = OWM('0a853551fe4a4b6808371f8b62b756cf')
mgr = owm.weather_manager()

observation = mgr.weather_at_coords(33.26, 70.39)
w = observation.weather

print(w.detailed_status)
