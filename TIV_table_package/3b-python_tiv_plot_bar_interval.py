# Creates a dashboard with two bar plots from user's choice: (Year) and (Number of countries)

imp_tiv = top_imp_values
exp_tiv = top_exp_values

#Prompts user to input the number of countires they would like to display, as "Top Importer" or "Top Exporters"

while True:
    try:
        n_country = int(input ('''Enter the number of "Top Importers" or "Top Exporters" you would like to display, (2 to 40): '''))
        if n_country in range(2, 41):
            break
    except:
        print("Error: Numbers are the only valid inputs. Please try again: " )
    else:
        print ("The number you selected is not in the correct range (2 to 40). Please try again: ")

# Create top "n_country" query for chosen year for both imports and exports
top_imp_values = imp_tiv.nlargest(int(n_country), "sum_col")
top_exp_values = exp_tiv.nlargest(int(n_country), "sum_col")

# Plots data with plotly: Top arms importers and Top arms exporters for specific year (previously selected by user)
import plotly.express as px
from plotly.subplots import make_subplots

#Determines what to display on each bar graph
fig1 = px.bar(top_imp_values, x="Country", y=str("sum_col"),
              text=str("sum_col"), color=top_imp_values[str("sum_col")])
fig2 = px.bar(top_exp_values, x="Country", y=str("sum_col"),
              text=str("sum_col"), color=top_exp_values[str("sum_col")])

# Defines plot areas and graphic options
fig = make_subplots(rows=2, cols=1, shared_xaxes=False, horizontal_spacing=0.1,
                    subplot_titles=["Top " + str(year_input1)+"-"+str(year_input2) + " Arms Imports Countries",
                                    "Top " + str(year_input1)+"-"+str(year_input2) + " Arms Exports Countries"],
                    y_title="Trend Indicator Values"
                    )
fig.add_trace(fig1['data'][0], row=1, col=1,)
fig.add_trace(fig2['data'][0], row=2, col=1,)
fig.update_layout(coloraxis_autocolorscale=False)
fig.update_coloraxes(colorscale='Portland')
fig.update_traces(texttemplate='%{text:.2s}')
fig.update_layout(uniformtext_minsize=6, uniformtext_mode='hide')
fig.layout.coloraxis.colorbar.title = 'TIV'
fig.update_layout(showlegend=False,
                  title_text="STOCKHOLM INTERNATIONAL PEACE RESEARCH INSTITUTE<br>" +
                             "<i>Trend Indicator Values<i>")

fig.show()

