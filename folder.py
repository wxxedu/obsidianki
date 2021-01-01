#!/usr/bin/env python3
import os
from typing import Optional
from aqt.utils import showInfo
from .file import file 

class folder():
	files = []
	folder_path = ""
	vault = ""
	folder_name = ""
	
	def __init__(self, folder_name, vault):
		self.folder_name = folder_name
		self.vault = vault
		self.folder_path = vault.get_path() + "/" + folder_name
		self.read_files()
		
	def read_files(self):
		files_catalog = os.listdir(self.folder_path)
#		files_catalog.remove(".DS_Store")
		for file_name in files_catalog:
			file_name_segments = file_name.split(".")
			attribute_index = len(file_name_segments) - 1
			if file_name_segments[attribute_index] == "md":
				self.files.append(file(file_name, self))
			else:
				files_catalog.remove(file_name)
				
	def get_name(self) -> str:
		return self.folder_name
	
	def get_path(self) -> str:
		return self.folder_path
	
		