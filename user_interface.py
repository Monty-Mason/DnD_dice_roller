import sys
import random

from character_stats_operations import PlayerStats
from dice_rolls_operations import DiceRolls

if __name__=='__main__':
	player_stats = PlayerStats(sys.argv[1])
	general_stats, general_combat_stats, additional_skills, abilities_and_modifiers, saving_throws, skills_expertise, skills, attack_and_spellcasting, features_and_traits, other_proficiences_and_language, equipment = player_stats.parse_config_file()
	stats_list = [general_stats, general_combat_stats, additional_skills, abilities_and_modifiers, saving_throws, skills_expertise, skills, attack_and_spellcasting, features_and_traits, other_proficiences_and_language, equipment]
	
	while 1:
		inp = input("[+] Input your selection:\n> ")
		if inp.lower() in ['-e', '--exit']:
			exit()
		elif ('-r' in inp.lower()) or ('--roll' in inp.lower()):
			# Normal roll: -r --acrobatics
			# Advantage roll: -r --adv --acrobatics
			# Disadvantage roll: -r --dadv --acrobatics
			# Weapon roll: -r --weapon_1
			roller = DiceRolls(inp, stats_list)
		else:
			print('Unrecognized input. Please enter a proper input option.\n')
		
