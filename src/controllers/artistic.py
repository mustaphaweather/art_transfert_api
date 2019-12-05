import connexion
import sys
import json
from logbook import Logger , ERROR, WARNING, DEBUG, INFO
sys.path.append("..")
from services.art_transfert import Art_transfert
from PIL import Image
import requests
from io import BytesIO
import numpy as np

log = Logger('logbook' , INFO)

def trans_art ():

	log.info('Calling art_transfert endpoint')

	if connexion.request.is_json:
		body = connexion.request.get_json()
		body_parse_content_url = body["content"]
		log.debug('content url : {}'.format(body_parse_content_url))
		body_parse_style_url = body["style"]
		log.debug('style url : {}'.format(body_parse_style_url))
		body_parse_num_ter = body["iter_num"]
		log.debug('num_iter : {}'.format(body_parse_num_ter))
		mod = Art_transfert(body_parse_content_url,body_parse_style_url,body_parse_num_ter)
		try:
			response = {"art_url" : mod.save_out()} , 200
			# response = requests.get("https://cdn.radiofrance.fr/s3/cruiser-production/2019/11/9daed29a-083d-44ad-ada4-cd8036250350/801x410_joker.jpg")
			# img = Image.open(BytesIO(response.content))
			# response = {"art_url" : np.asarray(img)} , 200
		except KeyError:
			response = {} , 404

	return response




	
