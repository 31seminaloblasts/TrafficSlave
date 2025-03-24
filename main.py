import openrouteservice
import points

location_points = points.locations() # enter location csv file path
population_points = points.population() # enter population csv file path
client = openrouteservice.Client(key='') # enter api key here

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
            
calculate()

