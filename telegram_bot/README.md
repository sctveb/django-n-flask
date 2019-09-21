# hphk 

## day1 - 파이썬 기초 + Web 입문

### 챗봇 link - py.hphk.io

```python
# 안녕
print("안녕하세요")
```

```python
# 메뉴
import random
list = ["20층", "김밥카페", "양자강"]
pick = random.choice(list)

print("오늘의 추천 메뉴는 {menu}".format(menu=pick))
```

```python
# 로또
import random

list = list(range(1,46))
lucky = random.sample(list,6)

print("행운의 번호 : {}".format(sorted(lucky)))
```

```python
# 메뉴사진
import random
list = ["짜장면", "김밥", "탕수육"]
dict = {
  "짜장면":"url",
  "김밥":"url",
  "탕수육":"url"
}
pick = random.choice(list)

print("오늘의 메뉴는 {}입니다!!!".format(pick))
print(dict[pick])
```

```python
# 미세먼지
import requests
from bs4 import BeautifulSoup
url = 'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey=QaGapZXPV5DTM72fy6lrf3hJnrJxhila1UVkPlUCo0N0g0F0RZ9WEngT8RkNjNo4IF%2BikV%2BthQLze39nK4IQjA%3D%3D&numOfRows=10&pageSize=10&pageNo=3&startPage=3&sidoName=%EC%84%9C%EC%9A%B8&ver=1.3'
request = requests.get(url).text
soup = BeautifulSoup(request,'xml')
gangnam = soup('item')[7]
location = gangnam.stationName.text
time = gangnam.dataTime.text
dust = int(gangnam.pm10Value.text)

print("{0} 기준 {1}의 미세먼지 농도는 {2}입니다.".format(time,location,dust))

if(dust > 150):
  print("매우나쁨")
elif(80 < dust <=150):
  print("나쁨")
elif(30< dust and dust <= 80 ):
  print("보통")
else:
  print("좋음")
```

```python
import requests
from bs4 import BeautifulSoup
url = "https://finance.naver.com/sise/"

html = requests.get(url).text
soup = BeautifulSoup(html, 'html.parser')
select = soup.select_one('#KOSPI_now')

print(select.text)
```

### pyenv

[pyenv github](https://github.com/pyenv/pyenv#installation)

- install

  ```bash
  git clone https://github.com/pyenv/pyenv.git ~/.pyenv
  ```

  >pyenv github에서 현재 컴퓨터로 파일 복사

- 환경변수 설정

  ```bash
  echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
  echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile
  # echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bash_profile
  echo 'eval "$(pyenv init -)"' >> ~/.bash_profile
  
  source ~/.bash_profile
  # 환경변수 추가 후 bash_profile 실행 => 터미널 새로고침
  ```


- pyhton install

  ```bash
  pyenv install 3.6.1
  pyenv global 3.6.1
  python -V
  pyenv versions
  ```


## pyenv-virtualenv

- install

  ```bash
  git clone https://github.com/pyenv/pyenv-virtualenv.git $PYENV_ROOT/plugins/pyenv-virtualenv
  ```

- setting

  ```bash
  echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bash_profile
  source ~/.bash_profile
  ```

## virtualenv

- 가상환경 만들기

  ```bash
  pyenv virtaulenv <파이썬 버전> <설정할 가상환경 이름>
  ```

- 가상환경 실행

  ```bash
  pyenv shell <설정한 가상환경 이름>
  # 커
  ```

- 모듈설치

  ```bash
  pip install
  ```

- 가상환경 해제

  ```bash
  
  ```


## telegram bot

### install

- telegram 설치

### bot init

- @BotFather 검색

- /start

- /newbot

- 이름을 생성 => 중복가능

- username => `bot`으로 끝나야하고 유니크한 값

- `token`, `url` 

- url 클릭하여 봇 활성화

- ### telegram.py

  - user id 가져오기

  ```python
  import requests
  token = "봇의 토큰값"
  method_name = "getUpdates"
  url = 'https://api.telegram.org/bot{0}/{1}'.format(token,method_name)
  
  print(url)
  print(requests.get(url))
  ```

  - 유저에게 메세지 보내기

  ```python
  import requests
  token = "763337042:AAEjq0JPofKKdu9_oYwVdi5O5L8JGz_xl6E"
  method_name = "getUpdates"
  url = 'https://api.telegram.org/bot{0}/{1}'.format(token,method_name)
  
  user_id = 'user_id'
  method_name = "sendmessage"
  msg = "안녕하세요!!!"
  msg_url = 'https://api.telegram.org/bot{0}/{1}?chat_id={2}&text={3}'.format(token,method_name,user_id,msg)
  print(msg_url)
  print(requests.get(msg_url))
  ```

  - id 값을 json에서 가져와봅시다.

  ```python
  import requests
  token = "763337042:AAEjq0JPofKKdu9_oYwVdi5O5L8JGz_xl6E"
  method_name = "getUpdates"
  url = 'https://api.telegram.org/bot{0}/{1}'.format(token,method_name)
  update = requests.get(url).json()
  
  user_id = update["result"][0]['message']['from']['id']
  method_name = "sendmessage"
  msg = "안녕하세요!!!"
  msg_url = 'https://api.telegram.org/bot{0}/{1}?chat_id={2}&text={3}'.format(token,method_name,user_id,msg)
  # print(msg_url)
  # print(requests.get(msg_url))
  ```

  - 코스피 정보 가져오기

  ```python
  import requests
  from bs4 import BeautifulSoup
  token = "763337042:AAEjq0JPofKKdu9_oYwVdi5O5L8JGz_xl6E"
  method_name = "getUpdates"
  url = 'https://api.telegram.org/bot{0}/{1}'.format(token,method_name)
  update = requests.get(url).json()
  
  user_id = update["result"][0]['message']['from']['id']
  method_name = "sendmessage"
  
  url_cos = "https://finance.naver.com/sise/"
  html_cos = requests.get(url_cos).text
  soup_cos = BeautifulSoup(html_cos, 'html.parser')
  select = soup_cos.select_one('#KOSPI_now')
  
  msg = select.text
  msg_url = 'https://api.telegram.org/bot{0}/{1}?chat_id={2}&text={3}'.format(token,method_name,user_id,msg)
  # print(msg_url)
  print(requests.get(msg_url))
  
  ```


## Git

git = 분산 버전 관리 시스템

1. init

   1) 저장소를 만든다

2. add

   1) 임시 저장

   2) `git add .`을 사용해서 현재 폴더 및 하위 모든 항목을 추가

   3) `git add <원하는 파일>`로 원하는 파일 하나만 추가

3. commit

   1) 새로운 버전을 만든다

   2) `git commit -m "수정된 내용"`

4.  remote

   1)  원격 저장소 설정

   2) `git remote add origin <url>` - cf. origin이 아니어도 상관 없지만 통상적으로 origin사용

5. push

   1)  내가 원하는 원격 저장소에 코드를 올리겠다

   2) `git push origin master`

6.  자주 사용하는 명령어

   1) `git status` - 폴더/파일의 변화 감지

   2) `git diff` - 몇 번째 줄이 어떻게 바뀌었는지 감지

   3) `git log` - 커밋 이력 확인

   4) `git remote`

7.  git 활용에 도움이 되는 사이트

   1) [누구나 쉽게 이해할 수 있는 Git 입문](https://backlog.com/git-tutorial/kr/)

   2) [git scm](https://git-scm.com/)