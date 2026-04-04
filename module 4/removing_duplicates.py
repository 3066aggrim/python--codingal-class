Student_data = {'id1':
                {'Student_name': ['Ghan shyam'],
                 'class': ['8'],
                 'Fav_subjects': ['Science,Coding(computer),Maths']},

                'id2':
                {'Student_name': ['Ghan shyam'],
                 'class': ['8'],
                 'Fav_subjects': ['Science,Coding(computer),Maths']},

                'id3':
                {'Student_name': ['shyam'],
                 'class': ['9'],
                 'Fav_subjects': ['Nepali,Coding(computer),H.P.E']},

                'id4':
                {'Student_name': ['Aggrim'],
                 'class': ['8'],
                 'Fav_subjects': ['Science,Coding(computer),Maths']},
                }

result = {}
for key, value in Student_data.items():
    if value not in result.values():
        result[key] = value

print(result)
