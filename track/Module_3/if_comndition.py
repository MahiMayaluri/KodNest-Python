marks = int(input("Enter the marks:"))
attendence = int(input("Enter the attendence percentage:"))
status = input("Enter the status:")
if marks >= 60 and attendence >= 75:
    if status == "yes":
        print("Eligible")
    else:
        print("Not Eligible")
else:
    print("Not Eligible") 
      
