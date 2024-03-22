# Exception : event detected during execution that interrupt the flow of a program

try:
    numerator = int(input("Enter the number to divide : "))
    denominator = int(input("Enter the number to divide by: "))
    ans = numerator/denominator
    print(ans)
except Exception:
    print("Somthing Went wrong")