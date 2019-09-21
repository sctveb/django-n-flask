from flask import Flask, render_template, request, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import *

app = Flask(__name__)

# DB 설정
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql:///todos'
app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False
db.init_app(app)
migrate = Migrate(app,db)

@app.route('/')
def index():
    todos = Todo.query.all()
    # todos = Todo.query.filter(Todo.deadline > datetime.datetime.now()).order_by(Todo.deadline.asc()).all()
    # todo = todos_1.query.order_by(Todo.deadline.asc()).all()
    return render_template('index.html',todos=todos)
    
@app.route('/todos/new')
def new():
    return render_template('new.html')
    
@app.route('/todos/create', methods=['POST'])
def create():
    title = request.form.get('title')
    content = request.form.get('content')
    deadline = request.form.get('deadline')
    todo = Todo(title=title, content=content, deadline=deadline)
    db.session.add(todo)
    db.session.commit()
    return render_template('create.html', todo=todo)
    
@app.route('/todos/<int:id>')
def read(id):
    todo = Todo.query.get(id)
    return render_template('read.html',todo=todo)

@app.route('/todos/<int:id>/edit')
def edit(id):
    todo = Todo.query.get(id)
    return render_template('edit.html', todo = todo)
    
@app.route('/todos/<int:id>/update', methods=['POST'])
def update(id):
    todo = Todo.query.get(id)
    todo.title = request.form.get('title')
    todo.content = request.form.get('content')
    todo.deadline = request.form.get('deadline')
    db.session.commit()
    return redirect('/todos/{}'.format(todo.id))
    
@app.route('/todos/<int:id>/delete')
def delete(id):
    todo = Todo.query.get(id)
    db.session.delete(todo)
    db.session.commit()
    return redirect('/')
    
@app.route('/todos/keyboard')
def keyboard():
    keyboard = {
        "type":"buttons",
        "buttons":["긴급","투두"]
    }
    return jsonify(keyboard)

@app.route('/todos/message', methods=['POST'])
def message():
    user_msg = request.json['content']
    if user_msg == "긴급":
        todo_now = Todo.query.filter(Todo.deadline >= datetime.datetime.now().strftime('%Y-%m-%d')).order_by(Todo.deadline.asc()).first()
        msg = todo_now.title + " | " + str(todo_now.content) + " | " + str(todo_now.deadline)
        return_dict = {'message':{'text':msg},
    'keyboard':{"type":"buttons","buttons":["긴급","투두"]}}       
        return jsonify(return_dict)
    elif user_msg == "투두":
        return_dict = {'message':{'text':'인덱스입니다', 'message_button':{'label':'링크입니다','url':'http://flask001-sctveb.c9users.io:8080/'}},
    'keyboard':{"type":"buttons","buttons":["긴급","투두"]}}
        return jsonify(return_dict)
# - "긴급" : deadline이 가장 가까운 todo 응답

# - "투두" : 해야 할 일 목록 인덱스 페이지 링크 버튼 전송