#!/usr/bin/env python3

import sys
from cpu_8051 import *
from termcolor import colored

def help():
	print("\t*** Intel 8051(basic) disassembler - coded by Fritz (@anarcheuz) ***\n\n")
	print(colored("\tSoftware coded for 256k flash dump, append with 0xff if not the case to avoid any inconvenience! \n", 'red'))
	
	print('\tquit|q - quit')
	print('\thelp|h - show this help\n')

	print('\tx/f <addr> - disassemble until ret|reti is found')
	print('\tx/i <addr> <count> - disassemble <count> instructions from <addr>')
	print('\tx/x <unit> <addr> <count> - disassemble from <count> words from <addr> as <unit>\n\t -(Big endian display. Why ? Because easier to read from left to right :))\n')
	print('\tx/s <addr> <count> - interpret <addr> as 0 terminated string')
	print('\txref <addr> - Try to find all xrefs to <addr>')
	print('\tfind <str> - find all occurences of <str>')

def int_(s):
	try :
		if '0x' in s:
			return int(s, 16)
		else:
			return int(s)
	except ValueError:
		return -1

def prompt():
	while 1:
		action = input("> ").split(' ')
		if action[0] == 'quit' or action[0] == 'q':
			break
		elif action[0] == 'help' or action[0] == 'h':
			help()
		elif action[0] == 'x/f':
			if len(action) == 2:
				addr = int_(action[1])
				if addr == -1:
					print("can't parse number")
				else :
					disas(addr)
			else:
				print('Syntax error')
		elif action[0] == 'x/i':
			if len(action) == 3:
				addr = int_(action[1])
				cnt = int_(action[2])
				if addr == -1 or cnt == -1:
					print("can't parse numbers")
				else:
					disas(addr, cnt)
			else:
				print('Syntax error')
		elif action[0] == 'x/x':
			if len(action) == 4:
				unit = int_(action[1])
				addr = int_(action[2])
				cnt = int_(action[3])
				if unit == -1 or addr == -1 or cnt == -1:
					print("can't parse numbers")
				else:
					dump(unit, addr, cnt)
			else:
				print('Syntax error')
		elif action[0] == 'x/s':
			if len(action) == 3:
				addr = int_(action[1])
				cnt = int_(action[2])
				if addr == -1 or cnt == -1:
					print("can't parse numbers")
				else:
					strings(addr, cnt)
			else:
				print('Syntax error')
		elif action[0] == 'find':
			if len(action) == 2:
				s = action[1]
				if s == -1:
					print("can't parse number")
				else :
					res = find(s)
					for l in res:
						print(hex(l) + ' = ' + str(l))
			else:
				print('Syntax error')
		elif action[0] == 'xref':
			if len(action) == 2:
				addr = int_(action[1])
				if addr == -1:
					print("can't parse numbers")
				else:
					xref(addr)
			else:
				print('Syntax error')
		elif len(action[0]) == 0:
			continue
		else:
			print('Unknown command')

def main():
	if len(sys.argv) == 2:
		env['file'] = sys.argv[1]
		try:
			env['data'] = open(env['file'], 'rb').read()
		except FileNotFoundError as e:
			print(e)
			return
		prompt()
	else:
		print(sys.argv[0] + ' <file>')

if __name__ == '__main__':
	main()
