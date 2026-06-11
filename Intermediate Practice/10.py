# ONE OF THE MOST CONFUSING ONE YET
def RotateList(lst,n,direction):
    direction = lst[-n:] + lst[:-n]
    print(direction)

dict = {"List": [1, 2, 3, 4, 5], "Shift": 2, "Direction": 'right'}

RotateList(dict["List"], dict["Shift"], dict["Direction"])


# #def rotate_list(lst, n, direction):
#     if not lst:
#         return lst  # safety check

#     n = n % len(lst)

#     if direction == 'right':
#         return lst[-n:] + lst[:-n]

#     elif direction == 'left':
#         return lst[n:] + lst[:n]

#     else:
#         return "Invalid direction"