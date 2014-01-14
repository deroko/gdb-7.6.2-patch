From GDB Python documentation:

— Function: Breakpoint.__init__ (spec [, type [, wp_class [,internal [,temporary]]]])

Defines internal as possible option, but in py-breakpoint.c this argument is ignored.
My patch adds a few lines to the py-breakpoint.c to consider "internal" arg also in
bppy_init. This allows python script to set internal breaks which are < 0 thus 
breakpoints set in stepo command will not increase breakpoints number which you by
default set via (gdb) break

Also there are 2 provided gdb_*.py which implement stepo for i386/x86_64 and arm.


Files have to be copied to:

/usr/share/gdb/python/ or /usr/local/share/gdb/python or wherever gdb was installed
during build/install time

In .gdbinit you may add:
python import gdb_stepo (i386/x86_64)
or
python import gdb_stepo_arm (for arm)

