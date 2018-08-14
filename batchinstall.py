#BatchInstall.py
import os
libs={'numpy','matplotlib','pillow','sklearn','request',\
      'jieba','beautifulsoup4','wheel','networkx','sympy',\
      'pyinstaller','django','flask','werobot','pyqts'\
      'pandas','pyopengl','pypdf2','docopt','pygame'}
try:
    for lib in libs:
        os.system("pip install "+lib)
    print('sucessful')
except:
    print('falied')
    
