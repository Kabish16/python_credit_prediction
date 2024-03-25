#author name - Kabishgarr kanagaram
#date - 12/10/2022
#purpose- predicting credit score results and displaying it in a text file

#========PART_1 ,PART_2 , PART_3 ,=======================

#opening the txt file 'credits'
creditfile=open('credits.txt','w')
creditfile.write("PART-3:\n")
#creating a function (user defining)
def prdict_score():
    Pass=0
    Defer=0
    Fail=0
    Total=0
In_range=[0,20,40,60,80,100,120]   #Validating 
prog_count=0
Trail_count=0
ret_count=0
exc_count=0
counter=0
marks=0
progress_list,trail_list,retrve_list,exc_list=[],[],[],[]

boolean=True

while boolean:
    
    # getting the credits and making sure they are integer values from the list[0,20,40,60,80,100,120]
    try:
        Pass=int(input("Please Enter your credits at Pass:"))
        if (Pass not in In_range):
           print("Credits entered is 'Out of Range'")
        Defer=int(input("Please Enter your credits at Defer:"))
        if (Defer not in In_range):
            print("Credits entered is 'Out of Range'")
        Fail=int(input("Please Enter your credits at fail:"))
        if (Fail not in In_range):
           print("Credits entered is 'Out of Range'")
        else:       #checking the credits entered whether it is progress, module trailer, module retriever or exclude
            Total=Pass+Defer+Fail
            if Total>120:            
                print("Total is Incorrect")
            elif(Pass==120):
                print("progress")
                prog_count=prog_count+1
                marks=f"progress-{Pass},{Defer},{Fail}"
                progress_list.append(marks)
                creditfile.write(str(marks[0:])+'\n')
                
            elif(Pass==100):
                print("progress( module trailer )")
                Trail_count=Trail_count+1
                marks=f"trailer-{Pass},{Defer},{Fail}"
                trail_list.append(marks)
                creditfile.write(str(marks[0:])+'\n')
                
            elif (Fail in (0,20,40,60)):                 
                print("Module retriever")
                ret_count=ret_count+1
                marks=f"Retriever-{Pass},{Defer},{Fail}"
                retrve_list.append(marks)
                creditfile.write(str(marks[0:])+'\n')
            else:
                print('Exclude')
                exc_count=exc_count+1
                marks=f"Exclude-{Pass},{Defer},{Fail}"
                exc_list.append(marks)
                creditfile.write(str(marks[0:])+'\n')
                
            counter=counter+1    
  # Prompting the user whether they want to continue or quit and see the results
            prompt=(input(" Would you like to  Enter another set of Data?,\nEnter 'y' to continue and 'q' to quit the current program and view results (Histogram)"))
            if (prompt=='y'):
                    print('')
                    continue
                # Displaying the histogram 
            else:
                print('----------------------------------------------------------------')
                print('HISTOGRAM')
                print('Progress',prog_count,' :',"*"*prog_count)
                print('Trailer',Trail_count,'  :',"*"*Trail_count)
                print('Retriever',ret_count,':',"*"*ret_count)
                print('Excluded',exc_count,' :',"*"*exc_count)
                print(counter,'outcomes in total')
#printing the values (marks) stored in each list using for loop
                print('PART-2')
                for i in progress_list:
                    print(i,end="")
                    print()
                for i in trail_list:
                    print(i,end="")
                    print()
                for i in retrve_list:
                    print(i,end="")
                    print()
                for i in exc_list:
                    print(i,end="")
                    print()
                print()
                creditfile=open('credits.txt','r')
                print(creditfile.read())
                break
    except ValueError:
        print("Integer Reqired")
creditfile.close()        
#closing the text file

        
