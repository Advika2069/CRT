def Student_Grade_System(name,n1,n2,n3):
    average = (n1+n2+n3 )/ 3
    if average >= 40:
        status = "Pass"
    else:
        status = "Fail"
    print(f"Average grade: {average: .2f},Status: {status}")
if __name__ == "__main__":
    name = input()
    n1,n2,n3 = map(int,input().split())
    Student_Grade_System(name,n1,n2,n3)
