#! /usr/bin/python3


grid = [ 'GGGGGGGGGGGGGG','GGGGGGGGGGGGGG','GGBGBGGGBGBGBG','GGBGBGGGBGBGBG', 'GGGGGGGGGGGGGG','GGGGGGGGGGGGGG','GGGGGGGGGGGGGG', 'GGGGGGGGGGGGGG', 'GGBGBGGGBGBGBG','GGBGBGGGBGBGBG','GGBGBGGGBGBGBG','GGBGBGGGBGBGBG']

rows = len(grid)
print( rows )
columns = len(grid[0])    
plusAreas = [1,1]

def twoPluses(grid):
    for i in range(1,rows-1):
        for j in range(1,columns-1):
            print("i={0:d},j={1:d}".format(i,j))
            if( grid[i][j]=='G' ):
                checkForPlus(i,j,1)

    return (plusAreas[0]*plusAreas[1])

def checkForPlus(i,j,length):
    if( ( ((j+length)<columns ) and ((j-length)>=0) ) and ( ((i+length)<rows ) and ((i-length)>=0) ) ):
        if( ((grid[i-length][j]=='G') and (grid[i+length][j]=='G')) and ((grid[i][j-length]=='G') and (grid[i][j+length]=='G')) ):
            checkForPlus(i,j,length+1)
            return
        else:
            area = 4*(length-1) + 1
            for i in range(2):
                if ( area > plusAreas[i] ):
                    plusAreas[i] = area
                    break 
            return
    else:
        area = 4*(length-1) + 1
        for i in range(2):
            if ( area > plusAreas[i] ):
                plusAreas[i] = area
                break
        return


print ( "area = " + str(twoPluses(grid)) )        
