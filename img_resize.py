from PIL import Image
import os.path
import glob

#类型
config_anomaly_name = 'pianmo'

#要切割的每一类图像的存放路径
config_original_data_path = "/home/lgz/PycharmProjects/data/membrane/123"  +'/'+config_anomaly_name+"_segment//*.bmp"

#切割好存放的位置
config_target_data_path = "/home/lgz/PycharmProjects/data/membrane/123" +'/'+config_anomaly_name+"_resize"


config_resize_width = 256


config_resize_height = 256

def resize_image(img, outdir, width=256, height=256):

    name = (os.path.basename(img))
    img = Image.open(img)
    new_img = img.resize((width, height), Image.BILINEAR)
    new_img.save(os.path.join(outdir, name))

i=1

if not os.path.exists(config_target_data_path):
    os.mkdir(config_target_data_path)

for img in glob.glob(config_original_data_path):
    print(i, img)
    i += 1
    resize_image(img, config_target_data_path, config_resize_width, config_resize_height)
