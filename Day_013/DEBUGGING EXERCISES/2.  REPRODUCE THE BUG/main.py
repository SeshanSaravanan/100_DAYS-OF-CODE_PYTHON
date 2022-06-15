# # Reproduce the Bug -- Solution


from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(0, 5)  # here the index in debugged 
print(dice_imgs[dice_num])
