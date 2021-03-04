# Creates a dashboard with two bar plots from user's choice: (Year) and (Number of countries)
import pandas as pd

imp_tiv = pd.read_csv(r'0-Downloaded_files/imp_tiv.csv')
exp_tiv = pd.read_csv(r'0-Downloaded_files/exp_tiv.csv')

#Prompts user to input how many countries they would like to display data for. "Number of top countries"
while True:
    try:
        n_country = int(input ('''Enter the number of "Top Importers" or "Top Exporters" you would like to display, (2 to 40): '''))
        if n_country in range(2, 41):
            break
    except:
        print( "Error: Numbers are the only valid inputs. Please try again." )
    else:
        print ("The year you selected is not in the data's range. Please try again.")

# Creates top "n_country" query for chosen year for both "imports" and "exports"
top_imp_values = imp_tiv.nlargest(int(n_country), str(year_input))
top_exp_values = exp_tiv.nlargest(int(n_country), str(year_input))

# Plots data with plotly: greatest arms importers and exporters for specific year (previously selected by user)
import plotly.express as px
from plotly.subplots import make_subplots

# Determines what data is to be displayed in each bar graph
fig1 = px.bar(top_imp_values, x="Country", y=str(year_input),
              text=str(year_input), color=top_imp_values[str(year_input)])
fig2 = px.bar(top_exp_values, x="Country", y=str(year_input),
              text=str(year_input), color=top_exp_values[str(year_input)])

# Defines the plot areas and graphic options
fig = make_subplots(rows=2, cols=1, shared_xaxes=False, horizontal_spacing=0.1,
                    subplot_titles=["Top " + str(year_input) + " Arms Imports Countries",
                                    "Top " + str(year_input) + " Arms Exports Countries"],
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

