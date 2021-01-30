# uv-exporter  
Exports UV mapping from an obj file  
Now all coordinates will be mapped into the [0, 1] range, so everything will be cramped in the square. Better than a lot of details lost.  
  
A full rework is due. No more manual parsing, I'll get some better obj parser.  
  
## Usage:  
(in command promt)  
python uvexporter.py -i %SOURCE% [-o %OUTPUT%] [--h %HEIGHT%] [--w %WIDTH%] [-lw %LINEWIDTH%]  
  
## Parameters:  
  
\*-i	%SOURCE%	Path for your obj file. You must have this parameter or the script would not have anything to process.  
\*-o	%OUTPUT%	Path for your exported image file. If left blank, the image file will be named as the source obj file.  
\*--h	%HEIGHT%  
\*--w	%WIDTH%		Optional output image size. By default 2048 x 2048 px.  
\*-lw	%LINEWIDTH%	Optional line width. By default 1.  
  
## Other information / Limitations:  
Only one UVW mapped mesh per obj file, since the author didn't realise there could be multiple meshes in one obj file.  
UTF-8 encoding preferred, try saving your obj as UTF-8 if some locale error pops up. 