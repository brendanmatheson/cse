import os, pyPdf, sqlite3
from StringIO import StringIO

topdir = r"C:/Users/MZ/Dropbox/STARTUP ENGINEERING/LECTURES/"
pdfs = [x for x in os.listdir(topdir) if ".pdf" in x] 

conn = sqlite3.connect('sources.db')
c = conn.cursor()
c.execute('DROP TABLE IF EXISTS links')
c.execute('''CREATE TABLE links
             (Id INTEGER PRIMARY KEY, lecture text, link text)''')

def insert_row(lecture, link):
	insertion = (lecture, link)
	c.execute("INSERT INTO links (lecture, link) VALUES (?, ?)", insertion)

def extract_links(directory, lecture):
	path = directory + lecture 
	try: 
	    f = open(path,'rb')

	    pdf = pyPdf.PdfFileReader(f)

	    pgs = pdf.getNumPages()
	    key = '/Annots'
	    uri = '/URI'
	    ank = '/A'

	    for pg in range(pgs):

	        p = pdf.getPage(pg)
	        o = p.getObject()

	        if o.has_key(key):
	            ann = o[key]
	            for a in ann:
	                u = a.getObject()
	                if u[ank].has_key(uri):
	                    #print u[ank][uri]
	                    insert_row(lecture, u[ank][uri])
	except KeyError:
		pass 

for pdf in pdfs:
	#print pdf 
	#print "~"*50
	extract_links(topdir, pdf)

# # From: http://docs.python.org/2/library/stringio.html

conn.commit()
conn.close()


# allfiles = (os.path.join(path,name)
#     for path, dirs, files in os.walk(topdir)
#         for name in files)