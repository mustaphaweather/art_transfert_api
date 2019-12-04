import matplotlib as plt
import time
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from PIL import Image
import requests
from io import BytesIO
import matplotlib.pyplot as plt
import torchvision.transforms as transforms
import torchvision.models as models
import copy

from image_loader import Image_loader
from show_image import Show_image

### test if the GPU through cuda is available , else use CPU
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
# desired size of the output image
imsize = 300 if torch.cuda.is_available() else 128  # use small size if no gpu
if torch.cuda.is_available() : print("RUN USING GPU")

cont_url = "https://widoobizweb.s3.amazonaws.com/wp-content/uploads/2019/05/02124054/rsz-simon-migaj-421505-unsplash-1072x568.jpg"
styl_url = "https://images.unsplash.com/photo-1552510373-7a6449943736?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&w=1000&q=80"

test_ = Image_loader(cont_url , styl_url , imsize , device)
image_ctn = test_.image_loader_path_content()
image_sty = test_.image_loader_path_style(image_ctn[1])

show_test = Show_image(image_sty)
plt.ion()
plt.figure()
show_test.imshow('style image')
plt.figure()




