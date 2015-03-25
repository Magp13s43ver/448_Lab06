#Name: Brandon Teh
#KUID: 2769066
#Subject Code: EECS 448
#Lab06
#Date Due: 4/3/2015

#Read file
file1 = file('A.csv', 'r')
file2 = file('B.csv', 'r')

#Create two arrays to store the matrix
matrix1 = []
matrix2 = []

#For each line in file1
for line in file1:
	temp = line.split(",")
	
	for i in range(0,len(temp)):
		temp[i] = float(temp[i])
	
	matrix1.append(temp)
print(matrix1)

#For each line in file2
for line in file2:
	temp = line.split(",")
	
	for i in range(0,len(temp)):
		temp[i] = float(temp[i])
	
	matrix2.append(temp)
print(matrix2)


#function assumes the matricies are matricies
#the funciton will try to multiply them in the order they are passed in
#otherwise it will decare them to have invalid dimensions
def multiply(a, b):
        if (len (a[0]) == len (b)):
                tempMtx = [[0 for i in range(len(b[0]))]for j in range(len(a))]
                for i in range(len(a)):
                        for j in range (len (b[0])):
                                for k in range (len(a[0])):
                                        tempMtx[i][j] = tempMtx[i][j] + (a[i][k]*b[k][j])
                return tempMtx
        else:
                print("Not multiplyable, invalid dimensions")
