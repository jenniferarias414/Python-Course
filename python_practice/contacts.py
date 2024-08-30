contacts = {
    'number': 4,
    'students':
    [
        {'name': 'Jenny Arias', 'email': 'jenny@jenny.com'},
        {'name': 'India Arias', 'email': 'indi@indi.com'},
        {'name': 'Corbin Arias', 'email': 'corb@corb.com'},
        {'name': 'Pam Stockero', 'email': 'pstockero@yahoo.com'}
    ]
}

print('Student emails:')
for student in contacts['students']:
    print(student['email'])