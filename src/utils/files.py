from shutil import copyfile as cp

def try_copy( src, dest ):
    try:
        cp( src, dest )
        return True
    except IOError as e:
        print "OOPs... that was a bad copy"
        print e
        return False

