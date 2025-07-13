def count_frequency(arr):
  frequency={}
  for i in arr:
    if i in frequency:
      frequency[i] += 1
    else:
      frequency[i] = 1
  for key,value in frequency.items():
    print(f"{key} -> {value} times")    
  return frequency 
arr=[2,4,4,1,1,3,9]
count=count_frequency(arr)
print(count)
