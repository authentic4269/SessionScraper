import cookielib
import os.path
import urllib2

import os.path
import urllib2

COOKIEFILE = 'cookies.lwp'
# the path and filename to save your cookies in

cj = None
ClientCookie = None
cookielib = None

from HTMLParser import HTMLParser

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def __init__(self):
	HTMLParser.__init__(self)
	self.elements = {}
    def handle_starttag(self, tag, attrs):
	if tag in self.elements:
		self.elements[tag].append(attrs)	
	else:
		self.elements[tag] = [attrs]
    def get_tags(self):
	return self.elements
    def handle_endtag(self, tag):
        print "Encountered an end tag :", tag
    def handle_data(self, data):
        print "Encountered some data  :", data


# Let's see if cookielib is available
try:
    import cookielib
except ImportError:
    # If importing cookielib fails
    # let's try ClientCookie
    try:
        import ClientCookie
    except ImportError:
        # ClientCookie isn't available either
        urlopen = urllib2.urlopen
        Request = urllib2.Request
    else:
        # imported ClientCookie
        urlopen = ClientCookie.urlopen
        Request = ClientCookie.Request
        cj = ClientCookie.LWPCookieJar()

else:
    # importing cookielib worked
    urlopen = urllib2.urlopen
    Request = urllib2.Request
    cj = cookielib.LWPCookieJar()
    # This is a subclass of FileCookieJar
    # that has useful load and save methods

if cj is not None:
# we successfully imported
# one of the two cookie handling modules

    if os.path.isfile(COOKIEFILE):
        # if we have a cookie file already saved
        # then load the cookies into the Cookie Jar
        cj.load(COOKIEFILE)

    # Now we need to get our Cookie Jar
    # installed in the opener;
    # for fetching URLs
    if cookielib is not None:
        # if we use cookielib
        # then we get the HTTPCookieProcessor
        # and install the opener in urllib2
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
        urllib2.install_opener(opener)

    else:
        # if we use ClientCookie
        # then we get the HTTPCookieProcessor
        # and install the opener in ClientCookie
        opener = ClientCookie.build_opener(ClientCookie.HTTPCookieProcessor(cj))
        ClientCookie.install_opener(opener)

try:
    txheaders =  {'User-agent' : 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}
    req = Request("http://www.facebook.com/", None, txheaders)
    # create a request object

    handle = urlopen(req)
    # and open it to return a handle on the url

except IOError, e:
    print 'We failed to open "%s".' % theurl
    if hasattr(e, 'code'):
        print 'We failed with error code - %s.' % e.code
    elif hasattr(e, 'reason'):
        print "The error object has the following 'reason' attribute :"
        print e.reason
        print "This usually means the server doesn't exist"
        print "is down, or we don't have an internet connection."
    sys.exit()

else:
    print 'Here are the headers of the page :'
    print handle.info()
    print handle.read() 
    # handle.geturl() returns the true url of the page fetched
    # (in case urlopen has followed any redirects, which it sometimes does)
if cj is None:
    print "We don't have a cookie library available - sorry."
    print "I can't show you any cookies."
else:
    print 'These are the cookies we have received so far :'
    for index, cookie in enumerate(cj):
        print index, '  :  ', cookie
    cj.save(COOKIEFILE)
