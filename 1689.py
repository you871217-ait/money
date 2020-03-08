for i in range(1, 1689+1):
    for j in range(1, int(1689/5)+1):
        for k in range(1, int(1689/10)+1):
            for l in range(1,int(1689/50)+1):
             if((i+5*j+10*k+50*l) > 1689):
                break
             if(((i+j+k+l) == 108)and((i+5*j+10*k+50*l) == 1689)):
                print(i, j, k,l)

         
