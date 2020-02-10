import urllib.request
from PIL import Image

print("paste_image_url_here" + str(1) + ".JPG", "original/" + str(1) + ".JPG")
urllib.request.urlretrieve("paste_image_url_here" + str(1) + ".JPG", "original/" + str(1) + ".JPG")
im=Image.open("original/" + str(1) +".JPG")
im.show()