#!/usr/bin/env python3
from aqt.utils import showInfo
from .settings import settings 
from .obsidian_url import obsidian_url

class line():
	
	line_content = ""
	line_index = 0
	file = ""
	line_segments = []
	
	preferences = settings()
	
	cloze_front = "{{c¡::"
	cloze_back = "}}"
	
	def __init__(self, line_content, line_index, file):
		self.file = file
		self.line_content = line_content
		self.line_index = line_index
		self.segmentation()

	def segmentation(self):
		for i in range(0, len(self.line_content)):
			self.line_segments.append(self.line_content[i])
	
	def desegmentation(self):
		self.line_content = "".join(self.line_segments)
		
	def get_line(self):
		self.desegmentation()
		return self.line_content
		
	def process_line(self):
		# basic processing to remove possible conflicts in anki html file and in mathjax.
		self.replacement(">", "&gt;")
		showInfo("> replaced: " + self.get_line())
		self.replacement("<", "&lt;")
		showInfo("< replaced: " + self.get_line())
		self.replacement("{", "{", "{ {")
		showInfo("left curly brackets spaced: " + self.get_line())
		self.replacement("}", "}", "} }")
		showInfo("right curly brackets spaced: " + self.get_line())
		self.replacement("\\", "(", "$")
		showInfo("inline math left swapped: " + self.get_line())
		self.replacement("\\", ")", "$")
		showInfo("inline math right swapped: " + self.get_line())
		self.replacement("\\", "[", "$$")
		showInfo("display math left swapped: " + self.get_line())
		self.replacement("\\", "]", "$$")
		showInfo("display math right swapped: " + self.get_line())
		self.bold_conversion()
		showInfo("bold converted: " + self.get_line())
		self.hightlight_conversion()
		showInfo("highlight converted: " + self.get_line())
#		self.wikilink_conversion()
		
	def whether_to_cloze(tf, to_sign1, to_sign2):
		if tf:
			to_sign1 = self.cloze_front + to_sign1
			to_sign2 = to_sign2 + self.cloze_back
			return [to_sign1, to_sign2]
		else:
			return [to_sign1, to_sign2]
	
	def bold_conversion(self):
		pair_of_sign = self.whether_to_cloze(self.preferences.get_bold_to_cloze(), "<b>", "</b>")
		self.replacer(self.replacement("*", "*", ""), pair_of_sign)
		
	# Use Opt + 0 and Opt + 10 to mark out the wiki links, because we need to process it more in the future. For now, we won't need to deal with the link content. 
	def hightlight_conversion(self):
		pair_of_sign = self.whether_to_cloze(self.preferences.get_highlight_to_cloze(), "<label style = \"background-color: yellow;\">", "</label>")
		self.replacer(self.replacement("=", "=", ""), pair_of_sign)
		
	def wikilink_conversion(self):
		self.replacement("[", "[", "º")
		self.replacement("]", "]", "º")
		items_to_change = self.replacement("º", "º")
		self.wikilink_processing(items_to_change)
	
	def wikilink_processing(self, items_to_change):
		is_beginning = True
		for i in range(0, len(items_to_change)):
			if is_beginning == True:
				is_beginning = False
				full_ztk_link_name = ""
				has_identifier = False
				keep_adding = True
				for j in range(self.line_segments[items_to_change[i]] + 2, self.line_segments[items_to_change[i + 1]]):
					if self.line_segments[j] == "#":
						keep_adding = False
					if keep_adding:
						full_ztk_link_name = full_ztk_link_name + self.line_segments[j]
						if self.line_segments[j] == "|":
							has_identifier = True
				ztk_link_segments = []
				ztk_name = ""
				if has_identifier:
					ztk_link = full_ztk_link_name.split("|")[0]
					ztk_name = full_ztk_link_name.split("|")[1]
					ztk_link_segments = ztk_link.split(" ")
				else:
					ztk_link_segments = full_ztk_link_name.split(" ")
					for k in range(1, len(ztk_link_segments) - 1):
						ztk_name = ztk_name + ztk_link_segments[k] + " "
					ztk_name = ztk_name[:-1]
				ztk_id = int(ztk_link_segments[0])
				
				url = obsidian_url(ztk_id, self.get_file())
				obsidian_beginning = "<a href = \"" + url + "\">"
				obsidian_end = "</a>"
				pair_of_sign = self.whether_to_cloze(obsidian_beginning, obsidian_end)
				self.line_segments[items_to_change[i]] = pair_of_sign[0]
				self.line_segments[items_to_change[i+1]] = pair_of_sign[1]
				for j in range(self.line_segments[items_to_change[i]] + 1, self.line_segments[items_to_change[i + 1]]):
					self.line_segments[j] = ""
			else:
				is_beginning = True
		
		
	
	def replacer(self, items_to_change, pair_of_sign):
		is_sign_1 = True
		for item in items_to_change:
			if is_sign_1:
				self.line_segments[item] = pair_of_sign[0]
				is_sign_1 = False
			else:
				self.line_segments[item] = pair_of_sign[1]
				is_sign_1 = True
		
			
	def replacement(self, sign_1, sign_2, to_sign) -> list:
		items_to_change = []
		for i in range(0, len(self.line_segments) - 1):
			if self.line_segments[i] == sign_1 and self.line_segments[i + 1] == sign_2:
				self.line_segments[i] = to_sign
				self.line_segments[i+1] = ""
				items_to_change.append(i)
		return items_to_change
			
	
				
	def replacement(self, from_sign, to_sign) -> list:
		items_to_change = []
		for i in range(0, len(self.line_segments)):
			if self.line_segments[i] == from_sign:
				self.line_segments[i] = to_sign
				items_to_change.append(i)
		return items_to_change