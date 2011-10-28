'''Converts a file in the following ways:
I.   One delimiter to another.
II.  Delimited to a specified fixed-width format.
III. Fixed-width to a demilited format.
IV.  One fixed-width format to another.

To convert a file from one delimiter(,) to another(:):
python converttextfile.py input.txt output.txt "," ":"

To convert a file from delimited(,) to fixed width fields
of widths 5,9,6,4:
python converttextfile.py input.txt output.txt "," "(5,9,6,4)"

To convert a file from fixed-width fields of widths 5,9,6,4
to delimited(,):
python converttextfile.py input.txt output.txt "(5,9,6,4)" ","

To convert a file from fixed-width fields of one size 5,9,6,4
to another 10,12,7,5:
python converttextfile.py input.txt output.txt "(5,9,6,4)" "(10,12,7,5)"

'''

import sys

# Module-level variables
inputfile = ''
outputfile = ''

def validateargs():
  pass

# Convert one delimited file to another
def convertfile(source, target):
  '''If source or target is a list or tuple, then the format is
      fixed width; else delimited file.
  '''
  linelist = []
  if (len(source) == len(target) == 1):
     for line in open(inputfile):
        linelist.append(target.join(line.rstrip("\n").split(source)))
  elif (len(source) == 1):
     target = tuple(target.strip("()").split(","))
     for line in open(inputfile):
        linelist.append(''.join([field.ljust(int(width))
           for width,field in zip(target, line.rstrip("\n").split(source))]))
  elif (len(target) == 1):
     source = tuple(source.strip("()").split(","))
     for line in open(inputfile):
        fieldlist = []
        index = 0
        for length in source:
           fieldlist.append(line[index:index+int(length)].strip())
           index += int(length)
        linelist.append(target.join(fieldlist))
  else:
     source = tuple(source.strip("()").split(","))
     target = tuple(target.strip("()").split(","))
     for line in open(inputfile):
        fieldlist = []
        index = 0
        for length in source:
           fieldlist.append(line[index:index+int(length)].strip())
           index += int(length)
        linelist.append(''.join([field.ljust(int(width))
           for width, field in zip(target, fieldlist)]))

  open(outputfile, "w").write(("\n").join(linelist))

# Main program   
if __name__ == '__main__':
  inputfile = sys.argv[1]
  outputfile = sys.argv[2]
  convertfile(sys.argv[3], sys.argv[4])


