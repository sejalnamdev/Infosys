s = str(input())

mp = {}
ans = -1

for ch in s:
    if ch  in mp:
        mp[ch] += 1
    else:
        mp[ch] = 1

for i in range(len(s)):
    if mp[s[i]] == 1:
        ans = i
        break

print(ans)



