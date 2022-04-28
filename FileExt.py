#!/usr/bin/python
#
#  The 1st line tells UNIX like OS variants where to find the correct Python 
#  interpreter. This is ingnored by Operating systems such as Windows
#
#  fileext.py
#
#  A python script to parse file extensions (of the windows style filename.ext) 
#  It should be noted that this tyoe of file extension construct is not 
#  mandatory
#  on UNIX like operating systems and it is perfectly  valid for a UNIX file not
#  to have such a construct
#
#  Read through a recursive directory listing file (currently provided on 
#  sharepoint) parse out  the file extension using the os.path.splitext method.
#  Save a count of the occurenses each distinct file type in a dictionary data
#  structure (associative array in other languages)
#
#   version 1.0  17/03/22   Dave Herdman
#   version 1.1  28/04/22   Dave Herdman
#
#   Developed using the Pycharm IDE
#   See PyCharm help at https://www.jetbrains.com/help/pycharm/
#
#   Usage: ext.py <Path-of-File-to-Process> <Path-to-output-File>
#
import sys
import os


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # process the command line agruments (if any)
    if len(sys.argv) > 2:
        # Assume first argument is the path to the filename
        # silently ignore any other arguments
        #print("File to process is %s" % (sys.argv[1]))
        in_file = sys.argv[1]
        #print("Output File is %s" % (sys.argv[2]))
        out_file = sys.argv[2]
    else:
        print("Usage: fileext.py  <input-file-path> <output-file-path>")
        sys.exit("Incorrect number of arguments")


    dirlist = open(in_file, "r")
    outfile = open(out_file,"w")
    file_types = dict()

    for line in dirlist:

    

        # There may be white space in the file & Directory names, so we can't rely on
        # an element number to locate these. Instead, we scan forwards for the full path
        #  & backwards for the filename.
        full_path = line[line.find(r'/'):]
        #print("full path %s" % (full_path,))
        file_name = full_path[full_path.rfind(r'/')+1:]
        #print("File name is %s" % (file_name,))

        file_ext = os.path.splitext(file_name)[1]
	# 
        # Check if the dictionary key exists. If it does increment the value of 
        # matching the key. If not then create the key-value pair
        #
        if file_types.has_key(file_ext):
	    # key exists so increment the frequency value
            kval = file_types.get(file_ext) + 1
            file_types[file_ext] = kval
        else:
            file_types[file_ext] = 1

    # Now write out the populated dictionary structure

    for key , value in file_types.items():
       # Print the data in the dictionry
       key = key.rstrip('\n')
       out_str = "%s , %s\n" %(key,value)
       outfile.write(out_str)

    dirlist.close()
    outfile.close()
