import torchvision.transforms as transforms
from PIL import Image
import requests
from io import BytesIO
import torch
import matplotlib.pyplot as plt

### class of loading ad preparing image from url
class Show_image():

    def __init__(self,tensor):
        ### save the urls for style and content
        self.tensor = tensor
        self.unloader = transforms.ToPILImage()

    def imshow(self,title):
        tensor = self.tensor
        image = tensor.cpu().clone()  # we clone the tensor to not do changes on it
        image = image.squeeze(0)      # remove the fake batch dimension
        image = self.unloader(image)
        plt.imshow(image)
        if title is not None:
            plt.title(title)
        plt.pause(0.001)

