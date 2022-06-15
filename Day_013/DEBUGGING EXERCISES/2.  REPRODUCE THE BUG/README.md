# Reproduce the Bug

```
from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(1, 6)
print(dice_imgs[dice_num])
```

# Bug -- randint function includes both endpoints, hence it will throw an index error when index of six occurs 
