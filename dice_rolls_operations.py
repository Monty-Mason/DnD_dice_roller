import random

class DiceRolls:
	def __init__(self, args, user_stats=[]):
		self.args = args
		self.user_stats = user_stats
		self.parse_args(self.args, self.user_stats)
		
	def parse_args(self, dice_args, user_stats=[]):
		self.clean_dice_list = []
		dice_list = dice_args.split(' ')
		dice_list = dice_list[1:]
		
		self.adv_dadv_flag = 0 # 0 - No advantage or disadvantage, 1 - Advantage roll, 2 - Disadvantage roll
		if '--adv' in dice_list:
			self.adv_dadv_flag = 1
		elif '--dadv' in dice_list:
			self.adv_dadv_flag = 2
		
		i = 0
		while i < len(dice_list):
			j = 0
			while j < len(user_stats):
				if dice_list[i] in user_stats[j]:
					for k, v in user_stats[j].items():
						if dice_list[i] == k:
							if 'weapon' in dice_list[i]:
								# Do something
								print('lol')
							else:
								self.clean_dice_list.append(v)
							break
				j+=1
			i+=1
		self.roll(self.clean_dice_list, self.adv_dadv_flag)
		
	def roll(self, roll_values, roll_adv_dadv_flag):
		# Figure out how many d20s we need based on advantage/disadvantage/normal roll
		self.d_rolls = 1 # Number of d20 rolls
		if roll_adv_dadv_flag != 0:
			self.d_rolls = 2
			
		# Roll the d20
		i = 0
		self.d20_roll_val = [] # Stores the d20 roll
		while i < self.d_rolls:
			self.d20_roll_val.append(random.randrange(1, 20))
			i+=1
				
		# See if len is more than one in d20_roll_val
		if len(self.d20_roll_val) > 1:
			# Yes - check for advantage/disadvantage roll flag
			if roll_adv_dadv_flag == 1:
				# Advantage roll - Take the higher of the two rolls
				if self.d20_roll_val[0] > self.d20_roll_val[1]:
					self.d20_roll_val = self.d20_roll_val[:1]
				else:
					self.d20_roll_val = self.d20_roll_val[1:]
			elif roll_adv_dadv_flag == 2:
				# Disadvantage roll - Take the lower of the two rolls
				if self.d20_roll_val[0] < self.d20_roll_val[1]:
					self.d20_roll_val = self.d20_roll_val[:1]
				else:
					self.d20_roll_val = self.d20_roll_val[1:]
						
		# Add the modifier to the d20 value
		print('Result of roll: {}'.format(self.d20_roll_val[0] + int(roll_values[0])))