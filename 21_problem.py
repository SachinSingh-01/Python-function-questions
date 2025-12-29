'''Write a function student_result(name, *marks) that:
Calculates average marks
Returns:
Name
Average
Result (Pass if average ≥ 40, else Fail)'''
def student_result(name,*marks):
    total=0
    for m in marks:
        total+=m
    average=total/len(marks)
    if average>=40:
        result="Pass"
    else:
        result="Fail"
    return name,average,result
name,avg,res=student_result("Sachin Singh",67,87,54,56,88)
print(f"Name:{name}")
print(f"Average:{avg}")
print(f"Result:{res}")