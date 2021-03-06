# Django 데이터베이스 설계



## DB

- models.py에 Genre, Movie, Score class를 작성하였습니다.
- 제공된 genre.csv와 movie.csv파일을 통해 데이터베이스에 반영하였습니다.

### Movies

- 영화목록
  - /movies/ 경로를 통해 영화 목록에 접근하도록 하였습니다.
  - 영화목록페이지에는 모든 영화의 목록이 표시되고, 각 영화의 title과 영화포스터를 표시하였습니다.
  - title을 클릭 시 해당 영화정보조회페이지로 이동하도록 설정하였습니다.
- 영화정보조회
  - /movies/movie_id/경로를 통해 영화정보조회페이지로 이동하도록 하였습니다.
  - movie_id에는 영화에 해당하는 primarykey가 들어갑니다.
  - 해당 Primary Key를 가진 영화의 모든 정보를 표시하였습니다.
  - 영화정보 최 하단에는 목록 수정 삭제 링크가 있으며, 목록을 클릭하면 영화목록으로, 삭제를 클릭하면 영화를 삭제하도록만들고 수정버튼은 disabled로 만들었습니다.
- 영화정보삭제
  - /movies/movie_id/delete/ 경로를 통해 영화를 삭제하는 기능을 실행하도록 하였습니다.
  - 삭제 후에 영화 정보 목록 페이지로 redirect하는 기능을 생성하였습니다.
- 평점 목록
  - 평점에 대한 html 파일을 따로 만들어 영화정보조회 페이지에 include하였습니다.
  - 평점 목록에서는 한줄평과 평점을 모두 출력합니다.
- 평점 삭제
  - 작성자가 영화정보조회에 들어갔을 때 삭제버튼을 볼 수 있게 구현하였습니다.
  - 삭제부튼 클릭시 해당 Primary Key를 가진 평점 정보를 데이터베이스에서 삭제한 후 영화 정보 조회 페이지로 redirect하도록 구현하였습니다.