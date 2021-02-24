def twoStacks(x, a, b):
    i, j, sum = 0,0,0
    while i<len(a) and (sum+a[i])<=x:
        sum+=a[i]
        i+=1
    ans=i
    while j<len(b) and i>=0:
        sum+=b[j]
        j+=1
        while sum>x and i>0:
            i-=1
            sum-=a[i]
        if sum<=x and i+j>ans:
            ans=i+j

    return ans





x = 55
a = [11 ,6, 1, 13, 14, 7, 8 ,10 ,3 ,17 ,7 ,18 ,6 ,4 ,5, 13, 17, 4 ,16 ,9 ,17, 16, 12, 6, 7]
# a = [4,2,4,6,1]
b = [10 ,15, 13, 17, 10, 7 ,0 ,16, 8 ,13, 11, 8 ,14, 13]
# b = [2,1,8,5]
print(twoStacks(x,a, b))

