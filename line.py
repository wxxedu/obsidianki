#!/usr/bin/env python3
from aqt.utils import showInfo

class line():
	line_content = ""
	words = []
	file = ""
	
	def __init__(self, line_content, file):
		self.line_content = line_content
		self.words = line_content.split(" ")
		self.file = file
		showInfo("|".join(self.words))
		
	
	