credit_dic={}#creating a dictionary
studnt_list=[]
a = 0

def prdict_score():
    Pass=0
    Defer=0
    Fail=0
    Total=0
In_range=[0,20,40,60,80,100,120]   #Validating 
counter=0
marks=0
Studnt_id=0
Studnt_list=[]
#progress_list,trail_list,retrve_list,exc_list=[],[],[],[]



boolean=True
while boolean:    
    # getting the credits and making sure they are integer values from the list[0,20,40,60,80,100,120]
    try:
        Studnt_id=str(input('Enter your student id:'))
        if (Studnt_id[0] != 'w'): 
            print("Student ID must start with a 'w'. Please try again next time.")
            continue
            
                                         
        Pass=int(input("Please Enter your credits at Pass:"))
        if (Pass not in In_range):
           print("Credits entered is 'Out of Range'")
        Defer=int(input("Please Enter your credits at Defer:"))
        if (Defer not in In_range):
            print("Credits entered is 'Out of Range'")
        Fail=int(input("Please Enter your credits at fail:"))
        if (Fail not in In_range):
           print("Credits entered is 'Out of Range'")
        else:
            Total=Pass+Defer+Fail
            if Total>120:            
                print("Total is Incorrect")
            elif(Pass==120):
                print("progress")               
                marks=f"progress-{Pass},{Defer},{Fail}"
                credit_dic[Studnt_id]=(marks)#adding progress data to dictionary
                
            elif(Pass==100):
                print("progress( module trailer )")                
                marks=f"trailer-{Pass},{Defer},{Fail}"
                credit_dic[Studnt_id]=(marks)#adding trailer data to dictionary
                                
                
            elif (Fail in (0,20,40,60)):                 
                print("Module retriever")                
                marks=f"Retriever-{Pass},{Defer},{Fail}"
                credit_dic[Studnt_id]=(marks)#adding retriever data to dictionary
                
                
            else:
                print('Exclude')               
                marks=f"Exclude-{Pass},{Defer},{Fail}"
                credit_dic[Studnt_id]=(marks)#adding exclude data to dictionary
                
                
                
            counter=counter+1

            prompt=(input("Would you like to  Enter another set of Data?,\nEnter 'y' to continue and 'q' to quit the current program and view results"))
            if (prompt=='y'):
                print('')
                continue
            elif (prompt=='q'):
                #to print the dictionary
                print('\nPART-4:')
                for x,y in credit_dic.items():
                    print(x,":",y,end=" ") 
                print()
                break
            
    except ValueError:
        print('Integer required \n')
                
                
                   

