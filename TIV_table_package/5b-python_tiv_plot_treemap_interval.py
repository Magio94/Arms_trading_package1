# Creates a dashboard with tree map plot from user choice: (importers or exporters) and (Year or Total)

imp_tiv = top_imp_values
exp_tiv = top_exp_values

#Erases rows where "Country" reads "Total" so the "Total" doesn't display in the tree map
index_names = imp_tiv[imp_tiv['Country'] == 'Total'].index
imp_tiv.drop(index_names, inplace=True)

index_names = exp_tiv[exp_tiv['Country'] == 'Total'].index
exp_tiv.drop(index_names, inplace=True)

#Prompts user to input if they want to display "import" or "export" data.

type_input = input ('''Enter the type of data you would like to display, either "Imports" or "Exports": ''')
while True:
    if type_input == "Imports" or type_input == "imports":
        selected_data = imp_tiv
        break
    elif type_input == "Exports" or type_input == "exports":
        selected_data = exp_tiv
        break
    else:
        print ("Error: Not a valid entry. Please try again. ")
        type_input = input('''Enter the type of data you would like to display, either "Imports" or "Exports": ''')

#Plots data with plotly: greatest arms importers and exporters for specific year (previously selected by user)
import plotly.express as px

#Determines what data is to be displayed in each tree map
fig = px.treemap(selected_data, path=['Country'], values=str("sum_col"),
                title="STOCKHOLM INTERNATIONAL PEACE RESEARCH INSTITUTE<br>" +
                      "<i>Arms " + str(type_input)+ " : " + str(year_input1)+"-"+str(year_input2) + " Trend Indicator Values<i>")

fig.show()