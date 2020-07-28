from cx_Freeze import *

includefiles = ['cal.ico']
base = None
if sys.platform == 'win32':
    base = "Win32GUI"

shortcut_table = [
    ('DesktopShortcut',
     'DesktopFolder',
     'Calculator',
     "TARGETDIR",
     "[TARGETDIR]\mycalculator.exe",
     None,
     None,
     None,
     None,
     None,
     None,
     "TARGETDIR",)
]

msi_data = {"Shortcut": shortcut_table}

bdist_msi_options = {"data":msi_data}
setup(
    version="0.1",
    description="My Calculator",
    author="Ashwini",
    name="My Calculator",
    options={'build_exe':{'include_files': includefiles}, "bdist_msi":bdist_msi_options, },
    executables=[
        Executable(
             script="mycalculator.py",
             base=base,
             icon='cal.ico',
        )
    ]
)