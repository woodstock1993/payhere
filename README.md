<div align="center"><img src="https://user-images.githubusercontent.com/67543838/210616105-a53b771a-f8bc-4524-afd4-5a626c8eb0bc.png"></div>


# 목차

- [구현 요구사항](#구현-요구사항)
- [구현](#구현)
- [명세](#명세)
- [Step to run](#step-to-run)

## 구현 요구사항
- [x] 회원가입
- [x] 로그인
- [x] 로그아웃
- [x] 가계부 CRUD
- [x] 특정 가계부 복사
- [x] 가계부 전체 목록 조회
- [x] 가계부 세부내역 공유

## 구현

### 기술 스택
<img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=Python&logoColor=white"/> <img src="https://img.shields.io/badge/Django-092E20?style=flat-square&logo=Django&logoColor=white"/> <img src="https://img.shields.io/badge/SQLite-003B57?style=flat-square&logo=SQLite&logoColor=white"/> <img src="https://img.shields.io/badge/PyCharm-000000?style=flat-square&logo=PyCharm&logoColor=white"/> <img src="https://img.shields.io/badge/VSCode-007ACC?style=flat-square&logo=Visual Studio Code&logoColor=white"/>

### 개발 기간
- 2023.01.03 - 2023.01.05


## 명세
<img width="1444" alt="image" src="https://user-images.githubusercontent.com/67543838/210618278-54b01ef7-3304-4b27-9328-129fb84854fb.png">


### 인증 테스트 방법
- api/member/join : 회원가입
<img src="https://user-images.githubusercontent.com/67543838/210619918-afb98067-0a72-40b6-bcc2-654f3deecb87.png">
<img width="1266" alt="image" src="https://user-images.githubusercontent.com/67543838/210620099-38188521-b3c0-4ee2-ad1c-3d9cd470b022.png">


- api/member/login : 로그인후 JWT token 획득
<img width="1271" alt="image" src="https://user-images.githubusercontent.com/67543838/210620265-5515a227-629b-49da-ba16-103ba357c541.png">


#### swagger 페이지에 'JWT + {획득한 어세스 토큰} 기입, JWT 한칸 띄우고 access_token 기입후 Authorize Click 
<img width="1261" alt="image" src="https://user-images.githubusercontent.com/67543838/210620530-b1ed4027-5a44-4f45-922b-18c4bbfb7be1.png">
<img width="614" alt="image" src="https://user-images.githubusercontent.com/67543838/210620617-3932c3a1-83bd-4894-a4c1-15a2a431d7aa.png">


#### 이후 모든 API 호출
- api/member/logout
- api/member/token/refresh
- api/post
- api/post/{id}
- api/post/{id}/copy

### Step to run
```
$ python -m venv venv
$ source venv/vin/activate [MAC]
$ python install -r requirements.txt
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver
```
