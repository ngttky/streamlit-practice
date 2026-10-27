import streamlit as st
import json
from pathlib import Path
from models.highlow import draw_cards, judge

# タイトル
st.title("High & Low Game")

if "base_card" not in st.session_state:
    st.session_state.base_card, st.session_state.result_card = draw_cards()

base_card = st.session_state.base_card
result_card = st.session_state.result_card

st.write("次のカードは大きい？ 小さい？")

# 最初のカードを表示
st.write("最初のカード")
st.header(
    f"{base_card['suit']} {base_card['rank']}"
)

# まだ選択していない場合
if "choice" not in st.session_state:

    st.write("次のカードを予想してください")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("High", use_container_width=True):
            st.session_state.choice = "High"
            st.rerun()

    with col2:
        if st.button("Low", use_container_width=True):
            st.session_state.choice = "Low"
            st.rerun()

# 選択した後
else:

    # 次のカードを表示
    st.write("次のカード")
    st.header(
        f"{result_card['suit']} {result_card['rank']}"
    )

    # 勝敗判定
    result = judge(
        base_card["rank"],
        result_card["rank"],
        st.session_state.choice
    )

    # 判定結果を表示
    if result == "win":
        st.success("正解！ You Win!")

    elif result == "lose":
        st.error("残念！ You Lose!")

    elif result == "draw":
        st.info("引き分け！ Draw!")

    # リセット
    if st.button("もう一度"):
        del st.session_state.choice
        del st.session_state.base_card
        del st.session_state.result_card
        st.rerun()

