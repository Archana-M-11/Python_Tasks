'''
3.Create 2 sets containing names of users who visited the website at Day-1 and Day-2
Display:
Visitors on both days.
Visitors who visited only on Day 1.
Visitors who visited only on Day 2.
Total unique visitors.
'''

day1= {"Achu", "Anu", "Revathi", "Neha"}
day2= {"Jithin", "Neha", "Arjun", "Maya","Edwin"}
print('visitors on both days : ', day1&day2)
print('visitors only on day1: ',day1-day2)
print('visitors only on day2: ',day2-day1)
print('all visitors : ',day1 | day2)