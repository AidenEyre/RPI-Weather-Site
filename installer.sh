#!/bin/bash

# Install Flask and other required libraries
sudo apt-get update
sudo apt-get install -y python3-pip
pip3 install Flask

# Clone the repository containing the project files
git clone https://github.com/AidenEyre/RPI-Weather-Site.git
cd "RPI-Weather-Site" || exit 1

# fullname="USER INPUT"
read -pr "OpenWeather API key: " OPEN_WEATHER_API_KEY
cat <<EOF > constants.py
OPEN_WEATHER_MAP_API_KEY = "${OPEN_WEATHER_API_KEY}"
EOF

# Start the Flask application in the background
nohup python3 main.py --port 5000 &

# Start the fetch_data.py script in the background
nohup python3 fetch_data.py &

# Save the process id of the scripts for later use
echo $! > flask_app.pid
echo $! > fetch_data.pid