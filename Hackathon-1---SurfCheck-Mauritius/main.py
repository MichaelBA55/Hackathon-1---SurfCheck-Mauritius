from weather import get_weather_by_coords
from database import init_db, save_surf_log

beaches = {
    "Flic en Flac": (-20.2707, 57.3734),
    "Tamarin": (-20.3419, 57.3661),
    "Le Morne": (-20.4489, 57.3189),
    "Belle Mare": (-20.1900, 57.7650),
    "Grand Baie": (-20.0131, 57.5803)
}

def main():
    init_db()
    print("Surf Check")

    while True:
        print("\nChoose a beach:")
        for i, name in enumerate(beaches.keys()):
            print(f"{i + 1}. {name}")
        print("q. Quit")

        choice = input("Enter choice: ")
        if choice.lower() == 'q':
            break

        try:
            beach_name = list(beaches.keys())[int(choice) - 1]
            lat, lon = beaches[beach_name]
            report = get_weather_by_coords(lat, lon)

            print(f"\nBeach: {beach_name}")
            print(f"Weather: {report['weather']}")
            print(f"Wind Speed: {report['wind_speed']} m/s")
            print(f"Temperature: {report['temp']} °C")

            save_surf_log(beach_name, report["weather"], report["wind_speed"], report["temp"])
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
