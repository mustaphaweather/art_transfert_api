import torchvision.transforms as transforms
from PIL import Image
import requests
from io import BytesIO
import torch

### class of loading ad preparing image from url
class Image_loader():

    def __init__(self,content_url,style_url,imsize,device):
        ### save the urls for style and content
        self.content_url = content_url
        self.style_url = style_url
        self.loader = transforms.Compose([
                            transforms.Resize(imsize),  # scale imported image
                            transforms.ToTensor()])  # transform it into a torch tensor
        self.device = device

    def image_loader_path_content(self):
        image_path = self.content_url
        response = requests.get(image_path)
        image = Image.open(BytesIO(response.content))
        # fake batch dimension required to fit network's input dimensions
        size_ = image.size
        image = self.loader(image).unsqueeze(0)
        return [image.to(self.device, torch.float),size_]

    def image_loader_path_style(self,ctn_size):
        image_path = self.style_url
        response = requests.get(image_path)
        image = Image.open(BytesIO(response.content))
        ## resize to content size
        image = image.resize(ctn_size, Image.NEAREST) 
        # fake batch dimension required to fit network's input dimensions
        image = self.loader(image).unsqueeze(0)
        return image.to(self.device, torch.float)
