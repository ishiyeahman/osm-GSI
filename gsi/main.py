import gsi

def main():
    print("Kyushu University, Hakozaki campus.")
    print( gsi.get_max_depth(33.62677707060762, 130.42496194503377) )
    print( gsi.get_max_depth_keys() )
    print( gsi.get_max_depth(33.62677707060762, 130.42496194503377, "Depth") )
    
    
    
if __name__ == '__main__':
    main()