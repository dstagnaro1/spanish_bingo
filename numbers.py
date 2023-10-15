from random import shuffle
from words import *

def get_shuffled_numbers():
	# local_max_len = 24
	# if MAX_LEN > 24:
	# 	local_max_len = MAX_LEN
	
	# numbers = [i for i in range(local_max_len)]
	numbers = [i for i in range(24)]

	shuffle(numbers)
	shuffled_numbers = numbers[:24]
	shuffled_numbers.insert(12, 999)

	return shuffled_numbers