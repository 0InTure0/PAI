#-*- coding:utf-8 -*-
import urllib3
import json
import base64
openApiURL = "http://aiopen.etri.re.kr:8000/WiseASR/Recognition"
accessKey = "87e83362-6183-4a71-930f-5ce4515ea20a"
audioFilePath = "hello.wav"
languageCode = "korean"

file = open(audioFilePath, "rb")
audioContents = base64.b64encode(file.read()).decode("utf8")
file.close()

requestJson = {"access_key": accessKey, "argument": {"language_code": languageCode, "audio": audioContents}}
http = urllib3.PoolManager()
response = http.request("POST", openApiURL, headers={"Content-Type": "application/json; charset=UTF-8"}, body=json.dumps(requestJson))

#print("[responseCode] " + str(response.status))
#print("[responBody]")
print((str(response.data,"utf-8")))
#녹음된 음성만 문자열로 바꿔주는 기능
list_data = list(str(response.data,"utf-8"))
data_length = len(list_data)
a = "".join(list_data[43:data_length-3])
print(a)
