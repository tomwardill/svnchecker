SVNCHECKER
----------

This is a simple script that will catch an svn commit, and run a command, such as tests.

Installation
============

Add this part to your buildout::

  [svnchecker]
  recipe = zc.recipe.egg
  eggs = svnchecker
  initialization = 
        args = {'bin': '${buildout:bin-directory}',
        'command': 'django',
        'apps': ['main'],
        }   
  arguments = args

where `bin` is the directory containing the command you want to run, `command` is the command you'd like to run and `apps` is a list of arguments (called apps as it's a django heritage).

Usage
=====

The usage is fairly simple, simple run `bin\svn` rather than svn. If it's a `commit` or `ci` command, it will execute the command you specified, after a short delay in case of accidental commit. Any other command is passed directly through to the SVN binary.
