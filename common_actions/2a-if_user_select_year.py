#ENSURES THE INPUT YEAR IS IN THE DATA'S RANGE
while True:
    try:
        year_input = int( input( "Enter year of interest (1950 to 2019): " ) )
        if year_input in range(1950, 2020):
            break
    except:
        print("Error: Numbers are the only valid inputs. Please try again. ")
    else:
        print("The year you selected is not in the data's range. Please try again. ")


