"""
Full name: Nguyen An Hung Doan
Emaik: h.doan@tcu.edu
Position applied: Graduate Leadership Program - Data & Technology
Date: 02/04/2022
Note: The following program solves the CSV Combiner challenge.
    I developed this program on a Windows 10 computer and
    used Anaconda/Window command line interface to execute the program.

    Instead of using the original command line to run, please use the following:
        python csv-combiner-Doan.py accessories.csv clothing.csv household_cleaners.csv > combined.csv
    
    I already included the 'fixtures' folder name in the sourcePath (line 44)
    Assumption: the default output file head will have: "email_hash", "category", "filename"

Solution:
    - Read file names from commandline into a list of file names
    - For each file:
        + Create a temporary column with the same height as the dataset
        + Fill the temporary column with the name of the original file
        + Attach the column to the main dataset
        + Print the dataset to the stdOut
"""
# Importing the libraries
import sys #for stdin and stdout
import os.path as path
import numpy as np
import pandas as pd 

DIR = path.abspath(path.dirname(__file__)) #getting the absolute path of the parent folder
argLen = len(sys.argv) - 1 #numbers of files from command line
argList = [] #list of file names

#appending each file name to file list
for iCMD in range (len(sys.argv)):
    argList.append(sys.argv[iCMD]) 
argList.pop(0) #remove the source file name

#Function to chekc if any file path is wrong
def checkFilePath (argList):
    result = True
    #Loop through this argument list and validate file path
    for i in range (len(argList)):
        sourcePath = path.join(DIR,'fixtures', argList[i])
        if (not path.exists(sourcePath)):
            print ("File is not valid!" + sourcePath)
            result = False        
    return result

#Process input data
def printOutPut(numberOfFiles, fileList):
    print ("\"email_hash\",\"category\",\"filename\"")
    for iArgL in range (numberOfFiles):
        sourcePath = path.join(DIR,'fixtures', fileList[iArgL])
        dataset = pd.read_csv (sourcePath)
        dataLen = len(dataset.axes[0])
            
        fileNCol = [] #last column to hold file names
        for i in range (dataLen):
            fileNCol.append(fileList[iArgL]) #prefill the last column by the name of the file.
        lastCol = np.array(fileNCol)    #convert the last column to numpy array
        lastCol = np.reshape (lastCol,(lastCol.size,1)) #covert the column to 2D array
        temp = dataset.iloc[:,:].to_numpy()     #convert the whole data set to 2D numpy array
        temp = np.append(temp,lastCol,axis=1)   #Append the last column to the dataset
        #printing the output to STD out
        for xItem in temp:
            print ("\""+xItem[0]+"\"" + ',' + "\""+xItem[1]+"\"" + ','+ "\""+xItem[2]+"\"")

def main():
    if (checkFilePath (argList)):
        #parsing the arguments from command line.
        printOutPut(argLen, argList)
    else:
        print("Error in reading files!")
    

if __name__ == '__main__':
    main()


'''
#In case we dont specify the target file in the commandline.
#This approach will use the csv library in python to write directly 
#to the desired file. In following code, I am printing results to out.csv

import csv #to write to CSV files
outFileName = 'out.csv'

with open(path.join(DIR, outFileName), 'w',newline='', encoding='utf-8') as fh:
        writer = csv.writer(fh, doublequote=False, escapechar='\\', quoting=csv.QUOTE_ALL)
        writer.writerow(['email_hash', 'category', 'filename'])
        for iArgL in range (argLen):
            sourcePath = path.join(DIR,'fixtures', argList[iArgL])
            dataset = pd.read_csv (sourcePath)
            dataLen = len(dataset.axes[0])
        
            fileNCol = []
            for i in range (dataLen):
                fileNCol.append(argList[iArgL])
            lastCol = np.array(fileNCol)
            lastCol = np.reshape (lastCol,(lastCol.size,1))
            temp = dataset.iloc[:,:].to_numpy()
            temp = np.append(temp,lastCol,axis=1)
            for xItem in temp:
                writer.writerow(xItem)
                
            
#if we want to combine every file and print to the outfile at once, the we 
# loop through all the file and concatenate it to the data set.
# This approach will save performance time but will take a lot of space/memory.
#            X = None
#            if X is None:
#                X = temp
#            else:
#                X = np.concatenate((X, temp), axis=0)

'''





