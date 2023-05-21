map_list = open('geojson_sweden')
new_map_list = []
for line in map_list:
    if "Gnesta" in line or "Nyköping" in line or "Flen" in line or "Vingåker" in line or "Katrineholm" in line or "Eskilstuna" in line or "Strängnäs" in line or "Oxelösund" in line or "Trosa" in line:
        new_map_list.append(line)
with open('sormland_map.geojson', 'a') as f:
    f.write("{'type':'FeatureCollection', 'features': [")
    for line in new_map_list:
        f.write(line)
    f.write("]")