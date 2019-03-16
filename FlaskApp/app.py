from flask import Flask, render_template, request
import json
import hashlib

app = Flask(__name__)

userlist_dir =  'D:/PythonProject/NewSite/HiComm/FlaskApp/userlist/'


def CreateHash(_password):
    passStr = str(_password)
    return hashlib.sha1(passStr.encode('utf-8')).hexdigest()


def CreateUser(_name, _email,_password):
    _password = CreateHash(_password)
    data = {'name': _name,
            'Level': 'A',
            'emaile': _email,
            'password': _password}
    with open(userlist_dir+_name, 'w')as file:
        json.dump(data, file, indent=4, ensure_ascii=False)




@app.route("/showlenta")
def showlenta():
    return render_template('lenta.html')

@app.route("/showadmin")
def showadmin():
    return render_template('admin.html')




def CheckUser(_name,_password):

    try:
        file = open(userlist_dir+_name)
    except IOError as e:
        return json.dumps({'html': '<spain>Username not registrated</spain>'})
    else:
        h = json.load(file)['password']
        if h == CreateHash(_password):
            if _name =="admin":
                return render_template('admin.txt')
            else:
                return render_template('lenta.txt')
        else:
           return json.dumps({'html': '<spain>Password error</spain>'})


@app.route("/")
def main():
    return render_template('index.html')

@app.route('/showSignIn')
def showSignIn():
    return render_template('signin.html')



@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')



@app.route('/signIn', methods=['POST'])
def signIn():
    _name = request.form['inputName']
    _password = request.form['inputPassword']
    return CheckUser(_name,_password)






@app.route('/signUp', methods=['POST'])
def signUp():
    # read the posted values from the UI
########################################################
    _name = request.form['inputName']
    _email = request.form['inputEmail']
    _password = request.form['inputPassword']
########################################################
   # print ("Result " + _name + " " + _email+" "+_password)
    '''
    Данная функция считывает  значения из поля регистрации 
    и, если ник не использовался, то регестрирует пользователя
    '''
    try:
        file = open(userlist_dir+_name)
    except IOError as e:
        CreateUser(_name, _email, _password)
    else:
        #print('Пользователь был создан раньше')
        return json.dumps({'html':'<spain>Username occupied</spain>'})





    # validate the received values
    if _name and _email and _password:
        return json.dumps({'html': '<span>All fields good !!</span>'})
    else:
        return json.dumps({'html': '<span>Enter the required fields</span>'})
if __name__ == "__main__":
    app.run()
