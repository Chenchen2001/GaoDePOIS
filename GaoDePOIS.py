import requests
key = "<Your GaoDe POIS API KEY HERE>" # key of GaoDe API, get it from GaoDe
keywords = "<Your Keyword Here>" # The keyword you want to search
offset = 99999  # the offset of a search
types = "风景名胜;风景名胜相关;旅游景点" # type of what you want
output_filename = "data.txt" # the output file's name

cities = ["北京市","天津市","上海市","重庆市","河北省","山西省","辽宁省","吉林省","黑龙江省","江苏省","浙江省","安徽省","福建省","江西省","山东省","河南省","湖北省","湖南省","广东省","海南省","四川省","贵州省","云南省","陕西省","甘肃省","青海省","台湾省","内蒙古自治区","广西壮族自治区","西藏自治区","宁夏回族自治区","新疆维吾尔自治区","香港特别行政区","澳门特别行政区"] # 城市列表
# list above is all provinces of China
for city in cities:
    params = {"key": key, "keywords": keywords, "city": city, "offset" : offset, "types" : types}
    response = requests.get("https://restapi.amap.com/v3/place/text?", params) # send request
    res = response.json() # get response 
    with open(output_filename, "a") as f: # write it into file
        for i in res["pois"]:
            f.write(i['pname']+","+i['name']+","+i['pname']+i['cityname']+i['adname']+(i['address'] if type(i['address'])== str else "-无具体地址-")+"\n")