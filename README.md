Vidlio
======
(recommended) 
Install virtualenv

	$ pip install virtualenvwrapper

	After it's installed, add the following lines to your shell's start-up file 
	(.zshrc, .bashrc, .profile, etc).

	export WORKON_HOME=$HOME/.virtualenvs
	export PROJECT_HOME=$HOME/directory-you-do-development-in
	source /usr/local/bin/virtualenvwrapper.sh

	Reload your start up file (e.g. source .zshrc) and you're ready to go.

Creating a new environment

	Creating a virtual environment is simple. Just type
	$ mkvirtualenv vidlio

	You'll notice a few things happen right away: Your shell is prepended by "(vidlio)" 
	distribute and pip were automatically installed

	This is an extremely helpful part of virtualenvwrapper: it automatically prepares 
	your environment in a way that lets you start installing packages using pip right 
	away. The "(vidlio)" portion is a reminder that you're using a virtualenv instead 
	of your system's Python installation. To exit the virtual environment, simply type 
	'deactivate'. When you want to resume work on your project, it's as easy as 
	'workon vidlio'. 
	Note that unlike the vanilla virtualenv tool, where you run these commands doesn't matter.



Install Django and other modules with pip

	$ pip install django

	there is a requirements.txt file located in the project, to install everything 
	necessary for the project just run
	$ pip install -r requirements.txt

Start project

	To run the project we will be using Foreman, just run
	$ foreman start
	and the project should be running on http://localhost:5000
