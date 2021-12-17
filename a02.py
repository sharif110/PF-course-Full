### YOUR CODE FOR calculateArea() FUNCTION GOES HERE ###
def calculateArea(width, length):
    return (width * length)

#### End OF MARKER



### YOUR CODE FOR checkTilesFit() FUNCTION GOES HERE ###
def checkTilesFit(plot_width, plot_length,tile_width, tile_length ):
    
       
    if (tile_width > plot_length and tile_width > plot_width) or (tile_length > plot_length and tile_length > plot_width):
        plot_area =(plot_width * plot_length)
        tile_area =(tile_width * tile_length)
        if plot_area % tile_area == 0:
            return True
        
    if (plot_length) < 0 or (plot_width) < 0 or (tile_length) < 0 or (tile_width) <0:
        return False
    elif plot_width % tile_width ==0 and plot_length % tile_length == 0:
        return True
    elif plot_length % tile_width == 0 and plot_width % plot_width ==0:
        return True
    #if plot_area  tile_width == 0 or plot_area % tile_length == 0:
        #return True
        #if plot_area < tile_area:
            #return False
        #if plot_area > tile_area:
            #return False
    
    else:
        return False
    
    
#### End OF MARKER



### YOUR CODE FOR calculateTiles() FUNCTION GOES HERE ###
def calculateTiles(plot_width, plot_length, tile_width, tile_length):
    
    if type (plot_width) == str or type(plot_length) == str or type(tile_width) == str or type(tile_length) == str:
        return "Invalid Input"
    
    if (plot_width == 0 or plot_length == 0 or tile_width == 0 or tile_length == 0 ):
        return None
    
    if  checkTilesFit(plot_width, plot_length, tile_width, tile_length):
    
        plot_area = calculateArea(plot_width, plot_length)
        tile_area = calculateArea(tile_width, tile_length)
        calculateTiles = (plot_area) // (tile_area)
        
        return calculateTiles
        
    return "Not Possible"

    
   

#### End OF MARKER



