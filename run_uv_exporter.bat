@ECHO OFF

for /r %%f in (*.obj) do (python uvexporter.py -i "%%f")
PAUSE

@ECHO ON