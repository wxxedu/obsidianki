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
		folder_names.remove(".DS_Store")
		for folder_name in folder_names:
			folder_name_segments  = folder_name.split(".")
			if len(folder_name_segments) > 1:
				folder_names.remove(folder_name)
			else:
				self.folders.append(folder(folder_name, self))
	
	def get_name(self) -> str:
		return self.vault_name
	
	def get_path(self) -> str:
		return self.vault_path
	
	def get_folders(self) -> list:
		return self.folders