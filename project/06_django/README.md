# Django Intro

## DB

- `models.py`에서 ORM을 사용하여 `Movie` 클래스를 생성하였습니다.
- `Movie`클래스에 `title`, `audience`, `genre`, `score`, `poster_url`, `description`항목을 column으로 저장하였습니다.
- `data.csv`파일을 프로젝트 내부에 옮기고, terminal에서 sql을 사용하여 내부 정보를 import 하였습니다.



## 페이지

`detail`, `edit`, `update`, `delete`에 접근하는 url에 동적으로 할당하여 영화의 Primary Key를 추가하였습니다.



### 1. URL 설정

- 프로젝트 `djangopro/urls.py`에서 중복되는 url인 `movies/`를 `include`를 사용하여 설정합니다.
- 앱 `movies`에 `urls.py`파일을 생성하여 각 페이지로 이동할 url을 작성해줍니다.

### 2. 영화 목록[index]

- 데이터베이스에 존재하는 모든 영화의 `Primary Key`, `title`, `score`를 표시하였습니다.
- 영화의 `title`을 클릭하면 해당 영화 정보 조회 페이지로 이동합니다.
- 새 영화 등록 버튼을 생성하여 클릭하면 새 영화 등록 페이지로 이동하도록 링크를 만듭니다.



### 3. 영화 정보 생성

#### new

- `input`태그와 `textarea`태그를 사용하여 영화 정보를 입력하도록 만들었습니다.
- 영화 등록 버튼 클릭시 `create`로 이동합니다.

#### create

- `new`에서 넘어온 영화 정보를 db에 저장 후 해당 영화 정보 조회 페이지로 이동합니다.



### 4. 영화 정보 조회[detail]

- 해당 Primary Key를 가진 영화의 모든 정보를 표시하였습니다.
- 최 하단에는 목록, 수정, 삭제 버튼을 생성하여 클릭하면, 영화목록, 해당 영화 정보 수정 Form, 해당 영화 정보 삭제 페이지로 이동하도록 링크를 만들었습니다.



### 5. 영화 정보 수정

#### edit

- 해당 Primary Key를 가진 영화의 모든정보를 표시하여 기존 정보에서 수정 할 수 있도록 설정합니다.
- 영화 정보 수정 버튼을 클릭하면 영화 정보를 가지고 `update`로 이동하도록 링크를 만들었습니다.

#### update

- `edit`에서 넘어온 영화 정보를 해당 Primary Key를 가진 기존 영화정보에 다시 저장합니다.
- 저장 후 해당 영화 정보 조회 페이지로 넘어갑니다.

### 6. 영화 정보 삭제[delete]

- 해당 Primary Key를 사용하여 영화의 정보를 데이터베이스에서 삭제합니다.
- 삭제 후 영화 목록 페이지로 넘어갑니다.

