from PIL import Image, ImageDraw
import re
import argparse
import sys


#defines the default size of the output
_outw = 2048
_outh = 2048
_outfile = ''
_sourcefile = ''
_width = 1
#def main(argv):
#    _outfile = argv[1]

#main(sys.argv)


class Vertex(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

vertices = []
faces = []
sides = []

parser = argparse.ArgumentParser(description='Exports UV mapping of an obj file.')
parser.add_argument('-i', dest='sourcefile', help='Path of the source obj file.')
parser.add_argument('-o', dest='outfile', help='Path of the exported image file. By default "%sourcename%.png".')
parser.add_argument('--h', dest='height', help='Height of the exported file.')
parser.add_argument('--w', dest='width', help='Width of the exported file.')
parser.add_argument('-lw', dest='linewidth', help='Width of the lines.')

args = parser.parse_args()
if args.sourcefile == None:
    print('No source file indicated!')
    sys.exit()
else:
    _sourcefile = str(args.sourcefile)
if args.outfile == None:
    _outfile = _sourcefile.replace('.obj', '')
else:
    _outfile = str(args.outfile)
if args.height != None:
    _outh = int(args.height)
if args.width != None:
    _outw = int(args.width)
if args.linewidth != None:
    _width = int(args.linewidth)

print("height/width: " + str(_outh) + ' ' + str(_outw))

#print(_outfile)
def main():

    with open(_sourcefile, 'r') as source_file:
        for line in source_file:
            line.rstrip()
            line_split = re.split(r' ', line)
            if line_split[0] == 'vt':
                new_vertex = Vertex(float(line_split[1]) * _outw, float(line_split[2]) * _outh)
                vertices.append(new_vertex)
            elif line_split[0] == 'f':
                line_split.remove('f')
                current_face = []
                for vertex_indexes in line_split:
                    vertex_index = re.split(r'/', vertex_indexes)
                    if vertex_index[1] != '':
                        current_face.append(int(vertex_index[1]))
                faces.append(current_face)
        #print('vertex count:')
        #print(len(vertices))
        #print("Faces:")
        #print(faces)
        for current_face in faces:
            for i in range(len(current_face)-1):
                current_side = [current_face[i], current_face[i+1]]
                sides.append(current_side)
            current_side = [current_face[len(current_face)-1], current_face[0]]
            sides.append(current_side)
        #print('Sides:')
        #print(sides)
        print("Processing " + _sourcefile + '...')
        print(str(len(vertices)) + ' vertices, ' + str(len(sides)) + ' sides, ' + str(len(faces)) + ' faces.')
        img = Image.new('RGBA', (_outw, _outh))
        colour = (125,255,23)
        draw = ImageDraw.Draw(img)
        for side in sides:
            draw.line((vertices[side[0]-1].x, vertices[side[0]-1].y, vertices[side[1]-1].x, vertices[side[1]-1].y), fill=colour, width=_width)
        del draw
        img.save(_outfile + '.png','PNG')

##########
main()