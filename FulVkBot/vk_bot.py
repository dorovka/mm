import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from course import *
from wikipedia import *
from wiki import *

token = "vk1.a.08XIe0VH5IiT6QP2AL2p9sEVzPl4pkDsvWLVXzz1ZeZKBSu0ILGV6p5_iRlHF8B2L_zwC6sE0Q0moR6EfCj4QluW-zNLxwFnFSU1MswVH-ObdRN3T9poMwH7BSQgSWRqzJUyJLymjIJRVTSDfmGeWvRMZ4ts6wKgtd8JS5Nn6EdMDRD4Sm9wHHyZeD-bcH1Pp5OM53yGBtQTeFF7Wk2xsA"

bot = vk_api.VkApi(token =token)
Vk = bot.get_api()
longpoll = VkLongPoll(vk=bot) #зажми ctrl и нажми на VkLongPoll

for event in longpoll.listen():
    print(event.type)
    if event.type == VkEventType.MESSAGE_NEW:
        msg = event.text.lower()
        user_id = event.user_id
        random_id = event.message_id
        print(f'{user_id} {msg}')
        if 'валюта' in msg and 'евро' in msg:
            response = "{0} рублей за евро".format(get_course("R01239"))
            Vk.messages.send(user_id=user_id, random_id=random_id, message=response)

        elif 'валюта' in msg and 'доллар' in msg:
            response = "{0} рублей за доллар".format(get_course("R01235"))
            Vk.messages.send(user_id=user_id, random_id=random_id, message=response)

        elif 'валюта' in msg and 'белорусский рубль' in msg:
            response = "{0} рублей за белорусский рубль".format(get_course("R01090B"))
            Vk.messages.send(user_id=user_id, random_id=random_id, message=response)



        elif msg[:3] == 'вик':
            art = msg[3:]
            wiki = get_wiki(art)
            Vk.messages.send(user_id = user_id, random_id = random_id, message =wiki)


        elif msg != True:
            print('1')
            Vk.messages.send(user_id = user_id, random_id = 1, message = 'Ошибка')