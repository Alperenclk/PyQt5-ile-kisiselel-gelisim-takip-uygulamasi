

from PyQt5 import uic

with open('ilkVersiyonUI.py', 'w', encoding="utf-8") as fout:
   uic.compileUi('ilkVersiyon.ui', fout)