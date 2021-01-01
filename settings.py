#!/usr/bin/env python3

class settings:
	
	bold_to_cloze = True
	wiki_links_to_cloze = True
	italic_to_cloze = False
	highlight_to_cloze = False
	inline_code_to_cloze = True
	path_to_vault = "/Users/xiuxuan/Library/Mobile Documents/iCloud~org~zrey~metion/Documents/Knowledge Base"
	
	def set_bold_to_cloze(self, tf) -> bool:
		self.bold_to_cloze = tf
		
	def get_bold_to_cloze(self):
		return self.bold_to_cloze

	def set_wiki_links_to_cloze(self, tf) -> bool:
		self.wiki_links_to_cloze = tf
		
	def get_wiki_links_to_cloze(self):
		return self.wiki_links_to_cloze
	
	def set_italic_to_cloze(self, tf) -> bool:
		self.italic_to_cloze = tf
		
	def get_italic_to_cloze(self):
		return self.italic_to_cloze
	
	def set_highlight_to_cloze(self, tf) -> bool:
		self.highlight_to_cloze = tf
		
	def get_highlight_to_cloze(self):
		return self.highlight_to_cloze
	
	def set_inline_code_to_cloze(self, tf) -> bool:
		self.inline_code_to_cloze = tf
		
	def get_inline_code_to_cloze(self):
		return self.inline_code_to_cloze
	
	def set_path_to_vault(self, path) -> str:
		self.bold_to_cloze = path
		
	def get_path_to_vault(self):
		return self.path_to_vault
	
	