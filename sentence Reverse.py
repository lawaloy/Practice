def reverse_words(arr):
  arr.reverse()
  last_item = 0
  for i, char in enumerate(arr):
    if char == " ":
      reverse_part(arr, last_item, i-1)
      last_item = i+1
      
        
  first = last_item
  n = len(arr)-1
  reverse_part(arr, first, n)
      
  return arr

def reverse_part(arr, start_i, end_i):

  while start_i < end_i:
    arr[start_i], arr[end_i] = arr[end_i], arr[start_i]
    start_i += 1
    end_i -= 1
