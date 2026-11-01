🏋️ Workout Tracker or Habit Tracker – Pixela API

A simple Python project that helps you track your daily workout hours using the Pixela API. It allows you to record your daily workout duration and visualize your fitness progress through a contribution graph.

📌 Features
Create a Workout Graph: Create a personalized graph to track workout hours.
Track Daily Workouts: Record the number of hours you work out each day.
Update Workout Records: Modify an existing workout entry.
Delete Workout Records: Remove a workout entry when needed.
Visualize Progress: View your workout consistency through Pixela's graph visualization.
🛠️ Technologies Used
Python
Requests Library
Pixela API
DateTime Module
📂 Project Structure
text
Workout-Tracker/
│
├── main.py
└── README.md

⚙️ Installation & Setup
1. Clone the Repository
bash
git clone https://github.com/YOUR-USERNAME/Workout-Tracker.git

2. Navigate to the Project Directory
bash
cd Workout-Tracker

3. Install Dependencies
bash
pip install requests

4. Create a Pixela Account
Visit Pixela.
Create an account.
Generate your API token.
Choose a username and graph ID.
5. Configure Your Credentials

Open main.py and replace the placeholder values:

python
TOKEN = "YOUR TOKEN"
USERNAME = "YOUR USERNAME"
GRAPH_ID = "YOUR GRAPH ID"


Note: Keep your API token private. Avoid uploading sensitive credentials to GitHub.

🚀 How to Run

Execute the Python script:

bash
python main.py


Enter the number of hours you worked out when prompted:

text
How many hours did you workout today? 2.5


The program sends your workout data to Pixela and displays the API response.

🔄 API Operations

This project uses the following HTTP methods:

HTTP Method	Operation	Description
POST	Create Graph	Creates a new workout graph
POST	Create Pixel	Records daily workout hours
PUT	Update Pixel	Updates an existing workout record
DELETE	Delete Pixel	Deletes a workout record
📊 Workout Graph

Your workout data is visualized using Pixela's contribution graph.

You can access your graph using:

text
https://pixe.la/v1/users/YOUR-USERNAME/graphs/YOUR-GRAPH-ID.html


Replace the placeholders with your Pixela username and graph ID.

🎯 Learning Outcomes

Through this project, I practiced:

Working with external APIs.
Sending HTTP requests using Python's requests library.
Understanding GET, POST, PUT, and DELETE operations.
Working with Python's datetime module.
Handling JSON data.
Building a simple real-world application using an API.
👨‍💻 Author

YOUR NAME

GitHub: YOUR-GITHUB-PROFILE

⭐ If you find this project useful, feel free to star the repository!
