nums = [3, 78, 42, 466, 324, 2, 12, 526, 34, 17, 24, 192, 348, 24, 1, 34, 12, 52, 53, 72, 143, 6, 535, 36]

# merge sort has two main sections to it
# the first splits a larger list into two smaller lists
  # split each larger list into two halves specifically
    # we can do that by calculating the midpoint
# the second part will merge two smaller lists into a single larger list
  # I'll have to iterate through each item in the list and compare them all in a WORST CASE SCENARIO

# can I assume that the input will always be a list of integers?
# Yes, for this time.
# are negative numbers and zero acceptable?
# We'll go with positive this time.
# a single list for an input
# output will be the single list but sorted from LEAST TO GREATEST
# is it okay if I alter the original list? or do I need to return a completely new list?
# EITHER IS ACCEPTABLE.
# what happens if there is only one or zero items?
# if there are one or zero items, just return the list.
# should I make this into a single function for more practical use such as exporting it?
# up to me to implement.

# input is named lst
# one single function that contains the whole logic for performing merge sort
def merge_sort(lst):
  # SPLITTING FUNCTION DEFINITION
  def split(ls):
    # output? two lists that are equal halves of the ls input
    # I have ls and I want to split it
    # seems like recursion would be more useful than iteration
    # I need a base case
    # otherwise perform the split
    # return merge() call in some fashion
    if len(ls) <= 1:
      return ls
    # // will ensure that we have an integer rather than float numbers
    midpoint = len(ls) // 2
    left = ls[:midpoint] # does not include midpoint
    right = ls[midpoint:] # does include midpoint
    # merge() takes in two lists
    return merge(split(left), split(right))



  # MERGING FUNCTION DEFINITION
  # merge is going to take two lists as an input
  # both inputs are sorted already
  def merge(ls1, ls2):
    # I need to compare each item in both lists in a WORST CASE SCENARIO
    # iteration
    output = []
    while len(ls1) and len(ls2):
      # inside of the while loop I'll be removing items from each list
      # so I was asking myself how do I compare an empty list with a non-empty list?
      # I can't - because there are no values to compare
      if ls1[0] < ls2[0]:
        output.append(ls1.pop(0))
      else:
        output.append(ls2.pop(0))
    # output the merged list that has been sorted
    return output + ls1 + ls2
    

  # Call split function
  return split(lst)

print(merge_sort(nums))
