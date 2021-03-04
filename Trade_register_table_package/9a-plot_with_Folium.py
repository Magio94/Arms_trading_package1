import folium, os, webbrowser

try:
    print_year = str(year_input1) + "-" + str(year_input2)
except:
    print_year = str(year_input)

print("Plotting in progress..... Two maps will be created shortly, one for the\n"
      "sellers and one for the buyers. Thank you for your patience")

#PLOTS MAP OF SELLERS

filePath = 'Number of arms sold by state.html'
try:
    os.remove(filePath)
except:
    print("\nThe file was not already present so it will be generated: ", filePath)

m = folium.Map(location=[0,0], zoom_start=1.5)

folium.Choropleth(
    state_sellers,
    name='choropleth',
    data=state_sellers,
    columns=['NAME_ENGL', 'n_arms'],
    key_on='feature.properties.NAME_ENGL',
    fill_color='YlGnBu',
    legend_name="Number of arms sold by state in the year: " + print_year
).add_to(m)

folium.LayerControl().add_to(m)

m.save("Number of arms sold by state.html")

filename = 'file:///'+os.getcwd()+'/' + 'Number of arms sold by state.html'
webbrowser.open_new_tab(filename)

# PLOTS MAP OF BUYERS

filePath = 'Number of arms bought by state.html'
try:
    os.remove(filePath)
except:
    print("\nThe file was not already present, so it will be generated: ", filePath)

m = folium.Map(location=[0,0], zoom_start=1.5)

folium.Choropleth(
    state_buyers,
    name='choropleth',
    data=state_buyers,
    columns=['NAME_ENGL', 'n_arms'],
    key_on='feature.properties.NAME_ENGL',
    fill_color='YlGnBu',
    legend_name="Number of arms bought by state in the year: " + print_year
).add_to(m)

folium.LayerControl().add_to(m)

m.save("Number of arms bought by state.html")

filename = 'file:///'+os.getcwd()+'/' + 'Number of arms bought by state.html'
webbrowser.open_new_tab(filename)
