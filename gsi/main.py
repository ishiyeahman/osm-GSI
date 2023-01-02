import gsi

def main():
    print("Kyushu University, Hakozaki campus.")
    print( gsi.get_max_depth( 130.42496194503377, 33.62677707060762) )
    print( gsi.get_max_depth_keys() )
    print( gsi.get_max_depth(130.42496194503377, 33.62677707060762, "Depth") )
    
    
    
if __name__ == '__main__':
    main()