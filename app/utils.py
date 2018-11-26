import re


# Sanitize tournament name for url
def sanitize(url):
    clean = url.replace(' ', '_')
    clean = re.sub("[^a-zA-Z0-9-_]", "-", clean)
    return clean


# Initialize a list of maps with none banned so far
def create_map_list():
    names = [
        "Hanamura", "Horizon Lunar Colony", "Temple of Anubis", "Volskaya Industries",
        "Dorado", "Junkertown", "Rialto", "Route 66", "Watchpoint: Gibraltar",
        "Blizzard World", "Eichenwalde", "Hollywood", "King's Row", "Numbani",
        "Busan", "Ilios", "Lijiang Tower", "Nepal", "Oasis"
    ]
    assault = "color: red;"
    escort = "color: purple;"
    hybrid = "color: blue;"
    control = "color: green;"
    # Assault, Escort, Hybrid, Control (aka 2CP, Payload, Hybrid, KOTH)
    types = [
        assault, assault, assault, assault,
        escort, escort, escort, escort, escort,
        hybrid, hybrid, hybrid, hybrid, hybrid,
        control, control, control, control, control]
    maps = []
    for i in range(len(names)):
        map_info = [names[i], types[i], i, i]  # name, map type/color, map id, order
        maps.append(map_info)
    maps.sort(key=lambda x: x[3])
    return maps
