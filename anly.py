from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
db = SQLAlchemy(app)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    day = db.Column(db.DateTime, nullable=False)
    match_name = db.Column(db.String(500), nullable=False)
    reflect = db.Column(db.String(500))
    all_attack = db.Column(db.Integer, nullable=False)
    score_attack = db.Column(db.Integer, nullable=False)
    miss_attack = db.Column(db.Integer, nullable=False)
    block_attack = db.Column(db.Integer, nullable=False)
    all_serve = db.Column(db.Integer, nullable=False)
    score_serve = db.Column(db.Integer, nullable=False)
    miss_serve = db.Column(db.Integer, nullable=False)

@app.route('/', methods=['GET', 'POST'])
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
        return redirect('/')


@app.route('/write')
def write():
    return render_template('write.html')

@app.route('/reflect/<int:id>')
def reflect(id):
    post = Post.query.get(id)

    return render_template('reflect.html', post=post)

@app.route('/delete/<int:id>')
def delete(id):
    post = Post.query.get(id)

    db.session.delete(post)
    db.session.commit()
    return redirect('/')

@app.route('/update/<int:id>', methods=['GET', 'POST'])
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
        return redirect('/')
    
@app.route('/analyze/<int:id>')
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
                           

if __name__ == '__main__':
    app.run(debug=True, port=5001)