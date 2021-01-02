#!/usr/bin/env python3
import os
from aqt.utils import showInfo
from .file_content import file_content
from .file import file

class file():
	file_ztk_id = None
	file_name = None
	file_content = None
	folder_name = None
	def __init__(self, file_name, file_content, folder_name):
		self.file_name = file_name
		self.file_content = file_content
		self.folder_name = folder_name
		self.get_ztk_id()
	
	def get_file_ztk_id(self):
		file_name_segments = self.file_name.split(" ")
		self.ztk_id = file_name_segments[0]
		return self.ztk_id
	
	def get_file_name(self):
		return self.file_name
	
	def get_file_content(self):
		return self.file_content
	
	def get_folder_name(self):
		return self.get_folder_name()
	
	def write_to_anki(self):
		
		return ""