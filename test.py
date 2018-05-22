
# encoding: utf-8 
import Augmentor
from PIL import Image
import os

import shutil



imgpath='D:/test_augmentor/B/'
imgs = os.listdir(imgpath)

#print(imgs)
# print(imgpath+str(imgs[0]))

imgNum = len(imgs)

# 创建的目录
path = "D:/test_augmentor/B/456"

#================================================================

for i in range(2142):
    file=path+'/'+str(i)
    os.mkdir(file,0755)
    #print(i,'done!==============================')
    #print(imgpath+str(imgs[i+1]))
    img = Image.open(imgpath+str(imgs[i+1]))
    #print(file+'/'+str(imgs[i+1]))
    img.save(file+'/'+str(imgs[i+1]))
    #print(file)
    p = Augmentor.Pipeline(file)
    #p.rotate(probability=1, max_left_rotation=16, max_right_rotation=16)
    
    p.random_distortion(probability=1,grid_height=8,grid_width=8,magnitude=8)
    p.rotate(probability=1, max_left_rotation=10, max_right_rotation=10)
    #p.zoom(probability=1, min_factor=0.5, max_factor=0.8)
    p.sample(40)
    
    output=file+'/output/'
    #print('output:',output)
    out_imgs = os.listdir(output)
    #print('output:',out_imgs)
    out_len=len(out_imgs)
    for j in range(out_len):
        take=output+str(out_imgs[j])
        #print("take:",take)
        i_ = Image.open(take)
        save_img=file+'/'+str(out_imgs[j])
        #print('to:',save_img)
        i_.save(save_img)
        #print("save:",j+1,"done!")
   

for i in range(2142):
    p=path+'/'+str(i)+'/output/'
    print('remove:',p)    
    shutil.rmtree(p)      

#====================================================

# for i in range(2142):
    # file=path+'/'+str(i)
    # #print(file)
    # print(i,": ",file)
    # p = Augmentor.Pipeline(file)
    
    # #2形变
    # #p.skew(probability=1,magnitude=1)
    
    # # #3---弹性扭曲1
    # #p.random_distortion(probability=1,grid_height=6,grid_width=6,magnitude=8)


    # # #4弹性扭曲2
    # p.random_distortion(probability=1,grid_height=8,grid_width=8,magnitude=8)
    # p.rotate(probability=1, max_left_rotation=10, max_right_rotation=10)

    # # #5错切变化
    # #p.shear(probability=1,max_shear_left=12,max_shear_right=12)


    # # #6截取
    # #p.crop_by_size(probability=1,width=100,height=100,centre=True)


    # # #7镜像变换
    # #p.flip_random(probability=1)
    
    
    # p.sample(40)
    
    # output=file+'/output/'
    # #print('output:',output)
    # out_imgs = os.listdir(output)
    # #print('output:',out_imgs)
    # out_len=len(out_imgs)
    # for j in range(out_len):
        # take=output+str(out_imgs[j])
        # #print("take:",take)
        # i_ = Image.open(take)
        # save_img=file+'/'+str(out_imgs[j])
        # #print('to:',save_img)
        # i_.save(save_img)
        # #print("save:",j+1,"done!")
        
# for i in range(2142):
    # p=path+'/'+str(i)+'/output/'
    # print('remove:',p)    
    # shutil.rmtree(p)  
    
#====================================================

    

# p = Augmentor.Pipeline("./A")

# #旋转
# p.rotate(probability=1, max_left_rotation=16, max_right_rotation=16)
# p.zoom(probability=1, min_factor=0.5, max_factor=0.8)


#
#p.skew(probability=1,magnitude=1)


#----弹性扭曲1
#p.random_distortion(probability=1,grid_height=6,grid_width=6,magnitude=8)


#弹性扭曲2
# p.random_distortion(probability=1,grid_height=8,grid_width=8,magnitude=8)
# p.rotate(probability=1, max_left_rotation=10, max_right_rotation=10)

#错切变化
#p.shear(probability=1,max_shear_left=12,max_shear_right=12)


#截取
#p.crop_by_size(probability=1,width=100,height=100,centre=True)


#镜像变换
#p.flip_random(probability=1)

#p.flip_left_right(probability=1)
#p.flip_top_bottom(probability=1)


# p.sample(15)














































# encoding: utf-8 
# import Augmentor
# p = Augmentor.Pipeline('./A')

# #旋转
# p.rotate(probability=1, max_left_rotation=16, max_right_rotation=16)
# p.zoom(probability=1, min_factor=0.5, max_factor=0.8)


# #形变
# #p.skew(probability=1,magnitude=1)


# #----弹性扭曲1
# #p.random_distortion(probability=1,grid_height=6,grid_width=6,magnitude=8)


# #弹性扭曲2
# # p.random_distortion(probability=1,grid_height=8,grid_width=8,magnitude=8)
# # p.rotate(probability=1, max_left_rotation=10, max_right_rotation=10)

# #错切变化
# #p.shear(probability=1,max_shear_left=12,max_shear_right=12)


# #截取
# #p.crop_by_size(probability=1,width=100,height=100,centre=True)


# #镜像变换
# #p.flip_random(probability=1)

# #p.flip_left_right(probability=1)
# #p.flip_top_bottom(probability=1)


# p.sample(6426)



