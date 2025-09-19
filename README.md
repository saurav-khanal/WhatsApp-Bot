# WhatsApp Message Scheduler
A Python script that allows you to schedule WhatsApp messages to be sent at a specific date and time using the Twilio API.

## Features
- Schedule WhatsApp messages for future delivery
- Simple command-line interface
- Error handling for message delivery
- Uses Twilio's WhatsApp API for reliable messaging
  
# Prerequisites
- Python 3.x
- Twilio account
- Twilio phone number with WhatsApp capabilities

## Installation

1. Clone the repository:
```bash
git clone https://github.com/saurav-khanal/WhatsApp-Message-Scheduler.git
cd WhatsApp-Message-Scheduler
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in your project directory

4. Add your Twilio credentials to the `.env` file:
```bash
ACCOUNT_SID=your_twilio_account_sid_here
AUTH_TOKEN=your_twilio_auth_token_here
TWILIO_PHONE=your_twilio_phone_number_here
MY_PHONE=your_whatsapp_number_here
```

## Usage
Run the script:
```bash
python main.py
```

Follow the prompts to:
- Enter recipient name
- Enter recipient's WhatsApp number (with country code, e.g., +1234567890)
- Enter your message
- Schedule date (YYYY-MM-DD)
- Schedule time (HH:MM)

## File Structure
```
WhatsApp-Message-Scheduler/
├── main.py              # Main Python script
├── requirements.txt     # Python dependencies
├── .env                # Environment variables (create this)
└── .gitignore         # Git ignore file
```

## Important Notes
- Keep the script running until the scheduled time
- Recipient must have initiated conversation with your Twilio number first
- Twilio WhatsApp messages may incur costs
- Ensure proper timezone considerations when scheduling

## Error Handling
The script handles:
- Message delivery failures
- Invalid date/time formats
- Past scheduled times
- Twilio API authentication errors

## Support
For issues related to this project, please check the repository or create an issue.

---

**Note**: Replace placeholder values in `.env` with your actual Twilio credentials before use.
