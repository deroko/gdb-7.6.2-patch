import	gdb

class   stepover(gdb.Command):
        def __init__(self):
                super (stepover, self).__init__("stepo", gdb.COMMAND_USER);
        def invoke(self, arg, from_tty):
	        pc = gdb.parse_and_eval("$pc");
	        arch = gdb.selected_frame().architecture();
	        #print(arch.name());
		ins = arch.disassemble(long(pc), count=1);
	        if len(ins) == 0:
	        	return;
	        ins = ins[0];
	        if "call" in ins["asm"] or "movs" in ins["asm"] or "stos" in ins["asm"] or "loop" in ins["asm"]:
	        	next_address = long(pc) + ins["length"];
	        	next_address = "*" + hex(next_address)[:-1];
	        	bp = gdb.Breakpoint(next_address, internal=True, temporary=True);
	        	gdb.execute("continue");
		else:
	        	gdb.execute("stepi");
stepover();
