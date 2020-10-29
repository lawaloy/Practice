def convert(self, s: str, numRows: int) -> str:
        
    s_length = len(s)
        
    if numRows == 1 or numRows >= s_length:
        return s
    stack = [""] * numRows
    index, step = 0, 1
        
    for string in s:
        stack[index] += string
        if index == 0:
            step = 1
                
        elif index == numRows-1:
            step = -1
        index += step
            
    return "".join(stack)
    

                
                
