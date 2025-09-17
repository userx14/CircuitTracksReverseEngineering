To open the ghidra project, you need to change the project ownership to your username. 
Otherwise you will get a NotOwnerException and ghidra refuses to open the file.

Edit `fw-v4486-re.rep/project.prp` and change the VALUE line here to your current user name: `<STATE NAME="OWNER" TYPE="string" VALUE="pr0xima" />`
