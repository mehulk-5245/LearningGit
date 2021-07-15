'''
----------- Expt_No : 2 ----------------

Aim             : Write a program for implementing Bit Stuffing and character stuffing.
Author          : Mehul Y Khandhadiya
Roll No         : B-55
Language        : Python 3
'''
print("Let's go")
print("--------------------------")
numm = 1
while(numm==1):
    s=list(input("Enter the text : "))
    flg = input("Enter the flag character for stuffing : ")
    flglen=len(flg)

    #Stuffing
    print("\nPerforming character stuffing...")
    streq=""
    for k in range(len(s)):
        if(s[k]==flg):
            streq+=flg
            streq+=s[k]
        else:
            streq+=s[k]
            
    streq = flg+streq+flg
    print("Text after character stuffing : ",streq)        

    #Destuffing
    print("\nPerforming character destuffing...")
    de=""
    comp=len(streq)-flglen

    while(flglen!=comp):
        if(streq[flglen]==flg):
            de+=streq[flglen+1]
            flglen+=2
        else:
            de+=streq[flglen]
            flglen+=1

    print("Text after character destuffing : ",de)
    numm = int(input("\nPress 1 if you want to continue, any other number to exit : "))


   