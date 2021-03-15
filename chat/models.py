from chat import db,login_manager
from flask_login import UserMixin

#Answer Table to store the answer of the subquestions
class Ans(db.Model):
    __tablename__ = 'ans'
    id = db.Column(db.Integer , primary_key = True, autoincrement=True)
    ans_desc = db.Column(db.String(10000) , nullable = False)

    #Method to initialize the attributes of a class
    def __init__(self, ans_desc):
        self.ans_desc = ans_desc

    #to get the output in below format while using this table in terminal only
    def __ref__(self):
        return f"chatbot_ans('{self.ans_id}' , '{self.ans_desc}')"
        

#Sub-Question Table to store the sub-questions
class Sub_ques(db.Model):
    __tablename__ = 'sub_ques'
    id = db.Column(db.Integer , primary_key = True, autoincrement=True)
    sub_ques_id = db.Column(db.Integer ,nullable = False)
    perv_ans_id = db.Column(db.Integer , db.ForeignKey(Ans.id), nullable = False)
    next_ans_id = db.Column(db.Integer , db.ForeignKey(Ans.id), nullable = False)
    sub_ques_desc = db.Column(db.String(1000) , nullable = False)
    
    #Method to initialize the attributes of a class
    def __init__(self,sub_ques_id, perv_ans_id, next_ans_id,sub_ques_desc):
        self.sub_ques_id = sub_ques_id
        self.perv_ans_id = perv_ans_id
        self.next_ans_id = next_ans_id
        self.sub_ques_desc = sub_ques_desc

    # to get the output in below format while using this table in terminal only
    def __ref__(self):
        return f"chatbot_sub_ques('{self.sub_ques_id}' , '{self.perv_ans_id}' , '{self.next_ans_id}' , '{self.sub_ques_desc}')"

#Table for User-Queries to store the user's queries
class UserQueries(db.Model, UserMixin):
    __tablename__ = 'userqueries'
    id = db.Column(db.Integer , primary_key = True, autoincrement=True)
    name = db.Column(db.String(100), nullable = False)
    email = db.Column(db.String(100), nullable = False)
    phone =  db.Column(db.String(10), nullable = False)
    query = db.Column(db.String(10000), nullable = False)
    status = db.Column(db.String(8)) 

    #Method to initialize the attributes of a class
    def __init__(self,name,email,phone,query,status = "Unsolved"):
        self.name = name
        self.email = email
        self.phone = phone
        self.query = query 
        self.status = status

@login_manager.user_loader
def load_user(id):
    return Admin.query.get(id)

#Admin Table to store the admin login credentials
class Admin(db.Model, UserMixin):
    __tablename__ = 'Admin'
    id = db.Column(db.Integer , primary_key = True, autoincrement=True)
    email = db.Column(db.String, nullable = False, unique=True)
    password = db.Column(db.String, nullable = False)

    #Method to initialize the attributes of a class
    def __init__(self,email,password):
        self.email = email
        self.password = password




