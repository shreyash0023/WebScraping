import json
import csv
'''BASIC DATA ANALYTICS FOR FRIENDS'''
file_fr = open('friends.json')

dict = json.load(file_fr)

total_friends = len(dict['friends'])
list_men = []
list_women = []

for x in dict['friends']:
    if(x['name'].split()[0].endswith('i') or x['name'].split()[0].endswith('a') or x['name'].split()[0].endswith('l')):
        list_women.append(x['name'].split()[0])
    else:
        list_men.append(x['name'].split()[0])

#print(list_women)  #Uncomment to print the list of women in your friend list
#print(len(list_women))  #Uncomment to print the number of women in your friend list
#print(list_men)  #Uncomment to print the list of men in your friend list
#print(len(list_men)) #Uncomment to print the number of men in your friend list
'''Men to Women Ratio'''
print(len(list_men)/len(list_women))
file_fr.close()
'''CONTACT NUMBER ANALYTICS FOR FRIENDS'''

file_con = open('your_address_books.json')
add_dict = json.load(file_con)


contact_info = open('contact_info.csv','a')
writer = csv.writer(contact_info)
writer.writerow(['Name','Contact Number'])

for x in add_dict['address_book']['address_book']:
    if 'details' in x:
        for y in x['details']:
            print(x['name'],y['contact_point'])
            writer.writerow([x['name'],str(y['contact_point'])])

file_fr.close()