A= [15,8,5,30,25,55,40]
A.sort()

print (A)

#Binary search for 25 and 8


for data in [44,8]:
    ub= len(A) -1
    lb = 0
    mid = int((ub+lb)/2)
    i,j=0,0
    while (lb <= ub):

        if (A[mid] == data):
            print (data ,"Found")
            break

        elif (data < A[mid]):
            ub= mid-1
            print ("Less Than: ", i)
            i+=1 
        elif(data > A[mid]):
            lb = mid +1
            print ("Greater than Than: ", j)
            j+=1


        if (lb > ub):
            break
        mid = int((ub+lb)/2)
