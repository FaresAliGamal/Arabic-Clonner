from fastapi import FastAPI, UploadFile, Form
from fastapi.responses import FileResponse, JSONResponse
from gtts import gTTS
import os, tempfile

app = FastAPI(title="صوتي العربي API (Codespaces)")

os.makedirs("saved_models", exist_ok=True)
USER_VOICE_PATH = "saved_models/user_voice.wav"

@app.get("/")
async def root():
    return {"ok": True, "msg": "Sawty Arabi API running (Codespaces, CPU)"}

@app.post("/upload_voice")
async def upload_voice(file: UploadFile):
    with open(USER_VOICE_PATH, "wb") as f:
        f.write(await file.read())
    return {"message": "✅ تم تحميل صوتك بنجاح (سيُستخدم لاحقًا محليًا لـ RVC)",
            "path": USER_VOICE_PATH}

@app.post("/synthesize")
async def synthesize(text: str = Form(...)):
    if not text.strip():
        return JSONResponse({"error": "empty text"}, status_code=400)
    tts = gTTS(text=text, lang="ar")
    tmp_mp3 = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3").name
    tts.save(tmp_mp3)
    return FileResponse(tmp_mp3, media_type="audio/mpeg")

@app.post("/clone_voice")
async def clone_voice(text: str = Form(...)):
    # نسخة Codespaces: لا يوجد RVC. نعيد الصوت المحايد كحل تجريبي.
    if not text.strip():
        return JSONResponse({"error": "empty text"}, status_code=400)
    tts = gTTS(text=text, lang="ar")
    tmp_mp3 = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3").name
    tts.save(tmp_mp3)
    return FileResponse(tmp_mp3, media_type="audio/mpeg")
