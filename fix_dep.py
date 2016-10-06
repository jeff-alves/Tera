from subprocess import call

import pip

for dist in pip.get_installed_distributions():
    call("pip install --upgrade " + dist.project_name, shell=True)

call("pip install --upgrade enum", shell=True)
call("pip install --upgrade pywinauto", shell=True)
call("pip install --upgrade py2exe", shell=True)