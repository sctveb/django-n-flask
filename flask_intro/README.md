# flask
- 파이썬 환경 설정

- 플라스크

  ```bash
  pip install flask
  ```

- `app.py`

  ```python
  from flask import Flask
  app = Flask(__name__)
  
  @app.route("/")
  def hello():
      return "Hello World!"
  ```

- flask 구동

  ```bash
  flask run --host 0.0.0.0 --port 8080
  ```