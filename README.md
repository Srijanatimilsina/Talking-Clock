# Talking-Clock

This is the App to convert the clock time into hunman friendly text format

Feature:
1. Current time changes into Human friendly text
2. Specific time changes into Human friendly text
3. The Specific time is provided in JSON format

Steps for Configuration:
1. Clone the repo into the system git clone https://github.com/Srijanatimilsina/Talking-Clock.git
2. Create the Virtual environment and run the requirements.txt file pip install -r requirements.txt
3. To run the app, flask run or python app.py in the terminal, the app will start in the localhost
4. To run the unit testing python test_app.py

Steps to check the results
1. Browse the localhost provided in the terminal http://127.0.0.1:5000 http://127.0.0.1:<port>
2. It will show the crruent time in human friendly text
3. For specific time browse http://127.0.0.1:<port>/time, input the time in the terminal in HH:MM format , will show the human friendly text in termal, also provides the result in JSON format.
