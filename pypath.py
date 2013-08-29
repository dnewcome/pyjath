from lxml import etree

def trace(msg):
	print msg

class PyPath(object):

	def parse(self, template, xml):
		if type(template) == dict:
			self.parse_dict(template, xml)

		elif type(template) == list:
			self.parse_list(template, xml)

		else:
			self.parse_item(template, xml)

	def parse_list(self, template, xml):
		trace('parsing list')	
		r = xml.xpath(template[0])
		for i in range(0, len(r)):
			self.parse(template[1], r)
			

	def parse_dict(self, template, xml):
		trace('parsing dict')	
		retval = {}
		for item in template:
			retval[item] = self.parse(template[item], xml)
		return retval

	def parse_item(self, template, xml):
		trace('parsing item')	
		trace(str(xml))	
		node = xml.xpath(template)
		if node:
			return node.text
		else:
			return None

