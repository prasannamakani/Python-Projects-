email=input("enter your email :")
s,c,d = 0,0,0
if len(email)>=6:
    if email[0].isalpha():
        if ("@" in email) and (email.count("@")==1):
            if email[-4]=="." or email[-3]==".":
                for i in email:
                    if i.isspace():
                        s=1
                        print("space")
                    elif i.isalpha():
                        if i==i.upper():
                            c=1
                            print("upper")
                    elif i=="." or i=="@" or  i=="_":
                        continue
                    elif i.isdigit():
                        continue
                    else:
                        d=1
                        print("another charecter")
                if s==1 or c==1 or d==1:
                    print("wrong email with capital letters or spaces or another charecter, except '.' and '_' and '@'.")                
                else:
                    print("right email")



            else:
                print("wrong email with missing '.' symbol on correct position")    
        else:
            print("wrong email with missing @ symbol")
    else:
        print("wrong email with first char is not alphabetic")  
else:
    print("wrong email with less than 6 charecters")
