import streamlit as st
import requests, io

st.set_page_config(page_title="صوتي العربي (Codespaces)", page_icon="🎙️", layout="centered")

API_URL = st.secrets.get("API_URL", "http://127.0.0.1:8000")

LIGHT_CSS = """
<style>
:root {
  --brand:#0a84ff;
  --bg:#ffffff;
  --card:#f7f9fc;
  --text:#0f172a;
  --muted:#475569;
  --border:#e2e8f0;
}
html, body, [data-testid="stAppViewContainer"] {
  background: var(--bg);
  color: var(--text);
  font-family: 'Cairo', 'Tajawal', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}
h1,h2,h3 { letter-spacing:.3px; }
.block-container { padding-top: 1.5rem; }
.stButton>button {
  background: var(--brand);
  color: white; border: 0; border-radius: 12px;
  padding: 0.6rem 1rem; font-weight: 700;
}
.stButton>button:hover { filter: brightness(0.95); }
.card {
  background: var(--card); border:1px solid var(--border);
  padding: 1rem 1.2rem; border-radius: 16px; margin-bottom: 1rem;
  box-shadow: 0 2px 10px rgba(2,6,23,.04);
}
.small { color: var(--muted); font-size:.9rem; }
hr { border-color: var(--border); }
</style>
<link href="https://fonts.googleapis.com/css2?family=Cairo:wght@300;400;600;700&display=swap" rel="stylesheet">
"""
st.markdown(LIGHT_CSS, unsafe_allow_html=True)

st.title("🎙️ تطبيق **صوتي العربي** (Codespaces)")
st.caption("نسخة تجريبية تعمل على CPU في Codespaces باستخدام gTTS. لنسخة RVC الواقعية شغّل محليًا مع GPU.")

st.markdown('<div class="card">', unsafe_allow_html=True)
st.subheader("🗣️ ١) ارفع صوتك للتدريب لاحقًا (محليًا)")
voice_file = st.file_uploader("ارفع ملف WAV بصوت واضح (60–600 ثانية)", type=["wav"])
if voice_file and st.button("رفع الصوت"):
    files = {"file": (voice_file.name, voice_file.getvalue(), "audio/wav")}
    r = requests.post(f"{API_URL}/upload_voice", files=files)
    if r.ok:
        st.success("✅ تم رفع الصوت!")
    else:
        st.error("حدث خطأ أثناء الرفع.")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="card">', unsafe_allow_html=True)
st.subheader("✍️ ٢) اكتب النص بالعربية")
text = st.text_area("اكتب هنا النص الذي تريد نطقه…", height=150, value="السلام عليكم ورحمة الله وبركاته. هذا اختبار لنسخة Codespaces.")
col1, col2 = st.columns(2)
with col1:
    if st.button("🔊 توليد صوت محايد (gTTS)"):
        if not text.strip():
            st.warning("اكتب نصًا أولًا.")
        else:
            with st.spinner("جاري التوليد…"):
                resp = requests.post(f"{API_URL}/synthesize", data={"text": text})
                if resp.ok:
                    st.audio(io.BytesIO(resp.content), format="audio/mp3")
                    st.download_button("⬇️ تحميل MP3", data=resp.content, file_name="neutral_ar.mp3", mime="audio/mpeg")
                else:
                    st.error("تعذر توليد الصوت.")
with col2:
    if st.button("🗣️ توليد بصوتي الواقعي (Stub)"):
        if not text.strip():
            st.warning("اكتب نصًا أولًا.")
        else:
            with st.spinner("جاري التوليد (Stub)…"):
                resp = requests.post(f"{API_URL}/clone_voice", data={"text": text})
                if resp.ok:
                    st.audio(io.BytesIO(resp.content), format="audio/mp3")
                    st.download_button("⬇️ تحميل MP3", data=resp.content, file_name="my_voice_stub.mp3", mime="audio/mpeg")
                else:
                    st.error("تعذر التوليد.")
st.markdown('</div>', unsafe_allow_html=True)

st.info("ℹ️ هذه النسخة لا تستخدم Coqui/RVC داخل Codespaces. للواقعية العالية: شغّل المشروع محليًا مع GPU.")
