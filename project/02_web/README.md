# 영화평점서비스 CSS/HTML

## HTML
1. html언어는 한국어(ko), 인코딩은 UTF-8로 설정
2. Bootstrap사용
3. 파비콘링크 삽입
4. Navigation Bar
    * 최상단에 위치하며 반응형으로 구성되어 있음
    * Sticky-top 클래스 사용 - Sticky navigation bar로 구성되어 스크롤을 내리면 상단에 navigation bar가 고정되어 있음
    * disabled 클래스 사용 - Home을 제외한 Item List의 속성들을 클릭불가능하게 설정함
5. Header
    * Navigation Bar 바로 아래에 위치함

6. 레이아웃
    * 영화 리스트는 container에 속함
7. subtitle
    * h3 태그에 글씨 입력함
8. Card view
    * row, col 클래스 사용 - 카드 6개를 반응형으로 배치
    * 한 줄에 보이는 카드개수: 
        * 576px 미만 : 1개
        * 576px 이상 768px 미만 : 2개
        * 768px 이상 992px 미만 : 3개
        * 992px 이상 : 4개
    * img의 alt속성은 해당 영화이름 입력함
    * h4 태그에 영화 제목 입력함
    * 영화제목 옆에 네이버 영화 평점 작성함 - badge-info를 사용하여 9점 이상인 경우 청색 계열의 색을 지정함
    * 영화 장르와 개봉일 작성함
    * a 태그(영화정보 바로가기)에 네이버 영화 상세 정보 링크를 만듬(새 창)
9. 영화 상세 보기
    * modal, carousel을 사용 - 포스터 이미지를 클릭하면 영화에 대한 상세 정보와 추가 이미지 보여줌
    * 영화의 한글명과 영문명을 같이 작성함
10. Footer
    * 브라우저 최하단(내용 최하단)에 위치함
    * a와 img태그를 사용하여 오른쪽에 header로 올라가는 링크 설정함

## CSS
1. Navigation Bar
    * Navbar의 배경색을 흰색(#fff), 투명도를 50%(0.5)로 하여 스크롤 이동을 할 때 페이지의 정보가 가려지지 않도록 함
2. Header
    * 높이 350px 설정
    * 좌우 padding을 390px로 주어 글자가 두 줄로 출력되게 함
    * 백그라운드 이미지를 아래쪽에 두어서 이미지는 반투명하게 만들고 글씨가 원래와 같이 출력되게 함(#header, #header::after)
    * text-align을 사용하여 글자를 가운데 정렬함
    * title 폰트는 Black Han Sans, sans-serif 사용(**폰트1**)
3. subtitle
    * 위아래 margin 3rem 설정함
    * subtitle 폰트는 Black Han Sans, sans-serif 사용(**폰트1**)
    * weight가 70px인 #7e5bef 색 밑줄 삽입함
4. card view
    * 각 카드의 위아래 margin 1rem 설정함
    * text-align을 사용하여 왼쪽정렬함
    * card의 폰트는 Jua, sans-serif 사용(**폰트3**)
5. Footer
    * 높이 50px, 좌우 padding 3rem 설정
    * footer 전체 폰트는 Sunflower, sans-serif 사용(**폰트2**)
## Bootstrap
    * Navbar, Card, Modal, Carousel 사용함