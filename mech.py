import mechanize
from HTMLParser import HTMLParser

class MyHTMLParser(HTMLParser):
    formflag = False
    form_objects = []
    action = ""
    def __init__(self):
	 HTMLParser.__init__(self)
	 self.formflag = False
    def handle_starttag(self, tag, attrs):
        if tag == "form":
		for (k, v) in attrs:
			if k == "id" and v == "login_form":
				self.formflag = True
				for (p, j) in attrs:
					if p =="action":
						self.action = j
				break
	elif self.formflag:
		self.form_objects.append((tag, attrs))
    def handle_endtag(self, tag):
	if tag == "form" and self.formflag:
		self.formflag = False
    def handle_data(self, data):
	return
    def get_form_objects(self):
	return (self.form_objects, self.action)

request = mechanize.Request("http://www.facebook.com/")
response = mechanize.urlopen(request)

browser = mechanize.Browser(factory=mechanize.RobustFactory())
browser.set_handle_robots(False)
browser.open("http://www.facebook.com/")
browser.select_form(nr=0)
browser.form['email'] = "vogel_mitchell@yahoo.com"
browser.form['pass'] = "b157dc03vogel62415"
req = browser.submit()
print req.read()
#p = MyHTMLParser()
#str = str(response.read())
#p.feed(str)
#post_dict = {}
#for t in p.get_form_objects():
#	(tag, attrs) = t
#	if tag == "input":
#		for (k, v) in attrs:
#			if k == "type" and v == "password":				
#	for attr in attrs
