import streamlit as st #call streamlit
import random #call random
from PIL import Image #이미지 삽입에 필요한 함수
import numpy as np #넘파이 함수 정의
from math import exp #수치해석 과제 관련 함수 정의
import matplotlib.pyplot as plt #그래프 함수 정의
import pandas as pd #판다스 함수 정의
from math import * #수학 관련 모든 함수 정의

st.title("**_Better Late Than Never_** :pencil:") #make title, 아무것도 하지 않는니 보다는 늦게라도 하는게 낫다
st.text("아무것도 하지 않는 것 보다는 늦게라도 하는게 낫습니다!")#사이트 제목 해석
st.error("2023학년도 1학기 기말고사 시험 정리 ( °̀ᗝ°́)و.*･ﾟ✧") #사이트 목적

add_selectbox = st.sidebar.selectbox(
    "*** SUBJECT ***",
    ("😊 동기부여 하기","🔩 기계요소설계","📈 수치해석",
     "🔚오늘 하루 마무리")
) #과목 별 분류하기

if add_selectbox == "😊 동기부여 하기" : #첫번째 셀렉트 박스 지정
    st.subheader("공부가 하기 싫은 당신을 위한 명언 생성기") #첫 페이지의 제목
    
    text = [
        "성공의 비밀은 처음 시작하는 것입니다. - 마크 트웨인",
        "어려움 속에서 성장이 있습니다. - 알버트 아인슈타인",
        "매일 조금씩이라도 나아가면 어느 날 도착할 수 있습니다. - 카렌 켈리",
        "성공은 준비된 기회와 만나는 것입니다. - 밥 존슨",
        "실패는 성공의 기반이다. - 토마스 에디슨",
        "한 걸음 한 걸음이 중요합니다. 빠르게 달리는 것보다 늦게라도 꾸준히 가는 것이 중요합니다. - 마라톤 선수",
        "당신이 할 수 있다고 믿든, 할 수 없다고 믿든, 믿는 대로 됩니다. - 헨리 포드",
        "행동은 우리의 꿈을 현실로 만들어 줍니다. - 토니 로빈스",
        "실패는 새로운 기회를 창조하는 것입니다. - 마이클 조던",
        "성공은 가장 어려운 시기에 가장 가까워져 있습니다. - 나폴레옹 힐",
        "위대한 것을 이루기 위해 위대한 꿈을 꾸세요. - 존 나쉬",
        "매일 조금씩 나아가면, 일 년 후에는 큰 변화를 만들 수 있습니다. - 카렌 램지",
        "자신을 믿고 처음부터 끝까지 꿈을 펼쳐보세요. - 월트 디즈니",
        "실패는 새로운 시작입니다. - 제리 스타크",
        "가장 어두운 밤에도 별빛은 찾아옵니다. - 찰리 채플린",
        "성공은 결코 최종 목적이 아니라, 지속적인 여정입니다. - 우노",
        "자신의 한계를 믿지 마세요. 자신의 한계를 넘어서세요. - 마이클 퍼펙트",
        "끝이 보이지 않을 때라면, 지금이 시작할 때입니다. - 피터 드러커",
        "당신이 결정하는 순간, 운명은 움직입니다. - 테니슨",
        "현재의 행동이 미래를 결정짓습니다. - 오프라 윈프리",
        "불가능은 자신의 생각에 따라 정해진 것입니다. - 알버트 아인슈타인",
        "성공은 준비된 마음이 만나는 기회입니다. - 존 우든",
        "희망을 가져라. 그리고 행동하라. 희망 없이는 행동이 없고, 행동 없이는 희망이 없다. - 달라이 라마",
        "오늘의 노력은 내일의 성공을 만듭니다. - 헤스터 린드그렌",
        "당신은 당신이 믿을 수 있는 만큼 멀리 갈 수 있습니다. - 존 우든",
        "당신이 할 수 있다고 믿는다면, 당신은 이미 절반은 성공한 것입니다. - 테오도어 루스벨트",
        "꿈을 이루려면 먼저 깨어나야 합니다. - J.M. 파워",
        "실패는 성공의 일부입니다. 중요한 것은 계속해서 도전하고 있는 것입니다. - 윈스턴 처칠",
        "자신의 한계에 도전하지 않으면, 한계를 알 수 없습니다. - 프랭크 블레이크",
        "가장 어려운 순간에도 자신을 믿으세요. 그리고 그때가 바로 당신이 변화하고 성장하는 순간입니다. - 로이 T. 베넷",
        "목표를 설정하고 그에 몰두하십시오. 성공의 첫 번째 비결입니다. - 톰 스미스",
        "당신은 믿는 대로 되기를 원한다면, 먼저 성공하는 사람처럼 행동하세요. - 마이클 존 보바크",
        "자신을 믿고 앞ubheader으로 나아가세요. 누구도 당신보다 먼저 시작할 수 없습니다. - 로버트 H. 슐러",
        "실패는 성공의 밑거름입니다. 더 많이 실패할수록 더 가까이 성공에 다가갑니다. - 토마스 워슬리",
        "오늘 하지 않으면, 내일의 성공을 기대할 수 없습니다. - 레스 브라운",
        "불가능이란 단어는 바보들의 사전에만 있습니다. - 나폴레옹 본파르트",
        "꿈은 현실이 되기 전에 먼저 마음에서 시작됩니다. - 아노니오 그라시안",
        "작은 성공들이 모여 큰 성공을 이루게 됩니다. - 오디 액슬로드",
        "당신의 가치는 당신의 열정을 결정합니다. - 워렌 버핏",
        "불가능한 일은 아직 시도해보지 않은 일입니다. - 윌스미스",
        "힘들어도 계속해서 나아가세요. 그럴 때가 가장 가치있는 때입니다. - 윈스턴 처칠",
        "나는 실패한 적이 없다. 그저 10,000가지 방법을 발견한 것 뿐이다. - 토마스 에디슨",
        "성공의 열쇠는 어떤 일을 하는 동안 당신의 100%를 쏟는 것입니다. - 로저 스타우트",
        "성공은 잠을 자지 않고 꿈을 이루기 위해 노력하는 것입니다. - 헨리 포드",
        "당신이 꿈꾸는 것은 이미 누군가의 현실입니다. - 존 레논",
        "당신이 하고 싶은 일을 하면서 돈을 벌 수 있다면, 그건 성공입니다. - 앤디 워홀",
        "현재의 선택이 미래의 성공을 결정짓습니다. - 앤서니 로빈스",
        "성공의 비결은 기회를 잡는 것이 아니라, 기회를 만드는 것입니다. - 프랭크 허버트",
        "성공은 준비된 마음과 운이 만나는 순간입니다. - 제임스 캐메론",
        "당신의 열정은 성공의 연료입니다. - 랄프 월도 에머슨"
    ] #한땀한땀 붙여넣은 명언 50가지를 변수에 저장해주기

    def motivation() : #명언을 생성할 함수를 정의
        return random.choice(text) #랜덤으로 텍스트를 주는 코드
    
    st.caption("**_!버튼을 누른 당신에게 :green[행운]이!_**") #caption을 사용하여 작은 글자를 표현
    st.caption("**_?버튼을 :red[다시] 누르면 새로운 명언이?_**") #caption을 사용하여 작은 글자를 표현
    st.caption("⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️") #caption을 사용하여 작은 글자를 표현

    if st.button("🍀Good Luck🍀"): #명언을 볼 수 있는 버튼 생성
        text = motivation() #text에는 motivation 함수가 나오게 끔
        st.header(text) #텍스트 사이즈는 크게


elif add_selectbox == "🔩 기계요소설계" : #두번째 셀렉트 박스 내용 구성하기
    st.title("기계요소설계")
    st.info("기계요소설계는 기계 시스템을 구성하는 요소들을 정확하고 효율적으로 설계하여 기능과 성능 요구사항을 충족시키는 과정입니다.") #기계요소설계의 정의
    tab1, tab2 = st.tabs(["9장","10장"]) #각 단원을 tab으로 구분
    with tab1: #첫번째 탭 부르기
        st.header("9장 축") #제목 생성
        st.caption("축은 동력전달에서 가장 기본이 되는 요소로서 :red[강도설계, 강성설계, 진동설계] 등을 다룬다.") #단원에 대한 설명
        st.subheader("9.1 축의 분류") #목차
        st.markdown("**□ 개요**") #굵은 글자 표기
        st.text("○ 정의") #텍스트 내용 작성
        st.text("- 축(shaft) : 베어링으로 지지, 하중을 받으며 정지 또는 회전운동으로 동력을 전달하는 요소") #텍스트 내용 작성
        st.text("- 축의 연결요소 : 풀리, 기어, 플라이 휠, 차륜") #텍스트 내용 작성
        st.text("○ 단면형상") #텍스트 내용 작성
        st.text("- 원형축(circular shaft) -> 중실축(solid shaft), 중공축(hollow shaft)") #텍스트 내용 작성
        st.text("○ 축선형식") #텍스트 내용 작성
        st.text("- 직선축, 크랭크축")
        st.text("○ 축에 작용하는 하중에 따른 분류") #텍스트 내용 작성
        st.text("- 주로 굽힘 작용") #텍스트 내용 작성
        st.text("- 주로 비틀림 작용") #텍스트 내용 작성
        st.text("- 비틀림, 굽힘, 인장, 압축이 동시에 작용") #텍스트 내용 작성

        st.text(" ") #공백으로 한 칸 띄우기
        st.markdown("**□ 주로 :blue[굽힘] 작용을 받는 축**") #굵은 글자 표기
        st.text("○ 정의") #텍스트 내용 작성
        st.text("- 베어링으로 지지되어 있는 축부") #텍스트 내용 작성
        st.text("⊙ 저널(journal), 차량의 차축(axle), 기차, 전차 등의 차축") #텍스트 내용 작성
        st.text("○ 종류")#텍스트 내용 작성
        st.text("- 정치차축(stationary shaft) : 차축은 정지, 휠은 회전(자동차 차축)")#텍스트 내용 작성
        image = Image.open('1.jpg') #이미지 삽입
        st.image(image, caption = '정지 차축') #삽입한 이미지에 대한 설명
        st.text("- 회전차축(rotating shaft) : 차축이 회전(철도 차축, 차축과 차륜이 고정)")#텍스트 내용 작성
        image = Image.open('2.jpg') #이미지 삽입
        st.image(image, caption = '회전 차축') #삽입한 이미지에 대한 설명
        
        st.text(" ") #공백으로 한 칸 띄우기
        st.markdown("**□ 주로 :blue[비틀림] 작용을 받는 축**") #굵은 글자 표기
        st.text("○ 정의") #텍스트 내용 작성
        st.text("- 동력전달을 주목적으로 하는 축") #텍스트 내용 작성
        st.text("○ 전동축(transmission shaft)") #텍스트 내용 작성
        image = Image.open('3.jpg')#이미지 삽입
        st.image(image, caption = '전동축') #삽입한 이미지에 대한 설명
        st.text("- 주로 비틀림 작용, 비틀림 + 굽힘 작용을 동시에 받아 동력 전달을 주 목적으로 함") #텍스트 내용 작성
        st.text("- 일반적인 공장용 축 (주축, 선축, 중간축)")#텍스트 내용 작성
        st.text("○ 작업축") #텍스트 내용 작성
        st.text("- 축 자체가 직접 작업을 수행 -> Spindle Shaft")#텍스트 내용 작성
        st.text("-Spindle 축 : 주로 비틀림 작용, 형상/치수 정밀, 변형량 극소, 짧은 회전 축") #텍스트 내용 작성
        image = Image.open('4.jpg')#이미지 삽입
        st.image(image, caption = 'Spindle 축')#삽입한 이미지에 대한 설명
        st.text("-> 선반 밀링머신 등 공작기계의 주축으로 사용")#텍스트 내용 작성
        st.text("○ Flexible Shaft(요축)") #텍스트 내용 작성
        st.text("- 축의 방향이 자유롭게 바뀜, 충격완화를 목적 flexibility(굴요성)") #텍스트 내용 작성
        st.text("- 비틀림 강성이 높으나, 굽힘 강성이 매우 작음") #텍스트 내용 작성
        st.text("-코일형 휨축(철사를 4~10겹 꼬아 제작)") #텍스트 내용 작성
        image = Image.open('5.jpg')#이미지 삽입
        st.image(image, caption = '코일형 휨축')#삽입한 이미지에 대한 설명
        st.text("-자유이음형 휨축(커플링, 단축원통을 수많이 이어 제작)") #텍스트 내용 작성

        st.text(" ") #공백으로 한 칸 띄우기
        st.markdown("**□ 주로 :blue[비틀림, 인장, 압축 등의 작용을 동시에 2종류 이상] 받는 축**")#굵은 글자 표기
        st.text("○ 크랭크축") #텍스트 내용 작성
        image = Image.open('6.jpg')#이미지 삽입
        st.image(image, caption = '크랭크축')#삽입한 이미지에 대한 설명
        st.text("- 곡선축, 왕복운동을 회전운동으로 변환")#텍스트 내용 작성
        st.text("- 내연기관, 압축기 등 사용")#텍스트 내용 작성
        st.text("○ 추진축") #텍스트 내용 작성
        st.text("- 굽힘, 비틀림 이외에 인장, 압축 하중을 동시에 받음")#텍스트 내용 작성
        st.text("- Propeller shaft, screw shaft, 선박의 프로펠러")#텍스트 내용 작성
        image = Image.open('7.jpg')#이미지 삽입
        st.image(image, caption = '선박의 프로펠러')#삽입한 이미지에 대한 설명

        st.text(" ")#공백으로 한 칸 띄우기
        st.text(" ")#공백으로 한 칸 띄우기
        st.subheader("9.2 축의 재료") #목차
        st.markdown("**□ 축의 재료**") #굵은 글자 표기
        st.text("○ 탄소강재") #텍스트 내용 작성
        st.text("- 탄소 함유량 0.1~0.4%") #텍스트 내용 작성
        st.text("- 공장용 전동축 : 탄소강 냉간 인발봉 + 표면경화") #텍스트 내용 작성
        st.text("- 고속회전 용 고하중이 가해지는 축 : Ni강, Ni-Cr강, Ni-Cr-Mo 강 (합금강)") #텍스트 내용 작성
        st.text("- 베어링과 접촉되는 내마모성 축 : 표면 경화강(침탄, 고주파 담금질)") #텍스트 내용 작성
        st.text("- 축지름 > 100mm : 탄소함량 0.4~0.5%인 열간 압연강재") #텍스트 내용 작성
        st.text("- 축지름 > 150mm : 단조 이후 선삭작업") #텍스트 내용 작성

        st.text(" ")#공백으로 한 칸 띄우기
        st.text(" ")#공백으로 한 칸 띄우기
        st.subheader("9.3 축 설계 시 고려사항") #목차
        st.markdown("**□ 개요**") #굵은 글자 표기
        st.text("○ 설계개념★") #텍스트 내용 작성
        st.text("- 파손방지를 위한 충분한 강도") #텍스트 내용 작성
        st.text("- 처짐, 비틀림이 한도 내에 있을 충분한 강성") #텍스트 내용 작성
        st.text("- 회전속도는 위험속도 25% 이상 떨어진 상태에서 사용") #텍스트 내용 작성
        st.text("☞ 일반적으로 강성 설계 후 강도 검토") #텍스트 내용 작성
        st.text("○ 강도(strength)") #텍스트 내용 작성
        st.text("- 정하중, 반복하중, 충격하중 등에 견디는 충분한 강도 유지") #텍스트 내용 작성
        st.text("- 키홈, 원주홈 등과 같은 노치에서 발생하는 응력집중 주목") #텍스트 내용 작성
        st.text("○ 강성(stiffness)") #텍스트 내용 작성
        st.text("- 휨 변형") #텍스트 내용 작성
        st.text("→ 강도를 만족해도 처짐이 한도 이상 발생하면 베어링 압력의 불균형") #텍스트 내용 작성
        st.text("→ 베어링 틈새의 불균일, 기어 맞물림 이상 등 발생") #텍스트 내용 작성
        st.text("→ 공작 기계의 경우 가공 정밀도 영향") #텍스트 내용 작성
        st.text("- 비틀림 변형 : 비틀림 각이 큰 경우 비틀림 진동에 의한 파손 발생") #텍스트 내용 작성
        st.text("○ 진동(vibration)") #텍스트 내용 작성
        st.text("- 굽힘, 비틀림 진동에 의한 축의 고유 진동수 = 축의 회전수") #텍스트 내용 작성
        st.text("→ 위험속도 (critical speed) 발생") #텍스트 내용 작성
        st.text("→ 공진(resonance) 발생") #텍스트 내용 작성
        st.text("→ 축의 파괴") #텍스트 내용 작성
        st.text("○ 부식(corrosion)") #텍스트 내용 작성
        st.text("- 액체와 접촉하는 축(선박, 수차, 펌프 축) -> 부식피로/파괴발생") #텍스트 내용 작성
        st.text("○ 열팽창(thermal expansion)") #텍스트 내용 작성
        st.text("- 고온에서 사용하는 축 → 고온 열팽창 → 축의 형상 변화") #텍스트 내용 작성

        st.text(" ")#공백으로 한 칸 띄우기
        st.text(" ")#공백으로 한 칸 띄우기
        st.subheader("9.4 축설계") #목차
        st.markdown("**□ 축 설계 순서**") #굵은 글자 표기
        st.text("1. 회전축에 작용하는 하중을 분석한다") #텍스트 내용 작성
        st.text("2. 축에 작용하는 최대응력 <= 허용응력이 되도록 최소축직경 결정") #텍스트 내용 작성
        st.text("3. 축에 작용하는 피로하중에 따른 최소축직경 계산") #텍스트 내용 작성
        st.text("4. 축의 형상 설계") #텍스트 내용 작성
        st.text("5. 회전축의 고유진동수를 계산") #텍스트 내용 작성
        st.text("- 고온에서 사용하는 축 → 고온 열팽창 → 축의 형상 변화") #텍스트 내용 작성st.text("- 고온에서 사용하는 축 → 고온 열팽창 → 축의 형상 변화") #텍스트 내용 작성

    with tab2: 
        st.header("10장 미끄럼 베어링") #제목 생성
        st.caption("미끄럼 베어링은 축과 베어링 사이에 :red[유체 윤활] 이 되는 베어링이다. 베어링의 특성을 기술하는 방정식 및 설계 변수 등을 다룬다.")#단원에 대한 설명
        st.subheader("10.0 개요") #목차
        st.text("○ 개요") #텍스트 내용 작성
        st.text("- 베어링(bearing) : ") #텍스트 내용 작성
        st.text("축 하중(자중 포함)에 의한 마찰 저항을 최소로 지지해주는 기계 요소") #텍스트 내용 작성
        st.text("- 저널(journal) : 베어링과 접촉하여 이를 지지하는 축경(반경방향 하중 지지)") #텍스트 내용 작성
        st.text("→ 저널 베어링") #텍스트 내용 작성
        st.text("- 피봇(pivot) : 축 방향의 하중을 받는 축경 → 피봇 베어링") #텍스트 내용 작성
        st.text("○ 저널의 종류") #텍스트 내용 작성
        st.text("- 횡축경 (lateral journal) ") #텍스트 내용 작성
        st.text("→ 힘이 축에 직각으로 작용(end, intermediate journal)") #텍스트 내용 작성
        st.text("- 추력축경(vertical journal)") #텍스트 내용 작성
        st.text("→ 힘이 축방향으로 작용(pivot, collar journal)") #텍스트 내용 작성
        image = Image.open('8.jpg')#이미지 삽입
        st.image(image, caption = '다양한 저널의 종류')#삽입한 이미지에 대한 설명

        st.text(" ") #공백으로 한 칸 띄우기
        st.markdown("**□ 베어링의 분류**") #굵은 글자 표기
        st.text("○ 베어링 형식") #텍스트 내용 작성
        st.text("- 하중방향에 의한 형식") #텍스트 내용 작성
        st.text("⊙Radial bearing : 레이디얼 저널에 사용, 반경방향 하중 지지") #텍스트 내용 작성
        st.text("⊙Thrust bearing : 추력 저널에 사용, 축방향 하중 지지") #텍스트 내용 작성
        st.text("- 감마 기구에 의한 형식") #텍스트 내용 작성
        st.text("⊙ Sliding bearing : 윤활유 막을 경계로 미끄럼 접촉, 주로 유막압력에 의한 하중 지지, 유체 윤활로 마찰 경감") #텍스트 내용 작성
        st.text("⊙Rolling bearing : 구름접촉의 접촉압력에 의한 하중 지지") #텍스트 내용 작성

        st.text(" ") #공백으로 한 칸 띄우기
        st.text(" ") #공백으로 한 칸 띄우기
        st.subheader("10.1 미끄럼 베어링의 형태") #목차
        st.text("○ 개요") #st.markdown("**□ 베어링의 분류**") #굵은 글자 표기링 사이에 얇은 유막을 형성하여 상대 미끄럼 운동") #텍스트 내용 작성
        st.text("- 롤링 베어링과 함께 적용 범위가 넓음") #텍스트 내용 작성
        st.text("- 종류 : Radial Bearing, Thrust Bearing") #텍스트 내용 작성
        st.text("- 윤활 원리상 구분 ") #텍스트 내용 작성
        st.text("⊙ 동압 : 베어링과 축 간의 상대운동으로 동역학적 유막압력 발생") #텍스트 내용 작성
        st.text("⊙ 정압 : 외부에서 높은 압력의 유체가 공급, 정역학적 유막압력 발생") #텍스트 내용 작성
        image = Image.open('9.jpg')#이미지 삽입
        st.image(image, caption = '베어링의 형태')#삽입한 이미지에 대한 설명
        st.markdown("**□ 미끄럼 베어링의 일반사항**") #굵은 글자 표기
        st.text("○ 미끄럼 베어링에 있어서 미끄럼의 현상") #텍스트 내용 작성
        st.text("- 평행 활동면(평행 미끄럼면)") #텍스트 내용 작성
        st.text("⊙ 미끄럼 면이 서로 평행인 상태") #텍스트 내용 작성
        st.text("→ 공작기계 안내면, 칼러 스러스트 베어링의 미끄럼 면, 크로스 헤드의 안내면") #텍스트 내용 작성
        st.text("- 경사윤활면(경사 미끄럼 면)") #텍스트 내용 작성
        st.text("⊙ 압력은 수압면적에 대한 적분치") #텍스트 내용 작성
        st.text("→ Michell Bearing, Kingsbury Bearing") #텍스트 내용 작성
        image = Image.open('10.jpg')#이미지 삽입
        st.image(image, caption = '스러스트 동압 저널 베어링')#삽입한 이미지에 대한 설명
        image = Image.open('11.jpg')#이미지 삽입
        st.image(image, caption = '스러스트 정압 저널 베어링')#삽입한 이미지에 대한 설명
        image = Image.open('12.jpg')#이미지 삽입
        st.image(image, caption = '레이디얼 정압 저널 베어링')#삽입한 이미지에 대한 설명

        st.text(" ") #공백으로 한 칸 띄우기
        st.text(" ") #공백으로 한 칸 띄우기
        st.subheader("10.2 마찰의 종류") #목차
        st.text("○ 상대운동에 따른 분류") #텍스트 내용 작성
        st.text("- 미끄럼 마찰") #텍스트 내용 작성
        st.text("⊙ 물체가 일정한 속도로 미끄러지고 있을 때") #텍스트 내용 작성
        st.markdown("Coluomb 법칙 : $\ F = µ * P $ (P 수직력, µ 마찰 계수)") #텍스트 내용 작성 및 수식 사용
        st.text("- 구름마찰") #텍스트 내용 작성
        image = Image.open('13.jpg')#이미지 삽입
        st.image(image, caption = '미끄럼 마찰에 대한 그림')#삽입한 이미지에 대한 설명
        st.text("○ 마찰면에 따른 분류") #텍스트 내용 작성
        st.text("- 건조마찰(dry friction)") #텍스트 내용 작성
        st.text("⊙ 접촉면에 윤활유가 없음, 물체의 재질, 표면 상태에 영향이 큼(µ = 0.1~1)") #텍스트 내용 작성
        st.text("- 유체마찰(fluid friction)") #텍스트 내용 작성
        st.text("⊙ 유막의 두께가 충분한 경우, 유체의 점성에 의해서 전단력 발생") #텍스트 내용 작성
        st.text("⊙ 물체의 재질, 표면 상태 관계 없음 (µ = 0.001~0.01)") #텍스트 내용 작성
        st.text("- 경계마찰(boundary friction)") #텍스트 내용 작성
        st.text("⊙ 유막이 얇게 되어 1/1000(mm) 이하 ") #텍스트 내용 작성
        st.text("→ Coloumb 법칙 성립, 마찰은 건조마찰 보다 작음(µ = 0.01~0.1)") #텍스트 내용 작성
        st.text("⊙ 유체 분자가 단분자층으로 물체 표면에 흡착찰") #텍스트 내용 작성
        st.text("→ 마찰은 유체 성질 보다 접촉 물체에 영향") #텍스트 내용 작성
        st.text("→ 이러한 유막을 경계층 이라 함") #텍스트 내용 작성
        st.text("- 완전윤활 vs. 불완전 윤활") #텍스트 내용 작성
        st.text("⊙ 완전 윤활 : 유체 마찰만의 윤활 상태") #텍스트 내용 작성
        st.text("⊙ 불완전 윤활 : 유체마찰~경계윤활의 영역") #텍스트 내용 작성

        st.text(" ") #공백으로 한 칸 띄우기
        st.text(" ") #공백으로 한 칸 띄우기
        st.subheader("10.3 점성유체에 대한 뉴턴의 법칙") #목차
        st.markdown(":red[○ 점성계수와 속도구배]") #텍스트 내용 작성
        image = Image.open('14.jpg')#이미지 삽입
        st.image(image, caption = '점성 유체')#삽입한 이미지에 대한 설명
        st.text("⊙ 유체 위에 판이 속도 U로 이동") #텍스트 내용 작성
        st.text("→ 유체의 속도는 0 ~ u 로 선형적으로 변화") #텍스트 내용 작성
        st.text("⊙ 판에 작용하는 힘 F(점성 저항을 이기는), 판의 면적 A") #텍스트 내용 작성
        st.markdown("$\ τ = F / A $ ↔ $\ τ = η * (du/dy) $ ") #수식 작성
        st.text("→ η  : 점성계수, $\ du/dy $ : y축 상의 속도 구배") #텍스트 내용 작성
        st.markdown("$\ τ = F / A = η * (U / h) $ , $\ η = (F*h)/(A*U) $") #수식 작성
        st.markdown("→ h : 유막의 두께, U : 속도 ($\ du/dy $ 가 선형적이라 하면)") #텍스트 내용 작성, 수식 작성
        st.text(" ") #공백으로 한 칸 띄우기
        st.markdown("**□ 점도 및 점도 측정**") #굵은 글자 표기
        st.text("⊙ 점도 단위") #공백으로 한 칸 띄우기
        st.text("- 절대점성계수 η (poise)") #공백으로 한 칸 띄우기
        st.markdown("$\ η = (F[dyne]*h[cm])/(A[cm^2]*U[cm/s]) * [dyne * s / cm^2] = 1 poise = 0.1 Pa*s $") #수식 작성
        st.text("→ 프와즈(poise, p), p/100(centipoise, cp) 점도단위") #텍스트 내용 작성
        st.markdown("→ 물리적 의미 : 1cm 유막 두께로 $\ 1 cm^2 $ 면적의 판을 $\ 1 cm / s $ 로 움직일 때 필요한 1 dyne의 힘") #텍스트 내용 작성, 수식 작성
        st.text("→ 실용적 단위 : 1cp = 1/100 poise") #텍스트 내용 작성
        st.text("- 동점성 계수 ν (stokes, St)")#텍스트 내용 작성
        st.markdown("$\ ν = η / ρ [cm^2 / s^2] $") #수식 작성
        st.markdown("→ ρ : 기름의 비중 $\ [dyne * s^2 / cm^4]  $ or  $\ [g / cm^3] $") #수식 작성
        st.text("→ St/100(centi-stoke, cSt)") #공백으로 한 칸 띄우기
        

elif add_selectbox == "📈 수치해석" : #세번째 셀렉트 박스 선택
    st.title("수치해석") #타이틀 작성
    st.warning("수치해석은 수학적 모델이나 문제를 컴퓨터를 사용하여 근사화하고, 수치적인 방법을 통해 해를 구하는 과정입니다.") #캡션을 통해 수치해석 정의 작성
    tab1, tab2 = st.tabs(["7장","8장"]) #각 단원을 tab으로 구분
    with tab1: #첫번째 탭 부르기
        st.header("7장 초기값 문제") #제목 생성
        st.caption("초기값 문제란, 미분방정식이나 차분방정식과 같은 수학적 모델에서 :red[초기 조건]을 주고, 해당 조건에서의 해를 수치적으로 구하는 문제를 의미합니다.") #단원에 대한 설명
        st.write("예제 문제 풀이") #예제 문제 풀이 글 작성
        st.write("Initial Value Problems 07-01") #07-01 문제 풀이 제목 작성
        code = '''# Problem 07-01
#        Initial Value Problems
#                       y' + 4y = t^2  subject to y(0)=1
#       1) Euler Forward Method
#       2) Euler Backward Method
#       3) Second-Order Central Scheme 

import numpy as np
from math import exp
import matplotlib.pyplot as plt

def yexact(t):
    y = (31.0/32.0)*exp(-4.0*t)+(1.0/4.0)*t**2-(1.0/8.0)*t+(1.0/32.0)
    return y

#---------------------------------------
tstrt = 0.0
tlast = 0.03
dt = 0.01

t = tstrt
ye = 1.0
yf = 1.0
yb = 1.0
yc = 1.0

tg = [t]
yeg = [ye]
yfg = [yf]
ybg = [yb]
ycg = [yc]

while t < tlast:
    to = t
    yfo = yf
    ybo = yb
    yco = yc

    t += dt

#       0) Exact Solution

    ye = yexact(t)
        
#       1) Euler Forward Method

    tmp = -4.0*yfo+to**2
    yf = yfo+dt*tmp

#       2) Euler Backward Method

    tmp = ybo+dt*t**2
    den = 1.0+4.0*dt
    yb = tmp/den

#       3) Second-Order Central Scheme

    tmp = (1.0-2.0*dt)*yco+dt*(0.5*(t+to))**2
    den = 1.0+2.0*dt
    yc = tmp/den

    tg.append(t)
    yeg.append(ye)
    yfg.append(yf)
    ybg.append(yb)
    ycg.append(yc)
#---------------------------------------

    ng = len(tg)-1

    yeg_tlast = yeg[ng]
    yfg_tlast = yfg[ng]
    ybg_tlast = ybg[ng]
    ycg_tlast = ycg[ng]
    err_yfg_tlast = abs((yfg_tlast-yeg_tlast)/yeg_tlast)*100.0
    err_ybg_tlast = abs((ybg_tlast-yeg_tlast)/yeg_tlast)*100.0
    err_ycg_tlast = abs((ycg_tlast-yeg_tlast)/yeg_tlast)*100.0

    print("\nAt t =",tg[ng])
    print("\nThe exact solution =",yeg_tlast)
    print("\nThe numerical solutions =")
    print("\nValue =",yfg_tlast,"/ error (%) =",err_yfg_tlast, \
          "by the Euler forward")
    print("\nValue =",ybg_tlast,"/ error (%) =",err_ybg_tlast, \
          "by the Euler backward")
    print("\nValue =",ycg_tlast,"/ error (%) =",err_ycg_tlast, \
          "by the Central difference")

#---------------------------------------
   
nex = 101
tex = np.linspace(tstrt,tlast,nex)
yex = np.zeros(nex)
for i in range(nex):
    yex[i] = yexact(tex[i])

plt.plot(tex,yex,label='exact')
plt.scatter(tg,yfg,label='Euler forward')
plt.scatter(tg,ybg,label='Euler backward')
plt.scatter(tg,ycg,label='Central')

plt.legend()
plt.show()
#---------------------------------------

input("\nPress return to exit")'''
        st.code(code, language = 'python') #코드 입력 및 코드 부르기

        #07-01에 대한 풀이 코드
        def yexact(t):
            y = (31.0/32.0)*exp(-4.0*t)+(1.0/4.0)*t**2-(1.0/8.0)*t+(1.0/32.0)
            return y

        tstrt = 0.0
        tlast = 0.03
        dt = 0.01

        t = tstrt
        ye = 1.0
        yf = 1.0
        yb = 1.0
        yc = 1.0

        tg = [t]
        yeg = [ye]
        yfg = [yf]
        ybg = [yb]
        ycg = [yc]

        while t < tlast:
            to = t
            yfo = yf
            ybo = yb
            yco = yc

            t += dt
        #       0) Exact Solution

            ye = yexact(t)
                
        #       1) Euler Forward Method

            tmp = -4.0*yfo+to**2
            yf = yfo+dt*tmp

        #       2) Euler Backward Method

            tmp = ybo+dt*t**2
            den = 1.0+4.0*dt
            yb = tmp/den

        #       3) Second-Order Central Scheme

            tmp = (1.0-2.0*dt)*yco+dt*(0.5*(t+to))**2
            den = 1.0+2.0*dt
            yc = tmp/den

            tg.append(t)
            yeg.append(ye)
            yfg.append(yf)
            ybg.append(yb)
            ycg.append(yc)
        #---------------------------------------

            ng = len(tg)-1

            yeg_tlast = yeg[ng]
            yfg_tlast = yfg[ng]
            ybg_tlast = ybg[ng]
            ycg_tlast = ycg[ng]
            err_yfg_tlast = abs((yfg_tlast-yeg_tlast)/yeg_tlast)*100.0
            err_ybg_tlast = abs((ybg_tlast-yeg_tlast)/yeg_tlast)*100.0
            err_ycg_tlast = abs((ycg_tlast-yeg_tlast)/yeg_tlast)*100.0

            print("\nAt t =",tg[ng])
            print("\nThe exact solution =",yeg_tlast)
            print("\nThe numerical solutions =")
            print("\nValue =",yfg_tlast,"/ error (%) =",err_yfg_tlast, \
                "by the Euler forward")
            print("\nValue =",ybg_tlast,"/ error (%) =",err_ybg_tlast, \
                "by the Euler backward")
            print("\nValue =",ycg_tlast,"/ error (%) =",err_ycg_tlast, \
                "by the Central difference")
        nex = 101
        tex = np.linspace(tstrt,tlast,nex)
        yex = np.zeros(nex)
        for i in range(nex):
            yex[i] = yexact(tex[i])

        plt.plot(tex,yex,label='exact')
        plt.scatter(tg,yfg,label='Euler forward')
        plt.scatter(tg,ybg,label='Euler backward')
        plt.scatter(tg,ycg,label='Central')

        plt.legend()
        plt.xlabel('t')
        plt.ylabel('y')

        st.pyplot(plt.gcf()) #위 코드는 07-01에 대한 풀이 코드, 이 코드는 pyplot을 불러와서 그래프를 표현함. 그런데 오류가 발생해서 구글링 했다.

        st.write("Initial Value Problems 07-04") #07-04 문제 풀이 할 거라고 적은것
        code = '''# Problem 07-04
#        Initial Value Problems
#                       y'' + 0.1y' = -x  subject to y(0)=0 and y'(0)=1

#       by the 4th-order Runge-Kutta Method

import numpy as np
import matplotlib.pyplot as plt

X,Y = integrate(F,x,y,xStop,h).
    4th-order Runge-Kutta method for solving the
    initial value problem {y}' = {F(x,{y})}, where
    {y} = {y[0],y[1],...y[n-1]}.
    x,y   = initial conditions
    xStop = terminal value of x
    h     = increment of x used in integration
    F     = user-supplied function that returns the
            array F(x,y) = {y'[0],y'[1],...,y'[n-1]}.

def integrate(F,x,y,xStop,h):
    
    def run_kut4(F,x,y,h):
        K0 = h*F(x,y)
        K1 = h*F(x + h/2.0, y + K0/2.0)
        K2 = h*F(x + h/2.0, y + K1/2.0)
        K3 = h*F(x + h, y + K2)
        return (K0 + 2.0*K1 + 2.0*K2 + K3)/6.0    
    
    X = []
    Y = []
    X.append(x)
    Y.append(y)
    while x < xStop:
        h = min(h,xStop - x)
        y = y + run_kut4(F,x,y,h)
        x = x + h
        X.append(x)
        Y.append(y)
    return np.array(X),np.array(Y)

def F(x, y):
    F = np.zeros(2)
    F[0] = y[1]
    F[1] = -0.1*y[1]-x
    return F

#---------------------------------------
x = 0.0                                  # Start of integration
xStop = 2.0                          # End of integration
y = np.array([0.0, 1.0])      # Initial values of {y}
h = 0.05                               # Step size

X,Y = integrate(F,x,y,xStop,h)
yExact = 100.0*X - 5.0*X**2 + 990.0*(np.exp(-0.1*X) - 1.0)

plt.plot(X,Y[:,0],'o',X,yExact,'-')오늘 학습 태도를 점검하며 잘한 점과 반성할 점에 대해 스스로 생각해보기
plt.grid(True)
plt.xlabel('x'); plt.ylabel('y')
plt.legend(('Numerical','Exact'),loc=0)
plt.show()'''
        st.code(code, language = 'python') #코드 입력 및 코드 부르기

        #07-04 문제 풀이 
        def integrate(F,x,y,xStop,h):
    
            def run_kut4(F,x,y,h):
                K0 = h*F(x,y)
                K1 = h*F(x + h/2.0, y + K0/2.0)
                K2 = h*F(x + h/2.0, y + K1/2.0)
                K3 = h*F(x + h, y + K2)
                return (K0 + 2.0*K1 + 2.0*K2 + K3)/6.0    
            
            X = []
            Y = []
            X.append(x)
            Y.append(y)
            while x < xStop:
                h = min(h,xStop - x)
                y = y + run_kut4(F,x,y,h)
                x = x + h
                X.append(x)
                Y.append(y)
            return np.array(X),np.array(Y)
        
        def F(x, y):
            F = np.zeros(2)
            F[0] = y[1]
            F[1] = -0.1*y[1]-x
            return F
        
        x = 0.0                                  # Start of integration
        xStop = 2.0                          # End of integration
        y = np.array([0.0, 1.0])      # Initial values of {y}
        h = 0.05                               # Step size

        X,Y = integrate(F,x,y,xStop,h)
        yExact = 100.0*X - 5.0*X**2 + 990.0*(np.exp(-0.1*X) - 1.0)

        plt.plot(X,Y[:,0],'o',X,yExact,'-')
        plt.grid(True)
        plt.xlabel('x'); plt.ylabel('y')
        plt.legend(('Numerical','Exact'),loc=0)
        plt.show()

        st.pyplot(plt.gcf()) #위 코드는 07-04에 대한 풀이 코드, 이 코드는 pyplot을 불러와서 그래프를 표현함. 그런데 오류가 발생해서 구글링 했다.

    with tab2: #두번째 탭 부르기
        st.header("8장 2점 경계값 문제") #제목 생성
        st.caption("2점 경계값 문제는 주어진 구간의 양 끝점에서만 조건을 주고, 그 사이의 값을 찾는 문제를 의미합니다. 이를 통해 구간 내에서 함수의 근사치를 구하거나, 미분 방정식의 초기값 문제를 해결하는 등 다양한 수치해석적인 문제를 다룰 수 있습니다.") #단원에 대한 설명
        st.write("예제 문제 풀이") #예제 문제 풀이 글 작성
        st.write("Boundary Value Problem, Example 08-06") #08-06 문제 풀이 제목 작성
        code = '''# Example 08-06 -> 코드를 수정함.
#        Boundary Value Problem
#                       y''=-4y+4x  subject to y(0)=0 and y'(pi/2)=dyn
# Finite Difference Method: Second-Order Central Scheme

import numpy as np
from math import *
import matplotlib.pyplot as plt

#---------------------------------------

#----- Exact solution

def yexact(x,dyn):
    y = x+0.5*(1.0-dyn)*sin(2.0*x)
    return y

#----- Find Segment

def findSegment(xData,x):
    iLeft = 0
    iRight = len(xData)- 1
    while 1:
        if (iRight-iLeft) <= 1: return iLeft
        i = int((iLeft + iRight)/2)
        if x < xData[i]: iRight = i
        else: iLeft = i

#----- TDMA solver

def TDMAsolver(a,d,c,b):

    n = len(b)
    x = np.zeros(n)

    for i in range(0,n-1):
        lam = a[i]/d[i]
        d[i+1] = d[i+1] - lam*c[i] 
        b[i+1] = b[i+1] - lam*b[i]

    x[n-1] = b[n-1]/d[n-1]
    
    for i in range(n-2,-1,-1):
        x[i] = (b[i]-c[i]*x[i+1])/d[i]

    return x

#---------------------------------------

#----- Dirichlet boundary condition

xo = 0.0; yo = 0.0

#----- Neumann boundary condition

xn = pi/2; dyn = 3.0  # textbook to be corrected

#----- Resolution

n = 10

xl = xn-xo
h = xl/n

#----- Solving based on the Finite Difference

x = np.linspace(xo,xn,n+1)

a = np.zeros(n)
d = np.ones(n+1)
c = np.zeros(n)
b = np.zeros(n+1)

a[0:n-1] = 1.0
d[1:n] = -2.0+4.0*h**2
c[1:n] = 1.0
b[1:n] = 4.0*x[1:n]*h**2 

#----- Dirichlet boundary condition

b[0] = yo

#----- Neumann boundary condition

a[n-1] = 2.0
d[n] = -2.0+4*h**2
b[n] = 4.0*x[n]*h**2-2*h*dyn

y = TDMAsolver(a,d,c,b)

#---------------------------------------

#----- Comparison with the exact solution by the numbers

xc = xn

ic = findSegment(x,xc)
fac = (xc-x[ic])/(x[ic+1]-x[ic])

yex_c = yexact(xc,dyn)
y_c = y[ic]*(1.0-fac)+y[ic+1]*fac
err_y_c = abs((y_c-yex_c)/yex_c)*100.0

print("\nAt x =",xc)
print("\nThe exact solution =",yex_c)
print("\nThe numerical solutions =")
print("\nValue =",y_c,"/ error (%) =",err_y_c)

#----- Comparison with the exact solution by the graph

nex = 101
xex = np.linspace(xo,xn,nex)
yex = np.zeros(nex)
for i in range(nex):
    yex[i] = yexact(xex[i],dyn)

plt.plot(xex,yex,label='exact')
plt.scatter(x,y,label='numerical')

plt.legend()
plt.show()'''
        st.code(code, language = 'python') #코드 입력 및 코드 부르기

        #08-06 문제 풀이
        def yexact(x,dyn):
            y = x+0.5*(1.0-dyn)*sin(2.0*x)
            return y

        def findSegment(xData,x):
            iLeft = 0
            iRight = len(xData)- 1
            while 1:
                if (iRight-iLeft) <= 1: return iLeft
                i = int((iLeft + iRight)/2)
                if x < xData[i]: iRight = i
                else: iLeft = i

        def TDMAsolver(a,d,c,b):

            n = len(b)
            x = np.zeros(n)

            for i in range(0,n-1):
                lam = a[i]/d[i]
                d[i+1] = d[i+1] - lam*c[i] 
                b[i+1] = b[i+1] - lam*b[i]

            x[n-1] = b[n-1]/d[n-1]
            
            for i in range(n-2,-1,-1):
                x[i] = (b[i]-c[i]*x[i+1])/d[i]

            return x

        xo = 0.0; yo = 0.0
        xn = 3.14/2; dyn = 3.0
        n = 10

        xl = xn-xo
        h = xl/n

        x = np.linspace(xo,xn,n+1)

        a = np.zeros(n)
        d = np.ones(n+1)
        c = np.zeros(n)
        b = np.zeros(n+1)

        a[0:n-1] = 1.0
        d[1:n] = -2.0+4.0*h**2
        c[1:n] = 1.0
        b[1:n] = 4.0*x[1:n]*h**2 

        b[0] = yo

        a[n-1] = 2.0
        d[n] = -2.0+4*h**2
        b[n] = 4.0*x[n]*h**2-2*h*dyn

        y = TDMAsolver(a,d,c,b)

        xc = xn

        ic = findSegment(x,xc)
        fac = (xc-x[ic])/(x[ic+1]-x[ic])

        yex_c = yexact(xc,dyn)
        y_c = y[ic]*(1.0-fac)+y[ic+1]*fac
        err_y_c = abs((y_c-yex_c)/yex_c)*100.0

        print("\nAt x =",xc)
        print("\nThe exact solution =",yex_c)
        print("\nThe numerical solutions =")
        print("\nValue =",y_c,"/ error (%) =",err_y_c)

        nex = 101
        xex = np.linspace(xo,xn,nex)
        yex = np.zeros(nex)
        for i in range(nex):
            yex[i] = yexact(xex[i],dyn)

        plt.plot(xex,yex,label='exact')
        plt.scatter(x,y,label='numerical')

        plt.legend()
        plt.show()
        st.pyplot(plt.gcf()) #위 코드는 08-06에 대한 풀이 코드, 이 코드는 pyplot을 불러와서 그래프를 표현함. 그런데 오류가 발생해서 구글링 했다.

elif add_selectbox == "🔚오늘 하루 마무리" : # 셀렉트 박스 불러우기
    st.write("# 오늘의 학습 점검") #학습 점검 글귀 쓰기
    st.success("오늘 학습 태도를 점검하며 잘한 점과 반성할 점에 대해 스스로 생각해보기") #이 페이지에서 해야할 일 알리기
    achievement = st.slider('오늘의 성취도를 표현해주세요', 0, 100, 50) #성취도를 표현하는 슬라이더 나타내기
    st.write("나는 오늘", achievement, '% 달성!!') #슬라이더 글로 표현하기
    
    
    q = st.selectbox("Did you study hard?",("No","Yes")) #셀렉트 박스 주제 및 보기 제시

    if q == "No" : #첫번째 경우
        st.write("😱 I'm sorry to hear that.") #첫번째 경우에 해당하는 대응
        txt = st.text_area('어떤 점이 문제였고 어떻게 고칠 수 있는지 적어보아요!', '''
    
        ''') #첫번째 경우에 해당하는 내용 작성
        st.write('문제점 및 반성할 점 :', txt) #작성한 내용 보이게 하기 
    
    else :
        st.write("🎉🎉You Did Well done🎉🎉") #두번째 선택 시 나타나는 글귀 작성
        st.balloons() #풍선으로 축하해주는 효과 삽입
        image = Image.open('15.jpg')#이미지 삽입
        st.image(image, caption = 'Thumbs up...for you^^')#삽입한 이미지에 대한 설명


else :
    st.write("# This is my page.")
