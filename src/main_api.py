from services.art_transfert import Art_transfert
import time
import torch


### read content and style
cont_url = "https://widoobizweb.s3.amazonaws.com/wp-content/uploads/2019/05/02124054/rsz-simon-migaj-421505-unsplash-1072x568.jpg"
styl_url = "https://cdn.catawiki.net/assets/marketing/marketing/upload_images-files/26249-4c79df8296bce1edc663949b5602a3fdd76083ce-original.jpg"
num_iter = 50

art_transfert = Art_transfert(cont_url , styl_url , num_iter)
art_transfert.save_out()