'''
1.Create 2 sets containing studets joined in dama club andsports club
Display students in both clubs.
Display students only in the drama club.
Display students only in the sports club.
Display all students.
 '''
drama_club = {"Achu", "Anu", "Revathi", "Neha"}
sports_club = {"Jithin", "Neha", "Arjun", "Maya","Edwin"}

print('students in both clubs:')
print(drama_club & sports_club)

print('students only in the drama club:')
print(drama_club - sports_club)

print('students in only sports club:')
print( sports_club - drama_club )

print('all students:')
print(drama_club | sports_club)