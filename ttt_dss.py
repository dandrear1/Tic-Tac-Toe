while True:
    # put each tictactoe game into a dictionary using a list of dictionaries
    tictactoe = {'top left' :  'x', 'top middle'   : 'x', 'top right'   : 'b', 
                'left middle': 'o', 'center'       : 'x', 'right middle': 'o',
                'bottom left': 'x', 'bottom middle': 'b', 'bottom right': 'x'}
    
    # have the user load a Tic-tac-toe game into the dictionary
    print("Please input your Tic-tac-toe board right to left and top to bottom")
    print("Type exit to exit")
    
    # some handling to let the user exit the program
    value = ''
    for key in tictactoe:
        value = input(f"What is in the {key}\n> ")
        if value != 'exit':
            tictactoe[key] = value
        else:
            break
    
    if value == 'exit':
        break
    
    # Start the tree
    # center node: center_0 <= 0.5
    if tictactoe['center'] != 'o':
        
        # left side of root note
        # top-left_o <= 0.5
        if tictactoe['top left'] != 'o':
            
            # left node of top-left_o <= 0.5
            # if bottom-right_o <= 0.5
            if tictactoe['bottom right'] != 'o':
                
                # left node of bottom-right_o <= 0.5
                # Reach a leaf deciding that x wins
                print('x is likely to win')
            
            # right node of bottom-right <= 0.5
            # if bottom-left_0 <= 0.5
            elif tictactoe['bottom left'] != 'o':
                
                # left node of bottom-left_0 <= 0.5
                # if top-right_o <= 0.5
                if tictactoe['top right'] != 'o':
                    
                    # left node of top-right_o <= 0.5
                    # Reach a leaf deciding that x wins if the expression is true
                    print('x is likely to win')
                else:
                    
                    # right node of top-right_o <= 0.5
                    # Reach a leaf deciding that x doesn't win the expression is false
                    print('x is not likely to win')
            
            # right node of bottom-left <= 0.5
            # if bottom-middle_o <= 0.5
            elif tictactoe['bottom middle'] != 'o':
                
                # left node of bottom-middle_o <= 0.5
                # Reach a leaf deciding that x wins if the expression is true
                print('x is likely to win')
            else:
                
                # right node of bottom-middle_o <= 0.5
                # Reach a leaf deciding that x doesn't win the expression is false
                print('x is not likely to win')

        # right node of top-left_o <= 0.5
        # if top-right <= 0.5
        elif tictactoe['top right'] != 'o':
            
            # left node of top-right <= 0.5
            # if bottom-left <= 0.5
            if tictactoe['bottom left'] != 'o':
                
                # left node of bottom-left <= 0.5
                # Reach a leaf decifing that x wins
                print('x is likely to win')
            
            # right node of bottom-left_o <= 0.5
            # if middle-left_0 <= 0.5
            elif  tictactoe['left middle'] != 'o':
                
                # left node of middle-left_0 <= 0.5
                # reach a leaf deciding that x wins
                print('x is likely to win')
            else:
                
                # left node of middle-left_0 <= 0.5
                # reach a leaf deciding that x doesn't win
                print('x is not likely to win')
        
        # right node of top-right_o <= 0.5
        # if top-middle_o <= 0.5
        elif tictactoe['top middle'] != 'o':
            
            # right node of top-middle_o <= 0.5
            # reach a leaf deciding that x wins
            print('x is likely to win')
        else: 
            # left node of top-middle_o <= 0.5
            # reach a leaf deciding that x doesn't win
            print('x is not likely to win')
    
    # right node of center_o <= 0.5
    # if bottom-left_o <= 0.5
    elif tictactoe['bottom left'] != 'o':

        # left node of bottom-left <= 0.5
        # if top-left-x <= 0.5
        if tictactoe['top left'] != 'x':

            # left node of top-left_x <= 0.5
            # if bottom-right_x <= 0.5
            if tictactoe['bottom right'] != 'x':
                
                # left node of bottom-right_x <= 0.5
                # Reach a leaf deciding that x doesn't win
                print('x is not likely to win')

            # right node of bottom-right_x <= 0.5
            # in bottom-middle_x <= 0.5
            elif tictactoe['bottom middle'] != 'x':
                
                # right node of bottom-middle_x <= 0.5
                # reach a leaf deciding that x does not win
                print('x is not likely to win')
            else:
                
                # left node of bottom-middle_x <= 0.5
                # reach a leaf deciding that x wins
                print('x is likely to win')
        
        # right node of top-left-x <= 0.5
        # if middle-left_x <= 0.5
        elif tictactoe['left middle'] != 'x':
            
            # left node of top-middle_o <= 0.5
            # reach a leaf deciding that x doesn't win
            print('x is not likely to win')

        # right node of middle-left_x <= 0.5
        # if bottom-left_x <= 0.5
        elif tictactoe['bottom left'] != 'x':
            
            # left node of bottom-right_x <= 0.5
            # Reach a leaf deciding that x doesn't win
            print('x is not likely to win')
        else:
            
            # right node of top-middle_o <= 0.5
            # reach a leaf deciding that x wins
            print('x is likely to win')
        
    
    # right node of bottom-left_o <= 0.5
    # if top-right_x <= 0.5
    elif tictactoe['top right'] != 'x':
        
        # left node of top-right_x <= 0.5
        # reach a leaf deciding that x doesn't win
        print('x is not likely to win')
    else:
        
        # right node of top-right_x <= 0.5
        # reach a leaf deciding that x wins
        print('x is likely to win')
    
    print("=========================\n\n")
