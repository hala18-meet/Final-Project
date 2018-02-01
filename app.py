#import sys
#import math
# flask imports
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

# SQLAlchemy
# from database import Base, Pos

app = Flask(__name__)
app.debug = True
app.config['SQLAlCHEMY_DATABASE_URI']='sqlite:////tmp/test.db'
db=SQLAlchemy(app)




class Songs(db.Model):
    id            = db.Column(db.Integer, primary_key=True , autoincrement=True)
    title         = db.Column(db.String(30), nullable=False)
    category      = db.Column(db.String(30), nullable=False)
    
    def __reper__(self):
        return '<songs %r>' % self.title

db.create_all()
    


# setup


@app.route('/')
def main():
    print("hi")
    # posts = session.query(Post).order_by("id desc").all()
    # i = 0
    # total_posts = len(posts)
    
    # mid_way = math.ceil(total_posts/2)

    # #print(total_posts, file=sys.stderr)
    # posts_1 = []
    # posts_2 = []
    # while i < mid_way:
    #     posts_1.append(posts[i])
    #     i += 1
    # j = mid_way
    # while j < total_posts:
    #     posts_2.append(posts[j])
    #     j += 1
    return render_template('main.html', posts=None)


@app.route('/mood_music')
def mood_music():
    return render_template('post.html')

@app.route('/find_mood')
def find_mood():
    return render_template('findmymood.html')

@app.route('/game')
def game():
    return render_template('game.html')

@app.route('/articles')
def articles():
    return render_template('articles.html')

@app.route('/main_page')
def main_page():
    return render_template('main.html')
@app.route('/quizz')
def quizz():
    return render_template('the quizz.html')




# @app.route('/<string:category_name>')
 #def sad (category_name):
     #category_posts= session.query(Songs).filter_by(category="sad songs").all()
     #return render_template('post.html', category_name=category_name, posts=category_posts)


@app.route('/songs', methods=['GET', 'POST'])
def songs():
    if request.method == "GET":
        return render_template('post.html')
    elif request.method == "POST":

        new_song=Songs()
        
        new_song.title=request.form.get('title')
        new_song.category= request.form.get('category')
        db.session.add(new_song)
        db.session.commit()

        return render_template("post.html")


        
        # print('This error output %s' % new_title,  file=sys.stderr)

        #post = Post( title=new_title, category=new_category)
        #session.add(post)
        #session.commit()
        # ADD SQL SESSION


        return redirect('/')

@app.route('/sadsongs', methods=['GET', 'POST'])
def sadsongs():
    sad_s=Songs.query.filter_by(category="sad")
    return render_template('sadsongs.html', sad_s=sad_s)

@app.route('/happysongs', methods=['GET', 'POST'])
def happysongs():
    happy_s= Songs.query.filter_by(category="happy")
    return render_template('happy.html', happy_s=happy_s)

@app.route('/powerfullsongs', methods=['GET', 'POST'])
def powerfullsongs():
    powerfull_s=Songs.query.filter_by(category="powerfull")
    return render_template('powerfull.html', powerfull_s=powerfull_s)

@app.route('/romanticsongs', methods=['GET', 'POST'])
def romanticsongs():
    romantic_s=Songs.query.filter_by(category="romantic")
    return render_template('romantic.html', romantic_s=romantic_s)





if __name__ == '__main__':
   app.run()