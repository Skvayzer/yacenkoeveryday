import time
import vk_api
import schedule
import random
import requests


from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType


def write_msg(user_id,s):
    vk.method('messages.send', {'user_id': user_id, 'message': s, 'random_id':''})

def write_chat_msg(peer_id,k):
    s=k[0]*'РАДОЗДЬ\n'
    vk.method('messages.send', {'peer_id': peer_id, 'message': s, 'random_id':''})

def job(k):
    print("I'm working...")
    write_chat_msg(2000000000 + 3,k)
    k[0]=k[0]*2
    #photo4ka(random.randint(1, 9), 2000000000 + 1)
def photo4ka(i,id):
    session = requests.Session()
    attachments = []
    upload = vk_api.VkUpload(vk)
    image_url = 'paste_image_url_here' + str(i) + '.jpg'
    image = session.get(image_url, stream=True)
    photo = upload.photo_messages(photos=image.raw)[0]
    attachments.append(
        'photo{}_{}'.format(photo['owner_id'], photo['id'])
    )
    vk2.messages.send(
        peer_id=id,
        attachment=','.join(attachments),
        message="Yacenko",
        random_id=''
    )

token = "paste_your_token_here"
vk = vk_api.VkApi(token=token)

vk._auth_token()
vk2=vk.get_api()
#try:
#    vk.auth()

#except vk_api.AuthError as error_msg:
#    print(error_msg)

#write_msg('175383048', 'hello world')

k=[1]

timeik="05:05"

schedule.every(1).seconds.do(job,k)





#write_chat_msg(2000000000 + 1,'Соня, как ты?')

longpoll = VkBotLongPoll(vk,186365852)

while True:
    schedule.run_pending()
    time.sleep(2)

