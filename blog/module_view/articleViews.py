class tagsView():
	def __init__(self, href="", count=0):
		self.href = href
		self.count = count

class commentView():
	def __init__(self, href="", count=0):
		self.href = href
		self.count = count
		
class articleView():
	def __init__(self, title="", tags=None, content=None, create_time=None, view_times=0, comment=None, category=None):
		self.title = title
		self.tags = tags
		self.content = content
		self.create_time = create_time
		self.view_times = view_times
		self.comment = comment
		self.category = category


