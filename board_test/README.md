# 플라스크 게시판 만들기
#### [파이썬 환경 설정](https://github.com/mcDeeplearning/TIL/blob/master/%ED%8C%8C%EC%9D%B4%EC%8D%AC%20%ED%99%98%EA%B2%BD%EC%84%A4%EC%A0%95.md)

### 데이터베이스

- 설정
```bash
$ sudo apt-get update
# ubuntu에 postgresql 설치
$ sudo apt-get install postgresql postgresql-contrib libpq-dev
# python(flask)에서 postgresql를 사용하기 편하게 해주는 psycopg2 설치
$ pip install psycopg2 psycopg2-binary
# import 해서 쓸 친구들
$ pip install Flask-SQLAlchemy Flask-Migrate
```

- DB 설정
```bash
$ psql
ubuntu=# CREATE DATABASE DB이름 WITH template=template0 encoding='UTF8';
ubuntu=# \q
```

### 'models.py' 설정
### 'app.py' 설정
### migration

- flask db initialize : `flask db init`
- `migration`폴더 생성
- 파일의 현재 상태를 반영 : `flask db migrate`
- `flask db upgrade`
- psql board