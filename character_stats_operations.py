import sys

class PlayerStats:
	def __init__(self, filename):
		self.fname = filename
		
	def parse_config_file(self):
		with open(self.fname, 'r') as file_handler:
			self.content = file_handler.readlines()
			
		self.clean_content = []
		for val in self.content:
			self.clean_content.append(val.strip())
		
		self.general_stats = {}
		self.general_combat_stats = {}
		self.additional_skills = {}
		self.abilities_and_modifiers = {}
		self.saving_throws = {}
		self.skills_expertise = {}
		self.skills = {}
		self.attack_and_spellcasting = {}
		self.features_and_traits = {}
		self.other_proficiences_and_language = {}
		self.equipment = {}
		
		i = 0 # Content index
		while i < len(self.clean_content):
			if self.clean_content[i] == '# General - Character':
				self.clean_content, self.general_stats = self.format_stats_dictionary(self.clean_content, '# General - Character Combat Stats')
			elif self.clean_content[i] == '# General - Character Combat Stats':
				self.clean_content, self.general_combat_stats = self.format_stats_dictionary(self.clean_content, '# Additions_skills')
			elif self.clean_content[i] == '# Additions_skills':
				self.clean_content, self.additional_skills = self.format_stats_dictionary(self.clean_content, '# Abilities and modifiers')
			elif self.clean_content[i] == '# Abilities and modifiers':
				self.clean_content, self.abilities_and_modifiers = self.format_stats_dictionary(self.clean_content, '# Saving Throws')
			elif self.clean_content[i] == '# Saving Throws':
				self.clean_content, self.saving_throws = self.format_stats_dictionary(self.clean_content, '# Expertise in the following skills')
			elif self.clean_content[i] == '# Expertise in the following skills':
				self.clean_content, self.skills_expertise = self.format_stats_dictionary(self.clean_content, '# Skills')
			elif self.clean_content[i] == '# Skills':
				self.clean_content, self.skills = self.format_stats_dictionary(self.clean_content, '# Attack and Spellcasting')
			elif self.clean_content[i] == '# Attack and Spellcasting':
				self.clean_content, self.attack_and_spellcasting = self.format_stats_dictionary(self.clean_content, '# Features and Traits')
			elif self.clean_content[i] == '# Features and Traits':
				self.clean_content, self.features_and_traits = self.format_stats_dictionary(self.clean_content, '# Other Proficiencies and Languages')
			elif self.clean_content[i] == '# Other Proficiencies and Languages':
				self.clean_content, self.other_proficiences_and_language = self.format_stats_dictionary(self.clean_content, '# Equipment')
			elif self.clean_content[i] == '# Equipment':
				self.clean_content, self.equipment = self.format_stats_dictionary(self.clean_content, '# eof')
			else:
				break
				
		return self.general_stats, self.general_combat_stats, self.additional_skills, self.abilities_and_modifiers, self.saving_throws, self.skills_expertise, self.skills, self.attack_and_spellcasting, self.features_and_traits, self.other_proficiences_and_language, self.equipment

	def format_stats_dictionary(self, data_list, next_heading):
		self.mod_data_list = []
		self.stats_dict = {}
		i = 0
		while data_list[i] != next_heading and i < len(data_list):
			if '# ' in data_list[i] or data_list[i] == '':
				i+=1
				continue
			self.stats_dict[data_list[i].split(':')[0]] = data_list[i].split(': ')[1]
			i+=1

		self.mod_data_list = data_list[i:]
		return self.mod_data_list, self.stats_dict