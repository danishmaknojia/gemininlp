# Gemini Joke Fetcher

A simple Python script that fetches jokes from the Gemini API every 30 seconds.

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set your Gemini API key as an environment variable:
```bash
export GEMINI_API_KEY='your-api-key-here'
```

You can get your API key from [Google AI Studio](https://makersuite.google.com/app/apikey).

## Usage

Run the script:
```bash
python joke_fetcher.py
```

The script will fetch a new joke every 30 seconds. Press `Ctrl+C` to stop.

## Notes

- Make sure you have a valid Gemini API key
- The script will run indefinitely until you stop it with Ctrl+C
- Each joke is timestamped for easy tracking

