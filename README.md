# 8051-disassembler

Small tool to help disassemble Intel 8051 opcodes.

Python3 termcolor library is needed. 

```
$ ./disas.py dump.bin
> help
	*** Intel 8051(basic) disassembler - coded by Fritz (@anarcheuz) ***


	Software coded for 256k flash dump, append with 0xff if not the case to avoid any inconvenience! 

	quit|q - quit
	help|h - show this help

	x/f <addr> - disassemble until ret|reti is found
	x/i <addr> <count> - disassemble <count> instructions from <addr>
	x/x <unit> <addr> <count> - disassemble from <count> words from <addr> as <unit>
	 -(Big endian display. Why ? Because easier to read from left to right :))

	x/s <addr> <count> - interpret <addr> as 0 terminated string
	xref <addr> - Try to find all xrefs to <addr>
	finds <str> - find all occurences of <str>
	find <hexSequence> - find all occurences of the bytes <hexSequence> (eg: find 0a1032897f)
```

# Refs
* http://www.keil.com/support/man/docs/is51/is51_overview.htm
* https://github.com/adamdunkels/contiki-fork/wiki/8051-Memory-Spaces
* https://en.wikipedia.org/wiki/Intel_MCS-51
* http://what-when-how.com/8051-microcontroller/8051-register-banks-and-stack/
* http://www.8052.com/tutint.phtml
