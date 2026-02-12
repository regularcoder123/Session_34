def check(list):
    result = {}
    for item in list:
        result[item[0]] = item[1:]
    return result

students = [[1,"Jimmey Cowell", "IV"],[2,"Samara Johnson","V"],[3,"Mark Rober",'VII']]

print("Orignal List")
print(students)
print("/nConverted to Dictionary")
print(check(students))