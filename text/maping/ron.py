import folium
map = folium.Map(location=[24.76039928416675, 84.36473644075765],zoom_start=15)
folium.CircleMarker(location=[24.76039928416675, 84.36473644075765],radius=50,popup="anyplace").add_to(map)
folium.Marker([24.76039928416675, 84.36473644075765],popup="unkown place").add_to(map)
folium.Marker([24.76039928416675, 84.36473644075765],popup="place").add_to(map)


map.save("map.html")