Version: 1.01
Update: added support for multiple mesh groups (with independent UV mappings).

Usage:
(in command promt)
python uvexporter.py -i %SOURCE% [-o %OUTPUT%] [--h %HEIGHT%] [--w %WIDTH%] [-lw %LINEWIDTH]

Parameters:

-i	%SOURCE%	Path for your obj file. You must have this parameter or the script would not have anything to process.
-o	%OUTPUT%	Path for your exported image file. If left blank, the image file will be named as the source obj file.
--h	%HEIGHT%
--w	%WIDTH%		Optional output image size. By default 2048 x 2048 px.
-lw	%LINEWIDTH%	Optional line width. By default 1.


Other information:
Now you can export multiple UV mappings of different mesh groups in a single obj file.