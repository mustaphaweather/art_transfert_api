from PIL import Image
import requests
from io import BytesIO
import numpy as np
from matplotlib import cm




### read content and style
cont_url = "https://widoobizweb.s3.amazonaws.com/wp-content/uploads/2019/05/02124054/rsz-simon-migaj-421505-unsplash-1072x568.jpg"
styl_url = "https://cdn.catawiki.net/assets/marketing/marketing/upload_images-files/26249-4c79df8296bce1edc663949b5602a3fdd76083ce-original.jpg"
num_iter = 50

response = requests.get(cont_url)
img = Image.open(BytesIO(response.content))

data = np.asarray(img)
print(data)
print(data.shape)
imh_1 = Image.fromarray(data.astype('uint8'), 'RGB')

imh_1.show()