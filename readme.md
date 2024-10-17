<h1 align="center" id="title">FitSheet</h1>

<p id="description">FitSheet is a workout tracking application that allows users to log and monitor their workouts using natural language input. It integrates with the Nutritionix API to process and retrieve exercise data and uses the Google Sheets API to record and manage workout logs.</p>

<h2>🧐 Overview</h2>

* **Natural Language Input**: Log and track workouts easily by entering details in natural language, such as "I ran 8 km and cycled for 5 minutes."
* **Nutritionix Integration**: Utilize the Nutritionix API to fetch and process exercise data for accurate calorie counting.
* **Google Sheets API**: Record data (date, time, exercise name, duration, calories) in a Google Sheet for easy tracking and analysis.

<h2>🔑 Obtain API Keys and Endpoints</h2>

1. **Nutritionix API**:  
   Obtain your API ID, API Key, and API URL Endpoint from the Nutritionix API.

2. **Google Sheets API**:  
   Get your Google Sheets endpoint URL and credentials from the Google Sheets API. Ensure your Google Sheet is configured to accept POST requests and set up the necessary access permissions.

<h2>🛠️ Setup</h2>

1. **Clone the Repository**:  
   ```bash
   git clone https://github.com/CodingSakshi/FitSheet.git
   ```

2. **Configure Environment Variables**:  
   Create a `.env` file with the following contents:
   ```plaintext
   EXERCISE_API_ID=<your_nutritionix_api_id>
   EXERCISE_API_KEY=<your_nutritionix_api_key>
   EXERCISE_ENDPOINT=<your_google_sheets_endpoint>
   SHEET_ENDPOINT=<your_nutritionix_endpoint>
   ```

3. **Run the Application**:  
   Execute the `main.py` file to start the app. Enter your workout details when prompted.
   ```bash
   python main.py
   ```

   Alternatively, you can input data directly into the Nutritionix endpoint URL.

<h2>💻 Built with</h2>

Technologies used in the project:

* **Programming Language**: Python
* **APIs**: Nutritionix API, Google Sheets API

<h2>📚 Resources</h2>

- [Nutritionix API Documentation](https://developer.nutritionix.com/docs/v2)
- [Google Sheets API Documentation](https://developers.google.com/sheets/api)

