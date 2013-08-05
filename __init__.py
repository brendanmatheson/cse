from flask import Flask, render_template, request, url_for
import os, sqlite3

if os.path.exists('/home/droz/webapps/coursera/coursera/sources.db'):
	DATABASE = '/home/droz/webapps/coursera/coursera/sources.db'
else:
	DATABASE = 'sources.db'
#DATABASE = 'sources.db'

app = Flask(__name__)

app.config.from_object(__name__)

app.secret_key = 'coursera'

def connect_db():
	return sqlite3.connect(app.config['DATABASE'])

@app.route('/')
def home():
	g = connect_db()
	cur = g.execute('SELECT lecture, link FROM links')
	#Rewrite below as a named tuple, more space efficient, in collections module
	list = [dict(lecture=row[0], link=row[1]) for row in cur.fetchall()]
	g.close()
	return render_template("index.html", list=list)


if __name__ == '__main__':
	app.run(debug=True)