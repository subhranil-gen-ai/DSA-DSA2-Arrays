def count_max_element(arr):
  frequency={}
  for i in arr:
    if i in frequency:
        frequency[i] += 1
    else:
        frequency[i] = 1
  max_element=max(frequency.keys())
  count=frequency[max_element]      
  print(f" {max_element} -> {count} times")
  return count
arr=[2,4,4,1,1,3,9]
max_count=count_max_element(arr)
