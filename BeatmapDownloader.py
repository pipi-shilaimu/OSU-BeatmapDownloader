import json
import requests

#输入osusearch.com获取的内容
print("______________________________________________________________")
print("本脚本需要搭配osusearch.com使用。进入网站，在筛选条件之后使用搜索，后将URL输入即可，获取的osz文件会储存在根目录，如有报错请搭配VPN使用")
searchURl = input("输入osusearch.com获取的URL:")
#截取后半部分
var1 = searchURl.partition("?") 
list1 = list(var1)
var2 = "?"+str(list1[2])
#拼接
var3 ="https://osusearch.com/query/"+var2
response = requests.get(var3)
data = json.loads(response.text)
# 使用列表推导式提取 beatmapset_id
beatmapset_ids = [x["beatmapset_id"] for x in data["beatmaps"]]
#转换为str
beatmapset_ids_list = [str(i) for i in beatmapset_ids]
length = len(beatmapset_ids_list)
lstr = str(length)
count = input("检索到"+lstr+"个结果，请输入将要下载的数量:")
#获取URL，使用镜像：Chimu.moe
def getdownloadURl(beatmapset_ids_list):
    return "https://api.chimu.moe/v1/download/"+beatmapset_ids_list+"?n=1"
DownloadURl=list(map(getdownloadURl,beatmapset_ids_list))
#遍历列表DownloadURl，下载osz
for n in range(int(count)):
    name=beatmapset_ids_list[n]+".osz"
    print(str(n+1)+"/"+count)
    f=requests.get(DownloadURl[n])
    with open(name,"wb") as code:
        code.write(f.content)
    





