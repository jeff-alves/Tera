from distutils.core import setup
import glob
import shutil
import py2exe


dist_dir = 'Release'
build_dir = 'build'
# Remove the build folder
shutil.rmtree(build_dir, ignore_errors=True)
# do the same for dist folder
shutil.rmtree(dist_dir, ignore_errors=True)

MANIFEST_TEMPLATE = """
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<assembly xmlns="urn:schemas-microsoft-com:asm.v1" manifestVersion="1.0">
  <assemblyIdentity
    version="5.0.0.0"
    processorArchitecture="x86"
    name="%(prog)s"
    type="win32"
  />
  <description>%(prog)s</description>
  <trustInfo xmlns="urn:schemas-microsoft-com:asm.v3">
    <security>
      <requestedPrivileges>
        <requestedExecutionLevel
            level="requireAdministrator"
            uiAccess="false">
        </requestedExecutionLevel>
      </requestedPrivileges>
    </security>
  </trustInfo>
  <dependency>
    <dependentAssembly>
      <assemblyIdentity
            type="win32"
            name="Microsoft.VC90.CRT"
            version="9.0.21022.8"
            processorArchitecture="x86"
            publicKeyToken="1fc8b3b9a1e18e3b">
      </assemblyIdentity>
    </dependentAssembly>
  </dependency>
  <dependency>
    <dependentAssembly>
        <assemblyIdentity
            type="win32"
            name="Microsoft.Windows.Common-Controls"
            version="6.0.0.0"
            processorArchitecture="X86"
            publicKeyToken="6595b64144ccf1df"
            language="*"
        />
    </dependentAssembly>
  </dependency>
</assembly>
"""

class Target(object):
    def __init__(self, **kw):
        self.__dict__.update(kw)

data_files = [("res", glob.glob(r'res/*.*'))]
includes = []
excludes = ['_gtkagg', '_tkagg', 'bsddb', 'curses', 'email', 'pywin.debugger',
            'pywin.debugger.dbgcon', 'pywin.dialogs', 'tcl',
            'Tkconstants', 'Tkinter']
packages = []
dll_excludes = ['libgdk-win32-2.0-0.dll', 'libgobject-2.0-0.dll', 'tcl84.dll',
                'tk84.dll', 'MSVCP90.dll', 'mswsock.dll', 'powrprof.dll']
icon_resources = [(0, 'res/icon.ico')]
bitmap_resources = []
other_resources = [(24, 1, MANIFEST_TEMPLATE % dict(prog="Tera DPS"))]
py26MSdll = glob.glob(r"c:\Dev\Py26MSdlls-9.0.21022.8\msvc\*.*")
data_files += [("", py26MSdll), ]

windows = [{
    'script':"test_ui.py",
    'icon_resources':icon_resources,
    'bitmap_resources':bitmap_resources,
    'other_resources':other_resources,
    'dest_base':"Tera DPS",
    'version':"0.1",
    'company_name':"No Company",
    'copyright':"No Copyrights",
    'name':"Tera DPS/BOT"
}]

setup(
    data_files=data_files,
    options={"py2exe": {
	    "compressed": True,
		"optimize": 2,
		"includes": includes,
		"excludes": excludes,
		"packages": packages,
		"dll_excludes": dll_excludes,
		"bundle_files": 2,
		"dist_dir": "Release",
		"xref": False,
		"skip_archive": False,
		"ascii": False,
		"custom_boot_script": '',
	}},
    zipfile="lib\library.zip",
    windows=windows
    )

shutil.rmtree("build", ignore_errors=True)
