s=[]
class std:
    pass
class exam:
    d={}
    a={}
    scnt=2000
    created=0
class staff:
    def sflogin():
        while True:
            print("\t1.Create Exam\n\t2.Student Info\n\t3.Report\n\t4.Logout")
            x=input()
            if x=='1':
                if(exam.created==0):
                    nq=int(input("Enter the no of questions:\n"))
                    for i in range(nq):
                        print("Enter the question no",i+1)
                        q=input()
                        print("Enter the options:\n")
                        op=[]
                        op.append(input())
                        op.append(input())
                        op.append(input())
                        exam.d[q]=op
                        print("Enter the answer:\n")
                        exam.a[q]=(input())
                        exam.created=1
                else:
                    print("Exam already created")
            elif x=='2':
                if exam.scnt<=2000:
                    print("NO student found!................")
                else:
                    for i in range(len(s)):
                        print(s[i].name,i+2000,s[i].mark,s[i].report)
            elif x=='3':
                if exam.scnt<=2000:
                    print("NO student found!................")
                else:
                    for i in s:
                        print(i.name,i.report)
            else:
                break

def stdlogin(rn):
    while True:
        print("\t1.Attend Exam\n\t2.Report\n\t3.Logout")
        n=input()
        if n=='1':
            if(s[rn].attend==0):
                if len(exam.d):
                    qns=list(exam.d.keys())
                    ops=list(exam.d.values())
                    for j in range(len(qns)):
                        print("Question",j+1," is: "+qns[j])
                        print("OPtions: ",end='')
                        print(*ops[j],sep='\n\t')
                        print("ENter the answer:\n\t")
                        ans=input()
                        s[rn].attend=1
                        if exam.a[qns[j]]==ans:
                            s[rn].mark+=5
                    if s[rn].mark>=((len(exam.d)*5)//2):
                        s[rn].report="Pass"
                    else:
                        s[rn].report="Fail"
                else:
                    print("Exam not started yet..........")
            else:
                print("Test attended already")
        elif n=='2':
            print(s[rn].report)
        else:
            break
def __main__():
    print("T4TEQ EXAM\n")
    while True:
        print("Login as\n\t1.Staff\n\t2.Student\n\t3.Exit")
        n=input()
        if n=='1':
            staff.sflogin()
        elif n=='2':
            while True:
                print("\t1.Sign in\n\t2.Sign up\n\t3.Logout")
                x=input()
                if x=='1':
                    rgn=int(input("Enter the register number:\n"))
                    if rgn<2000 or rgn-2000>=len(s):
                        print("NO student found")
                    else:
                        pwd=input("ENter the password:\n")
                        if s[rgn-2000].ps==pwd:
                            stdlogin(rgn-2000)
                elif x=='2':
                    s.append(std())
                    s[exam.scnt-2000].name=input("Enter your name:\n")
                    s[exam.scnt-2000].ps=input("create password:\n")
                    s[exam.scnt-2000].mark=0
                    s[exam.scnt-2000].report="Not attended"
                    s[exam.scnt-2000].attend=0
                    print("Your reg no is : ",exam.scnt)
                    exam.scnt+=1
                else:
                    break
        else:
            break
__main__() 
