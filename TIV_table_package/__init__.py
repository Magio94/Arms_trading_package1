print("\n*** Welcome to our program based on the STOCKHOLM INTERNATIONAL PEACE RESEARCH INSTITUTE\n"
      "Arms Trading Database and the DEPARTMENT OF PEACE AND CONFLICT RESEARCH, UPPSALA UNIVERSITY\n"
      "and CENTER FOR THE STUDY OF CIVIL WARS, INTERNATIONAL PEACE RESEARCH INITIATIVE, Oslo Armed\n"
      "Conflict Dataset ***\n\n"
      "*** WELCOME TO THE FIRST PART OF THE PROGRAM ***.\n")

# DEFINE THE NAME OF THE DIRECTORY TO BE CREATED WHERE INSERT DOWNLOADED FILES
import os

try:
    os.mkdir("0-Downloaded_files")
    print ("Successfully created the directory: downloaded_files")
except:
    print ("'Downloaded_files' directory already present")

# DOWNLOADS THE TIV IMPORT AND EXPORT TABLES ON ARMS TRADING AND SAVES THE FILE ON ARMS TRADING AS CSV FOR CHECKING
choose_import_or_export = str("import")
exec(open('TIV_table_package/1-download_TIV_table.py').read())
save_csv = "0-Downloaded_files/TIV-Import-All-1950-2019.csv"
exec(open('common_actions/1-save_csv_tables.py').read())

choose_import_or_export = str("export")
exec(open('TIV_table_package/1-download_TIV_table.py').read())
save_csv = "0-Downloaded_files/TIV-Export-All-1950-2019.csv"
exec(open('common_actions/1-save_csv_tables.py').read())

print("The import and export arms trade data has been downloaded\n")

# PROCESSES THE TABLES ON IMPORT AND EXPORT ARMS TRADING
csv_table = "0-Downloaded_files/TIV-Import-All-1950-2019.csv"
file_name = "0-Downloaded_files/imp_tiv.csv"
exec(open('TIV_table_package/2-process_TIV_table.py').read())
print("\nImport arms trading printed above for your preview.\n")

csv_table = "0-Downloaded_files/TIV-Export-All-1950-2019.csv"
file_name = "0-Downloaded_files/exp_tiv.csv"
exec(open('TIV_table_package/2-process_TIV_table.py').read())
print("\nExport arms trading printed above for your preview.\n")

# SELECTS TO INVESTIGATE A SINGLE YEAR OR AN INTERVAL OF CONSECUTIVE YEARS
choose_function= input(
    "Would you like to investigate a single year or an interval of several years?"
    "\n - Choose (y) if you would like to investigate a SINGLE year"
    "\n - Choose (i) if you would like to investigate an INTERVAL of several years\n\nWrite your input: ")

while True:
    if choose_function == 'I' or choose_function == 'i':
        print( "You selected to investigate an interval of several years" )

        # SELECTS THE INTERVAL OF INTEREST
        exec(open('common_actions/2b-if_user_select_interval.py').read())

        # CREATES A LIST TO SELECT COLUMNS IN THE TABLE
        selected_years = list( range( year_input1, year_input2 ) )
        selected_years = [str( i ) for i in selected_years]
        print( "You selected to investigate the following years: " )
        print( selected_years )

        # PROCESSING TABLE ON INTERVAL OF YEARS FOR IMPORTS
        file_name = "0-Downloaded_files/imp_tiv.csv"
        exec(open('common_actions/3b-process_table_to_plot_interval.py').read())
        top_imp_values = dataset

        # PROCESSES TABLE ON INTERVAL OF YEARS FOR EXPORTS
        file_name = "0-Downloaded_files/exp_tiv.csv"
        exec(open('common_actions/3b-process_table_to_plot_interval.py').read())
        top_exp_values = dataset

        # PLOTS INTERVAL OF YEARS
        # PRODUCES DASHBOARDS WITH PLOTLY - WITH TWO OPTIONS
        dash_choice = input( '''Select the type of dashboard you would like to display: "Bar", "Polar" or "Tree": ''' )
        while True:
            if dash_choice == "Bar" or dash_choice == "bar": # This will display Dashboard with bar plot with top 20 importers and exporters for chosen
                exec(open('TIV_table_package/3b-python_tiv_plot_bar_interval.py').read())
                print( "*** Bar plot dashboard will display in your browser momentarily ***" )
                break

            elif dash_choice == "Polar" or dash_choice == "polar": # This will display Dashboard with tree map plot from user choice: (Imports or Exports)
                exec(open('TIV_table_package/4b-python_tiv_plot_polar_interval.py').read())
                print( "*** Polar map dashboard will display in your browser momentarily ***" )
                break

            elif dash_choice == "Tree" or dash_choice == "tree": # This will display Dashboard with tree map plot from user choice: (Imports or Exports)
                exec(open('TIV_table_package/5b-python_tiv_plot_treemap_interval.py').read())
                print( "*** Tree map dashboard will display in your browser momentarily***" )
                break

            else:
                print( "Not a valid selection. Please try again: ")
                dash_choice = input( '''Select the type of dashboard you would like to display: "Bar", "Polar" or "Tree": ''' )
        break

    elif choose_function == 'Y' or choose_function == 'y':
        print( "You selected to investigate a single year" )

        # SELECT THE YEAR OF INTEREST
        exec(open('common_actions/2a-if_user_select_year.py').read())

        # PROCESSING TABLE ON ONE YEAR IMPORT
        file_name = "0-Downloaded_files/imp_tiv.csv"
        exec(open('common_actions/3a-process_table_to_plot_year.py').read())
        top_imp_values = top_values

        # PROCESSING TABLE ON ONE YEAR EXPORT
        file_name = "0-Downloaded_files/exp_tiv.csv"
        exec(open('common_actions/3a-process_table_to_plot_year.py').read())
        top_exp_values = top_values

        # PLOTTING YEAR
        # PRODUCE DASHBOARDS WITH PLOTLY - TWO OPTIONS
        dash_choice = input( '''Select the type of dashboard you would like to display: "Bar", "Polar" or "Tree": ''' )
        while True:
            if dash_choice == "Bar" or dash_choice == "bar":  # Dashboard with bar plot with top 20 importers and exporters for chosen
                exec(open('TIV_table_package/3a-python_tiv_plot_bar_year.py').read())
                print( "*** Bar plot dashboard will display in your browser momentarily ***" )
                break

            elif dash_choice == "Polar" or dash_choice == "polar": # Dashboard with tree map plot from user choice: (Imports or Exports)
                exec(open('TIV_table_package/4a-python_tiv_plot_polar_year.py').read())
                print( "*** Polar map dashboard will display in your browser momentarily ***" )
                break

            elif dash_choice == "Tree" or dash_choice == "tree":  # Dashboard with tree map plot from user choice: (Imports or Exports)
                exec(open('TIV_table_package/5a-python_tiv_plot_treemap_year.py').read())
                print( "*** Tree map dashboard will display in your browser momentarily ***" )
                break
            else:
                print( "Not a valid type of dashboard. Please try again: ")
                dash_choice = input( '''Select the type of dashboard you would like to display: "Bar", "Polar" or "Tree": ''' )
        break

    else:
        print( "Not a valid selection. Please try again: ")
        choose_function = input(
               "Would you like to investigate a single year or an interval of several years?"
                "\n - Choose (y) if you would like to investigate a SINGLE year"
                "\n - Choose (i) if you would like to investigate an INTERVAL of several years\n\nEnter your choice: ")
