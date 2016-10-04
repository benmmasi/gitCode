def disassemble():
	instructions = [0x022DA822, 0x8EF30018, 0x12A70004, 0x02689820, 0xAD930018, 0x02697824, 0xAD8FFFF4, 0x018C6020, 0x02A4A825, 0x158FFFF6, 0x8E59FFF0]
	program_counter = 0x7A060

	for instruction in instructions:
		opcode_mask = int('FC000000', 16)
		rs_reg_mask = int('3E00000', 16)
		rt_reg_mask = int('1F0000', 16)
		rd_reg_mask = int('F800', 16)
		offset_mask = int('FFFF', 16)
		func_mask = int('3F', 16)

		opcode_shift = 26
		rs_reg_shift = 21
		rt_reg_shift = 16
		rd_reg_shift = 11

		opcode_preshift = opcode_mask & instruction
		opcode = opcode_preshift >> opcode_shift
		rs_reg_preshift = rs_reg_mask & instruction
		rs_reg = rs_reg_preshift >> rs_reg_shift
		rt_reg_preshift = rt_reg_mask & instruction
		rt_reg = rt_reg_preshift >> rt_reg_shift
		rd_reg_preshift = rd_reg_mask & instruction
		rd_reg = rd_reg_preshift >> rd_reg_shift
		function = func_mask & instruction
		offset = offset_mask & instruction
		if offset >= 0x8000:
			offset -= 0x10000

		
		if opcode == 0:
			if function == 32:
				print hex(program_counter), 'add', '$',rd_reg,',' '$',rs_reg,',' '$',rt_reg
				program_counter = program_counter + 4
			if function == 34:
				print hex(program_counter), 'sub', '$',rd_reg,',' '$',rs_reg,',' '$',rt_reg
				program_counter = program_counter + 4
			if function == 36:
				print hex(program_counter), 'and', '$',rd_reg,',' '$',rs_reg,',' '$',rt_reg
				program_counter = program_counter + 4
			if function == 37:
				print hex(program_counter), 'or', '$',rd_reg,',' '$',rs_reg,',' '$',rt_reg 
				program_counter = program_counter + 4

		if opcode == 35:
			print hex(program_counter), 'lw', '$',rt_reg,',', offset,',', '(', rs_reg, ')'
			program_counter = program_counter + 4
		if opcode == 43:
			print hex(program_counter), 'sw', '$',rt_reg,',', offset,',', '(', rs_reg, ')'
			program_counter = program_counter + 4

		if opcode == 4:
			program_counter = program_counter + 4
			print hex(program_counter), 'beq', '$',rs_reg,',' '$',rt_reg,',', hex(program_counter + offset)
		if opcode == 5:
			program_counter = program_counter + 4
			print hex(program_counter), 'bne', '$',rs_reg,',' '$',rt_reg,',', hex(program_counter + offset)

disassemble()
