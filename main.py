#Name: Brandon Teh and Daniel Murtha
#KUID: 2769066
#Subject Code: EECS 448
#Lab06
#Date Due: 4/3/2015

import sys

#Read file
file1 = file('A.csv', 'r')
file2 = file('B.csv', 'r')
#Store files in an array
filemat = [file1,file2];

#Create three arrays to store the matrices
matrix1 = []
matrix2 = []
#Store matrices in an array
matrix = [matrix1, matrix2];

#Splitting the values in the file and store them in matrices
for i in range(0,len(filemat)):
#For each line in file1
	for line in filemat[i]:
		temp = line.split(",")
		
		for j in range(0,len(temp)):
			temp[j] = float(temp[j])
	
		matrix[i].append(temp)

#Printing the matrices
for i in range(0,len(matrix)):
	s = "Matrix " + repr(i+1) + " = " + repr(matrix[i]);
	print(s)

#Check if the matrices are valid
for i in range(0,len(matrix)):
	flag = 0

	check = len(matrix[i][0])
	
	for j in range(1, len(matrix[i])):
    		check1 = len(matrix[i][j])
		
    		if check != check1:
        		flag = 1
        		break
    		else:
        		flag = 0
        
	if flag == 1:
		s = "Error. Matrix " + repr(i+1) + " is not valid.";
    		print(s)
    		sys.exit()
	else:
		s = "Matrix " + repr(i+1) + " is valid.";
    		print(s)
    		


#Function assumes the matrices are matrices
#The function will try to multiply them in the order they are passed in
#Otherwise it will decare them to have invalid dimensions
def multiply(a, b):
        if (len (a[0]) == len (b)):
                tempMtx = [[0 for i in range(len(b[0]))]for j in range(len(a))]
                for i in range(len(a)):
                        for j in range (len (b[0])):
                                for k in range (len(a[0])):
                                        tempMtx[i][j] = tempMtx[i][j] + (a[i][k]*b[k][j])
                return tempMtx
        else:
                return("Not multiplyable, invalid dimensions")

#Function assumes the matrices are matrices
#The function will try to add them in the order they are passed in
#Otherwise it will decare them to have invalid dimensions
def addMtx(a, b):
        if ((len(a) == len(b))and(len(a[0]) == len(b[0]))):
                tempMtx = [[0 for i in range(len(a[0]))]for j in range(len(a))]
                for i in range(len(a)):
                        for j in range (len (a[0])):
                                tempMtx[i][j] = a[i][j]+b[i][j]    
                return tempMtx
        else:

                return("Not addable, invalid dimensions")

                
#Function assumes the matrix is a matrix
#The function will output a matrix that represents the input matrix transposed
def transposeMtx(a):
        tempMtx = [[0 for i in range(len(a))]for j in range(len(a[0]))]
        for i in range(len(a)):
                for j in range (len (a[0])):
                        tempMtx[j][i] = a[i][j]
        return tempMtx


print("Transpose of Matrix 1 =")
#print(multiply(matrix1, matrix2))
#print(addMtx(matrix1, matrix2))
print(transposeMtx(matrix1))
