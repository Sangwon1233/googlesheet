import streamlit as st
import gspread
from google.oauth2.service_account import Credentials

# JSON 키 경로
SERVICE_ACCOUNT_FILE = 'C:/Users/sangwon/dev/useful-cyclist-465911-a1-31a58e298ed8.json'

# 인증 범위
SCOPES = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

# 인증 처리
creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
gc = gspread.authorize(creds)

# 시트 열기
spreadsheet = gc.open("구글시트")  # 실제 시트 제목으로 변경
sheet = spreadsheet.sheet1
# Streamlit UI 시작
st.title("📊 구글 시트 연동 테스트")

# 현재 시트 데이터 표시
data = sheet.get_all_values()
st.write("현재 시트 데이터:")
st.table(data)

# 사용자 입력
st.subheader("행 추가")
col1, col2 = st.columns(2)
name = col1.text_input("이름")
score = col2.text_input("점수")

if st.button("시트에 추가"):
    if name and score:
        sheet.append_row([name, score])
        st.success(f"{name}, {score} 추가 완료!")
        st.experimental_rerun()
    else:
        st.warning("모든 값을 입력하세요.")
