def bubble(samplearray =[99,76,2,7,90]):
   for i in range(len(samplearray)):
       for j in range(len(samplearray)-1):
           if samplearray[j]>samplearray[j+1]:
               samplearray[j],samplearray[j+1]=samplearray[j+1],samplearray[j]
   return samplearray
YourArray =[]   #Enter Your Array Here
print(bubble(YourArray))

