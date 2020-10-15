import vk_api, time,colorama
from colorama import Fore, Back, Style
from vk_api import VkUpload
colorama.init()

priva = [
"""
EDIT BY ANDRO HACKS   ( ͡° ͜ʖ ͡°)
"""
]

opicanya = [
"""
Накрутка фотографий в ВК\nЧто бы продолжить впишите пароль
"""
]
print(Fore.GREEN + priva[0])
print(Fore.RED + opicanya[0])
vibor = input('-->')
if vibor == "andr0 hAck":
	login1 = input('Введите логин от страницы:')
	password1 = input('Введите пароль от страницы:')
	album = input('Введите ID альбома:')
vk_session = vk_api.VkApi(login=login1, password=password1, app_id='2685278')
vk_session.auth(token_only=True)
vks = vk_session
upload = VkUpload(vk_session)

while True: 
	upload.photo(photos="photo.jpg",album_id=album)
