set -euo pipefail
sudo apt-get update -y
sudo apt-get install -y ffmpeg
python -m pip install --upgrade pip setuptools wheel
pip install fastapi uvicorn streamlit gTTS pydub requests python-multipart
