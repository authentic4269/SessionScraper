import mechanize
from HTMLParser import HTMLParser

class MyHTMLParser(HTMLParser):
    formflag = False
    def __init__(self):
	 HTMLParser.__init__(self)
	 self.formflag = False
    def handle_starttag(self, tag, attrs):
        if tag == "form":
		for (k, v) in attrs:
			if k == "id" and v == "login_form":
				self.formflag = True
				print "login form"		
	elif self.formflag:
		print "Encountered a tag :" + tag
    def handle_endtag(self, tag):
	if tag == "form" and self.formflag:
		self.formflag = False
    def handle_data(self, data):
        if self.formflag:
		print "Encountered some data  :", data

request = mechanize.Request("http://www.facebook.com/")
response = mechanize.urlopen(request)
p = MyHTMLParser()
str = str(response.read())
p.feed(str)
