'''Write a function student_info(**data) that prints:
Name: <name>
Age: <age>
Course: <course>
Pass the values using keyword arbitrary arguments.'''
def student_info(**data):
    print(f"Name: {data['name']}")
    print(f"Age: {data['age']}")
    print(f"Course: {data['course']}")

student_info(name="Sachin Singh", age=12, course="BCA")
