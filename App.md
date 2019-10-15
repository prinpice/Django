# App

## 생성 패턴

`view` -> `routing` -> `html`



## views.py

* 각 어플리케이션어 대해 각 `view`가 존재함

* 기본 구조

  * 함수 형태
  * view로 정의한 모든 함수는 request를 인자로 가지고 있음

  ```python
  from django.shortcuts import render
  
  def [함수 이름](request):
      return render(request, '[이동할 html파일 명]')
  ```

  * 변수는 dictionary 형태로 보냄(key : String)

  ```python
  from django.shortcuts import render
  
  def [함수 이름](request):
      # return render(request, 'index.html', {'key': 'value'})
      context = {'key': 'value', 'key': 'value'}
      return render(request, '[이동할 html파일 명]', context)
  ```

  예시) 

  ```python
  from django.shortcuts import render
  
  # Create your views here.
  
  def index(request):
      context = {'msg': "hello", "name": "hong"}
      return render(request, 'index.html', context)
  ```

  

## templates

* app 폴더 안에 `templates` 폴더 생성
* 폴더명은 지정되어 있음
* `html`, `css`등의 파일을 저장함

### html

* html 파일명은 함수명과 유사 또는 동일하게 사용함

* `{{}}` : Django Template Language

  예시)

  ```html
  <h1>First Django!</h1>
  <h2>{{name}}</h2>
  <h3>{{msg}}</h3>
  ```

#### base.html

* html에서 반복되는 기본 구조를 저장한 파일

* 바꾸고 싶은 부분은 아래와 같은 문법을 사용한 후 상속받아 사용

  ```html
  {% block %}
  {% endblock %}
  ```

* 기본 구성

  ```html
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <meta http-equiv="X-UA-Compatible" content="ie=edge">
      <title>{%block title%}{%endblock%}</title>
  </head>
  <body>
      {%block body%}
      {%endblock%}
  </body>
  </html>
  ```

* 상속받는 파일에서는 아래의 문법을 사용하여 상속받아 사용

  ```html
  {%extends 'base.html'%}
  ```

  예시)

  ```html
  {%extends 'base.html'%}
  
  {%block title%}
  장고 홈페이지
  {%endblock%}
  
  {%block body%}
  <h1>First Django!</h1>
  <h2>{{name}}</h2>
  <h3>{{msg}}</h3>
  {%endblock%}
  ```

### CSS

* `static` 폴더 생성 후 폴더 안에 파일 생성 가능함

  `templates/static/style.css`

## urls.py

* 사용자가 특정 요청을 url에 보내면 url에서 해당 `view`로 요청을 보냄

  * `urls.py`는 `views`를 모르기 때문에 사용하기 위해서는 import 해줌

    ```python
    from pages import views
    ```

  ```python
  path(url, views.[함수 명])
  ```

  * `url` : url을 입력하여 접근 할 경우 해당 함수로 이동

  * `views.[함수 명]` : 해당 요청을 다룰 view 함수

  * route url

    ```python
    path('', views.index)
    ```

  예시) **기본 구조**

  ```python
  from django.contrib import admin
  from django.urls import path
  from pages import views
  
  urlpatterns = [
      path('admin/', admin.site.urls),
      path('index/', views.index)
  ]
  
  ```

### variable routing



## models.py

* 사용하게 될 다양한 DB(의 생김새)가 들어감

* 모델 지정

  * 자동으로 테이블 생성
  * `id`를 정하지 않으면 자동으로 생성

  ```python
  class [테이블 명](models.Model):
      title = models.TextField()
      content = models.TextField()
  ```

* migration step

  * git과 같이 스냅샷을 찍어 버전관리함
  * `sql`문을 사용하여 `delete table`을 통해 테이블을 삭제하는것 보다는 django ORM을 통하여 id를 사용하여 table 삭제명령을 하는 것이 좋음

  1. migration 파일 생성

     ```git
     $ python manage.py makemigrations
     ```

     * migrations 폴더 안에 `0001_initial.py`가 생성된 것을 볼 수 있음

       **0001 : migration파일의 id**

     * 

