📈 Stock Trading News Alert

A Python automation project that monitors daily stock price movements and sends SMS alerts with the latest relevant news articles whenever a stock experiences a significant price change.

The project uses the Alpha Vantage API to retrieve stock market data, NewsAPI to fetch related news articles, and Twilio to deliver SMS notifications.

🚀 Features
Stock Price Monitoring: Retrieves daily stock closing prices using the Alpha Vantage API.
Price Change Calculation: Compares the latest closing price with the previous day's closing price.
Percentage Change Detection: Calculates the percentage change in stock prices.
News Integration: Fetches the latest news articles when the stock price changes by 5% or more.
SMS Notifications: Sends the top three relevant news articles directly to your phone using Twilio.
Environment Variables: Keeps API keys and credentials secure using environment variables.
🛠️ Technologies Used
Python 3
Requests – HTTP requests to external APIs
Alpha Vantage API – Stock market data
NewsAPI – Financial news articles
Twilio API – SMS notifications
Python os module – Environment variable management
📂 Project Structure
text
Stock-News-Alert/
│
├── stock.py
├── README.md
└── .env  (optional, should not be committed)

⚙️ Installation and Setup
1. Clone the Repository
bash
git clone https://github.com/your-username/Stock-News-Alert.git
cd Stock-News-Alert

2. Install Dependencies
bash
pip install requests twilio

3. Get API Keys

You will need API credentials from the following services:

Alpha Vantage: https://www.alphavantage.co/support/#api-key
NewsAPI: https://newsapi.org/register
Twilio: https://www.twilio.com/
4. Configure Environment Variables

Set the following environment variables:

Variable	Description
ALPHAVANTAGE_API_KEY	Alpha Vantage API key
NEWS_API_KEY	NewsAPI API key
TWILIO_ACCOUNT_SID	Twilio account SID
TWILIO_AUTH_TOKEN	Twilio authentication token
TWILIO_FROM_NUMBER	Twilio phone number
TWILIO_TO_NUMBER	Your recipient phone number

For example, on macOS/Linux:

bash
export ALPHAVANTAGE_API_KEY="your_api_key"
export NEWS_API_KEY="your_news_api_key"
export TWILIO_ACCOUNT_SID="your_account_sid"
export TWILIO_AUTH_TOKEN="your_auth_token"
export TWILIO_FROM_NUMBER="your_twilio_number"
export TWILIO_TO_NUMBER="your_phone_number"


On Windows PowerShell:

powershell
$env:ALPHAVANTAGE_API_KEY="your_api_key"
$env:NEWS_API_KEY="your_news_api_key"
$env:TWILIO_ACCOUNT_SID="your_account_sid"
$env:TWILIO_AUTH_TOKEN="your_auth_token"
$env:TWILIO_FROM_NUMBER="your_twilio_number"
$env:TWILIO_TO_NUMBER="your_phone_number"

▶️ How to Run

Execute the Python script:

bash
python main.py


The program will:

Retrieve the latest daily closing price of Tesla (TSLA).
Retrieve the previous trading day's closing price.
Calculate the percentage difference between the two prices.
Check whether the absolute percentage change is 5% or higher.
If the threshold is reached, fetch the latest three related news articles.
Send the news headlines and descriptions as SMS messages using Twilio.
📱 Example SMS Notification
text
TSLA: 🔺5.42%

Headline: Tesla Announces New Developments.

Brief: Tesla shares experience a significant price movement following the latest company announcement.


A downward price movement is represented by 🔻, while an upward price movement is represented by 🔺.

🎯 Project Configuration

The project currently monitors:

Stock Symbol: TSLA
Company: Tesla Inc
Price Change Threshold: 5%
Number of News Articles: 3
Stock Data Frequency: Daily

These settings can be modified directly in the Python script.

🔐 Security
Never upload API keys, Twilio credentials, or other secrets to GitHub.
Use environment variables to store sensitive information.
Add .env to .gitignore if you use a .env file.
Never share your Twilio authentication token publicly.

