# 서울 소상공인 상권 정보 테스트 페이지 구현

## Data
사용 데이터 : 국가중점데이터 中 [상권정보 데이터](https://www.data.go.kr/data/15083033/fileData.do) csv 다운로드 -- 서울만 이용

해당 데이터 명을 seoul-commercial-district.csv로 변경 -> server/uploads/seoul-commercial-district.csv에 위치시킴

## Server(back) - Client(front)

flask - Vue.js3로 구현 : [flask - vue 구현 참고 사이트](https://testdriven.io/blog/developing-a-single-page-app-with-flask-and-vuejs/)


## Sever : Flask Setup

server 디렉토리로 이동 (전체 프로젝트를 새로 생성하려 하는 과정 중이라면 server 폴더를 직접 만든 후 이동)
```sh
cd server
```
가상환경 생성
```sh
python -m venv venv
```
가상환경 접속
```sh
venv/Scripts/activate
```

flask 설치
```sh
pip install Flask==2.2.3 Flask-Cors==3.0.10
```
flask 실행
```sh
flask run
```



## Client : Vue Setup
Vue Project를 위해서 로컬에 Node.js와 npm 설치 선행적으로 필요 : [node.js설치](https://nodejs.org/ko)


vue 설치
```sh
npm create vue@3.6.1
```
```sh
npm install
```
vue 실행
```sh
npm run dev
```

## 프로젝트 이용하기
이용하기 위해 server와 client 모두 실행해두는 것이 선행적으로 필요


vue로 실행시켜 띄운 사이트에서 접근할 수 있는 엔드포인트는 /search , /chart 2가지

### 기본 주소/search 
서울 소상공인 상권 업종 정보 검색
<img width="885" alt="image" src="https://github.com/CHOIEUNHYE/seoul-commercial/assets/68359686/a5591336-ca7e-40b1-9dbd-9195550d49b5">

### 기본 주소/chart
서울 소상공인 업종대분류별 자치구별 업종 수 현황 확인 
<img width="772" alt="image" src="https://github.com/CHOIEUNHYE/seoul-commercial/assets/68359686/b86d8c01-1681-49cb-b4fc-c9c3dd787719">




