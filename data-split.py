#!/usr/bin/env python
# coding: utf-8

# In[2]:





import random,os,shutil
train = 0.7
valid = 0.13
test = 0.17
path = "/notebooks/storage/dataset-resized"
train_dir = path + '/train'
valid_dir = path + '/valid'
classes = os.listdir(path + '/dataset-resized/')
def create_dir():
    for c in classes:
        os.makedirs(train_dir + '/' + c)
        os.makedirs(valid_dir + '/' + c)

def move_files():
    for c in classes:
        src = path + '/dataset-resized' + '/' + c #os.path.join(path,'dataset-resized',c)
        filenames = os.listdir(src)
        count = len(filenames)
        num_train_files = int(train * count)
        num_valid_files = int(valid * count)
        for _ in range(num_train_files):
            new_src = os.listdir(src)	
            choice = random.choice(new_src)
            dest = train_dir +'/'+ c
            print(dest)
            shutil.move(src + '/' + choice, dest)
        for _ in range(num_valid_files):
            new_src = os.listdir(src)
            choice = random.choice(new_src)
            dest = valid_dir + '/' + c
            shutil.move(src + '/' + choice, dest)

create_dir()
move_files()


# In[ ]:




