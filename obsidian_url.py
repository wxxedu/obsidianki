#!/usr/bin/env python3

from aqt.utils import showInfo

class obsidian_url:
	
	vault_root_url = "obsidian://open?vault="
	file_root_url = "&file="
	
	ztk_id = 0
	
	vault = ""
	
	file = ""
	
	file_name = ""
	
	folder_name = ""
	
	vault_name = ""
	
	def __init__(self, ztk_id, file_object):
		self.ztk_id = ztk_id
		
	def gen_obsidian_url(self):
		vault_url = self.vault_root_url + self.encode(self.vault_name)
		file_url = self.file_root_url + self.encode(self.folder_name) + "%2F" + self.encode(self.file_name)
		showInfo(vault_url + file_url)
		return vault_url + file_url
		
	def remove_file_attribute(file):
		portions = file.split(".")
		return_string = ""
		for index in range(0, len(portions)-1):
			return_string = return_string + portions[index]
		return return_string
				
	def encode(string):
		string = str(str(string).encode("utf-8"))
		string = string.replace("\\x", "%")
		string = string.replace(" ", "%20")
		string = string.replace("/", "%2F")
		string = string.lstrip("\'b")
		string = string.rstrip("\'")
		string = capitalize_unicode(string)
		return string
	
	def capitalize_unicode(string):
		new = []
		position = -5
		for index in range(0, len(string)):
			if string[index] == "%":
				position = index
				new.append(string[index])
			elif index == position + 1 or index == position + 2:
				new.append(string[index].capitalize())
			else:
				new.append(string[index])
		return "".join(new)
	