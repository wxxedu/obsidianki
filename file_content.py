#!/usr/bin/env python3

from aqt.utils import showInfo

class file_content:
	lines = []
	file_metadata = []
	def __init__(self, content):
		self.lines = content
		self.process_file_content()
		
	def process_file_content(self):
		
		return self.lines 
	
	def get_file_content(self):
		
		return "".join(self.lines)
	
	def get_file_metadata(self):
		
		return "".join(self.file_metadata)