# 🕰️ Time Zone Converter

## Overview
This Streamlit application allows users to view and convert times between different time zones. It provides real-time updates and an easy-to-use interface for selecting and converting times across multiple global time zones.

## Features
- **View current time**: Displays the current time in multiple selected time zones.
- **Convert time between time zones**: Allows users to input a time in one time zone and convert it to another.
- **Time zone selection**: Supports multiple global time zones, including UTC, Karachi, New York, London, Sydney, and more.
- **User-friendly interface**: Built with Streamlit for a simple and interactive experience.

## Installation
To run this application, ensure you have Python installed, and then install the required dependencies:

```sh
pip install streamlit
```

## Usage
Run the Streamlit application with the following command:

```sh
streamlit run time_zone_converter.py
```

## How It Works
### Displaying Current Time in Selected Time Zones
1. Users select multiple time zones from the dropdown.
2. The app displays the current time in each selected time zone, formatted as `YYYY-MM-DD HH:MM:SS AM/PM`.

### Converting Time Between Time Zones
1. Users input a time.
2. They select a "From" time zone and a "To" time zone.
3. Clicking the "Convert Time" button converts the entered time to the target time zone and displays the result.

## Technologies Used
- **Python**: Core programming language.
- **Streamlit**: Framework for building the web interface.
- **Datetime & ZoneInfo**: Handling and converting time across different time zones.

## Example Output
```
Selected Timezones:
Asia/Karachi: 2025-03-04 10:30:00 AM
America/New_York: 2025-03-04 12:30:00 AM

Time Conversion:
From Asia/Karachi: 2025-03-04 10:00:00 AM
To America/New_York: 2025-03-04 12:00:00 AM
```

## License
This project is open-source and available for modification and use under the MIT License.

---
Enjoy using the Time Zone Converter! 🚀
