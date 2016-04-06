def pt(n):
    triples = []
    for a in range(1,n):
        for b in range(1,n):
            for c in range(b,n):
                if (a*a + b*b == c*c):
                    triples.append([a,b,c])
    return triples

#print pt(16)
        
def pt2(n):
    return [(a,b,c) for a in range(1,n) for b in range(a+1,n) for c in range(b+1,n) if (a*a + b*b == c*c)]

#print pt2(16)


    
