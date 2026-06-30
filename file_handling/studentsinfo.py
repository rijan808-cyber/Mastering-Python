def storestudentsdetails():
    i = 1
    f = open('studentsdetails.txt','a')
    while True:
        name = input(f"Enter Student {i} name: ")
        age = int(input(f"Enter Student {i} age: "))
        id = int(input(f"Enter Student {i} id: "))
        email = input(f"Enter Student {i} email: ")
        contact = int(input(f"Enter Student {i} contact: "))
        fees = float(input(f"Enter Student {i} fees: "))
        print()

        f.write(f'{id} | {name} | {age} | {email} | {contact} | {fees} \n')

        i = i+1

        option = input('Do you want to add more details? [yes/no]: ')
        if option.lower() == 'no':
                break
    f.close()

def readstudentdetails():
    f = open('studentsdetails.txt')
    data = f.readlines()
    for line in data:
        print(line, end='')
    f.close()

def search_by_id():
    f = open('studentsdetails.txt')
    data = f.readlines()
    ids=int(input("Enter Students ID for search: "))
    for line in data:
        id, name, age, email, contact, fees = line.split('|')
        if int(id) == ids:
            print(f'Student Name: {name}')
            print(f'Student ID: {id}')
            print(f'Student Age: {age}')
            print(f'Student Contact: {contact}')
            print(f'Student Email: {email}')
            print(f'Student Fees: {fees}')
            break
    else:
        print("Student Not Found")
    f.close()

search_by_id()