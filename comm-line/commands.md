#CLI

	Ctrl+D = end of file 
	Ctrl+Z = suspend 



## Remove items

To remove a directory:

	rm -d dirname
	rmdir dirname

To remove a nonempty directory, add the -r (recursive) option:

	rm -r dirname

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


 

#virtual environments


Add the virtualenv as a jupyter kernel
	(your-venv)$ ipython kernel install --name "local-venv" --user





