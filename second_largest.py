def find_second_largest(arr):
  if len(arr)<2:
     return None
  largest=second=float("-inf") 
  for i in arr:
    if i>largest:
       second=largest
       largest=i
    elif i>second and i!=largest:
       second=i
  return second if second!=float("-inf") else None
arr=[6,7,18,22,9]
result=find_second_largest(arr)
print(result)
