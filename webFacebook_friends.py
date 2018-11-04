import json

file_fr = open('friends.json')
print(file_fr)
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