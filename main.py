import openrouteservice
client = openrouteservice.Client(key='') # put your own key here

def d(start, end):
    try:
        return client.directions([start, end], format='geojson')['features'][0]['properties']['segments'][0]['duration']
    except:
        print("d() function error.")
        return None
def calculate():
    for i in range(len(population_points)): 
        data = []
        for ii in range(len(location_points)): 
            duration = d(population_points[i]["coordinates"], location_points[ii]["coordinates"]) 
            if duration is not None:
                data.append((duration, ii))
            data.sort()
            location_points[ii]["customers"] += population_points[i]["population"]
population_points = [
    {"coordinates": (0, 0), "population": 0},
    {"coordinates": (0, 0), "population": 0},
]
location_points = [
    {"coordinates": (0, 0), "customers": 0},
    {"coordinates": (0, 0), "customers": 0},
]
calculate()
