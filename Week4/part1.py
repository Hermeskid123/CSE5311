def merge(a, b, c):
    m = len(a)
    n = len(b)
    o = len(c)
    i = 0 
    j = 0
    k = 0
 
    ans = []
 
    while i < m and j < n and k < o:
 
        small = min(a[i], b[j], c[k])
 
        ans.append(small)
 
        if a[i] == small:
            i += 1
        elif b[j] == small:
            j += 1
        elif c[k] == small:
            k += 1
    while i < m and j < n:
        if a[i] <= b[j]:
            ans.append(a[i])
            i += 1
        else:
            ans.append(b[j])
            j += 1
    while j < n and k < o:
        if b[j] <= c[k]:
            ans.append(b[j])
            j += 1
        else:
            ans.append(c[k])
            k += 1
    while i < m and k < o:
        if a[i] <= c[k]:
            ans.append(a[i])
            i += 1
        else:
            ans.append(c[k])
            k += 1
    while i < m:
        ans.append(a[i])
        i += 1
    while j < n:
        ans.append(b[j])
        j += 1
    while k < o:
        ans.append(c[k])
        k += 1
 
    return ans
 
array1 = [1,3,5,7]
array2 = [2,4,6,8]
array3 = [0,9,10,11] 
ans = merge(array1,array2,array3)
print(ans)

array1 = [1,3,7]
array2 = [2,4,8]
array3 = [9,10,11]

ans = merge(array1,array2,array3)
print(ans)


