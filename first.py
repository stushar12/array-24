import sys

n=int(input("Enter number of elements of array1"))
print("Enter elements :")
arr=[]
for i in range(0,n):
        z=int(input())
        arr.append(z)


m=int(input("Enter number of elements of array2"))
print("Enter elements :")
arr1=[]
for i in range(0,m):
        z=int(input())
        arr1.append(z)


arr.sort()
arr1.sort()

first=0
second=0
minimum=sys.maxsize
diff=0
while(first<n and second<m):
        if(arr[first]>=arr1[second] ):
                diff=arr[first]-arr1[second]
                second=second+1

        else:
                diff=arr1[second]-arr[first]
                first=first+1


        
        if(diff<minimum and diff>=0):
                minimum=diff


print("Minimum Difference is :",minimum)   



