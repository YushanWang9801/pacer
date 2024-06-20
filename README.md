# Custom Park Trail GPT

## Overview

Custom Park Trail GPT is a Streamlit application that provides detailed information about parks and trails using the National Park Service API and OpenAI's GPT model. This project includes several components to help you get started and ensure everything is set up correctly.

### Demo Screenshot

![Demo Screenshot](/demo.png)

## Project Structure

- **.env**: Contains environment variables such as API keys.
- **app.py**: The main Streamlit application.
- **test_env.py**: A script to test the OpenAI API key setup.
- **utils.py**: Utility functions used within the application.
- **requirements.txt**: List of required Python packages.
- **README.md**: Project documentation.

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)
- Streamlit

### Installation

1. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

2. Obtain an API key for the National Park Service:

    - Go to the [National Park Service Developer Portal](https://www.nps.gov/subjects/developer/get-started.htm).
    - Sign up for an account if you don't have one.
    - Once logged in, navigate to the "My Apps" section and create a new application to get your API key.


3. Create a `.env` file in the project root directory with the following content:

    ```plaintext
    NPS_API_KEY=your_nps_api_key_here
    OPENAI_API_KEY=your_openai_api_key_here
    ```

    Replace `your_nps_api_key_here` and `your_openai_api_key_here` with your actual API keys.

5. Test your API keys:

    You can test if your OpenAI API key is set up correctly by running the `test_env.py` script:

    ```bash
    python test_env.py
    ```

    This script will attempt to make a simple request to the OpenAI API and print the result.

## Running the Application

To run the Streamlit application, use the following command:

```bash
streamlit run app.py
```

### How It Works

1. **User Interface**: The application is built using Streamlit, a tool that makes it easy to create web apps for machine learning and data science projects. Users interact with the app through a simple web interface where they can enter their queries about specific parks or trails.

2. **Fetching Real-time Data**: When a user asks about a park, the app first fetches real-time alerts and updates from the National Park Service (NPS) API. This ensures that users get the latest information about park conditions, closures, and other important alerts.

3. **Processing User Queries**: The user's question, along with any real-time data from the NPS, is sent to OpenAI's GPT model. This model is like a very smart assistant that can understand natural language and generate detailed, human-like responses.

4. **Generating Responses**: The GPT model processes the input and generates a comprehensive response. This response includes details such as the park's name, location, description, activities available, facilities, and tips for visitors.

5. **Displaying Information**: The generated response is then displayed back to the user in the Streamlit app, providing them with all the information they need in a structured and easy-to-read format.

### Key Components

- **Streamlit**: Creates the web interface where users interact with the app.
- **NPS API**: Provides real-time data about park alerts and conditions.
- **OpenAI GPT**: Processes user queries and generates detailed responses.