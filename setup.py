
import sys

from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(includes=["json"], include_files=["src/img", "src/log.conf", "src/settings.conf"],
                    path=sys.path + ['./src', './src/Window', './src/MIA', './src/Database', './src/Controller'])

base = 'Win32GUI' if sys.platform == 'win32' else None

executables = [
    Executable('src/start.py', base=base, targetName='lung-cancer-diagnosis')
]

setup(name='lung-cancer-diagnosis',
      version='0.1',
      description='alpha',
      options=dict(build_exe=buildOptions),
      executables=executables)
