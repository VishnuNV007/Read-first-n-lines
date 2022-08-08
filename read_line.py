F1= open("C:\Users\Win 10\Desktop","r")
n= int(input("How Many Lines you want to Display"))
if n<=0:
    print("Kindely Enter +ve Integer Value")
else:
    for i in range(1,n+1):
        line= F1.readline()
        print(line)  
        