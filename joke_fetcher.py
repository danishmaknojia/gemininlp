import time
import os
import google.generativeai as genai
from datetime import datetime

def get_joke():
    """Fetch a joke from Gemini API"""
    try:
        # Initialize the model - using gemini-1.5-flash (faster) or gemini-1.5-pro (better quality)
        # gemini-pro has been deprecated
        model = genai.GenerativeModel('gemini-2.5-flash')
        
        # Prompt for a joke
        prompt = "Tell me a funny joke. Keep it clean and family-friendly."
        
        # Generate response
        response = model.generate_content(prompt)
        
        return response.text
    except Exception as e:
        return f"Error fetching joke: {str(e)}"

def list_available_models():
    """List all available models (helper function for debugging)"""
    try:
        models = genai.list_models()
        print("Available models:")
        for model in models:
            if 'generateContent' in model.supported_generation_methods:
                print(f"  - {model.name}")
    except Exception as e:
        print(f"Error listing models: {str(e)}")

def main():
    """Main loop that fetches jokes every 30 seconds"""
    # Get API key from environment variable
    api_key = os.getenv('GEMINI_API_KEY')
    
    if not api_key:
        print("Error: GEMINI_API_KEY environment variable is not set.")
        print("Please set it using: export GEMINI_API_KEY='your-api-key'")
        return
    
    # Configure the API
    genai.configure(api_key=api_key)
    
    print("Starting joke fetcher. Press Ctrl+C to stop.\n")
    
    try:
        while True:
            # Get current timestamp
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"[{timestamp}] Fetching joke...")
            
            # Get and print the joke
            joke = get_joke()
            print(f"\n{joke}\n")
            print("-" * 60)
            print(f"Next joke in 30 seconds...\n")
            
            # Wait 30 seconds
            time.sleep(30)
            
    except KeyboardInterrupt:
        print("\n\nStopped by user. Goodbye!")

if __name__ == "__main__":
    main()

