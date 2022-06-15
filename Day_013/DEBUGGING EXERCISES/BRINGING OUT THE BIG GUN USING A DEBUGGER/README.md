# #Use a Debugger

```
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
  b_list.append(new_item)
  print(b_list)

mutate([1,2,3,5,8,13])
```

## BUG
  - HERE THE b.list append(new_item) is outside of the for loop. So it gives output corresponding to the last item in the a.list
