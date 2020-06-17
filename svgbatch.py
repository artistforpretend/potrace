# This script assumes Potrace is installed and a system path is created where
# potrace exists

import os
from pathlib import Path

os.chdir('C:\\Users\\username\\bmpfolder')
p = Path.cwd()
filelist = list(p.glob('*.bmp'))

for file in filelist:
    command = f"potrace -s {file} -o {os.path.splitext(file)[0]}.svg"
    os.system(command)
