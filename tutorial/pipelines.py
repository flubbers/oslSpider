# -*- coding: utf-8 -*-

import json

class FicheroJsonTagsPipeline(object):
	file = ''
	linea = ''
	def __init__(self):
		self.file = open('noticiasTags.json', 'wb')
	def process_item(self, item, spider):
		linea = json.dumps(dict(item)) + "\n"
		self.file.write(linea)
		return item

class FicheroJsonPipeline(object):
	file = ''
	linea = ''
	def __init__(self):
		self.file = open('noticias.json', 'wb')
	def process_item(self, item, spider):
		linea = json.dumps(dict(item)) + "\n"
		self.file.write(linea)
		return item
