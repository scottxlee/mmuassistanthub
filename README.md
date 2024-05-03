MMU Assistants Hub User Manual
Introduction
Purpose of the Manual
This manual is designed to guide users through the process of setting up and effectively interacting with the MMU Assistants Hub. It provides detailed instructions from initial setup to daily usage, ensuring a smooth experience for all users.

Overview of MMU Assistants Hub
The MMU Assistants Hub is a collection of AI-powered chatbots designed to assist Manchester Metropolitan University students and staff. These chatbots can answer queries related to academic and administrative matters, providing real-time, accurate information and support. The system utilizes advanced AI technology to understand and respond to user inputs, making it a valuable tool for enhancing the educational experience.

2. Getting Started
Creating an OpenAI Account
Visit the OpenAI website: Go to OpenAI’s registration page.
Sign up: Complete the registration form with your details. Ensure you use a valid email address as it will be used for verification purposes.
Verify your account: Check your email for a verification link from OpenAI and click on it to activate your account.
Obtaining an API Key
Log into OpenAI Dashboard: Once your account is active, log in to the OpenAI dashboard.
Navigate to API settings: Find the ‘API Keys’ section in the dashboard.
Generate a new API key: Click on ‘Create new key’. Label your API key for future reference and click ‘Create’.
Copy your API key: Safeguard your key as it will be used to authenticate API requests.
Setting Up the Environment
Create a .env file in your project directory: This file will store sensitive information such as your API key.
Open the .env file in a text editor and input the following line:

OPENAI_API_KEY='Your_OpenAI_API_Key_Here'
Replace 'Your_OpenAI_API_Key_Here' with the API key you obtained from OpenAI.
3. Installation and Setup
Installing Required Software
Integrated Development Environment (IDE): Download and install an IDE suited for Python development (e.g., VS Code, PyCharm).
Streamlit: Streamlit will be used to run the web application. Installation instructions are provided in the next steps.
Downloading and Setting Up Project Files
Clone or download the project repository: If you have git installed, you can clone the repository using:

git clone https://github.com/scottxlee/mmuassistanthub
Alternatively, download the zip file from the repository and extract it in your desired location.
Installing Dependencies
Navigate to the project directory in your terminal or command prompt.
Install required packages by running the following command:

pip install -r requirements.txt
4. Running the Application
Starting the Application
Open your terminal or command prompt.
Navigate to the project directory where the application file (assistanthub.py) is located.
Run the application by executing:

streamlit run assistanthub.py
Access the application: Open a web browser and go to http://localhost:8501 to interact with the MMU Assistants Hub.
5. Using the Chatbot
Initiating a Chat Session
Enter the Assistant ID: When the application loads, enter the Assistant ID in the input box provided. This ID connects you to the specific chatbot tailored for your needs.
Start chatting: Type your questions or commands into the chat interface and press enter to send. The chatbot will respond in real-time.
6. Troubleshooting
Common Setup Issues
API Key Not Recognized: Ensure there are no typos in your .env file and that the API key is correctly formatted.
Packages Not Installing: Check your internet connection, ensure your Python environment is active, and try running the install command again.
Reporting Issues
Contact Support: If you encounter unresolved issues or discover bugs, please contact our technical support team at 20029364@stu.mmu.ac.uk for assistance.
