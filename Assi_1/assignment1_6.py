
def chknum(no):
    if no == 0:
        print("number is Zero")
    elif no > 0:
        print("number is Positive ")
    elif no < 0 :
        print("number is Negative")



print("Enter the number");
no = int(input())
chknum(no)
