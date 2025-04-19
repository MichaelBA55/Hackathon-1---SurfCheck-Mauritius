# Hackathon-1---SurfCheck-Mauritius
SurfCheck MRU - A terminal-based program designed to check live weather, wind and wave conditions in order to aid surfers make a safe and calculated decision on whether or not to surf at any beach on the island.


SurfCheck Mauritius

**SurfCheck Mauritius** is a beginner-friendly Python terminal app that checks real-time surf conditions for popular beaches in Mauritius using the OpenWeatherMap API. It displays the weather, wind speed, and temperature, and logs each check into an SQLite database for future reference.

Features

- Select from 5 popular beaches in Mauritius
- Get live weather, wind speed, and temperature
- Saves each surf check in a local database
- Simple setup using Python, JSON, API, and SQLite

Technologies Used

- Python
- SQLite
- JSON
- OpenWeatherMap API
- Requests module
- OS module (for file paths)

Coastal regions/Beaches Included

- Flic en Flac
- Tamarin
- Le Morne
- Belle Mare
- Grand Baie

How to Run

1. Download the repository content
2. Add your OpenWeatherMap API key to `config.json`:
   ```json
   {
     "api_key": "your_api_key_here"
   }
3. Run main.py
4. Enter a number appropriate to the list provided in the terminal ( 1 - 5 )
5. Read information provided
