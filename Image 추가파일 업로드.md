# Image 추가/파일 업로드

## 참고개념

* python에서는 선언이 없고, 변수와 상수 개념을 따로 두지 않기 때문에 상수는 대문자로 상수명을 입력하는 것이 약속

  ```python
  var a = 1
  const b = 2
  a = 2
  b = 3
  
  a에 저장된 값 : 2
  b에 저장된 값 : 2
  ```
  
* encoding/decoding의 반복이 많을수록 비효율적임

## 저장소 추가

* 이미지 파일을 사용하기 위해 저장소 위치 선언 및 추가함

  * `settings.py`에 변수 정의(가장 하단에 정의함)

  ```python
  MEDIA_URL = '/media/'
  MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
  ```

  * `project`의 `urls.py`에 url정의(가장 하단에 정의함)

  ```python
  from django.conf.urls.static import static
  from django.conf import settings
  
  # ststic : list를 return하는 함수
  # Dev 에서는 꼭 써야 함. (DEBUG=True) # DEBUG=False이면 빈 리스트를 return 함
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
  ```


## Model 생성(클래스)

* `ImageField`사용함

  * 저장폴더에 `[폴더명]/[폴더명]/[폴더명] ..

  ```python
  class Post(models.Model):
      image = models.ImageField(blank=True, upload_to='[저장폴더경로]')
  ```

## 이미지를 사용하기 위한 패키지

* 이미지를 사용하려면 `pillow`패키지 필요(installedapp에 등록안하는 패키지)

  ```git
  $ pip install pillow
  ```

## 이미지 관리

* admin 페이지에서 이미지가 포함되어있는 클래스를 관리하기 위한 클래스 생성

  예시) 위의 Post클래스 관리

  ```python
  class PostModelAdmin(admin.ModelAdmin):
      readonly_fields = ('create_at', 'updated_at') # 개별화면에서 확인만 가능
      list_display = ('id', 'content', 'created_at', 'updated_at') # 리스트에서 보여질 컬럼들
      list_display_links = ('id', 'content')  # 리스트에서 clickable할 컬럼들
  
  # Register your models here.
  admin.site.register(Posting, PostingModelAdmin) # 여기도 추가해야 함
  ```



## Image Process

* 컴퓨터가 가장 힘들어하는 작업

* **resource는 전부 돈. 이미지 크기마다 비용이 있고 주고받는 것에 모두 비용이 발생함**

* `django-imagekit`설치 및 `settings.py`의 `installedapp`에 추가

  ```
  $ pip install django-imagekit
  ```

  ```python
  ...
  
  INSTALLED_APPS = [
      ...,
      'imagekit',
  ]
  ```

### Image resizing

* db저장(`models.py`)

   * `ImageField`대신 `ProcessImageField`사용

   ```python
   # Imagekit
   from imagekit.models import ProcessedImageField
   from imagekit.processors import ResizeToFit
   
   # Create your models here.
   class Posting(models.Model):
       content = models.TextField(default='')
       icon = models.CharField(max_length=20, default='')
       # Origin
       # # image = models.ImageField(blank=True, upload_to='postings/%Y/%m/%d')
       # image = models.ImageField(blank=True, upload_to='postings/%Y%m%d')
   
       # Resize
       image = ProcessedImageField(
           blank=True,
           upload_to='postings/resize/%Y%m%d',
           # processors=[ResizeToFit(width=960, height=960)], # 복수 이므로 list 가능
           # height와 width를 둘다 주면 비율을 맞추어버려 더 작은 사진도 해당 크기로 맞춰준다.
           processors=[ResizeToFit(width=960, upscale=False)], # 복수 이므로 list 가능
           # upscale=False 이미지가 창의 사이즈에 반응형이 되지 않도록 한다.
           format='JPEG' # 확장자(Processing이 끝났음)
       )
   ```

   * **이미지의 원본 사이즈가 매우 큰 경우 다운받는데 엄청 오래걸림(보이는 사이즈는 마음대로 수정가능**

### thumbnail image 만들기

* `ImageField` 대신 `ImageSpecField`사용(`models.py`)

  ```python
  from imagekit.models import ImageSpecField
  
  image_thumbnail = ImageSpecField(
          source='image',
          processors=[ResizeToFit(width=320, upscale=False)],
          format='JPEG',
          options={'quality': 60}, # 원본 quality의 60%로 유지
      )
  ```

* `image_thumbnail`이 실행되었을 때 해당 파일이 생성됨

### browser cashing

* ctrl + shift + r : 저장된 것을 날리고 새로 받기