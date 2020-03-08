
for i in range(1, 86+1):
    for j in range(1, int(86/5)+1):
        for k in range(1, int(86/10)+1):
            if((i+5*j+10*k) > 86):
                break
            if(((i+j+k) == 16)and((i+5*j+10*k) == 86)):
                print(i, j, k)
