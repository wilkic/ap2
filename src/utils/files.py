import errno
from os import makedirs as mkdir
from os import path as os_path

def mkdir_p(path):
    try:
        mkdir(path)
    except OSError as exc:  # Python >2.5
        if exc.errno == errno.EEXIST and os_path.isdir(path):
            pass
        else:
            raise


from shutil import copyfile as cp

def try_copy( src, dest ):
    try:
	mkdir_p(dest)
        cp( src, dest )
        return True
    except IOError as e:
        print "OOPs... that was a bad copy"
        print e
        return False

from re import match
from time import strptime, mktime, sleep

def parse_ts( fname ):
    for i in range(0,2):
        try:
            with open(fname) as f:
                s = f.read()
        except Exception, e:
            if i < 2:
                print "Can't open timestamp %s" % fname
                print "\t Waiting a second to try again"
                sleep(1)
            else:
                print "Tried too many times..."
                raise

    m = match(r".*\'(.*)\'",s)
    tt = strptime(m.group(1),"%Y-%m-%d %H:%M:%S")
    ts = mktime( tt )
    return ts

