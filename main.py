import streamlit as st

# 1. 페이지 설정
st.set_page_config(
    page_title="MBTI 단짝 포켓몬 찾기",
    page_icon="⚡",
    layout="centered"
)

# 2. 커스텀 CSS (따뜻한 크림/노란색 톤, 큰 글씨, 깔끔한 카드 스타일)
st.markdown("""
<style>
    /* 배경 및 기본 폰트 설정 */
    .stApp {
        background-color: #FFFDF0;
        color: #333333;
        font-family: 'Pretendard', -apple-system, BlinkMacSystemFont, system-ui, Roboto, sans-serif;
    }

    /* 헤더 스타일 */
    .main-title {
        text-align: center;
        font-size: 2.3rem;
        font-weight: 800;
        color: #B8860B;
        margin-bottom: 0.5rem;
    }
    
    .sub-title {
        text-align: center;
        font-size: 1.2rem;
        color: #665C38;
        margin-bottom: 2rem;
    }

    /* 포켓몬 정보 카드 */
    .pokemon-card {
        background-color: #FFFFFF;
        border: 3px solid #F6D55C;
        border-radius: 20px;
        padding: 24px;
        box-shadow: 0 8px 20px rgba(246, 213, 92, 0.25);
        margin-top: 15px;
        text-align: center;
    }

    .pokemon-name {
        font-size: 1.8rem;
        font-weight: 700;
        color: #2D3748;
        margin-top: 10px;
    }

    .pokemon-type {
        display: inline-block;
        background-color: #FFE600;
        color: #4A3E00;
        font-weight: 700;
        padding: 6px 16px;
        border-radius: 20px;
        font-size: 1.05rem;
        margin: 10px 0;
    }

    .reason-box {
        background-color: #FFF9E6;
        border-left: 5px solid #EDC967;
        padding: 15px;
        border-radius: 8px;
        text-align: left;
        font-size: 1.15rem;
        line-height: 1.7;
        color: #4A4A4A;
        margin-top: 15px;
    }

    /* 셀렉트박스 및 버튼 큰 글씨 스타일 */
    div[data-baseweb="select"] {
        font-size: 1.2rem;
    }
    
    .stButton>button {
        width: 100%;
        background-color: #F6D55C;
        color: #4A3E00;
        font-size: 1.2rem;
        font-weight: bold;
        padding: 12px;
        border-radius: 12px;
        border: none;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05);
        transition: all 0.2s ease;
    }
    
    .stButton>button:hover {
        background-color: #EDC967;
        color: #000000;
    }
</style>
""", unsafe_allow_html=True)

# 3. 16가지 MBTI & 단짝 포켓몬 데이터 정의 (공식 이미지 링크 활용)
POKEMON_DATA = {
    "ISTJ": {
        "name": "아머까오",
        "en_name": "Corviknight",
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/823.png",
        "type": "비행 / 강철",
        "feature": "높은 책임감과 철저한 의무감을 지닌 완벽주의자",
        "reason": "원칙과 규칙을 철저히 지키며 신뢰를 최우선으로 생각하는 ISTJ처럼, 아머까오는 침착하고 묵직한 카리스마로 신뢰받는 최고의 단짝 포켓몬입니다."
    },
    "ISFJ": {
        "name": "잠만보",
        "en_name": "Snorlax",
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/143.png",
        "type": "노멀",
        "feature": "따뜻하고 헌신적이며 언제나 온화한 성품",
        "reason": "주변 사람들을 수호하고 마음을 평화롭게 해주는 ISFJ처럼, 잠만보는 언제나 푹신하고 넓은 품으로 포근함과 안정감을 선물해 줍니다."
    },
    "INFJ": {
        "name": "뮤",
        "en_name": "Mew",
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/151.png",
        "type": "에스퍼",
        "feature": "신비로운 직관력과 깊은 통찰력을 지닌 이상가",
        "reason": "조용하지만 깊은 통찰력과 이상향을 가슴에 품고 살아가는 INFJ의 순수하고 신비로운 이미지와 가장 어울리는 단짝입니다."
    },
    "INTJ": {
        "name": "뮤츠",
        "en_name": "Mewtwo",
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/150.png",
        "type": "에스퍼",
        "feature": "독립적이며 뛰어난 분석력을 보유한 용의주도한 전략가",
        "reason": "타인의 시선에 휘둘리지 않고 자신의 주관과 전략을 밀고 나가는 INTJ의 압도적인 지성과 독립적인 성향에 맞춰 깊은 공감을 나눌 수 있습니다."
    },
    "ISTP": {
        "name": "루카리오",
        "en_name": "Lucario",
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/448.png",
        "type": "격투 / 강철",
        "feature": "냉철한 파악력과 뛰어난 순발력을 지닌 해결사",
        "reason": "상황 파악이 빠르고 실전 능력에 강한 ISTP와 파동을 감지하여 차분하고 효율적으로 대처하는 루카리오는 환상의 호흡을 자랑합니다."
    },
    "ISFP": {
        "name": "메타몽",
        "en_name": "Ditto",
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/132.png",
        "type": "노멀",
        "feature": "유연하고 수용적이면서 독창적인 감성의 소유자",
        "reason": "어디든 잘 맞춰주고 온화하면서도 자유로운 예술가적 기질을 가진 ISFP에게 어떤 모양으로든 유연하게 변신하는 메타몽은 완벽한 친구입니다."
    },
    "INFP": {
        "name": "이상해씨",
        "en_name": "Bulbasaur",
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/1.png",
        "type": "풀 / 독",
        "feature": "따뜻한 마음에 풍부한 상상력을 품은 낭만파",
        "reason": "조용하지만 자상하고 자연 친화적인 따뜻한 감성을 지닌 INFP에게 차분히 햇볕을 쬐며 당신의 이야기를 들어줄 이상해씨가 매칭됩니다."
    },
    "INTP": {
        "name": "로토무",
        "en_name": "Rotom",
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/479.png",
        "type": "전기 / 고스트",
        "feature": "호기심이 왕성하고 창의적인 아이디어 제조기",
        "reason": "색다른 관점으로 사물을 관찰하고 탐구하는 것을 좋아하는 INTP처럼, 전자기기에 들어가 새로운 가능성을 실험하는 호기심 많은 로토무입니다."
    },
    "ESTP": {
        "name": "리자몽",
        "en_name": "Charizard",
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/6.png",
        "type": "불꽃 / 비행",
        "feature": "모험을 즐기며 에너지가 넘치는 모험가",
        "reason": "스릴 넘치는 과감한 액션과 열정이 넘치는 ESTP에게, 거침없이 하늘을 날아오르며 모험을 함께할 당당한 리자몽이 꼭 맞습니다."
    },
    "ESFP": {
        "name": "피카츄",
        "en_name": "Pikachu",
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/25.png",
        "type": "전기",
        "feature": "주변을 밝게 만드는 분위기 메이커",
        "reason": "상대방을 즐겁게 해주고 톡톡 튀는 매력을 발산하는 ESFP처럼, 언제나 밝고 에너지가 톡톡 튀는 피카츄는 인생의 무대를 한층 밝혀줍니다."
    },
    "ENFP": {
        "name": "이브이",
        "en_name": "Eevee",
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/133.png",
        "type": "노멀",
        "feature": "무궁무진한 가능성과 열정을 가진 호기심 대장",
        "reason": "어디로 튈지 모르는 순수한 열정과 다양한 가능성을 품은 ENFP처럼, 무한한 진화 가능성을 지닌 사랑스러운 이브이가 최고의 단짝입니다."
    },
    "ENTP": {
        "name": "팬텀",
        "en_name": "Gengar",
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/94.png",
        "type": "고스트 / 독",
        "feature": "위트 넘치고 정형화된 틀을 깨는 아이디어파",
        "reason": "장난기 넘치는 표정과 독창적인 발상으로 지루할 틈을 주지 않는 ENTP처럼, 재치 있고 허를찌르는 매력을 가진 팬텀이 딱입니다."
    },
    "ESTJ": {
        "name": "윈디",
        "en_name": "Arcanine",
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/59.png",
        "type": "불꽃",
        "feature": "당당한 리더십과 든든한 추진력을 겸비한 전사",
        "reason": "목표를 향해 솔선수범하고 신의를 지키는 ESTJ의 리더십에 어울리는, 용맹하고 신뢰성 높은 전설의 단짝 윈디입니다."
    },
    "ESFJ": {
        "name": "해피너스",
        "en_name": "Blissey",
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/242.png",
        "type": "노멀",
        "feature": "타인에게 다정하고 세심하게 케어해주는 분위기 창조자",
        "reason": "주변 사람들의 행복과 평화를 살뜰히 챙기는 ESFJ처럼, 모두에게 행복의 알을 나눠주며 큰 기쁨을 전달하는 해피너스입니다."
    },
    "ENFJ": {
        "name": "망나뇽",
        "en_name": "Dragonite",
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/149.png",
        "type": "드래곤 / 비행",
        "feature": "넓은 마음과 친절함으로 모두를 이끄는 리더",
        "reason": "바다를 건너 어려운 이를 돕는 다정하면서도 강인한 망나뇽은, 사람들에게 긍정적인 영향을 주며 격려하는 ENFJ의 큰 품과 닮아있습니다."
    },
    "ENTJ": {
        "name": "한카리아스",
        "en_name": "Garchomp",
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/445.png",
        "type": "드래곤 / 땅",
        "feature": "원대한 목표와 목표 달성을 향한 과감한 지도력",
        "reason": "카리스마와 압도적인 실력으로 목표를 정복해나가는 ENTJ에게, 결단력 있고 지혜로운 파트너 한카리아스가 완벽한 조력자가 됩니다."
    }
}

# 4. 앱 헤더 화면
st.markdown("<h1 class='main-title'>💛 MBTI 단짝 포켓몬 찾기 ⚡</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-title'>나의 MBTI를 선택하면 어울리는 단짝 포켓몬을 찾아드립니다!</p>", unsafe_allow_html=True)

# 5. MBTI 선택 셀렉트박스
mbti_list = list(POKEMON_DATA.keys())
selected_mbti = st.selectbox(
    "👉 당신의 MBTI 유형을 선택해 주세요:",
    options=["선택하세요..."] + mbti_list,
    index=0
)

# 6. 결과 출력 영역
if selected_mbti != "선택하세요...":
    # 단짝을 찾았을 때 축하 애니메이션 폭죽(Balloons) 및 Snow 효과 실행
    st.balloons()
    
    data = POKEMON_DATA[selected_mbti]
    
    st.markdown(f"""
        <div class='pokemon-card'>
            <h3 style='color: #8B6508; margin-bottom: 0;'>🎉 {selected_mbti}의 운명적인 단짝 포켓몬</h3>
            <div class='pokemon-name'>{data['name']} <span style='font-size: 1.1rem; color: #718096;'>({data['en_name']})</span></div>
            <div><span class='pokemon-type'>타입: {data['type']}</span></div>
            <img src='{data['img']}' width='260' style='margin: 15px 0;' alt='{data['name']}'>
            <div style='font-size: 1.1rem; font-weight: bold; color: #333;'>✨ 성향 키워드: {data['feature']}</div>
            <div class='reason-box'>
                <strong>💡 어울리는 이유:</strong><br>
                {data['reason']}
            </div>
        </div>
    """, unsafe_allow_html=True)

    # 추가 축하 효과
    st.toast(f"🎉 {selected_mbti}의 단짝 포켓몬 [{data['name']}]을(를) 발견했습니다!", icon="⚡")
    
else:
    st.info("💡 위 목록에서 MBTI를 선택하면 귀여운 단짝 포켓몬이 등장합니다!")
