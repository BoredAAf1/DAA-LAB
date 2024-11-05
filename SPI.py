
grades=eval(input("Enter grades:"))
credits=eval(input("Enter credits:"))
subjects=eval(input("enter number of subjects:"))
if(len(grades)!=len(credits)):
    print("Error:Number of grades not equal to credits")
    exit()
if(int(subjects)!=subjects):
    print("Error:Number of subjects cannot be decimal")
    exit()
if(subjects!=len(grades)):
    print("Error:Number of grades not equal to subjects")
    exit()
if(subjects==0):
    print("not defined")
    exit()
g_sum=0;    
while(subjects>0):
    if(grades[subjects-1]<0):
        print("Error:Grade cannot be negative")
        exit()
    g_sum=g_sum+(grades[subjects-1]*credits[subjects-1])
    subjects=subjects-1
SPI=g_sum/sum(credits)    
print(SPI)



       

