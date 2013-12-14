import psycopg2
con = psycopg2.connect(database='suhail') 
cur = con.cursor()
cur.execute("DROP TABLE IF EXISTS paintstore")
cur.execute("CREATE TABLE paintstore(id serial,title text,imagedata text)")
con.commit()
con.close()
