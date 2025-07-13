def rotate_left_one(arr):
  if len(arr)==0:
    return arr
  first=arr[0]
  rest=arr[1:]
  return rest+[first]
arr=[6,7,18,22,9]
rotated=rotate_left_one(arr)
print(rotated)    
