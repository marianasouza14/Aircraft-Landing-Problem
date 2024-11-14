# ##############################################################
# Aircraft landing
# Analytical Decision Support Systems - Practical Assignment 
# Rojan Aslani, Farzam Salimi, Luis Henriques 
# December 2022
# ##############################################################
# This .py file does the following: 
# 1. reads text file
# 2. organizes it 
# 3. creates and export an excel file containing the organized data 
# 
# For 13 data files used for this project
# * the input files must be placed in the input folder 
# * the output files will be generated in the output folder
# ##############################################################

import pandas as pd

for x in range(1,14): # for all text files files

    print('Processing airland'+str(x)+'...')

    inputfile = 'C:\\Users\\mariana.souza\\Documents\\ALP\\airland\\airland' + str(x) + '.txt'

    #1. Open the files

    with open(inputfile) as f:
        lines = f.readlines()

    #2. Organizing .txt files
    #
    
    test_list = []
    for i in range (len(lines)):
        blah = lines[i].split() 
        test_list.append(blah)

    resultList = sum(test_list, []) # put all values in the same list (not lists in lists)

    # change to int - eventhough the costs are float, they are always int vlaues in the files we have
    resultList = list(map(float, resultList))

    # values to dataframes
    #P = number of planes
    
    P = int(resultList[0]) 
    

    df1 = pd.DataFrame(columns = ["P", "freeze_time"])
    df1.loc[0] = [resultList[0], resultList[1]]
    pos = 1+1 #current position = 2

    # we have 6 variables for each plane (appearanceT	eLandingT	tLandingT lLandingT	penaltyBef	penaltyAft) for each plane, and a separation time matrix
    df2 = pd.DataFrame(columns=['appearanceT', 'eLandingT', 'tLandingT', 'lLandingT', 'penaltyBef', 'penaltyAft'])
    sep_df = pd.DataFrame(columns=range(P))

    for n in range (P):
        # 6 variables
        row = []
        for n in range(pos, pos+6): #6 is the number of variables
            row.append(resultList[n])
            pos = n+1
        df2.loc[len(df2)] = row

        # separation time
        row = []
        for n in range(pos, pos+P):
            row.append(resultList[n])
            pos = n+1
        sep_df.loc[len(sep_df)] = row

    #### 3. Create and export Excel file with the data
    results = 'C:\\Users\\mariana.souza\\Documents\\ALP\\results\\airland' + str(x) + '.xlsx'
    writer = pd.ExcelWriter(results, engine='xlsxwriter')

    df1.to_excel(writer, sheet_name='Sheet1',
                startrow=0, startcol= 0, header=True, index=False)

    df2.to_excel(writer, sheet_name='Sheet1',
                startrow=0, startcol= 2, header=True, index=False)

    sep_df.to_excel(writer, sheet_name='Sheet1',
                startrow=0, startcol= 8, header=True, index=False)

    writer.close()

print('End - All txt files are converted to xlsx.')