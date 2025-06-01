# 🛠️ Discord Selfbot Faucet

A simple selfbot that sends a faucet request (`!faucet ...`) automatically to a specific Discord channel every 6 hours plus a random delay (0–3 hours). Built with `selfcord`.

---

## 📦 Requirements

### Python

* Python **3.8** or higher

### Dependencies

Install all dependencies using:

```bash
pip install -r requirements.txt
```

---

## 🔐 Setup Environment Variables

1. Create a `.env` file in the project root directory.
2. Add the following content:

```env
TOKEN=your_discord_token_here
CHANNEL_ID=your_channel_id_here
FAUCET_COMMAND=!faucet youraddress
```

> Make sure you use a **user token**, not a bot token. Selfbots violate Discord's ToS — use at your own risk.

---

## 🚀 How to Run

```bash
python bot.py
```

---

## ❓ How to Get Discord Token and Channel ID

### Get Your Discord User Token

⚠️ **Selfbots are against Discord's Terms of Service. Use at your own risk.**

1. Open Discord in Chrome.
2. Press `Ctrl + Shift + I` to open Developer Tools.
3. Go to the `Network` tab and refresh the page.
4. Filter by `science` or `messages`.
5. Click on the request, go to the `Headers` tab.
6. Find the `authorization` header — this is your **token**.

### Get the Channel ID

1. Enable Developer Mode in Discord:
   `User Settings` → `Advanced` → enable `Developer Mode`.
2. Right-click on the target channel → click **Copy Channel ID**.

---

## ⏱️ Faucet Timing Logic

* On startup, the bot sends the `FAUCET_COMMAND`.
* It will then wait for **6 hours + a random delay (0 to 3 hours)** before sending the next message.
* If rate-limited (error 429), the bot waits for the time Discord tells it before retrying.

---

## ✅ Sample Output

```bash
Logged on as yourusername
Message sent at 2025-06-02 00:04:55
Cooldown. Wait 21600 seconds...
```

---

## 📂 File Structure

```
.
├── bot.py
├── .env
├── requirements.txt
└── README.md
```
