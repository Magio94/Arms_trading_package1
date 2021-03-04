# Creates a dashboard with polar chart plot from user choice: (importers or exporters) and (Year or Total)

imp_tiv = top_imp_values
exp_tiv = top_exp_values

# Erase rows where "Country" reads "Total" so it doesnt show in the tree map
index_names = imp_tiv[imp_tiv['Country'] == 'Total'].index
imp_tiv.drop(index_names, inplace=True)

index_names = exp_tiv[exp_tiv['Country'] == 'Total'].index
exp_tiv.drop(index_names, inplace=True)

#Prompts user to input how many countries they would like to display data for. Number of "top countries"
while True:
    try:
        n_country = int(input ('''Enter the number of "Top Importers" or "Top Exporters" you would like to display, (2 to 40): '''))
        if n_country in range(2, 41):
            break
    except:
        print( "Error: Numbers are the only valid inputs. Please try again."  )
    else:
        print ("The number you selected is not in the correct range (2 to 40). Please try again.")

#Creates top 10 query for chosen year for both imports and exports
top_imp_values = imp_tiv.nlargest(n_country, "sum_col")
top_exp_values = exp_tiv.nlargest(n_country, "sum_col")

#Prompts user to input if they want to display "import" or "export" data.
type_input = input ('''Enter the type of data you would like to display, either "Imports" or "Exports": ''')
while True:
    if type_input == "Imports" or type_input == "imports":
        selected_data = top_imp_values
        break
    elif type_input == "Exports" or type_input == "exports":
        selected_data = top_exp_values
        break
    else:
        print ("Error: Not a valid entry. Please try again. ")
        type_input = input('''Enter the type of data you would like to display, either "Imports" or "Exports": ''')

#Plots data with plotly: greatest arms importers or exporters (previously selected by user)
import plotly.express as px

#Determines what data to display on the polar chart
fig = px.bar_polar(selected_data, theta="Country", r=str("sum_col"),template = "plotly_dark", color="sum_col")

fig.update_layout(height=600, showlegend=True)
fig.update_layout(showlegend=False,
                  title_text="STOCKHOLM INTERNATIONAL PEACE RESEARCH INSTITUTE<br>" +
                      "<i>Arms " + str(type_input) + " : " + str(year_input1)+"-"+str(year_input2) + " Trend Indicator Values<i><br><br>")
fig.layout.coloraxis.colorbar.title = 'TIV'

fig.show()