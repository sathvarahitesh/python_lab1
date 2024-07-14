#3. Create a Marksheet for 5 subjects and calculate total, average and grade with if else.
a=int(input("Enter the c# mark:"))
b=int(input("Enter the os mark:"))
c=int(input("Enter the seo mark:"))
d=int(input("Enter the java mark:"))

total = a + b + c + d
pre = total/4

print("---------------------------marksheet------------------------------------------------------------")
print("\n subject \t\t\t total mark \t\t\t\t\t Obtain mark \t")
print("------------------------------------------------------------------------------------------------")
print("\n c# \t\t\t\t 100 \t\t\t\t\t\t ",a)
print("\n os \t\t\t\t 100 \t\t\t\t\t\t ",b)
print("\n seo \t\t\t\t 100 \t\t\t\t\t\t ",c)
print("\n java \t\t\t\t 100 \t\t\t\t\t\t ",d)
print("------------------------------------------------------------------------------------------------")
print("\n total mark \t\t\t 400 \t\t\t\t\t ",total)
print("------------------------------------------------------------------------------------------------")
print("\n persentage \t\t\t\t  \t\t\t\t ",pre)

if(pre>90):
    print("A gread")
elif(pre>80 and pre<90):
    print("B gread")
elif(pre>70 and pre<80):
    print("C gread")
elif(pre>60 and pre<70):
    print("D gread")
elif(pre>50 and pre<60):
    print("F gread")
elif(pre>40 and pre<50):
    print("E gread")
else:
    print("Error")
        

