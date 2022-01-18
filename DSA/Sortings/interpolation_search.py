A = [4,15,20,35,45,55,65]

A.sort()

low = 0 
high = len(A) -1 

#search 45 using interpolation
key = 45
mid = low + (high - low) * ( (key - A[low]) / (A[high] - A[low]))



print (int(mid))