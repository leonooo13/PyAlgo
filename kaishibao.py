from selenium.webdriver.common.by import By
import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
# Notice

options = Options()
options.add_experimental_option("debuggerAddress", "127.0.0.1:12306")
web = webdriver.Chrome(options=options)
pattern = r'([A-Z])\s+(.+?)\s+(?=[A-Z]|$)'

# url = "https://www.zaixiankaoshi.com/online/?paperId=11418944&practice=&modal=1&is_recite=&qtype=&text=%E9%A1%BA%E5%BA%8F%E7%BB%83%E4%B9%A0&sequence=0&is_collect=1&is_vip_paper=0"
# url="https://www.zaixiankaoshi.com/online/?paperId=11418944&practice=&modal=1&is_recite=&qtype=&text=%E9%A1%BA%E5%BA%8F%E7%BB%83%E4%B9%A0&sequence=30&is_collect=1&is_vip_paper=0"
url="https://www.zaixiankaoshi.com/online/?paperId=11418944&practice=&modal=1&is_recite=&qtype=&text=%E9%A1%BA%E5%BA%8F%E7%BB%83%E4%B9%A0&sequence=730&is_collect=1&is_vip_paper=0"
web.implicitly_wait(5)
web.get(url)
time.sleep(5)
for i in range(700):
    # if i % 50 == 0:
    #     web.implicitly_wait(0.3)
    # else:
    #     if i % 2 == 0:
    #         web.implicitly_wait(0.2)
    #     else:
    #         web.implicitly_wait(1)
    try:
        seq = web.find_element(By.XPATH, "//span[@style='float: left; font-weight: 700;']")
    except:
        print("seq error")
    finally:
        # web.implicitly_wait(1)
        seq = web.find_element(By.XPATH, "//span[@style='float: left; font-weight: 700;']")
    with open('mutilopt.txt', 'a', encoding="utf-8") as f:
        seq_num = seq.text
        print(seq_num, end="")
        f.write(f"{seq_num}")

    # locate the question
    question = web.find_element(By.XPATH, "//div[@class='qusetion-box']")

    with open('mutilopt.txt', 'a', encoding="utf-8") as f:
        str_q = question.text.replace("\n", " ")
        print(str_q)
        f.write(str_q + '\n')

    options = web.find_elements(By.XPATH, "//div[@class='select-left pull-left options-w']")
    if not options:
        try:
            options = web.find_elements(By.XPATH, "//div[@class='select-left pull-left options-w check-box']")
        except:
            print("option error")
        finally:
            # web.implicitly_wait(0.3)
            options = web.find_elements(By.XPATH, "//div[@class='select-left pull-left options-w check-box']")
    for opt in options:
        with open('mutilopt.txt', 'a', encoding="utf-8") as f:
            try:
                str_opt = re.sub(pattern, r'\1 \2\n', opt.text.replace("\n", " "))  # default is \n in every elem,now
            except:
                print("option error")
            # replace \n with blank in older to place in a row
            finally:
                str_opt = re.sub(pattern, r'\1 \2\n', opt.text.replace("\n", " "))
                print(str_opt)
                f.write(str_opt)

    # locate the right answer
    try:
        right_option = web.find_element(By.XPATH, "//div[@class='right-ans']")
    except:
        print("e")
    finally:
        web.implicitly_wait(0.1)
        right_option = web.find_element(By.XPATH, "//div[@class='right-ans']")

    with open('mutilopt.txt', 'a', encoding="utf-8") as f:
        right_ans = right_option.text.replace("\n", " ")
        print(right_ans)
        f.write("\n" + right_ans + "\n")

    # Next Click
    next_button = web.find_element(By.XPATH, "//button[@class='el-button el-button--primary el-button--small']")
    next_button.click()

web.quit()
