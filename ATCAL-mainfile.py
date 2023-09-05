
# EXAMPLES RETRIEVING FUNCTION

def examples(word):

    with open("ATCAL_implementation\examples.txt","r") as file:
        
        flag=False

        for line in file:

            if flag:

                return(line)
                
            if word in line:

                flag=True
        return None
    
# START OF THE ALGORITHM IMPLEMENTATION THROUGH NESTED IF-ELIF-ELSE STATEMENTS


first_question=input("Do you want use and distribution control on your new technology? ").lower() 

if first_question=="yes":   #for the second question

    second_question=input("Do you want to allow use on non-OSS? ").lower()

    if second_question=="yes": #for the third question

        third_question=input("Do you want copyright? ").lower()

        if third_question=="yes":

            print(f"You should use EULA. It comes in three versions: EULA FREEWARE (used for{examples('FREEWARE')})"+
                  f", EULA SHAREWARE (used for {examples('SHAREWARE')})"+
                  f", EULA COMMERCIAL (used for{examples('COMMERCIAL')}).")

        elif third_question=="no": #for the fourth question

            fourth_question=input("Do you want to implement reciprocity? ").lower()

            if fourth_question=="yes":

                print(f"You can use three different licenses: Apache (used for{examples('APACHE')})"+
                      f", LGPL (used for {examples('LGPL')})"+
                      f", Artistic (used for{examples('ARTISTIC')}).")
                
            elif fourth_question=="no":

                print(f"You can use EPL, CDDL, MPL (used for{examples('EPL_CDDL_MPL')})") 
            
            else:

                print("The answer can only be yes or no")

        else:

            print("The answer can only be yes or no")

    elif second_question=="no":

        print(f"You should use GPL (used for {examples('GPL')})")

    else:

        print("The answer can only be yes or no")

elif first_question=="no":

    print(f"You should use Public Domain (used for {examples('public_domain')})"+ 
          f", MIT/X11 (used for {examples('MIT_X11')})"+
          f", or BSD/Academic (used for {examples('BSD_Academic')})")
    
else:

    print("The answer can only be yes or no")
