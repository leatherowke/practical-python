import email


contacts = {
    'number':'4',
    'students': 
    [
        {'name':"Sarah Holderness", 'email':'sarah@example.com'},
        {'name':'Harry Potter', 'email':'harry@example.com' },
        {'name':'Hermoine Granger', 'email':'hermoine@example.com'},
        {'name':'Ron Weesley', 'email':'ron@exapmle.com'}
        ]
    }

for student in  contacts['students']:
    print(student['email'])