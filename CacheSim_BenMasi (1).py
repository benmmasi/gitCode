class cache_slot:
	def  __init__(self, slot_num, valid_bit, tag, dirty_bit, data, main_mem_add):
		self.slot_num = slot_num
		self.valid_bit = valid_bit
		self.tag = tag
		self.dirty_bit = dirty_bit
		self.data = data
		self.main_mem_add = main_mem_add

	def __print__(self):
		print str(self.slot_num) + "\t" + str(self.valid_bit) + "\t" + str(self.tag) + "\t" + str(self.data)


def cache_simulator():
	main_memory = [0]
	i = 0
	tempVal = main_memory[i] + 1
	while tempVal <= int("7ff", base = 16):
		main_memory.append(hex(tempVal))
		tempVal = tempVal + 1
	
	j = 1
	while j <= int("7ff", base = 16):
		main_memory[j] = main_memory[j][-2:]
		j = j + 1

	cache = []
	for count in xrange(16):
		x = cache_slot(str(hex(count)), 0, "0", 0, "0", "0")
		x.attr = count
		cache.append(x)


	leaving = False
	while leaving != True:
		print "Hello, would you like to Read, Write, Print Cache, or Exit?"
		choice = raw_input()
		if choice == "Read":
			print "What address would you like to read from?"
			address_prehex = raw_input()
			address = int(address_prehex, 16)
			block_offset = address & int('000F', 16)
			block_beginning = address & int('FFF0', 16) 
			slot_num = (address & int('00F0', 16)) >> 4
			tag = address >> 8

			if cache[int(slot_num)].valid_bit == 1 and tag == cache[int(slot_num)].tag:
				found_byte = cache[int(slot_num)].data[block_offset]
				print "Hit!  " + str(found_byte)
				dirty_bit = 0

			elif cache[int(slot_num)].valid_bit == 0:
				print "Miss!  " + main_memory[int(address)]
				cache[int(slot_num)].data = main_memory[int(block_beginning):int(block_beginning) + 16]
				cache[int(slot_num)].main_mem_add = address 
				cache[int(slot_num)].valid_bit = 1
				cache[int(slot_num)].tag = tag
				cache[int(slot_num)].dirty_bit = 0

			elif cache[int(slot_num)].valid_bit == 1 and tag != cache[int(slot_num)].tag and cache[int(slot_num)].dirty_bit == 0:
				print "Miss!  " + main_memory[int(address)]
				cache[int(slot_num)].data = main_memory[int(block_beginning):int(block_beginning) + 16]
				cache[int(slot_num)].main_mem_add = address 
				cache[int(slot_num)].tag = tag
				cache[int(slot_num)].dirty_bit = 0

			elif cache[int(slot_num)].valid_bit == 1 and tag != cache[int(slot_num)].tag and cache[int(slot_num)].dirty_bit == 1:
				print "Miss!  " + main_memory[int(address)]
				main_mem_beginning = str(cache[int(slot_num)].main_mem_add)[:-1]
				temp = cache[int(slot_num)].data
				cache[int(slot_num)].data = main_memory[int(block_beginning):int(block_beginning) + 16]
				cache[int(slot_num)].tag = tag
				cache[int(slot_num)].dirty_bit = 0



		
		if choice == "Write":
			print "What address would you like to print to?"
			address = raw_input()
                        block_offset = int(address, 16) & int('000F', 16)
                        block_beginning = int(address, 16) & int('FFF0', 16)
                        slot_num = (int(address, 16) & int('00F0', 16)) >> 4
                        tag = int(address, 16) >> 8
			
			print "What value?"
			new_val_preint = raw_input()
			new_val = int(new_val_preint)
			

			if cache[int(slot_num)].valid_bit == 0:
				print "Miss!  " + str(address) + " now is set to " + str(new_val)
				main_memory[int(address, 16)] = new_val
				cache[int(slot_num)].data = main_memory[int(block_beginning):int(block_beginning) + 16]
				cache[int(slot_num)].tag = tag
				cache[int(slot_num)].data[block_offset] = str(new_val)
				cache[int(slot_num)].valid_bit = 1
			
			elif cache[int(slot_num)].valid_bit == 1 and int(tag) == cache[int(slot_num)].tag:
				print "Hit!  " + str(address) + " now is set to " + str(new_val)
				main_memory[int(address, 16)] = new_val
				cache[int(slot_num)].tag = tag
				cache[int(slot_num)].data[block_offset] = str(new_val)
				cache[int(slot_num)].dirty_bit = 1



				
		if choice == "Print Cache":
			print "Slot |" + "  Valid |" + "  Tag |" + "  Data"
			for count in xrange(16):
				x = cache[count]
				x.__print__()


		if choice == "Exit":
			leaving = True

		

		
cache_simulator()
