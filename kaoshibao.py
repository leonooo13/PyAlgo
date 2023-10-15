from selenium.webdriver.common.by import By
import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from tqdm import tqdm
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Notice

options = Options()
options.add_experimental_option("debuggerAddress", "127.0.0.1:12306")
web = webdriver.Chrome(options=options)
pattern = r'([A-Z])\s+(.+?)\s+(?=[A-Z]|$)'

# url = "https://www.zaixiankaoshi.com/online/?paperId=11418944&practice=&modal=1&is_recite=&qtype=&text=%E9%A1%BA%E5%BA%8F%E7%BB%83%E4%B9%A0&sequence=0&is_collect=1&is_vip_paper=0"
# url="https://www.zaixiankaoshi.com/online/?paperId=11418944&practice=&modal=1&is_recite=&qtype=&text=%E9%A1%BA%E5%BA%8F%E7%BB%83%E4%B9%A0&sequence=30&is_collect=1&is_vip_paper=0"
url="https://www.kaoshibao.com/online/?paperId=11418944&practice=&modal=1&is_recite=&qtype=&text=%E9%A1%BA%E5%BA%8F%E7%BB%83%E4%B9%A0&sequence=30&is_collect=1&is_vip_paper=0"
# 3
url="https://www.kaoshibao.com/online/?paperId=11417507&practice=&modal=1&is_recite=&qtype=&text=%E9%A1%BA%E5%BA%8F%E7%BB%83%E4%B9%A0&sequence=0&is_collect=1&is_vip_paper=0"
# 4
url="https://www.kaoshibao.com/online/?paperId=11418148&practice=&modal=1&is_recite=&qtype=&text=%E9%A1%BA%E5%BA%8F%E7%BB%83%E4%B9%A0&sequence=0&is_collect=1&is_vip_paper=0"

web.implicitly_wait(5)
web.get(url)
time.sleep(3)

for i in tqdm(range(1587)):
    seq = web.find_element(By.XPATH, "//span[@style='float: left; font-weight: 700;']")
    # print(seq.text,end="")

    # locate the question
    question = web.find_element(By.XPATH, "//div[@class='qusetion-box']")
    str_q = question.text
    # print(str_q)

    options = web.find_elements(By.XPATH, "//div[@class='select-left pull-left options-w']")
    # options = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='select-left pull-left options-w']")))
    if not options:
        # options = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='select-left pull-left options-w']")))
        options = web.find_elements(By.XPATH, "//div[@class='select-left pull-left options-w check-box']")
    for opt in options:
        str_opt = re.sub(pattern, r'\1 \2\n', opt.text.replace("\n", " "))  # default is \n in every elem,now
        # replace \n with blank in older to place in a row
        # print(str_opt)

    right_option = web.find_element(By.XPATH, "//div[@class='right-ans']")
    # print(right_option.text.split(" ")[-1])
    right_ans = right_option.text.split(" ")[-1]
    # print("【正确答案】"+right_ans)

    # answer analsis
    # wait = WebDriverWait(web, 10)
    # answer_analysis_ele = wait.until(EC.visibility_of_element_located((By.XPATH, "//p[@class='answer-analysis']")))
    try:
        answer_analysis_ele=web.find_element(By.XPATH,"//p[@class='answer-analysis']")
        ans_explain=answer_analysis_ele.text.replace("\n\n", "\n")
    except Exception as e:
        print("error")
        ans_explain="无"

        # print("【解析】"+answer_analysis_ele.text.replace("\n\n","\n"))
    # Next Click
    with open('4_option_explain.txt', 'a', encoding="utf-8") as f:
        f.write("【题目】\n")
        f.write(seq.text)
        f.write(str_q+"\n")
        f.write("【选项】"+"\n")
        f.write(str_opt+"\n")
        f.write("【正确答案】"+right_ans+"\n")
        f.write("【解析】"+ans_explain+"\n")
        f.write("------------------------------------------------------------------------------"+'\n')
    next_button = web.find_element(By.XPATH, "//button[@class='el-button el-button--primary el-button--small']")
    next_button.click()

web.quit()
