# Rest API

c9의 insta에서 작성됨



## Setting

* 폴더 생성 및 들어가기

  ```git
  piie:~/workspace $ mkdir API
  piie:~/workspace $ cd API/
  ```

* 가상환경 설정(python 버전확인)

  ```git
  $ pyenv virtualenv 3.6.7 api-venv
  $ pyenv local api-venv
  ```

* django와 rest-framework 설치(django를 그냥 설치하면 2.2버전이 설치되기 때문에 지정해줘야 한다.)

  ```git
  (api-venv)$ pip install django==2.1.7
  (api-venv)$ pip install djangorestframework
  ```

* settings.py 에 경로와 사용할 앱을 넣어준다.

  * 아래와 같이 특정 주소가 아닌 '*'를 넣어주면 어디서든지 돌아가게 하겠다는 뜻이다.

    => 보안상으로 좋지 않다.

  ```python
  ALLOWED_HOSTS = ['*'] 
  INSTALLED_APPS = [
      ...
      'rest_framework',
  ]
  ```

* 프로젝트와 앱 생성

  ```git
  (api-venv)$ django-admin startproject api .
  (api-venv)$ python manage.py startapp music
  ```

* settings.py에 앱 추가

  ```python
  INSTALLED_APPS = [
      ...
      'rest_framework',
      'music',
  ]
  ```



## 사용할 Model을 정의하자

* models.py에서 model 생성

  ```python
  from django.db import models
  
  # Create your models here.
  # Artist, Music, Comment
  
  class Artist(models.Model):
      name = models.TextField()
      
      def __str__(self):
          return self.name
          
  class Music(models.Model):
      title = models.TextField()
      artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
      
      def __str__(self):
          return self.title
          
          
  class Comment(models.Model):
      content = models.TextField()
      music = models.ForeignKey(Music, on_delete=models.CASCADE)
      
      def __str__(self):
          return self.content
  ```

* migrate(model이 수정되었기 때문)

  ```git
  (api-venv)$ python manage.py makemigrations
  (api-venv)$ python manage.py migrate
  ```

* 관리자계정 생성

  ```git
  (api-venv)$ python manage.py createsuperuser
  ```

* 관리자 페이지에서 볼 수 있도록 admin.py에 추가

  ```python
  from django.contrib import admin
  from .models import Artist, Music, Comment
  
  
  # Register your models here.
  admin.site.register(Artist)
  admin.site.register(Music)
  admin.site.register(Comment)
  ```

* 메인 문지기에서 정의

  * 특정 url을 입력하였을 때 해당 앱의 urls.py로 보낸다.
  * 일반적으로(strict로 하면) 끝에 '/'를 붙이지 않으나 장고에서 사용하기 때문에 붙인다.
  * api/v1이 들어가는 url은 다음으로 보내라(해당 경로)

  ```python
  from django.contrib import admin
  from django.urls import path, include
  
  urlpatterns = [
      path('admin/', admin.site.urls),
      path('api/v1/', include('music.urls')),
  ]
  ```

  * 기본 정의
    * 모든 Artist 다 가져올 때 : GET '/artists/'
    * 특정 Artist 한 명만 가져올 때 : GET '/artists/1'
    * Artist를 만들 때 : POST '/artists/'
    * Artist를 수정할 때 : POST/PATCH '/artists/1'
    * Artist를 지울 때 : DELETE '/artists/1'
  * api의 JSON만 받아오고 싶을 때, api를 앞에 붙여준다.
    * 모든 Artist 다 가져올 때 : GET 'api/artists/'
    * 특정 Artist 한 명만 가져올 때 : GET 'api/artists/1'
    * Artist를 만들 때 : POST 'api/artists/'
    * Artist를 수정할 때 : POST/PATCH 'api/artists/1'
    * Artist를 지울 때 : DELETE 'api/artists/1'
  * 또는 도메인 시작을 api로 지정해도 된다.

* music 앱에 서브문지기 생성 및 정의

  ```python
  from django.urls import path
  from . import views
  
  urlpatterns = [
      # HOST/api/v1/musics
  ]
  ```



## Read

### music_list(전체보기) 생성

* music 앱의 urls.py에 list로 가는 경로를 작성

  ```python
  from django.urls import path
  from . import views
  
  urlpatterns = [
      # HOST/api/v1/musics
      path('musics/', views.music_list, name="list"),
  ]
  ```

* views.py에서  music_list 생성

  * api_view : api로 포장하기 위해 사용함

  ```python
  from django.shortcuts import render
  from rest_framework.decorators import api_view
  from .models import Music
  
  # Create your views here.
  
  # 허용할 HTTP Method
  @api_view(['GET'])
  def music_list(request):
      musics = Music.objects.all()
      return serializer(시리얼라이저) 객체를 반환(json)
  ```

  * serialize(JSON.stringify)
    * 중립적 포멧 형태로 사용하기 위해 파일로 변환해주는 것
    * django가 python/javascript 파일 내용을 JSON으로 바꿔줌
  * serializers.py 생성 및 작성

  ```python
  from rest_framework import serializers # 클래스 안에서 상속받아 사용하게 되어 있음
  from .models import Music
  
  class MusicSerializer(serializers.ModelSerializer):
      class Meta:
          model = Music
          fields = ['id', 'title', 'artist', ]
      
      
  # class MusicForm(forms.ModelForm): 모델폼과 사용방법 같음
  #   class Meta:
  #       model = 
  #       fields = []
  ```

  * views.py에 serializer추가

  ```python
  from django.shortcuts import render
  from rest_framework.decorators import api_view
  from rest_framework.response import Response
  from .serializers import MusicSerializer
  from .models import Music
  
  # Create your views here.
  
  # 허용할 HTTP Method
  @api_view(['GET']) # api로 포장해서 가기 위해 사용
  def music_list(request):
      musics = Music.objects.all()
      
      # serializer = MusicSerializer(어떤 것을 json파일로 만들지, many=True)
      serializer = MusicSerializer(musics, many=True)
  
      return Response(serializer.data) # Response라는 객체에 담아 반환
  ```

### music_detail(상세보기) 생성

* urls.py에 경로를 지정함

  * 참고) app_name과 path안의 name은 api에서 사용하지 않기 때문에 작성하지 않아도 된다.

  ```python
  from django.urls import path
  from . import views
  
  
  app_name="musics" # app_name도 써줘도 되고 안써줘도 됨
  
  urlpatterns = [
      ...,
      # 특정 music을 보여주는 url
      path('musics/<int:music_id>/', views.music_detail, name="detail"), # api 서버에서는 name을 쓸 일이 없다.
  ]
  ```

* views.py에서 메인 코드를 작성

  ```python
  from django.shortcuts import render, get_object_or_404
  from rest_framework.decorators import api_view
  from rest_framework.response import Response
  from .serializers import MusicSerializer
  from .models import Music
  
  # Create your views here.
  
  ...
  
  @api_view(['GET'])
  def music_detail(request, music_id):
      # 1개의 특정한 Music을 가져오는 코드
      music = get_object_or_404(Music, pk=music_id)
      serializer = MusicSerializer(music) # many=True를 작성하지 않으면 default값이 들어간다 # default : False
      print(serializer)
      print(dir(serializer))
      return Response(serializer.data)
  ```

## Swagger

* 프로젝트에서 지정한 URL들을 HTML 화면으로 확인할 수 있게 해주는 module

### swagger를 사용해보자

* 설치하기

  ```git
  (api-venv)$ pip install django-rest-swagger
  ```

* settings.py에 추가

  ```python
  INSTALLED_APPS = [
  	...
      'rest_framework',
      'rest_framework_swagger',
      'music',
  ]
  ```

* sub문지기(urls.py)에서 경로 설정

  ```python
  from django.urls import path
  from . import views
  from rest_framework_swagger.views import get_swagger_view # swagger는 자체적으로 많은 것을 해줌
  
  app_name="musics" # app_name도 써줘도 되고 안써줘도 됨
  
  urlpatterns = [
   	...,
      path('docs/', get_swagger_view(title="API 문서")) # 제목을 여기서 줄 수 있다.
  ]
  ```

  => 서버를 돌려보면 우리의 view를 알아서 읽어서 자동으로 만들어준 것을 볼 수 있음



## Create

#### post로 create 생성

* rest하게 짜기 위해서 post로도 받을 수 있도록 수정해야 함
* urls.py에서는 post와 get이 동일하게 들어오기 때문에 views.py에서 받아서 분깃함

* views.py 작성하기

  ```python
  @api_view(['GET', 'POST'])
  def music_list(request):
      if request.method == "POST":
          # CREATE (Form과 사용방법 동일함)
          serializer = MusicSerializer(data = request.data) #  POST로 넘어온 값은 data에 들어 있다. # key는 선택작성(안써도 됨)
          if serializer.is_valid():
              serializer.save()
              return Response(serializer.data)
      else:
           # READ (LIST)
          musics = Music.objects.all()
          
          # serializer = MusicSerializer(어떤 것을 json파일로 만들지, many=True)
          serializer = MusicSerializer(musics, many=True)
          
          # return 시리얼라이저 객체를 반환(json)
          return Response(serializer.data) # Response라는 객체에 담아 반환
  ```

  * 위와 같이 작성했을 때, 입력을 잘못하였을 경우 is_valid()를 통과하지 못함 => error는 발생하지 않지만 이상한 페이지로 넘어감

    => is_valid()에 raise_exception을 추가함

    * raise_exception=True : 검증이 안되면 통과하지 못하며 error를 발생하도록 해줌

  ```python
  @api_view(['GET', 'POST'])
  def music_list(request):
      if request.method == "POST":
          ...
          if serializer.is_valid(raise_exception=True): 
              serializer.save()
              return Response(serializer.data)
      else:
          ...
  ```