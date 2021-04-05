# Settings

c9의 workspace에서 작성됨

### pyenv

* 다양한 버전의 파이썬을 관리하는 도구

* url : `zzu.li/install-pyenv`

* 검색 : how to install pyenv on ubuntu

* terminal에 pyenv, pyenv-virtualenv 설치

  ```git
  git clone https://github.com/pyenv/pyenv.git ~/.pyenv
  echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
  echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
  echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bashrc
  exec "$SHELL"
  
  git clone https://github.com/pyenv/pyenv-virtualenv.git $(pyenv root)/plugins/pyenv-virtualenv
  echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc
  exec "$SHELL"
  ```

  * `exec "$SHELL"` : reload (창을 껏다가 킨 것과 같은 기능)

### python 설치

* pyenv를 사용하여 원하는 버전 다운로드

  ```git
  $ pyenv install [version]
  ```

* 3.6 버전부터 fstring이 사용 가능함

* 현재 전역으로 설정되어 있는 버전 확인

  ```git
  $ python --version
  ```

* 원하는 버전을 설치해도 전역으로 바꿔주지 않으면 기존 버전을 사용하므로 전역 설정이 필요함

* 전역 설정

  ```git
  $ pyenv global [version]
  ```

* 정리하면

  ```git
  pyenv install 3.6.7
  pyenv global 3.6.7
  ```



### 프로젝트 생성

* (전체)폴더 == 프로젝트

* 프로젝트 진행할 폴더 생성 및 해당 폴더로 이동

  ```git
  $ mkdir [폴더이름]
  $ cd [폴더이름]
  ```

  * mkdir :  폴더를 생성하는 명령어
  * cd : 특정 위치로 이동하는 명령어

* 가상환경 생성 및 설정

  ```git
  $ pyenv virtualenv [가상환경 버전] [가상환경 이름]
  $ pyenv local [가상환경 이름]
  ```

  * pyenv virtualenv : 가상 환경 생성

  * pyenv local : 해당 디렉토리에 특정 가상환경을 지정함(독립된 공간으로 만들어 가상환경으로 들어감), 해당 디렉토리는 프로젝트 폴더

  * 가상환경을 지정하면 아래와 같이 됨

    ```git
    ([가상환경 이름]) $
    ```

  * pyenv virtualenv에 3.6.7 버전으로 practice-venv 이름을 가진 가상환경을 만들어 달라고 요청

    ```git
    $ pyenv virtualenv 3.6.7 practice-venv
    $ pyenv local practice-venv
    (practice-venv) $
    ```

* django 설치

  * 사용하려는 python과 호환되는 버전으로 지정하여 설치
  
* 가상환경안에서 설치하는 경우 가상환경에만 설치가 됨
  * python 3.6.7과 호환되는 django버전은 2.1.7이기 때문에 버전을 지정하여 설치함
  
  ```git
$ pip install django==2.1.7
  ```
  
* Django 프로젝트 생성

  * 프로젝트 명과 프로젝트 폴더 이름은 공식적으로 맞춰줌(달라도 됨)
  * 프로젝트에 필요한 파일 설치

  ```git
  $ django-admin startproject [프로젝트 명] .
  ```

  * `.` : 현재 폴더에 생성하겠다는 의미로 입력하지 않으면 내부에 폴더가 추가적으로 생성됨
  
* Django 실행하기

  ```git
  python manage.py runserver $IP:$PORT
  ```

  * `settings.py`에서 설정 없이 실행할 경우 오류가 발생할 수 있음
  * 로켓 그림이 나오면 제대로 동작한 것

### 환경 설정(settings.py)

* **django는 reload하지 않아도 자동적으로 적용을 해주므로 새로고침만 하면 되지만 설정파일(settings.py)를 수정할 때는 서버를 꺼주는 것이 좋음**

* 접근 가능한 주소 지정

  ```python
  ALLOWED_HOSTS = ['앱 주소']
  ```

  * `앱 주소`에 `*`을 넣을 경우 모든 주소 접근을 허용함

* Internationalization(i18n)

  * 언어 수정(한글로)

    ```python
    LANGUAGE_CODE = 'ko-kr'
    ```

  * 시간 수정(서울로)

    ```python
    TIME_ZONE = 'Asia/Seoul'
    ```

### 앱 생성

* **django 프로젝트 안에 여러개의 앱이 존재할 수 있음**
* 프로젝트 안에서 앱을 설치하여 사용함

```git
$ python manage.py startapp [앱 이름]
```

* 앱을 생성할 경우 `settings.py`에 추가해야함

  ```python
  INSTALLED_APPS = [
  	'[앱 이름]',
  ]
  ```

   **트레일링 콤마 붙이는 것을 표준으로 함(마지막 인자에도 콤마 붙임)**

### url 추가

**기본구조(필수사항)**

```python
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
```

* 앱으로 이동할 url을 추가

  * 앱 안에 `urls.py`파일이 존재해야함

    `include`를 import 하고, 원하는 url 지정해줌

    ```python
    from django.contrib import include
    
    urlpatterns = [
        path('[url주소]/', include('[앱이름].urls'))
    ]
    ```

* 앱 안의 함수로 바로 이동가능함

  * 사용하고자 하는 앱의 `views`를 import하여 사용함

    ```python
    from [앱이름] import views
    
    urlpatterns = [
        path('[url주소]/', views.[함수이름])
    ]
    ```
  
  * 경로의 이름을 지정하여 사용가능함
  
    ```python
    urlpatterns = [
        path('[url주소]', views.[함수이름], name='[경로(를 간단하게 사용할 )이름]')
    ]
    ```

  ```python
  from django.contrib import admin, include
  from django.urls import path
  from posts import views
  
  urlpatterns = [
      path('admin/', admin.site.urls),
      path('posts/', include('posts.urls')),
      path('home/', path.views, name="home"),
      
  ]
  ```







