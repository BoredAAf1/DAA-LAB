SPI=eval(input("Enter all SPI:"))
credits=eval(input("Enter credits of respective semesters:"))
semesters=eval(input("Enter number of semesters:"))
if(semesters!=int(semesters)):
    print("Error:Number of semesters cannot be decimal")
    exit()
if(len(credits)!=len(SPI)):
    print("Error:Number of SPI not equal to number of credits")
    exit()    
if(semesters!=len(SPI)):
    print("Error:Number of SPI not equal to number of semesters")
    exit()    
if(semesters==0):
    print("not defined")
    exit()
c_sum=0;    
while(semesters>0):
    c_sum=c_sum+SPI[semesters-1]*credits[semesters-1]
    semesters-=1
CPI=c_sum/sum(credits)    
print(CPI)

    
