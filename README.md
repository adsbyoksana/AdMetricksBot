# 📊 AdMetricsBot

A simple Telegram bot that automates fetching and reporting Google Ads campaign data.

---

## 🚀 Features

- Start the bot with `/start`
- Get a campaign performance report with `/report`
- Integrates with Google Ads API
- Easy to configure and extend

---

## 📦 Project Structure

admetrics-bot/
- bot/
  - __init__.py
  - main.py
  - google_ads_client.py
  - report_builder.py
- config/
  - report_template.json
  - .env
- requirements.txt
- README.md

---

## ⚙️ Setup

1. Clone this repo:
   
   ```
   git clone https://github.com/adsbyoksana/admetrics-bot.git
   cd admetrics-bot
   ```
   
2. Create and activate a virtual environment:
   
   ```
   python -m venv venv
   source venv/bin/activate  # on Windows: venv\Scripts\activate
   ```

3. Install dependencies:

   ```
   pip install -r requirements.txt
   ```

4. Create a .env file in the config/ folder with the following content:

   ```
   BOT_TOKEN=your_telegram_bot_token
   GOOGLE_ADS_CLIENT_ID=your_google_ads_client_id
   GOOGLE_ADS_SECRET=your_google_ads_secret
   ```

5. Run the bot:

   ```
   python bot/main.py
   ```

---

📈 Example Output

📊 Report:

- Campaign: Test Campaign

- Clicks: 123

- Impressions: 4567

- Cost: $78.90

---

🤝 Contributing

Feel free to fork this project and enhance it. PRs are welcome!

---

🧠 About

Made with ❤️ by [@adsbyoksana](https://github.com/adsbyoksana/) – Marketing automation enthusiast.







