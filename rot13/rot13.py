import webapp2
import cgi

form = """
<form method="post">
	<b>Enter some text to ROT13</b>
  <br/>
  <label>
  <textarea name = "text" value = "%(text)s"></textarea>
  </label>	
  <br/>
  <input type = "submit">
</form>
"""

def escape_html(s):
  return cgi.escape(s, quote = True)

def rot13(text):
  out = ""
  abc1 ="ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz"
  abc2 = "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm"
  for e in s:
    if e in abc1:
      indx = abc1.index(e)
      out += e.replace(e, (abc2[indx]))
    else:
      out += e
  return out

class MainPage(webapp2.RequestHandler):
  def write_form(self, s=""):
    self.response.out.write(form % {"text":escape_html(text)})

  def get(self):
    self.write_form()
    

  def post(self):
    user_text = self.request.get('text')
    user = rot13(user_text)
    self.write_form(user)
   
application = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
