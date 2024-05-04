# EC530_Final
Logic Synthesis Engine Application

# Repo Organization
boolean_gui.py -- Contains GUI functionality

program1.py -- Contains main function as well as all sub-functions 

dist/ -- Contains tar.gz folders of the up-to-date implementation that can be downloaded for ease of use. Created when generating the Python package

# Updates
The backend of this application was first implemented in EC551 as a lab. This application was originally a terminal application, that only took files as inputs and was quite buggy. The backend was updated and has been streamlined as part of this project. The frontend GUI, unit tests/actions, and the distribution of the application are all new additions to this project as well. 

# Tool Description
This tool is an attempt to make a logic synthesis engine. It takes a boolean algebraic
expression as input and produces a variety of outputs:
1. The design as a canonical SOP
2. The design as a canonical POS
3. The design INVERSE as a canonical SOP
4. The design INVERSE as a canonical POS
5. A minimized number of literals representation in SOP
  a. The number of saved literals vs. the canonical version
6. A minimized number of literals representation in POS
  a. Report on the number of saved literals vs. the canonical version
7. The number of Prime Implicants
8. The number of Essential Prime Implicants
9. The number of ON-Set minterms
10. The number of ON-Set maxterms
11. The total number of transistors needed for the minimized SOP design
12. The total number of transistors needed for the minimized POS design
    
The tool also produces the inputted boolean expression, variable names, minterms, maxterms, and
recommends SOP or POS design based on required transistor numbers.

Essential prime implicants and prime implicants are found through the use of the Quine-
McCluskey method. An open-source Python library (shown here: https://github.com/tpircher-zz/quine-mccluskey/tree/master) 
was used to calculate the Essential Prime Implicants through the provided QM algorithm, and the 
sympy library was used for much of the boolean algebra.

# Demo
Upon start up the user will be shown this GUI:
![image](https://github.com/AidanNowa/EC530_Final/assets/98485635/5da91605-1cb1-49b0-a5db-2264977f5b5f)

The user can then enter their desired boolean expression. Due to the exponential increase in complexity with increasing variables, the current implementation supports only up to 4 different variables (A, B, C, D). The user then selects what they would like to see. Such as the Minimized SOP, Canonical SOP representation, Number of Prime Implicants, and the Number of transistors needed for the SOP design:
![image](https://github.com/AidanNowa/EC530_Final/assets/98485635/11832723-d05c-4e2b-ab5f-14fda5ad3c94)

With each button click the output is appended with the desired function. The user can than clear the output field with the 'Clear' button in the top right corner.

# How to run the program
Some libraries may need to be downloaded, such as sympy and pyeda, to run the code properly.
Ensure that input files are located in the same directory as the program.
The program can be run with the following command on windows:

**python .\boolean_gui.py**

After running the GUI should open.

The user can then enter their desired expression such as: 
`(A & B) | (~C & D) | (A & ~B) | (C & ~D)`

By pressing the corresponding buttons, the output will be printed to the screen.
The user can clear the output with the "Clear" button in the top right corner. 

# Distribution
Due to Docker containers being isolated from the host environment, utilizing the graphical display posed significant challenges.

Alternatively, the Python package in /dist offers a simpler alternative, by simply downloading and unzipping the package the user can run boolean_gui.py to spawn the GUI and use the app.

# Actions and Unit Test
Many of the functions are highly dependent upon the output of other functions. This is due to the nature of logic synthesis and the incremental approach to dismantling the inputted expression into usable subsets that are used to derive the desired outputs. 

However, for the base sub-functions unit tests were added and are automatically tested through GitHub actions whenever a push to main is made. This ensures that the application remains operational after each push.

# Collaborators 
This program was made with the assistance of ChatGPT-4 as an AI coding copilot. ChatGPT was 
used mainly for debugging/syntax and recommendations on function implementations.
  
