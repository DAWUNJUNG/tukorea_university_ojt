from fastapi import FastAPI, File, UploadFile, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import uvicorn
import csv
import codecs
import json
import dotenv
from dotenv import find_dotenv, load_dotenv
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import chromedriver_autoinstaller
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

app = FastAPI()
view_dir = Jinja2Templates(directory="view")


@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    context = {}
    context["request"] = request

    return view_dir.TemplateResponse("index.html", context)


@app.post("/upload")
def upload(file: UploadFile = File(...)):
    csvReader = csv.DictReader(codecs.iterdecode(file.file, 'utf-8-sig'))
    data = {}
    for rows in csvReader:
        data[rows['keyword']] = rows['answer']

    with open(f"./learning.conf", 'w+t') as conf:
        conf.write(json.dumps(data))
        conf.close()

    file.file.close()

    gpt_learning()


def gpt_learning():
    # 크로미움 설정
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('headless')
    # chrome_options.add_argument('--no-sandbox')
    # chrome_options.add_argument('window-size=1920x1080')
    # chrome_options.add_argument("disable-gpu")
    chrome_options.add_argument('lang=ko_KR')
    chrome_options.add_argument('ignore-certificate-errors')  # SSL 관련 오류 무시
    chrome_options.add_argument('ignore-ssl-errors')  # SSL 관련 오류 무시

    # 크롬 설치
    chromedriver_autoinstaller.install()

    # 셀레니움 드라이버 설정
    driver = webdriver.Chrome('chromedriver', options=chrome_options)
    driver.get('https://chat.openai.com/auth/login')

    # 로그인 버튼 클릭
    login_xpath = """//div[text()='Log in']"""
    target_wait(driver, 'xpath', login_xpath, 30)
    driver.find_element('xpath', login_xpath).click()

    # 환경 변수 파일 호출
    load_dotenv()

    # ID 입력 후 continue 진행 로직
    target_wait(driver, 'id', 'username', 30)
    username_ele = driver.find_element(By.ID, 'username')
    username_ele.send_keys(os.environ.get('ID'))
    username_ele.send_keys(Keys.ENTER)

    # 비밀번호 입력 후 continue 진행 로직
    target_wait(driver, 'id', 'password', 30)
    password_ele = driver.find_element(By.ID, 'password')
    password_ele.send_keys(os.environ.get('PW'))
    password_ele.send_keys(Keys.ENTER)

    # 초기 가이드 스킵 로직
    # Next 버튼 클릭
    next_btn_xpath = """//div[text()='Next']"""
    done_btn_xpath = """//div[text()='Done']"""
    target_wait(driver, 'xpath', next_btn_xpath, 30)
    driver.find_element(By.XPATH, next_btn_xpath).click()
    target_wait(driver, 'xpath', next_btn_xpath, 30)
    driver.find_element(By.XPATH, next_btn_xpath).click()
    # Done 버튼 클릭
    target_wait(driver, 'xpath', done_btn_xpath, 30)
    driver.find_element(By.XPATH, done_btn_xpath).click()

    # 새로운 채팅 실행
    new_chat_xpath = """//a[text()='New chat']"""
    target_wait(driver, 'xpath', new_chat_xpath, 30)
    driver.find_element(By.XPATH, new_chat_xpath).click()

    #프롬프트 영역 대기
    target_wait(driver, 'id', 'prompt-textarea', 30)
    prompt_ele = driver.find_element(By.ID, 'prompt-textarea')

    learning_data = {}
    with open(f"./learning.conf", 'rt') as conf:
        learning_data = json.loads(conf.read())
        conf.close()

    new_chat_xpath = """//div[text()='Regenerate']"""
    for data in learning_data:
        no_run = False
        if data != list(learning_data.keys())[-1]:
            no_run = True
        for i in range(4):
            # 4번 반복 학습
            prompt_ele.send_keys(f"질문에 '{data}'이 포함되어 있으면 '{learning_data[data]}'라고 답해")
            prompt_ele.send_keys(Keys.ENTER)
            if i == 3 and no_run:
                continue
            else :
                target_wait(driver, 'xpath', new_chat_xpath, 60)

    driver.quit()


def target_wait(driver, element_type, target, timeout):
    if element_type == 'id':
        WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.ID, target))
        )
    elif element_type == 'name':
        WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.NAME, target))
        )
    elif element_type == 'xpath':
        WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.XPATH, target))
        )


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=20081)
