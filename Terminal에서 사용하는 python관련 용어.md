 # Terminal에서 사용하는 python관련 용어

* `pip list`

  * 설치된 패키지와 버전 확인

  ```git
  (practice-venv) piie:~/workspace/PRACTICE $ pip list
  Package    Version
  ---------- -------
  Django     2.1.7  
  pip        10.0.1 
  pytz       2018.9 
  setuptools 39.0.1 
  You are using pip version 10.0.1, however version 19.0.2 is available.
  You should consider upgrading via the 'pip install --upgrade pip' command.
  ```

* `tree`

  * 폴더 구조 보기

  ```git
  (practice-venv) piie:~/workspace/PRACTICE $ tree .
  .
  ├── manage.py //거의 건드리지 않음 // 많이 불러옴
  └── practice
      ├── __init__.py //django패키지 -> 건드리지 않음
      ├── settings.py //가장 많이 사용
      ├── urls.py //가장 많이 사용
      └── wsgi.py //배포할 때 사용
  
  1 directory, 5 files
  ```

  