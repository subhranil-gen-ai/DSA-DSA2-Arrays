arr=[6,7,18,22,9]
count=0
avg= sum(arr)/len(arr)
for i in arr:
  if i ==  avg:
    count += 1 
print(count) 
