
import time

def timed_csv_reader(inputFile, accessmode = 'rb'):
    print '\nOpening file:\t' + inputFile
    
    INCREMENT = 0.05
    TIMEOUT = 60*3
    ind = 0
    bar = 0.0
    out = []
    start_time = time.time()
    
    print 'Starting',
    with open(inputFile, accessmode) as open_file:
        
        new_file = open_file.readlines()
        line_count = float( len( new_file))
        
        for line in new_file:
            
            if ind/line_count > bar:
                print '.',
                bar += INCREMENT
                
            temp = line.split(',')
            out.append(temp)
            ind += 1
            test = time.time()-start_time
            if test > TIMEOUT: 
                print '\nProcess failed:\tout of time',
                print round(time.time()-start_time, 2), 'seconds'
                return None
                
    print ' Done!'
    print 'Completed in:', round(time.time()-start_time, 2), 'seconds'
    return out

t = timed_csv_reader('data/bids.csv', 'rb')
#try:
#    print type(t), type(t[0])
#    print len(t), len(t[0])
#except:
#    pass
