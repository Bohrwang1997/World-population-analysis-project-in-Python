# Don't import any library file or module
# This is a place to submit your code for the project. 
# You are also required to attach the same code as a Python file (the name of the file should be your student ID e.g., 12345678.py). 
# Remember, your submitted code must be the same as your attached file.
# If you find errors or wrong test cases when you click check button then ensure that you remove the errors and fix the code. 
# Your submission will be thoroughly graded later after submission to ensure that it follows the project sheet guidelines. 
# Input: the file name and the region name
# output: the country name with the maximun population and minimum population in the input region with the positive net change, the average and standard diviation of countries in the input region, the density of all the countries in the input region, and the correlation coefficient of the population in all the countries in the input region
# name: Yiren Wang
# UWA ID:23794201
# Data: April 11, 2023
# creat a function called datafileread to read the file that provide
def datafileread(FIleread):

    # creat a empty list to store the data in csv file that we need
    countcsv = []

    # open the file the user input and read
    # set the opened file in the value called countrydatafile
    with open(FIleread,'r') as countrydatafile:

        # read lines in the file
        # store each lines in the file into the variable called concsv
        concsv = countrydatafile.readlines()

        # creat a for loop the read go over each line in the file
        # ignore the header
        for countryline in concsv[1:]:

            # splite the data from both side from the comma
            # ignore the blank part from the rest of the data
            data = countryline.strip().split(',')

            #store the rest of the data in the empty list
            countcsv.append(data)

    # save and print out the data in countcsv
    return countcsv

# create a function called minmaxxountries to find the maximun and minimum population in the dataset
def minmaxcountries(countcsv,region):

    # create a empty list to store the country data that has a positive net change
    # set the name of the empty list "country"
    country = []

    # use a for loop to check the data in countcsv line by line
    for countryrow in countcsv:

        # use if statement to check the region user input is match with the name in the fifth column in the data
        # use if statement to check the net change according to the region user inputted is positive
        if countryrow[5] == region and (float(countryrow[3])) > 0:

            # store the data into the empty list if it matches the information
            country.append(countryrow)

    # set the polulation in the first line to the value called popmini
    # use the midean value to compare the rest of the data to get the minimun value of population
    popmini = float(country[0][1])

    # set the polulation in the first line to the value called popmax
    # use the midean value to compare the rest of the data to get the maxmun value of population
    popmax = float(country[0][1])

    # set the country name to the value called minicountry that located in the fisrt line of the data for the further comparation
    minicountry = country[0][0]

    # set the country name to the value called maxcountry that located in the fisrt line of the data for the further comparation
    maxcountry = country[0][0]

    # create a for loop to select the country that has the greated and minimun value of population
    # set the data in the value named con
    for con in country:

        # set the poplulation column in the data to the value called pop_total
        pop_total = float(con[1])

        # check one by one if the number of in the population column is greater than the first value in the column
        if pop_total > popmax:

            # set the greater value to the popmax
            popmax = pop_total

            # change the value of maxcountry to the country that has the greater population from the result in the previous step
            maxcountry = con[0]


        # check one by one if the number of in the population column is smaller than the first value in the column
        if pop_total < popmini:

            # set the smaller value to the popmini
            popmini = pop_total

            # change the value of maxcountry to the country that has the greater population from the result in the previous step
            minicountry = con[0]

    # print and save the output of maxxountry and minicountry
    return [maxcountry,minicountry]

# set a function named denspop to calculate the average population and standard diciation in the specific region
def avespop(countcsv,region):

    # set a empty list called popu to store the value of population that match the following information
    popu = []

    # use a for loop to check the data in countcsv line by line and set the variable called popuraw
    for popuraw in countcsv:

        # use a if statement to check whether the region that the user input is in the sixth column of the data
        if popuraw[5] == region:
            
            # change the type of the value of population that matches the previous information in float
            # store the value into the empty list 
            popu.append(float(popuraw[1]))

    # calculate the average value of popilation and rount the result to four decimal places
    popuave = round(sum(popu) / len(popu), 4)

    # use the result of 
    # round the result to four decimal places
    popustvd = round(((sum([(countrypopu - popuave) ** 2 for countrypopu in popu])) / (len(popu)-1)) ** 0.5,4)

    # save and print out the result of standard deviation and average of the population
    return [popuave, popustvd]

# set a function named denspop to list the density of countries in input region with decent order
def denscountry(countcsv,region):

    # set a empty list called dens to store the value of calculated density that match the following information
    dens = []

    # use a for loop to check the data in countcsv line by line and store them in the variable called densrow
    for densrow in countcsv:

        # use a if statement to check whether the region that the user input is in the sixth column of the data
        if densrow[5] == region:

            # set the first column of data in the densrow with the variable name called countriesname
            countriesname = densrow[0]

            # set the second column of data in the densrow with the variable name called countriespopu
            countriespopu = float(densrow[1])

            # set the first column of data in the densrow with the variable name called countriesname
            countriesarea = float(densrow[4])

            # calculate the density using the data in population column and area column and store the value in densi
            # round the output in four decimal places
            densi = round (countriespopu / countriesarea, 4)

            # put the country name and its density value in a list
            # store the output in the empty list
            dens.append([countriesname,densi])

    # use for loop to re-arrange the order of the density output
    # using i to represent the number of the length in density output
    for small in range(len(dens)):

        # using j to represent the number of the length in density output
        # compare to i, j is representing the next number in the length
        for big in range(small + 1, len(dens)):

            # using if statement to compare two densities withe the adjaced countries
            if dens[small][1] < dens[big][1]:
            
                # if the second number is greater, put that at the front
                dens[small], dens[big] = dens[big], dens[small]

    # save and return the final answer of dens
    return dens

# set a function named coecor to calculate the Correlation coefficient of the countries data in the input region
def coecor(countcsv,region):

    # create an empty list to store the population data and the land area data in variables named conpop and conland
    conpopu, conland = [], []
    
    # use a for loop to check the data in countcsv line by line and store them in the variable called coerr
    for coerr in countcsv:

        # use a if statement to check whether the region that the user input is in the sixth column of the data
        if coerr[5] == region:

            # add the population value to the empty list
            conpopu.append(float(coerr[1]))

            # add the land area value to the population list   
            conland.append(float(coerr[4]))

    # calculate the mean of the population data
    meanpopu = sum(conpopu) / len(conpopu)

    # calculate the mean of the land area data
    meanland = sum(conland) / len(conland)

    # calculate the covariance of population and sum as numerator
    corvpopland = sum([(conpopu[i] - meanpopu) * (conland[i] - meanland) for i in range(len(conpopu))])

    # Calculate the variance for population  
    variancepop = sum([(countpopul - meanpopu) ** 2 for countpopul in conpopu])

    # Calculate the cariance for landarea
    varianceland = sum([(countland - meanland) ** 2 for countland in conland])

    # Calculate the correlation coefficient by dividing standard diviation from corveriance of pop
    ccpopuland = round( (corvpopland / (( variancepop * varianceland ) ** 0.5)), 4)

    # save and return the output
    return ccpopuland

# set up the main function to let user input the file name and region name
def main(csvfile, region):

    # read the input file and parse the data in the countrycsvfile function
    # store the data in the variable in the name of regiondata
    regiondata = datafileread(csvfile)

    # input data and region into the minmaxcountries function
    # set the output in the variable called MaxMin
    MaxMin = minmaxcountries(regiondata,region)

    # input data and region into the avespop function
    # set the output in the variable called stdvAverage
    stdvAverage = avespop(regiondata,region)

    # input data and region into the denscountry function
    # set the output in the variable called density
    density = denscountry(regiondata,region)
    
    # input data and region into the coecor function
    # set the output in the variable called corr
    corr = coecor(regiondata,region)

    # print out the result
    return MaxMin, stdvAverage, density, corr
    

