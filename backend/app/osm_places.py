import requests

OVERPASS_URL = "https://overpass-api.de/api/interpreter"

def fetch_nearby_restaurants(lat, lon, radius=2000):
    query = f"""
    [out:json];
    node
      ["amenity"="restaurant"]
      (around:{radius},{lat},{lon});
    out;
    """

    res = requests.post(OVERPASS_URL, data=query)
    data = res.json()

    places = []
    for el in data["elements"]:
        places.append({
            "name": el["tags"].get("name", "Unnamed Restaurant"),
            "lat": el["lat"],
            "lon": el["lon"]
        })

    return places[:15]
