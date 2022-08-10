from flask import Flask, render_template, request

app=Flask( __name__ , template_folder="templates")

emailList=[]
passwordList=[]
wholeCredentials=[]
email = ""
password = ""
firstName = ""
lastName = ""
std = ""
roll = ""
email = ""
phoneNumber = 0
place = ""
skills = ""
reason =""

authentic = ""

class Question:
    question= ""
    option1= ""
    option2= ""
    option3= ""
    option4= ""
    correct= ""
    qnum= ""

class Score:
    name= ""
    email= ""
    score= ""

class Details:
    firstName = ""
    lastName = ""
    std = ""
    roll = ""
    email = ""
    phoneNumber = 0
    place = ""
    skills = ""
    reason ="" 
    
#function to spearate username and password     
def getField(line,field): #separating username and password field
    
    storedField=""
    c=''
    idx=0
    commaFound=0   
    #storing the particular field in "storedField"
    #after certain existing commas
    while ( commaFound < field+1 and idx < len(line)):
        
        c=line[idx]
        
        if c == ',':
            commaFound+=1
        elif commaFound == field:
            storedField=storedField+c
        idx+=1    
    return storedField

def making_objects(listElement ,number):
    
    p=Question()
    p.question= getField(listElement, 0)
    p.option1= getField(listElement, 1)
    p.option2= getField(listElement, 2)
    p.option3= getField(listElement, 3)
    p.option4= getField(listElement, 4)
    p.correct= getField(listElement, 5)
    p.qnum= number
    
    return p


def making_marks(listElement):
    s= Score()
    s.name= getField(listElement , 0)
    s.email= getField(listElement , 4)
    s.score= getField(listElement , 10)
    return s

def getDet(listElement):
    det = Details()
    det.firstName = getField(listElement, 0)
    det.lastName = getField(listElement, 1)
    det.std = getField(listElement, 2)
    det.roll = getField(listElement, 3)
    det.email = getField(listElement, 4)
    det.phoneNumber = getField(listElement, 5)
    det.place = getField(listElement, 7)
    det.skills = getField(listElement, 8)
    det.reason = getField(listElement, 9)
    return det
    

@app.route("/quiz" , methods=["POST","GET"])
def quiz():
    qno = 0
    whole_quiz = []
    questions = []
    myFile=open("C:/Users/Anas/Downloads/Quiz-Web-App/Quiz-Web-App/questions.txt" , "r")
    questions = myFile.read().splitlines()
    myFile.close()
    
    for element in questions:
        qno+=1
        obj= making_objects(element, qno)
        whole_quiz.append(obj)
    
    qno=0
    return render_template("quiz.html" , array=whole_quiz)


@app.route("/")
def home():
    
    global email
    global password
    
    if email=="admin@host.local" and password == "12789":
        return render_template("admin.html")
    elif verify(email , password):
        return render_template("user.html" , var=authentic)
    return render_template("index2.html")

#return render_template("showProd.html" , list= objects_list)

@app.route("/onsignup", methods=["POST","GET"])
def submit():
    
    global email
    global password
    global firstName
    global lastName
    global std
    global roll
    global email
    global phoneNumber
    global place
    global skills
    global reason
    
    firstName=request.form.get('firstName')
    lastName=request.form.get('lastName')
    std=request.form.get('std')
    roll=request.form.get('roll')
    email=request.form.get('email')
    phoneNumber=request.form.get('phoneNumber')
    password=request.form.get('password')
    place=request.form.get('place')
    skills=request.form.get('skills').split(",")
    reason=request.form.get('reason').split()
    complete= str(firstName)+ ","+str(lastName)+ ","+str(std)+ "," +str(roll)+ "," +str(email)+ ","+str(phoneNumber)+ "," +str(password)+ ","+str(place)+ ","+("_".join(skills))+","+("_".join(reason))+"," +"0"+","+"0"+","+"0"
    
    myFile=open("C:/Users/Anas/Downloads/Quiz-Web-App/Quiz-Web-App/dataCSV.txt" , "a")
    print(complete , file= myFile , sep="\n")
    myFile.close()
    return render_template("login.html")

@app.route("/onlogin" , methods=["POST","GET"])
def userVerify():
    
    global email
    global password
    global wholeCredentials
    global authentic
    email=request.form.get('email')
    password=str(request.form.get('password'))
    
    myFile=open("C:/Users/Anas/Downloads/Quiz-Web-App/Quiz-Web-App/dataCSV.txt" , "r")
    wholeCredentials = myFile.read().splitlines()
    myFile.close()
    
    if verify(email , password):
        return render_template("user.html" , var=authentic)
    
    elif email=="admin@host.local" and password== "12789":
        return render_template("admin.html")
    return render_template("invalid.html")

    
def verify( email , pw ):
    
    emailList = []
    passwordList = []
    global authentic
    
    wholeCredentials = []
    
    myFile=open('C:/Users/Anas/Downloads/Quiz-Web-App/Quiz-Web-App/dataCSV.txt', "r")
    wholeCredentials = myFile.read().splitlines()
    myFile.close()
    
    for idx in range(0, len(wholeCredentials)):
        emailList.append(getField( wholeCredentials[idx] , 4 ))
        passwordList.append(getField( wholeCredentials[idx] , 6 ))
    
    # print(len(wholeCredentials))
    # print(len(emailList))
    # print(len(passwordList))
    
    for idx in range( 0 , len(emailList)):
        if email == emailList[idx] and pw == passwordList[idx]:
            authentic = getField( wholeCredentials[idx] , 0 )
            # print(authentic)
            return True 
    return False

@app.route("/showall" , methods=["POST","GET"])
def showll():
    
    objects_list = []
    whole= []
    myFile=open("C:/Users/Anas/Downloads/Quiz-Web-App/Quiz-Web-App/dataCSV.txt" , "r")
    whole = myFile.read().splitlines()
    myFile.close()
    num = 0
    for element in whole:
        
        obj = making_marks(element)
        objects_list.append(obj)
        
    return render_template("showall.html" , list= objects_list)

@app.route("/showdetails" , methods=["POST","GET"])
def showdet():
    
    objects_list = []
    whole= []
    myFile=open("C:/Users/Anas/Downloads/Quiz-Web-App/Quiz-Web-App/dataCSV.txt" , "r")
    whole = myFile.read().splitlines()
    myFile.close()
    num = 0
    for element in whole:
        
        obj = getDet(element)
        objects_list.append(obj)
        
    return render_template("showdetails.html" , list= objects_list)


@app.route("/addquestion" , methods=["POST","GET"])
def add_question():
    
    ques=request.form.get('question')
    op1=request.form.get('op1')
    op2=request.form.get('op2')
    op3=request.form.get('op3')
    op4=request.form.get('op4')
    cor=request.form.get('corop')
    
    complete = ques+ "," +op1+ "," +op2+ "," +op3+ "," +op4+ "," +cor
    myFile=open("C:/Users/Anas/Downloads/Quiz-Web-App/Quiz-Web-App/questions.txt" , "a")
    print(complete , file= myFile , sep="\n")
    myFile.close()
    return render_template("admin.html")
    

@app.route("/submit" , methods=["POST","GET"])
def submit_quiz():
    
    global email
    wholeCredentials = []
    
    attempts = []
    score = 0
    whole_quiz = []
    
    myFile=open("C:/Users/Anas/Downloads/Quiz-Web-App/Quiz-Web-App/questions.txt" , "r")
    questions = myFile.read().splitlines()
    myFile.close()
    number=0
    for element in questions:
        obj= making_objects(element , number)
        whole_quiz.append(obj)
    
    for idx in range(0,len(whole_quiz)):
        mcq="mcq"+str(idx+1)
        attempts.append(request.form.get(mcq))
    
    for udx in attempts:
        # print(udx)
        pass
    
    for idx in range(0,len(whole_quiz)):
        if whole_quiz[idx].correct == attempts[idx]:
            score+=1
        print(score)
    
    myFile=open("C:/Users/Anas/Downloads/Quiz-Web-App/Quiz-Web-App/dataCSV.txt" , "r")
    wholeCredentials = myFile.read().splitlines()
    myFile.close()
    
    for idx in range(0,len(wholeCredentials)):
        if email==getField(wholeCredentials[idx],4):
            wholeCredentials[idx]= str(getField(wholeCredentials[idx],0))+ ","+str(getField(wholeCredentials[idx],1))+ ","+str(getField(wholeCredentials[idx],2))+ ","+str(getField(wholeCredentials[idx],3))+ ","+str(getField(wholeCredentials[idx],4))+ ","+str(getField(wholeCredentials[idx],5))+ ","+str(getField(wholeCredentials[idx],6))+ ","+str(getField(wholeCredentials[idx],7))+ ","+str(getField(wholeCredentials[idx],8))+ ","+str(getField(wholeCredentials[idx],9))+ "," +str(score)+ "," +str(len(attempts))+ "," +str(len(whole_quiz))
    myFile=open("C:/Users/Anas/Downloads/Quiz-Web-App/Quiz-Web-App/dataCSV.txt" , "w")
    for record in wholeCredentials:
        print(record , file= myFile , sep="\n")
    
    myFile.close()

    print("Your score is:", score)
    return render_template("user.html")


@app.route("/login" , methods=["POST","GET"])
def validation():
    return render_template("login.html")


# @app.route("/show" , methods=["POST","GET"])
# def results():
    
#     global email
#     wholeCredentials = []
#     attempts = 0
#     myFile=open("dataCSV.txt" , "r")
#     wholeCredentials = myFile.read().splitlines()
#     myFile.close()
    
#     score = 0
#     print(email)
#     for result in wholeCredentials:
#         check = getField(result, 1)
#         if email == check:
#             score = str(getField(result, 3))
#             attempts = str(getField(result, 4))

#     return render_template("result.html" , var1=score, var2=attempts)

@app.route("/register" , methods=["POST","GET"])
def register():
    return render_template("register.html")

@app.route("/quizstrt" , methods=["POST","GET"])
def strt():
    return render_template("quizstrt.html")

@app.route("/contact" , methods=["POST","GET"])
def get_social():
    return render_template("contact.html")

@app.route("/add" , methods=["POST","GET"])
def add():
    return render_template("addques.html")

@app.route("/logout" , methods=["POST","GET"])
def logout():
    global email
    global password
    email = ""
    password= ""
    return render_template("index2.html")

if __name__ == "__main__":
    app.run(debug= True , host="0.0.0.0")