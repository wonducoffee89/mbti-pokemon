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
