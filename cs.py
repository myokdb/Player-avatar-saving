import requests,base64,json,io
from PIL import Image

def FetchSkin(name):
  fetchuuid = "https://api.mojang.com/users/profiles/minecraft/"#玩家uuid
  fetchBase64 = "https://sessionserver.mojang.com/session/minecraft/profile/"#玩家皮肤披风
  uuid = requests.get(fetchuuid+name)#玩家uuid
  Base64 = requests.get(fetchBase64+uuid.json()["id"]).json()["properties"][0]["value"]#未处理的Base64
  skin = json.loads(base64.b64decode(Base64).decode())["textures"]["SKIN"]["url"]#经过解码获取到的皮肤图片链接
  
  return skin

def SaveAvatar(skin,name):
  image = Image.new('RGB', (8,8), 'red') #创建图片
  skin = Image.open(io.BytesIO(requests.get(skin).content))#获取皮肤
  image.paste(skin.crop((8, 8, 16, 16)),(0,0))#剪切并粘贴
  image.save(name+".png")#以玩家名保存图片
  return

#name = "name"                     #玩家名字
#FetchSkin(name)                   #玩家皮肤链接
#SaveAvatar(FetchSkin(name),name)  #对皮肤裁切出同像并保存

with open('name.json', 'r') as f:
    name_list = json.load(f)

# 循环遍历名单并执行函数
for name in name_list:
    SaveAvatar(FetchSkin(name), name)
