def second_smallest_element(arr):
  if len(arr)<2:
    return None
  smallest=second=float("inf")
  for i in arr:
    if i<smallest:
      second=smallest
      smallest=i
    elif i<second and i!=smallest:
      second=i
    else:
      return second if second!=float("inf") else None
arr=[6,7,18,22,9]
result=second_smallest_element(arr)
print(result)
