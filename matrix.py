# written in Python 3.5.3

def matrix_add(lhs, rhs):
    if len(lhs) != len(rhs) or len(lhs[0]) != len(rhs[0]):
        return
    
    result = []

    m = len(lhs)
    n = len(lhs[0])
    
    for i in range(m):
        row = []
        
        for j in range(n):
            row.append(lhs[i][j] + rhs[i][j])
            
        result.append(row)
        
    return result

def matrix_mul(lhs, rhs):
    if len(lhs[0]) != len(rhs):
        return
    
    result = []

    m = len(lhs)
    k = len(lhs[0])
    n = len(rhs[0])
    
    for i in range(m):
        row = []
        
        for j in range(n):
            hap = 0

            for _ in range(k):
                hap += lhs[i][_] * rhs[_][j]
                
            row.append(hap)
            
        result.append(row)
        
    return result
