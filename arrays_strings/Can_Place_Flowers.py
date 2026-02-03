def canPlaceFlowers( flowerbed: list[int], n: int) -> bool:

    l=len(flowerbed)
    i=0
    while(i<l) and n>0:
        if n==0:
            break
        if i==0:
            if flowerbed[i]==0 and flowerbed[i+1]==0:
                flowerbed[i]=1
                n-=1
        elif i==l-1:
            if flowerbed[i]==0 and flowerbed[i-1]==0:
                flowerbed[i]=1
                n-=1
        else:
            if flowerbed[i] == 0 and flowerbed[i + 1] == 0 and flowerbed[i - 1] == 0:
                flowerbed[i] = 1
                n-=1
        i+=1
    if n==0:
        return True
    else:
        return False

print(canPlaceFlowers([1,0,1,0,1],0))