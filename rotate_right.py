def rotate_right_one(arr):
  for i in arr:
    last=arr[4]
    rest=arr[0:4]
    return [last]+rest
arr=[6,7,18,22,9]
right=rotate_right_one(arr)    
print(right)
