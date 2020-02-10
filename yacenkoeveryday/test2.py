import time
import vk_api
import schedule
import random
import requests
import threading


from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType


def write_msg(user_id,s):
    vk.method('messages.send', {'user_id': user_id, 'message': s, 'random_id':''})

def write_chat_msg(peer_id,s):
    vk.method('messages.send', {'peer_id': peer_id, 'message': s, 'random_id':''})

def job():
    print("I'm working...")
    #write_chat_msg(2000000000 + 1, 'hello world')
    photo4ka(random.randint(1, 9), 2000000000 + 3)
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

def thread():
    while True:
        schedule.run_pending()
        time.sleep(1)

token = "paste_your_token_here"
vk = vk_api.VkApi(token=token)

vk._auth_token()
vk2=vk.get_api()
#try:
#    vk.auth()

#except vk_api.AuthError as error_msg:
#    print(error_msg)

#write_msg('175383048', 'hello world')

# timeik="05:42"
#
# schedule.every().day.at(timeik).do(job)
#
#
# x = threading.Thread(target=thread, args=())
# x.start()


write_msg(197324579,'С Днём Рождения!')



# longpoll = VkBotLongPoll(vk,186365852)
#
# while True:
#     for event in longpoll.listen():
#         if event.type == VkBotEventType.MESSAGE_NEW:
#             print('yacenkoeveryday')
#             if event.object.peer_id != event.object.from_id:
#                 if event.object.text.lower().split(" ")[1] == "set":
#                     hours,minutes= event.object.text.lower().split(" ")[2].split(":")
#                     h=int(hours)
#                     m=int(minutes)
#                     if h<=24 and h>=0 and m>=0 and m<60 and len(hours)<=2 and len(minutes)<=2:
#
#                         if h>21:
#                             h=3+h -24
#
#                         else:
#                             h=h+3
#                         hours = str(h)
#                         if h < 10: hours = '0' + hours
#                         timeik=str(hours) + ":" + str(minutes)
#                         print(timeik)
#                         schedule.every().day.at(timeik).do(job)
#                         write_chat_msg(event.object.peer_id, "OKAY")
#                     else:
#                         write_chat_msg(event.object.peer_id, "Неверный формат времени")
#                 # vk.method("messages.send", {"peer_id": event.object.peer_id, "message": 'Приём',
#                 #                                "random_id": 0})
#                 else:
#                     photo4ka(random.randint(1,9),event.object.peer_id)
#                 print(event.object.peer_id)
#             else:
#                 #if event.object.text.lower() == "привет":
#                 # vk.method("messages.send", {"user_id": event.object.from_id, "message": 'Приём',
#                 #                                 "random_id": 0})
#                 photo4ka(random.randint(1, 9),event.object.from_id)
#

