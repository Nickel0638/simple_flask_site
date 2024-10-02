from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Python_Projects/new_flask/instance/newFlask.db'
db = SQLAlchemy(app)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(300), nullable=False)
    text = db.Column(db.Text, nullable=False)

menu = ['Установка','Первое приложение','Обратная связь']

@app.route('/')
def index():
    return render_template("index.html", title="New Site", menu=menu)

@app.route('/posts')
def posts():
    posts = Post.query.all()
    return render_template('posts.html', posts=posts)

@app.route('/create', methods=['POST', 'GET'])
def create():
    if request.method == 'POST':
        title = request.form['title']
        text = request.form['text']

        post = Post(title=title, text=text)

        try:
            db.session.add(post)
            db.session.commit()
            return redirect('/')
        except:
            return 'При добавлении статьи произошли ошибка.'
    else:
        return render_template('create.html')

if __name__ == "__main__":
    # Создаем контекст приложения для работы с базой данных
    with app.app_context():
        db.create_all() # Эта команда создаст все таблицы в БД
        print("----------Data Base and sheets created-----------")

    app.run(debug=True)
