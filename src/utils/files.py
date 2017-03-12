from shutil import copyfile as cp

def try_copy( src, dest ):
    try:
        cp( src, dest )
        return True
    except IOError as e:
        print "OOPs... that was a bad copy"
        print e
        return False

from re import match
from time import strptime, mktime

def parse_ts( fname ):
    with open(fname) as f:
        s = f.read()
    m = match(r".*\'(.*)\'",s)
    tt = strptime(m.group(1),"%Y-%m-%d %H:%M:%S")
    ts = mktime( tt )
    return ts

