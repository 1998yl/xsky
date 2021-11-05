
import json
from selenium import webdriver
import  time
driver = webdriver.Chrome().Option

url = "https://xskydata.jobs.feishu.cn/school"
path="staff.json"
driver.get(url)
time.sleep(10)
temp_2=driver.find_element_by_xpath("/html/body/div[1]/section/section/main/div/div/div[2]/div[3]/div[1]/div[1]").text
num=(temp_2[temp_2.index('（')+1:temp_2.index('）')])
driver.get("https://xskydata.jobs.feishu.cn/school/?keywords=&category=&location=&project=&type=&job_hot_flag=&current=1&limit="+num)
jods = []
time.sleep(10)
trs=driver.find_elements_by_xpath("/html/body/div[1]/section/section/main/div/div/div[2]/div[3]/div[1]/div[2]/a")
for tr in trs:
    staff= tr.find_element_by_xpath("div/div[1]/span").text
    pace=tr.find_element_by_xpath("div/div[2]").text
    centent=tr.find_element_by_xpath("div/div[3]").text
    staffType=pace[pace.index('\n')+1:]
    pace=pace[0:pace.index('\n')]

    centents= centent.split("\n")
    center=""
    for str in centents:
        centent+=str
    jods.append({"职位":staff,"工作地":pace,"工作内容":center,"职位类型":staffType})
data2 = json.dumps(jods,ensure_ascii=False)
print(data2)
print(jods)
with open(path, "w",encoding='utf-8') as f:
    f.write(data2)
print("写入完成")



