# THIS SCRIPT IS DESIGNED AND ORGANIZED IN A WAY TO ENSURE IT
# CONTINUES ALL PROCESSES UNTIL THE OPERATOR DECIDES STOP OR ABORT.
# FOR MORE INFORMATION AND DESCRIPTIONS RELATED TO THIS CODE PLEASE
# SEE THE README.md FILE OR GO TO AND
# SEE __init__.py FILE IN EACH PACKAGE FOLDER
# THIS MODULE INITIATES THE ENTIRE PIPELINE AND IS TO BE RUN FIRST.

exec(open('TIV_table_package/__init__.py').read())
while True:
    continue_or_quit = input(
        "\nWould you like to continue to (PART TWO) the Table Visualization component, "
        "restart (PART ONE) the Dashboard component, or abort the process and quit the program? "
        "\nIf you continue, you will have the opportunity to access a more detailed table "
        "on arms trading and query and print a custom map\n"
        " - Choose (q) to QUIT THE PROGRAM\n" 
        " - Choose (c) to CONTINUE TO PART TWO"
        "(***If you haven't already done so, please activate PostGreSQL now***)\n"
        " - Choose (r) to RESTART PART ONE\n"
        "Select your input: " )
    if continue_or_quit == "q" or continue_or_quit == "Q":
        print("\n Thank you for visiting. Have a nice day\n")
        quit()
    elif continue_or_quit == "r" or continue_or_quit == "R":
        exec(open('TIV_table_package/__init__.py').read())
    elif continue_or_quit == "c" or continue_or_quit == "C":
        exec(open('Trade_register_table_package/__init__.py').read())
        while True:
            # RUNS THE SECOND PART OF THE SCRIPT
            print("\n ** YOU ARE NOW IN THE SECOND PART OF THE PROGRAM **.\n")
            continue_or_quit = input(
                "\nWould you like to continue to (PART THREE) the GEO-Visualization component, restart "
                " (PART ONE) the Dashboard component or restart (PART TWO) the Table Visualization component, "
                "\nor abort the process and quit? " 
                "If you continue, you will have the opportunity to access a more detailed table "
                "on arms trading and query and print a custom map\ny"
                " - Choose (q) to QUIT THE PROGRAM\n"
                " - Choose (r1) to RESTART PART ONE OF THE PROGRAM\n"
                " - Choose (r2) to RESTART PART TWO OF THE PROGRAM"
                "\nSelect your input: " )
            if continue_or_quit == "q" or continue_or_quit == "Q":
                quit()
            elif continue_or_quit == "r1" or continue_or_quit == "R1":
                exec(open('TIV_table_package/__init__.py').read())
                pass
            elif continue_or_quit == "r2" or continue_or_quit == "R2":
                exec(open('Trade_register_table_package/__init__.py').read())
                pass
            else:
                print( "Not a valid selection! Please try again!: " )
    else:
        print( "Not a valid selection! Please try again!: " )