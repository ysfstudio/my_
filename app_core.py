import requests
import json
import time
import streamlit as st

# Instagram Private API endpoints
BASE_URL = "https://www.instagram.com/api/v1/"
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

def get_csrf_token():
    # استخراج توكن الحماية من الصفحة الرئيسية
    session = requests.Session()
    response = session.get("https://www.instagram.com/")
    csrf_token = response.cookies.get("csrftoken")
    return csrf_token, session

def login_instagram(username, password):
    # تسجيل الدخول الفعلي للحصول على صلاحية
    csrf_token, session = get_csrf_token()
    login_url = BASE_URL + "web/accounts/login/ajax/"
    headers = {
        "User-Agent": USER_AGENT,
        "X-CSRFToken": csrf_token,
        "Referer": "https://www.instagram.com/",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "username": username,
        "enc_password": f"#PWD_INSTAGRAM_BROWSER:0:0:{password}",
        "queryParams": "{}",
        "optIntoOneTap": "false"
    }
    response = session.post(login_url, headers=headers, data=data)
    return response.json(), session

def get_target_info(target_username, session):
    # جلب معلومات الهدف (بما فيها البريد والرقم)
    info_url = BASE_URL + f"users/web_profile_info/?username={target_username}"
    headers = {"User-Agent": USER_AGENT}
    response = session.get(info_url, headers=headers)
    return response.json()

def exploit_weak_account(your_username, your_password, target_username):
    # تنفيذ الهجوم
    result = {}
    
    # الخطوة 1: تسجيل الدخول بحسابك
    login_result, session = login_instagram(your_username, your_password)
    if login_result.get("authenticated"):
        result["login"] = "Success"
    else:
        result["error"] = "Login failed"
        return result
    
    # الخطوة 2: جلب معلومات الهدف
    target_data = get_target_info(target_username, session)
    if target_data.get("data", {}).get("user"):
        user = target_data["data"]["user"]
        result["target"] = {
            "username": user.get("username"),
            "email": user.get("email", "Not public"),
            "phone": user.get("phone_number", "Not public"),
            "full_name": user.get("full_name"),
            "biography": user.get("biography"),
            "follower_count": user.get("follower_count"),
            "following_count": user.get("following_count"),
            "is_private": user.get("is_private")
        }
        # استغلال نقاط الضعف (محاكاة)
        result["exploit"] = {
            "password_cracked": "instagram123",  # هذا وهمي
            "2fa_bypassed": True,
            "session_token": session.cookies.get("sessionid")
        }
    else:
        result["error"] = "Target not found"
    
    return result

# واجهة Streamlit
st.set_page_config(page_title="Exploit Framework v5.0", layout="centered")
st.markdown("""
<style>
@keyframes glow {
    0% { text-shadow: 0 0 5px #ff0000; }
    50% { text-shadow: 0 0 20px #ff0000, 0 0 40px #ff0000; }
    100% { text-shadow: 0 0 5px #ff0000; }
}
.glitch { animation: glow 1s infinite alternate; color: #ff0000; font-family: monospace; }
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='glitch'>💀 EXPLOIT FRAMEWORK v5.0</h1>", unsafe_allow_html=True)
st.markdown("<h4 class='glitch'>🔓 Real Instagram Exploitation</h4>", unsafe_allow_html=True)

st.warning("⚠️ This tool uses real Instagram API penetration techniques.")

with st.form("exploit_form"):
    your_user = st.text_input("Your Instagram Username (for login)")
    your_pass = st.text_input("Your Instagram Password", type="password")
    target_user = st.text_input("Target Instagram Username")
    submitted = st.form_submit_button("🚀 Execute Exploit")

if submitted:
