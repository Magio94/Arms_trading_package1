# CHOOSES THE NUMBERS FOR THE RANGE OF THE INTERVAL

while True:
    try:
        print("\nYou chose to investigate an interval of several years. The program will ask you to\n"
              "input two values for the interval you would like to investigate.\n\n"
              "The first number you choose must be smaller than the second.")
        year_input1 = int( input( "\nEnter the first year of interest for the interval range (1950 to 2019): " ) )
        year_input2 = int( input( "\nEnter the second year of interest for the interval range (1950 to 2019). "
                                  "It must be greater than the first: " ) )
        if year_input1 in range(1950, 2020) and year_input2 in range(1950, 2020) and year_input1 < year_input2:
            break
    except:
        print("\nError: Numbers are the only valid inputs. Please try again: ")
    if year_input1 > year_input2:
        print("\nThe second input must be greater than the first. Please try again. ")
    else:
        print("\nThe year you selected is not in the data's range. Please try again. ")



