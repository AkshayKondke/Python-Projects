# 🐍 Python Projects

Welcome to the **Python Projects** repository! This is a collection of Python-based projects showcasing various programming concepts, algorithms, and fun interactive games. 🎉

---

## 📋 Projects Included

### _1_. 🎮 Quiz Game 🧠
- A command-line quiz game that tests your knowledge of common technical abbreviations.
- **Features**:
  - 🎉 Celebratory feedback for correct answers.
  - 📊 Tracks and displays the player's score at the end.
  - 💪 Provides encouragement based on performance.

#### 📚 Prerequisites:
- No additional libraries are required; it runs with Python 3.x.

#### 🚀 How to Run:
1. Run the `quiz_game.py` script:
   ```bash
   python quiz_game.py
   ```
2. 📝 Answer the questions prompted in the terminal.

---

### _2_.🌦️ Weather App

This is a simple Python-based Weather App that fetches and displays real-time weather data for a given city using the [Weatherbit API](https://www.weatherbit.io/).

#### ✨ Features
- 🌡️ Get the current temperature, weather description, and timezone for any city.
- 🖥️ Simple and easy-to-use command-line interface.

#### 📋 Prerequisites
Before running this application, ensure you have the following:
- 🐍 Python 3.x installed on your system.
- 🔑 An API key from Weatherbit. You can get one by signing up at [Weatherbit.io](https://www.weatherbit.io/).

#### ⚙️ Installation
1. 📥 Clone or download this repository to your local system.
2. 📦 Install the required Python libraries:
   ```bash
   pip install requests
   ```
3. 🔧 Open the script file and replace `your api key here` with your actual Weatherbit API key:
   ```python
   api_key = "your api key here"
   ```

#### 🚀 Usage
1. 📂 Navigate to the directory containing the script.
2. ▶️ Run the script:
   ```bash
   python weather_app.py
   ```
3. ✏️ Enter the name of the city when prompted.
   Example:
   ```
   Enter the city name: London
   ```
4. 📊 The app will display the current weather information for the entered city, including:
   - 📍 City name
   - 🌡️ Temperature
   - 🌥️ Weather description
   - ⏰ Timezone

#### 🛠️ Example Output
```
Welcome to Weather App!! 🌦️

Enter the city name: London
City: London
Temperature: 15°C
Weather: Partly cloudy
Timezone: Europe/London
```

#### ⚠️ Error Handling
If the app is unable to fetch weather data (e.g., invalid API key, incorrect city name, or network issues), you will see the following message:
```
Unable to fetch weather data. Please try again.
```

---

## 🚀 How to Run
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/AkshayKondke/Python-Projects.git
   ```
2. 📂 Navigate to the project directory:
   ```bash
   cd Python-Projects
   ```
3. Follow the instructions for each project as detailed above. 📜

---

## 📜 License
This project is licensed under the MIT License. Feel free to use and modify it as needed.

