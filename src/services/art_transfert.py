from __future__ import print_function

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
from services.image_loader import Image_loader
from services.show_image import Show_image
from services.content_loss import ContentLoss
from services.style_loss import StyleLoss
from services.normalization import Normalization
from services.get_style_los import get_style_model_and_losses
from services.style_transfert import get_input_optimizer ,run_style_transfer


class Art_transfert():

    def __init__(self,cont_url,styl_url,num_iter):
        print('START PROGRAMM')
        start_1 = time.time()

        ### test if the GPU through cuda is available , else use CPU
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        # desired size of the output image
        imsize = 300 if torch.cuda.is_available() else 128  # use small size if no gpu
        if torch.cuda.is_available() : print("RUN USING GPU")

        test_ = Image_loader(cont_url , styl_url , imsize , device)
        content_img_req = test_.image_loader_path_content()
        content_img = content_img_req[0]
        content_img_size = content_img_req[1]
        style_img = test_.image_loader_path_style(content_img_size)

        assert style_img.size() == content_img.size(), \
            "we need to import style and content images of the same size"

        cnn = models.vgg19(pretrained=True).features.to(device).eval()
        cnn_normalization_mean = torch.tensor([0.485, 0.456, 0.406]).to(device)
        cnn_normalization_std = torch.tensor([0.229, 0.224, 0.225]).to(device)
        # desired depth layers to compute style/content losses :
        content_layers_default = ['conv_4']
        style_layers_default = ['conv_1', 'conv_2', 'conv_3', 'conv_4', 'conv_5']
        input_img = content_img.clone()

        end_1 = time.time()
        print('END PROGRAMM')
        print ('Time taken: {} seconds'.format(end_1-start_1))

        print('START TRANSFERT FUNCTION')
        start = time.time()
        output = run_style_transfer(cnn, cnn_normalization_mean, cnn_normalization_std,
                                    content_img, style_img, input_img, num_iter,
                                    1000000, 1,content_layers_default ,style_layers_default, device)
        end = time.time()
        print('END TRANSFERT')
        print ('Time taken: {} seconds'.format(end-start))
        output_1 = output
        image = output_1.cpu().clone()  # we clone the tensor to not do changes on it
        image = image.squeeze(0)      # remove the fake batch dimension
        unloader = transforms.ToPILImage()
        image = unloader(image)
        ## resize to content size
        content_img_size = (968, 512)
        image = image.resize(content_img_size, Image.NEAREST) 
        # print(image.size)
        # image.save('data/images/output_.jpg')
        self.image = image

    def save_out(self):
        self.image.save('data/images/output_.jpg')


