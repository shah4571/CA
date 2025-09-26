#!/bin/bash
# -------------------------------------------------
# Full Pyrogram Bot Starter Script
# Folder: /root/CA/Time
# Compatible with your CA/ bot structure
# Fixes BadMsgNotification [16] issues
# -------------------------------------------------

# 1️⃣ VPS টাইম সিঙ্ক
echo "[INFO] Syncing VPS time with NTP server..."
apt update -y
apt install -y ntpdate
ntpdate -u pool.ntp.org
timedatectl set-timezone Asia/Dhaka
echo "[INFO] Current server time: $(date -R)"

# 2️⃣ Virtual Environment সক্রিয় করা
VENV_PATH="/root/CA/venv"
if [ ! -d "$VENV_PATH" ]; then
    echo "[INFO] Virtual environment not found. Creating..."
    python3 -m venv "$VENV_PATH"
fi
echo "[INFO] Activating Python venv..."
source "$VENV_PATH/bin/activate"

# 3️⃣ Python dependencies ইনস্টল
REQUIREMENTS_FILE="/root/CA/requirements.txt"
if [ -f "$REQUIREMENTS_FILE" ]; then
    echo "[INFO] Installing required Python packages..."
    pip install --upgrade pip
    pip install -r "$REQUIREMENTS_FILE"
fi

# 4️⃣ পুরনো session ব্যাকআপ / মুছে ফেলা
SESSION_FILE="/root/CA/RajuNewBot.session"
if [ -f "$SESSION_FILE" ]; then
    echo "[INFO] Backing up old session file..."
    mv "$SESSION_FILE" "$SESSION_FILE.bak"
fi

# 5️⃣ Bot চালানো
echo "[INFO] Starting Pyrogram bot..."
cd /root/CA
python3 -m bot.main
