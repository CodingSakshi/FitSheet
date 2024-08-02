## FitSheet

### Overview

- This app lets you log and track workouts using natural language input. 
- It integrates with Nutritionix to input data and process it. 
- And used Google Sheets API to record data (date, time, exercise name, duration, calories) to a Google Sheet.

### Obtain API Keys and Endpoints

1. **Nutritionix API:**
   - Obtain your API ID, API Key, and API URL Endpoint from the [Nutritionix API](https://docx.syndigo.com/developers/docs/nutritionix-api-guide).

2. **Google Sheets API:**
   - Get your Google Sheets endpoint URL and credentials from [Google Sheet API](https://developers.google.com/sheets/api/guides/concepts). Configure your Google Sheet to accept POST requests and set up access permissions.

### Setup

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/CodingSakshi/FitSheet.git
   ```

2. **Configure Environment Variables:**
   Create a `.env` file with:
   ```env
   EXERCISE_API_ID=<your_nutritionix_api_id>
   EXERCISE_API_KEY=<your_nutritionix_api_key>
   EXERCISE_ENDPOINT=<your_google_sheets_endpoint>
   SHEET_ENDPOINT=<your_nutritionix_endpoint>
   ```

3. **Run the Application:**
   Execute `main.py` to start the app. Enter your workout details when prompted. 

   **Alternatively:** Input data directly into the Nutritionix endpoint URL.

