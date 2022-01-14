# CLI

	Ctrl+D = end of file 
	Ctrl+Z = suspend 

## Command-Line Options

Unix tradition encourages the use of command-line switches to control programs, so that options can be specified from scripts. 

This is especially important for programs that function as pipes or filters. Three conventions for how to distinguish command-line options from ordinary arguments exist; the original Unix style, the GNU style, and the X toolkit style.

In the original Unix tradition, command-line options are single letters preceded by a single hyphen. Mode-flag options that do not take following arguments can be ganged together; thus, if -a and -b are mode options, -ab or -ba is also correct and enables both. The argument to an option, if any, follows it (optionally separated by whitespace). In this style, lowercase options are preferred to uppercase. When you use uppercase options, it's good form for them to be special variants of the lowercase option.


-f:
File (with argument). Very often used with an argument to specify an input (or, less frequently, output) file for programs that need to randomly access their input or output (so that redirection via < or > won't suffice). 

-r:

Recurse (without argument). If the program operates on a directory, then this option might tell it to recurse on all subdirectories. Any other use in a utility that operated on directories would be quite surprising. The classic example is, of course, cp(1).

 




## Remove items

To remove a directory:

	rm -d dirname
	rmdir dirname

To remove a nonempty directory, add the -r (recursive) option and the file option -f:

	rm -rf dirname

To remove a file:
	
	rm filename


## cat
cat is a  utility that reads files sequentially, writing them to standard output. The name is derived from its function to concatenate files.

	cat file2 >> file1
	cat file1
	file1 contents
	file2 contents





# Git commands


Create new depository locally 

	git init reponame

Clone repository from Github so that you can access it via your desktop

	git clone path

Use HTTPS link or SSH from repository 

When adding or committing changes to files in repo

After the changes have been made and saved in the local, then do the following:

	git add

this adds the file to committ (stages)

next, once you've edited, added, removed, etc and used the corresponding git add commands

	git committ

then the vi/text editor will prompt to describe the changes you've made. you'll save that note and then the changes will be committed 

	git push

this publishes changes


# vi commands

To edit a file using vi editor:
	vi filename


to enter edit mode:
	i

to escape edit mode:
	esc

to save the file
	:wq


## VisualStudioCode

lets you open file from the terminal
	code filename


 # virtual environments


Add the virtualenv as a jupyter kernel
	(your-venv)$ ipython kernel install --name "local-venv" --user


# MySQL

mysql is a simple SQL shell with input line editing capabilities. It supports interactive and noninteractive use. When used interactively, query results are presented in an ASCII-table format. 

	mysql -u root -p


db_name is optional 


