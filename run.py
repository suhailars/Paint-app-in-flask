from flask import *
import psycopg2
app = Flask(__name__)
@app.route('/')
def home():
	return render_template('paintnew.html')
@app.route('/gallery/<filename>',methods=['GET'])
def load(filename=None):
	conn=psycopg2.connect(database='suhail')
	c=conn.cursor()	
	c.execute("SELECT * FROM paintstore WHERE title=%s",[filename])
	posts=[dict(id=i[0],title=i[1],imagedata=i[2]) for i in c.fetchall()]
        conn.commit()
	conn.close()
	return render_template('picload.html',posts=posts)

@app.route('/<filename>',methods=['POST'])
def save(filename=None):
	conn=psycopg2.connect(database='suhail')
	c=conn.cursor()
	c.execute("INSERT INTO paintstore (title,imagedata) VALUES (%s,%s)",[request.form['name'],request.form['data']])
	conn.commit()
	conn.close()
	return render_template('paintnew.html')
@app.route('/gallery')
def gallery():
	conn=psycopg2.connect(database='suhail')
	c=conn.cursor()
	c.execute("SELECT * FROM paintstore ORDER BY id desc")
	posts=[dict(id=i[0],title=i[1]) for i in c.fetchall()]
	conn.commit()
	conn.close()	
	return render_template('gallery.html',posts=posts)

app.run(debug = True)

