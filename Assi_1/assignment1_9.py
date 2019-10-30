def chknum(no):
    i=1
    while no>=i:
        if i %2==0:
            print(i,end=" ")
        i=i+1


print("Enter the number");
no = int(input())
chknum(no)
