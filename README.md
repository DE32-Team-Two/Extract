README

### 팀 이름 `t2`
#### 팀원 `정미은` `이정훈` `김태영`
***
#### 프로젝트 주제

영화박스오피스 데이터 수집(Extract)/처리(Transform)/보관 및 활용(Load)을 위한 AIRFLOW DAGS 기능 개발

#### 프로젝트 내용

영화 박스오피스 데이터 수집/처리/보관 및 활용에 대하여 
각 단계에 대한 파이썬 프로그램을 package(PIP 설치) 단위로  개발
개발 package를 airflow 적용 및 운영

#### 특별 미션
 
모든 PIP package에 Ice_breaking 함수를 생성하여 이를 호출하면 
아스키아트로 변환된 팀원 사진이 호출
***

#### 기본설정
```
# python version 3.11.9로 맞추기
$ pyenv global 3.11.9
# 팀플을 위한 가상환경 만들기
$ pyenv virtualenv 3.11.9 t2
# 프롬프트에서 사용하기 위한 설정
$ pyenv shell t2
# pdm 설치
$ cd code/t2/Extract
$ git init
$ pdm init
```
#### 패키지 설치
```pdm add <dependencies>
```
[dependencies]
pytest
pytest -cov
figlet
requets
pandas

# Extract

![LGTM](https://i.lgtm.fun/2t8f.png)

# Version
- v1.0.0
    - ice breacking 함수 생성 
	- ice breacking 테스트 ✅
	- req 테스트 ✅
	- url 테스트 ✅
	- Dataframe cols 테스트 ✅

- v2.0.0
    - parqeut 파일 생성 테스트 ✅
    - year, month, date 형식으로 partitioning ✅
    - 멱등성 유지 기능 테스트 ✅

# Member
- [정미은](https://github.com/orgs/DE32-Team-Two/people/hahahellooo)
- [김태영](https://github.com/orgs/DE32-Team-Two/people/tbongkim03)
- [이정훈](https://github.com/orgs/DE32-Team-Two/people/Jeonghoon2)

#### 참고 코드
- https://github.com/dMario24/mov/blob/0.3.3/url_param/src/mov/api/call.py 
