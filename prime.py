

ans = 1
for j in range(1,21):
    for i in range(max(ans,j),ans*j+1):
        if i%ans == 0 and i%j==0:
            ans = max(ans,i)
            break
    continue

print ans
