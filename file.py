#!/usr/bin/env python3
import os
from aqt.utils import showInfo
from .line import line

class file():
	ztk_id = -1
	file_name = ""
	file_path = ""
	folder = ""
	
	lines = []

	def __init__(self, file_name, folder):
		self.file_name = file_name
		self.folder = folder
		self.file_path = folder.get_path() + "/" + file_name
		self.read_file_content()
		self.set_ztk_id()
		
	def read_file_content(self) -> None:
		with open(self.file_path, mode = "r", encoding = "utf-8") as f:
			contents = f.readlines()
			count = 0
			for line_content in contents:
				if line_content == "\n":
					contents.remove(line_content)
				else:
					for i in range(0,1):
						line_content = line_content[:-1]
					self.lines.append(line(line_content, count, self))
					count = count + 1
					
	def get_file_content(self):
		file_content = ""
		for line_object in self.lines:
			file_content = file_content + line_object.get_line() + "</br>"
		return file_content
	
	def set_ztk_id(self):
		file_name_segments = self.file_name.split(" ")
		self.ztk_id = int(file_name_segments[0])
		
	def get_ztk_id(self):
		return self.set_ztk_id()
		
	def get_name(self):
		return self.file_name
	
	def get_folder(self):
		return self.folder
		
