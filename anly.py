from flask import Flask, render_template, request, redirect, url_for, Response
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')  
import io
from flask_login import UserMixin, LoginManager, login_user, login_required, logout_user
from flask_migrate import Migrate
from werkzeug.security import generate_password_hash, check_password_hash
import os


app = Flask(__name__)

# いったんランダム、本番で書き換える
app.config["SECRET_KEY"] = os.urandom(24)

login_manager = LoginManager()
login_manager.init_app(app)

dt_info = {
    'user':'haruto',
    'password':'Ha-ru-811',
    'host':'localhost',
    'database':'webapp_vb'
}
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://{user}:{password}@{host}/{database}'.format(**dt_info)
db = SQLAlchemy(app)

migrate = Migrate(app, db)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    day = db.Column(db.DateTime, nullable=False)
    match_name = db.Column(db.String(100), nullable=False)
    reflect = db.Column(db.String(500))
    all_attack = db.Column(db.Integer, nullable=False)
    score_attack = db.Column(db.Integer, nullable=False)
    miss_attack = db.Column(db.Integer, nullable=False)
    block_attack = db.Column(db.Integer, nullable=False)
    all_serve = db.Column(db.Integer, nullable=False)
    score_serve = db.Column(db.Integer, nullable=False)
    miss_serve = db.Column(db.Integer, nullable=False)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50),nullable=False, unique=True)
    password = db.Column(db.String(200),nullable=False)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/signup', methods = ['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        hashed_pass = generate_password_hash(password)
        user = User(username = username, password = hashed_pass)
        db.session.add(user)
        db.session.commit()
        return redirect('/')
    else:
        return render_template('signup.html')
    
@app.route('/', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username = username).first()
        if check_password_hash(user.password, password=password):
            login_user(user)
            return redirect('/index')
        else:
            return redirect('/', msg = 'ユーザー名かパスワードが違います')
    else:
        return render_template('login.html', msg = '')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/')





@app.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    if request.method == 'GET':
        posts = Post.query.order_by(Post.day).all()
        return render_template('index.html', posts=posts)
    
    else:
        day = request.form.get('day')
        match_name = request.form.get('match_name')
        reflect = request.form.get('reflect')
        all_attack = request.form.get('all_attack')
        score_attack = request.form.get('score_attack')
        miss_attack = request.form.get('miss_attack')
        block_attack = request.form.get('block_attack')
        all_serve = request.form.get('all_serve')
        score_serve = request.form.get('score_serve')
        miss_serve = request.form.get('miss_serve')
        
        day = datetime.strptime(day, '%Y-%m-%d')
        new_post = Post(
            day = day,
            match_name = match_name,
            reflect = reflect,
            all_attack = int(all_attack),
            score_attack = int(score_attack),
            miss_attack = int(miss_attack),
            block_attack = int(block_attack),
            all_serve = int(all_serve),
            score_serve = int(score_serve),
            miss_serve = int(miss_serve)
            )
        
        db.session.add(new_post)
        db.session.commit()
        return redirect('/index')


@app.route('/write')
@login_required
def write():
    return render_template('write.html')

@app.route('/reflect/<int:id>')
@login_required
def reflect(id):
    post = Post.query.get(id)

    return render_template('reflect.html', post=post)

@app.route('/delete/<int:id>')
@login_required
def delete(id):
    post = Post.query.get(id)

    db.session.delete(post)
    db.session.commit()
    return redirect('/index')

@app.route('/update/<int:id>', methods=['GET', 'POST'])
@login_required
def update(id):
    post = Post.query.get(id)
    if request.method == 'GET':
        return render_template('update.html', post=post)
    else:
        post.day = datetime.strptime(request.form.get('day'), '%Y-%m-%d')
        post.match_name = request.form.get('match_name')
        post.reflect = request.form.get('reflect')
        post.all_attack = request.form.get('all_attack')
        post.score_attack = request.form.get('score_attack')
        post.miss_attack = request.form.get('miss_attack')
        post.block_attack = request.form.get('block_attack')
        post.all_serve = request.form.get('all_serve')
        post.score_serve = request.form.get('score_serve')
        post.miss_serve = request.form.get('miss_serve')

        db.session.commit()
        return redirect('/index')
    
@app.route('/analyze/<int:id>')
@login_required
def analyze(id):
    post = Post.query.get(id)
    if post.all_attack > 0:
        seiko_attack = round(float(post.score_attack/post.all_attack)*100)
        koritu_attack = round(float((post.score_attack-post.miss_attack)/post.all_attack)*100)
        blocked_attack = round(float(post.block_attack/post.all_attack)*100)
        fail_attack = round(float(post.miss_attack/post.all_attack)*100)
    else:
        seiko_attack, koritu_attack, blocked_attack, fail_attack = 0 

    if post.all_serve > 0:
        seiko_serve = round(float(post.score_serve/post.all_serve)*100)
        koritu_serve = round(float((post.score_serve-post.miss_serve)/post.all_serve)*100)
        fail_serve = round(float(post.miss_serve/post.all_serve)*100)
    else:
        seiko_serve,koritu_serve,fail_serve = 0 

    return render_template('analyze.html',
                           post=post,
                           seiko_attack=seiko_attack,
                           koritu_attack=koritu_attack,
                           blocked_attack=blocked_attack,
                           fail_attack=fail_attack,
                           seiko_serve=seiko_serve,
                           koritu_serve=koritu_serve,
                           fail_serve=fail_serve 
                           ) 

@app.route('/plot_attack.png')
@login_required
def plot_attack_png():
    posts = Post.query.order_by(Post.day).all()

    labels = []
    seiko_attack = []
    koritu_attack = []
    blocked_attack = []
    fail_attack = []

    for p in posts:
        
        date_str = p.day.strftime('%Y-%m-%d')
        labels.append(date_str)

        if p.all_attack > 0:
            rate = (p.score_attack / p.all_attack) * 100
            rate = round(rate, 1)
        else:
            rate = 0
        
        seiko_attack.append(rate)

        if p.all_attack > 0:
            rate = ((p.score_attack - p.miss_attack) / p.all_attack) * 100
            rate = round(rate, 1)
        else:
            rate = 0
        koritu_attack.append(rate)

        if p.all_attack > 0:
            rate = (p.block_attack / p.all_attack) * 100
            rate = round(rate, 1)
        else:
            rate = 0
        blocked_attack.append(rate)

        if p.all_attack > 0:
            rate = (p.miss_attack / p.all_attack) * 100
            rate = round(rate, 1)
        else:
            rate = 0
        fail_attack.append(rate)

    fig, ax1 = plt.subplots(figsize=(10, 4))


    ax1.plot(labels, seiko_attack, marker='o', label='攻撃成功率')
    ax1.set_title("攻撃関連の推移 (%)")
    ax1.set_ylabel("成功率 (%)")
    ax1.set_xlabel("試合日")
    ax1.legend()


    ax1.plot(labels, koritu_attack, marker='x', label = '攻撃効果率')
    ax1.legend()

    ax1.plot(labels, blocked_attack, marker='^', label='ブロックされた割合')
    ax1.legend()


    ax1.plot(labels, fail_attack, marker='s', label='攻撃失敗率')
    ax1.legend()

    plt.xticks(rotation=45)
    plt.tight_layout()

    img = io.BytesIO()
    fig.savefig(img, format='png')
    plt.close(fig)
    img.seek(0)

    return Response(img.getvalue(), mimetype='image/png')

@app.route('/plot_serve.png')
@login_required
def plot_serve_png():
    posts = Post.query.order_by(Post.day).all()
    
    labels = []
    seiko_serve = []
    koritu_serve = []
    fail_serve = []
    
    for p in posts:

        date_str = p.day.strftime('%Y-%m-%d')
        labels.append(date_str)

        if p.all_serve > 0:
            rate = (p.score_serve / p.all_serve) * 100
            rate = round(rate, 1)
        else:
            rate = 0
        seiko_serve.append(rate)

        if p.all_serve > 0:
            rate = ((p.score_serve - p.miss_serve) / p.all_serve) * 100
            rate = round(rate, 1)
        else:
            rate = 0
        koritu_serve.append(rate)

   
        if p.all_serve > 0:
            rate = (p.miss_serve / p.all_serve) * 100
            rate = round(rate, 1)
        else:
            rate = 0
        fail_serve.append(rate)

    fig2, ax2 = plt.subplots(figsize=(10, 4))


    ax2.plot(labels, seiko_serve, marker='o', label='サーブ成功率')
    ax2.set_title("サーブ関連の推移 (%)")
    ax2.set_ylabel("成功率 (%)")
    ax2.set_xlabel("試合日")
    ax2.legend()


    ax2.plot(labels, koritu_serve, marker='x', label='サーブ効果率')
    ax2.legend()


    ax2.plot(labels, fail_serve, marker='s', label='サーブ失敗率')
    ax2.legend()

    plt.xticks(rotation=45)
    plt.tight_layout()

    img2 = io.BytesIO()
    fig2.savefig(img2, format='png')
    plt.close(fig2)
    img2.seek(0)

    return Response(img2.getvalue(), mimetype='image/png')



@app.route('/graph')
@login_required
def graph():
    return render_template('graph.html')


if __name__ == '__main__':
    app.run(debug=True, port=5001)