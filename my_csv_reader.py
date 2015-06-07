
import csv as csv
import time
import sys

def timed_csv_reader(inputFile, accessmode = 'rb'):
    start_time = time.time()
    print 'Opening file:\t' + inputFile
    out = []
    open_file = open(inputFile, accessmode)
    file_to_str = open_file.read()
    print 'Splitting lines...'
    line_split = file_to_str.split('\n')
    line_count = float( len(line_split))
    current_line = 0
    bar = 0.0
    INCREMENT = 0.05
    print 'Starting ',
    while len( line_split[ current_line]) > 0:
        if current_line/line_count > bar:
            sys.stdout.write('.')#unichr(9659))
            bar += INCREMENT
        temp = line_split[ current_line]#.split(',')
        out.append(temp)
        current_line += 1
    print ' Done!'
    print 'Completed in:', round(time.time()-start_time, 2), 'seconds'
    return out

