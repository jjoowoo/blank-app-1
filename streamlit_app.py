import streamlit as st
import random

st.title("🎮 숫자 맞추기 게임")

# 세션 상태에 랜덤 숫자 저장 (게임 처음 시작 시)
if "number" not in st.session_state:
    st.session_state.number = random.randint(1, 100)
    st.session_state.tries = 0

st.write("1부터 100 사이의 숫자를 맞춰보세요!")

# 사용자 입력
guess = st.number_input("숫자를 입력하세요:", min_value=1, max_value=100, step=1)

if st.button("확인"):
    st.session_state.tries += 1

    if guess < st.session_state.number:
        st.warning("UP! 더 큰 숫자입니다 ⬆️")
    elif guess > st.session_state.number:
        st.warning("DOWN! 더 작은 숫자입니다 ⬇️")
    else:
        st.success(f"🎉 정답입니다! {st.session_state.tries}번 만에 맞췄어요.")
        # 게임 리셋 버튼
        if st.button("다시 시작하기"):
            st.session_state.number = random.randint(1, 100)
            st.session_state.tries = 0
