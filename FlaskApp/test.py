import json
userlist_dir =  'D:/PythonProject/NewSite/HiComm/FlaskApp/userlist/'
file = open(userlist_dir + 'admin')
h = json.load(file)['Level']
print(h)