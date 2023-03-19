# 웹 개발 미니 프로젝트
> 기술 질문 커뮤니티

## 문제 정의
> 같은 교육을 듣는 교육생끼리의 발자취를 공유하여 필요한 정보를 보다 쉽게 얻을 수 있는 기술 질문 커뮤니티 제작 의도

>대상 : 공통 되는 교육 기관에서 교육을 듣는 모든 교육생

### 🤷 참여 인원
|이름|역할|github|
|:---|:---:|:---:|
|윤예진|베이스 템플릿 제작 및 상속, 네비게이션, 햄버거 제작|https://github.com/Lullunana|
|김주연|피그마를 통한 디자인 초안 및 푸터 제작|https://github.com/suco360|
|노지예|상세 페이지, 유저 페이지 제작|https://github.com/kkumtori|
|이찬웅|마이 페이지 제작|https://github.com/Leecw0610|   
|윤승현|FAQ, QNA 페이지 제작, 서버 데이터 출력|https://github.com/ysh21368|
|조세은|글 작성 폼 제작|https://github.com/ariel-ssen|
|이주환|데이터 베이스 설계 및 CRUD 구현, 서버와 웹 연동하여 데이터 출력|https://github.com/LeeJuHwan|

### 커뮤니티 이용 프로세스
> 신규 이용자
- 회원가입
- 게시글 페이지 이동
- 질문 작성

> 기존 이용자
- 로그인 
- 게시글 페이지 이동
- 질문 또는 답변 작성

> 참고
- 폼 라이브러리를 활용 하여 올바르지 못한 접근이나 입력은 에러를 유도한다.
- 로그인 하지 않은 사용자는 작성글을 읽기 권한은 있으나, 댓글 이나 게시글에 대해 수정 및 삭제 권한은 없다.
- 본인 계정이 아니라면 게시글이나 댓글에 접근 할 수 없다.

> 구조
#### <center><Strong>ERD</center>
<img width="1320" alt="image" src="https://user-images.githubusercontent.com/118493627/210129411-18754f13-f74e-4bee-af0c-575048d4c5e4.png">

#### <center><strong>폴더 구조
<img width="487" alt="image" src="https://user-images.githubusercontent.com/118493627/210129923-725dbe5a-393b-4dcf-8dc5-2595800c47e5.png">
</center>

- 플라스크
    - 서버 생성자 파일
        - 데이터베이스 연동 파일 모듈화
        - 게시판 관련 라우팅 함수 모듈화
        - 로그인 관련 라우팅 함수 모듈화
        - 메인 라우팅 모듈화
    - 폼 시크릿 키 파일

    

## KPT
<hr>

#### Keep
1. 로그인, 로그아웃, 회원가입, 게시글 질의, 게시글 검색, 수정, 삭제, 댓글 작성, 댓글 삭제 정상 구현 기능은 유지

#### Problem
1. 검색 기능, 마이 페이지 데이터베이스 연동, 필터링, 댓글 및 게시글 추천
    - 주어진 시간에 기능을 모두 구현하지 못함


#### Try
1. 게더타운 연동
    - 최초 기능 구현시 기획 했던 시스템이었으나, 못 했던게 너무 아쉬웠다.
2. 리더보드
    - 댓글이나 질문 이용자가 많은 추천을 받을 시 리더보드에 등록 되는 시스템을 구상 했으나 이도 마찬가지로 시간이 부족하여 못 만들었다.













### images
<img width=340px alt="스크린샷 2022-12-31 오후 2 19 53" src="https://user-images.githubusercontent.com/118493627/210126066-edfb4ddc-576a-4603-a8d7-6adef6105ecb.png"><img width=340px alt = "스크린샷 2022-12-31 오후 3.31.19" src="https://user-images.githubusercontent.com/118493627/210127670-63d5deb4-d49a-4bde-be38-acb8fd5c4a8c.png"><img width=340px alt = "스크린샷 2022-12-31 오후 3.31.38" src = "https://user-images.githubusercontent.com/118493627/210127694-a6cb78dd-bb38-4ab9-97a6-b39e49335b73.png" />
<img width=340px height = 300px src = "https://user-images.githubusercontent.com/118493627/210127705-7a24f2d8-0e20-45b9-aa8f-b0a51b59cc45.png">
<img width=340px height = 300px src ="https://user-images.githubusercontent.com/118493627/210127715-23aa7699-f24c-4b58-857e-dc85a080ac91.png">
<img width=340px height = 300px src ="https://user-images.githubusercontent.com/118493627/210127725-18b1a827-faa6-435b-acca-df91e2fac484.png">
<img width=340px height = 300px src ="https://user-images.githubusercontent.com/118493627/210127731-a687aaf1-59ef-4747-a6d2-748cc2b663d9.png">
<img width=340px height = 300px src ="https://user-images.githubusercontent.com/118493627/210127740-9155a5ff-97df-487f-ae2b-a5534388fcf5.png">
<img width=340px height = 300px src ="https://user-images.githubusercontent.com/118493627/210127752-de6f4158-b0c9-4626-95d0-267370fb8cdf.png">
<img width=340px height = 300px src ="https://user-images.githubusercontent.com/118493627/210127760-accacf76-a441-46fd-896c-feb1949a5c97.png">
<img width=340px height = 300px src ="https://user-images.githubusercontent.com/118493627/210127775-3d7b66b9-6d6e-4567-b2ed-35b97f0eec61.png">
<img width=340px height = 300px src ="https://user-images.githubusercontent.com/118493627/210127786-d7b60958-2661-4e10-8978-6705effa257e.png">
<img width=340px height = 300px src = "https://user-images.githubusercontent.com/118493627/210127798-07965e0f-abc5-43c7-9061-cf39a187958f.png">
<img width=340px height = 300px src ="https://user-images.githubusercontent.com/118493627/210127807-1f722bf0-8559-44ac-a422-3dec4d3020a7.png">
<img width=340px height = 300px src ="https://user-images.githubusercontent.com/118493627/210127825-366eeca5-1dc4-4bf2-ab78-b7539396412d.png">
<img width="340px" height = 300px src="https://user-images.githubusercontent.com/118493627/210674389-153fd0a1-46ed-47ac-9f71-a68cfd6f555b.png">

