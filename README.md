# 서울 소상공인 상권 정보 테스트 페이지 구현

## Data
사용 데이터 : 국가중점데이터 中 [상권정보 데이터](https://www.data.go.kr/data/15083033/fileData.do) csv 다운로드 -- 서울만 이용

해당 데이터 명을 seoul-commercial-district.csv로 변경 -> server/uploads/seoul-commercial-district.csv에 위치시킴

## Server(back) - Client(front)

flask - Vue.js3로 구현

## Sever : Flask Setup

server 디렉토리로 이동
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

