from __init__ import create_app
from gevent.pywsgi import WSGIServer
from config import Config
import os



application = create_app()
# print(Config.KEY_PATH)
# print(Config.CERT_PATH)
# # server = WSGIServer(('127.0.0.1', 5000), application)
# # server = WSGIServer(('127.0.0.1', 5000 ), application,  keyfile=Config.KEY_PATH, certfile=Config.CERT_PATH)
# # server = WSGIServer(('127.0.0.1', 5000), application,  keyfile='key.pem' , certfile='cert.pem')
PORT = int(os.environ.get("PORT", 5000))
print(PORT)
server = WSGIServer(('127.0.0.1', PORT), application)
server.serve_forever()

