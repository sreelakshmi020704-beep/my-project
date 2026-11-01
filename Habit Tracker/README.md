🏋️ Workout Tracker – Pixela API

A simple Python-based workout tracking application that uses the Pixela API to track daily workout hours and visualize workout consistency through a graph.

The application allows users to record their daily workout duration and store it in a personal Pixela graph. It also supports updating and deleting previously recorded workout data.

🚀 Features
Daily Workout Tracking: Enter the number of hours you worked out each day.
Graph Visualization: Visualize workout progress using the Pixela graph.
Create Pixel: Add a new workout record for a specific date.
Update Pixel: Modify an existing workout record.
Delete Pixel: Remove a workout record.
API Integration: Communicate with the Pixela API using Python Requests.
Date Handling: Automatically generates the current date for workout entries.
🛠️ Technologies Used
Python 3
Requests – For making HTTP requests to the Pixela API.
Pixela API – For tracking and visualizing workout data.
datetime – For handling dates and timestamps.
os – For environment variable management (optional).
📂 Project Structure
text
Workout-Tracker/
│
├── main.py
└── README.md

⚙️ Installation and Setup
1. Clone the Repository
bash
git clone https://github.com/your-username/Workout-Tracker.git
cd Workout-Tracker

2. Install Dependencies

Install the Requests library:

bash
pip install requests

3. Create a Pixela Account

Visit https://pixe.la/ and create your Pixela account.

You will need the following details:

Username: Your Pixela username.
Token: Your Pixela authentication token.
Graph ID: A unique identifier for your workout graph.
4. Configure Your Credentials

Update the following variables in your Python script:

python
TOKEN = "YOUR TOKEN"
USERNAME = "YOUR USERNAME"
GRAPH_ID = "YOUR GRAPH ID"


For better security, store your credentials as environment variables instead of hardcoding them.

python
TOKEN = os.getenv("PIXELA_TOKEN")
USERNAME = os.getenv("PIXELA_USERNAME")
GRAPH_ID = os.getenv("PIXELA_GRAPH_ID")


Set the environment variables before running the application.

📊 How It Works

The application communicates with Pixela through HTTP requests.

1. Create a Graph

The graph configuration contains:

Parameter	Value	Description
id	GRAPH_ID	Unique graph identifier
name	workout Graph	Name of the graph
unit	hours	Workout measurement unit
type	float	Accepts decimal values
color	ajisai	Graph color

Send a POST request to create the graph.

2. Create a Workout Record

The application automatically gets the current date and asks the user to enter their workout duration.

python
pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many hours did you workout today? "),
}


A POST request sends the workout data to Pixela.

3. Update a Workout Record

You can update an existing workout entry using a PUT request.

python
new_pixel_data = {
    "quantity": "12",
}

response = requests.put(
    url=update_endpoint,
    json=new_pixel_data,
    headers=headers
)

4. Delete a Workout Record

You can delete an existing workout entry using a DELETE request.

python
response = requests.delete(
    url=delete_endpoint,
    headers=headers
)

▶️ How to Run

Run the Python script from your terminal:

bash
python main.py


The application will prompt:

text
How many hours did you workout today?


Enter your workout duration, and the application will send the data to your Pixela graph.

🔗 View Your Workout Graph

You can view your workout progress using the following URL:

text
https://pixe.la/v1/users/YOUR_USERNAME/graphs/YOUR_GRAPH_ID.html


Replace YOUR_USERNAME and YOUR_GRAPH_ID with your actual Pixela username and graph ID.


🔐 Security
Never upload your Pixela authentication token to GitHub.
Use environment variables to manage sensitive credentials.
Add .env files to .gitignore if you use them.
Avoid sharing your API token publicly.
👨‍💻 Author

Developed as a Python project to practice API integration, HTTP requests, data management, and workout tracking automation.

⭐ If you find this project useful, consider giving the repository a star!
