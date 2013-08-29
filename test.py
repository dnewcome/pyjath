from lxml import etree
from pypath import PyPath
from io import StringIO
import unittest

class TestPyPath(unittest.TestCase):

	def test_nominal(self):
		self.assertTrue(True)

	def test_jath(self):
		pp = PyPath()
		xml = u"""
			<statuses userid="djn">
				<status id="1">
					<message>Hello</message>
				</status>
				<status id="3">
					<message>Goodbye</message>
				</status>
			</statuses>
		"""
		sio = StringIO(xml)
		tree = etree.parse(sio)

		expected = [ 
			{ "id": "1", "message": "Hello" }, 
			{ "id": "3", "message": "Goodbye" } 
		]


		template = [ "//status", { "id": "@id", "message": "message" } ]
		actual = pp.parse(template, tree)
		self.assertEqual(actual, expected)
