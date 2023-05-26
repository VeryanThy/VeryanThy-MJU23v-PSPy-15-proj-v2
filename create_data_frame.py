# This file calculates average values to use for the choropleth dataframe
import tkinter as tk
import pandas as pd
import plotly.graph_objects as go
#import numpy as np
#import geopandas as gpd
#import matplotlib.pyplot as plt
import plotly.express as px
import geojson
from geojson_rewind import rewind


vingaker = []
gnesta = []
flen = []
katrineholm = []
eskilstuna = []
trosa = []
oxelosund = []
nykoping = []
strangnas = []
kommun_list = ['Vingåker', 'Gnesta', 'Flen', 'Katrineholm', 'Eskilstuna', 'Trosa', 'Oxelösund', 'Nyköping', "Strängnäs"]

# takes property data and puts in arrays according to kommun
file_name = "properties_data.csv"
data = open(file_name)
properties = data.readlines()
for line in properties:
    elements = line.split(",")
    if elements[0] == "Vingåker":
        vingaker.append(line)
    if elements[0] == "Gnesta":
        gnesta.append(line)
    if elements[0] == "Flen":
        flen.append(line)
    if elements[0] == "Katrineholm":
        katrineholm.append(line)
    if elements[0] == "Eskilstuna":
        eskilstuna.append(line)
    if elements[0] == "Trosa":
        trosa.append(line)
    if elements[0] == "Oxelösund":
        oxelosund.append(line)
    if elements[0] == "Nyköping":
        nykoping.append(line)
    if elements[0] == "Strängnäs":
        strangnas.append(line)
# gets index in array of parameter
def get_index(field):
    if field == "area":
        index = 1
    if field == "rum":
        index = 2
    if field == "tomt":
        index = 3
    if field == "price":
        index = 4
    if field == "date":
        index = 5
    if field == "increase":
        index = 6
    return index
def mean(kommun, index):
    sum = 0
    for line in kommun:
        price = line[index]
        sum = sum + int(price)
    average = sum / len(kommun)
    return average

def create_data_frame(option):
    df = []
    if option == "Number of sales":
        num_sales = [len(vingaker), len(gnesta), len(flen), len(katrineholm), len(eskilstuna), len(trosa), len(oxelosund), len(nykoping), len(strangnas)]
        df =  pd.DataFrame({'Kommun': kommun_list[0:9], 'Antal': num_sales[0:9]})
    if option == "Average Sales Price":
        index = get_index("price")
        av_pris = [mean(vingaker, index), mean(gnesta, index), mean(flen, index), mean(katrineholm, index), mean(eskilstuna, index), mean(trosa, index), mean(oxelosund, index), mean(nykoping, index), mean(strangnas, index)]
        df =  pd.DataFrame({'Kommun': kommun_list[0:9], 'Price': av_pris[0:9]})
    return df

def generate_map():
    option = menu.get()
    df = create_data_frame(option)
    if option == "Number of sales":
        param = 'Antal'
    if option == "Average Sales Price":
        param = 'Price'
    with open("sormland_map.geojson") as f:
        geojson_file = geojson.load(f)
    sormland_geojson = rewind(geojson_file,rfc7946=False)

 
    fig = px.choropleth_mapbox(df,
                geojson = sormland_geojson,
                featureidkey='properties.kom_namn', 
                locations='Kommun', 
                color= param,
                color_continuous_scale="dense", 
                mapbox_style = 'carto-positron', 
                center={'lat': 59, 'lon': 16},
                opacity= 0.7,
                zoom = 7)                
    fig.show()
    
    
    #fig.update_geos(fitbounds="locations", visible=True)
    fig.show()

window = tk.Tk()
window.geometry("700x350")

heading = tk.Label(
    text="Choropleth Map Generator", 
    fg="white",
    bg="black",
    width=100,
    height=10)
heading.pack()
menu= tk.StringVar()
menu.set("Select Data Parameter")
drop= tk.OptionMenu(window, menu,"Average Sales Price", "Number of sales","Average Price/m^2","Average % over asking price")
drop.pack()
button = tk.Button(
    text="Generate Map!",
    width=25,
    height=5,
    bg="white",
    fg="black",
    command= generate_map
)
button.pack()
window.mainloop()



        


#def mean_value(parameter):

 



