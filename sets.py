def union( a, b ):
    thing = [ x for x in b if x not in a ]
    return
    
print( union( [1,2,3,4], [2,4,6,8] ) )
    
def inter( a, b ):
    return [ x for x in a if x in b ]

print( inter( [1,2,3,4], [2,4,6,8] ) )

def diff( u, a ):
    return [ x for x in u if x not in a ]

print( diff( [1,2,3,4], [2,4,6,8] ) )

def symDiff( a, b ):
    return

def product( a, b ):
    return [ [x,y] for x in a for y in b ]

print( product( [1,2,3,4], [2,4,6,8] ) )
