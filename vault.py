#!/usr/bin/env python3

#############################################
#											#
#	Read the files in Obsidian vault foler.	#
#											#
#	2 Level Organization:					#
#		1)	Folders							#
#		2)	Files (only ztk format)			#
#											#
#	read Output: Dictionary					#
#		Key   = ZTK ID of the file name		#
#		Value = List of the lines in the	#
#				the file					#
#											#
#	search Output:	String of URL after		#
#					searching through the	#
#					database				#
#											#
#############################################

import os
import sys
from aqt.utils import showInfo
from .folder import folder

class vault():
	folders = []
	vault_name = ""
	vault_path = ""
	
	def __init__(self, vault_path):
		self.vault_path = vault_path
		vault_name_segments = vault_path.split("/")
		self.vault_name = vault_name_segments[len(vault_name_segments) - 1]
		showInfo("Vault Added")
		self.read_folders()
	
	def read_folders(self) -> None:
		folder_names = os.listdir(self.vault_path)
		for folder_name in folder_names:
			folder_name_segments  = folder_name.split(".")
			if len(folder_name_segments) > 1:
				folder_names.remove(folder_name)
			elif folder_name == ".DS_Store":
				folder_names.remove(".DS_Store")
			else:
				self.folders.append(folder(folder_name, self))
	
	def get_name(self) -> str:
		return self.vault_name
	
	def get_path(self) -> str:
		return self.vault_path
	
	def get_folders(self) -> list:
		return self.folders
	
	# search for the folder containing the file using ztk_id
	
	def get_folder_by_file_ztk_id(self, ztk_id):
		for folder_object in self.folders:
			if folder_object.get_file_by_ztk_id(ztk_id) != None:
				return folder_object
		return None
	
	# Do not recomment using this, as it may potentially cause problems if you change the name of your file. Therefore, it is much better to use ZTK id to identify the file. 
	
	def get_folder_by_file_name(self, file_name):
		for folder_object in self.folders:
			if folder_object.get_file_by_name(file_name) != None:
				return folder_object
		return None
				
	# search for the file in the entire databse using ztk_id
	
	def get_file_by_file_ztk_id(self, ztk_id):
		for folder_object in self.folders:
			if folder_object.get_file_by_ztk_id(ztk_id) != None:
				return folder_object.get_file_by_ztk_id(ztk_id)
		return None
	
	# Do not recomment using this, as it may potentially cause problems if you change the name of your file. Therefore, it is much better to use ZTK id to identify the file. 
	
	def get_file_by_file_name(self, file_name):
		for folder_object in self.folders:
			if folder_object.get_file_by_ztk_id(ztk_id) != None:
				return folder_object.get_file_by_ztk_id(ztk_id)
		return None
	
	def get_folders_and_files(self):
		vault_of_cards = {}
		for folder_object in self.folders:
			vault_of_cards[folder_object.get_name()] = folder_object.get_file_contents()
		return vault_of_cards