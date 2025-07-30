# 🧠 Study Notifier — Google Sheets to Mac Notification Bot

A lightweight Python bot that reads tasks/reminders from **Google Sheets** and sends **Mac notifications** at the scheduled time. Perfect for personal study plans, reminders, and task tracking.

---

## 🚀 Features

- 📅 **Reads daily tasks from Google Sheets**
- ⏰ **Sends native Mac notifications** (using `pync`)
- 🔄 Runs automatically on a schedule (via `cron` or script)
- 🔒 Secure authentication with Google Sheets API

---

## 🛠 Tech Stack

- Python 3
- Google Sheets API
- `gspread` for sheet access
- `pync` for Mac notifications
- `schedule` or `cron` for automation

---

## 📋 How It Works

1. Store your task schedule in a Google Sheet  
2. Authenticate using your Google API credentials (`key.json`)  
3. Python script fetches today's tasks  
4. Sends notifications directly to your Mac

---

## 🔐 Setup

1. Clone this repo  
2. Set up Google Sheets API & download `key.json`  
3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Run the script:
    ```bash
    python notifier.py
    ```

---

## 📁 Sheet Format

| Date       | Time  | Task                |
|------------|-------|---------------------|
| 2025-07-30 | 08:00 | Revise Azure Notes  |
| 2025-07-30 | 21:00 | Python LeetCode     |

---

## 🧠 Use Cases

- Daily study planner  
- Workout or medicine reminders  
- Side project task tracking  

---

## 📦 Project Structure
study_notifier/
├── notifier.py # Main Python script
├── key.json # Google API credentials (DO NOT SHARE)
├── requirements.txt
└── README.md


---

## 🔔 Sample Notification

> "🔔 08:00 - Revise Azure Notes"

---

## ⚠️ Note

- Keep `key.json` secure and **never commit it to GitHub**
- Works on **macOS only** (uses `pync` for notifications)

---

## 🙌 Inspired By

Personal productivity needs for managing daily study and office tasks.


