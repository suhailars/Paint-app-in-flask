from flask import *
import psycopg2
app = Flask(__name__)
@app.route('/')
def home():
	return render_template('paintnew.html')
@app.route('/<filename>',methods=['POST'])
def save(filename=None):
	conn=psycopg2.connect(database='suhail')
	c=conn.cursor()
	c.execute("INSERT INTO paintstore (title,imagedata) VALUES (%s,%s)",[request.form['name'],request.form['data']])
	conn.commit()
	conn.close()
	return render_template('paintnew.html')
app.run(debug = True)

