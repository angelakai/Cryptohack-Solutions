def egcd(p,q):
    #Initialize variables
    u = p//q #Quotient of p/q
    v = p%q  #Remainder of p/q
    s1=1
    s2=0
    s3 = s1 - u * s2
    t1=0
    t2=1
    t3 = t1 - u * t2 
    #Starting the loop and based on Extended GCD updating the values
    while v!=0:
        p=q  #Assign q to p
        q=v  #Assign v to v
        #Update values
        s1=s2
        s2=s3
        t1=t2
        t2=t3
        #Update u and v for next iteration
        u = p//q
        v = p%q
        #Update s3 and t3 using the extended Euclidean algorithm
        s3 = s1 - u * s2
        t3 = t1 - u * t2
    #Returning the smallest number
    return(min(s2,t2))

print(egcd(26513,32321))
