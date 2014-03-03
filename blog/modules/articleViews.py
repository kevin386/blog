class urlView():
	def __init__(self,href="",name=""):
		self.href = href
		self.name = name

class countView():
	def __init__(self, url=None, count=0):
		self.url = url
		self.count = count

class commentView():
	def __init__(self, href="", content=""):
		self.content = content
		
class articleView():
	def __init__(self, title=None, tags=None, content=None, pub_date=None, vist_times=0, comment=None, comCount=0, category=None):
		self.title = title
		self.tags = tags
		self.content = content
		self.cont_trun = content[:200] + "..."
		self.pub_date = pub_date
		self.vist_times = vist_times
		self.comment = comment
		self.comCount = comCount
		self.category = category

class blogView():
	def __init__(self, image=None,vist_times=0, gender=None,art_cats=None,date_cats=None,lastest_comment=None):
		self.image = image
		self.vist_times = vist_times
		self.gender = gender
		self.art_cats = art_cats
		self.date_cats = date_cats
		self.lastest_comment = lastest_comment
