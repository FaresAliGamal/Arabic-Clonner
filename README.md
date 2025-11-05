# 🎙️ صوتي العربي – نسخة GitHub Codespaces (CPU)

**نسخة جاهزة بالكامل لـ GitHub Codespaces** تعمل فورًا على المعالج (CPU).
- واجهة عربية أنيقة بـ **Streamlit**
- خادم **FastAPI**
- توليد صوت عربي تجريبي بـ **gTTS** (إنترنت مطلوب في Codespaces)
- نقطة `/clone_voice` حالياً تُعيد الصوت المحايد (stub). للتطابق 99% (RVC + Coqui) استخدم نفس الواجهة على جهاز محلي مع GPU لاحقًا.

## ✅ البدء السريع (في Codespaces)
1) افتح الريبو في Codespaces. يتم تشغيل سكربت الإعداد تلقائيًا.
2) افتح تبويب Terminal وشغل:

**خادم API:**
```bash
uvicorn api_server:app --host 0.0.0.0 --port 8000 --reload
```

**الواجهة:**
```bash
streamlit run app.py --server.address 0.0.0.0 --server.port 8501
```

3) من تبويب **Ports** في Codespaces افتح المنفذين 8000 (يُفتح تلقائي) و 8501 لواجهة Streamlit.

## 🧩 ملفات مهمة
- `.devcontainer/devcontainer.json` — يُهيّئ بيئة Python 3.10 ويستدعي `setup.sh` تلقائياً.
- `.devcontainer/setup.sh` — يثبّت المتطلبات (ffmpeg + حزم بايثون).
- `api_server.py` — خادم FastAPI بنقط `/upload_voice`, `/synthesize`, `/clone_voice`.
- `app.py` — واجهة Streamlit عربية فاتحة.
- `requirements.txt` — تبع المشروع (خفيف وملائم لـ Codespaces).
- `.streamlit/config.toml` — ثيم فاتح أنيق.

## 🧪 تشغيل محليًا (اختياري)
على جهازك (Windows/Linux/macOS) مع Python 3.10:
```bash
python -m venv .venv
source .venv/bin/activate  # أو .\.venv\Scripts\Activate.ps1 على ويندوز
python -m pip install --upgrade pip
pip install -r requirements.txt
uvicorn api_server:app --host 0.0.0.0 --port 8000 --reload
streamlit run app.py
```
ثم افتح http://localhost:8501

## 🔁 تطوير لاحق (اختياري)
- استبدال gTTS بـ **Coqui TTS** محليًا (ليس في Codespaces) لتحسين جودة العربية بدون إنترنت.
- إضافة وحدة **RVC v2** حقيقية بدل الـ stub في `clone_voice` للحصول على تطابق 95–99% (يتطلب GPU).
