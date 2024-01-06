# Monitoring
## Detection of Online Sexism Load Testing

### Overview
The file `locustfile.py` is a Python script for performing load testing on web services designed to detect online sexism. The script uses Locust, an open-source load testing tool, to simulate users accessing different endpoints and performing various tasks. The tests are designed to assess the robustness and responsiveness of the services under simulated traffic.

### Features
* **Multiple Task Simulation**: Simulates various user tasks, including fetching main endpoint descriptions, task-specific details, preprocessing information, and sending prediction requests.
* **Custom User Behavior**: Custom user class with tasks assigned different weights, representing the likelihood of each task being performed during testing.
* **Error Handling**: Includes checks for response status codes and expected response content, raising exceptions in case of failure or unexpected responses.

### Installation
1. Ensure that Python 3.6 or later is installed on your system.
2. Install Locust using pip:
```bash
pip install locust
```

### Usage
1. Navigate to the directory containing the script.
2. Execute the following command to start Locust with CSV reporting:
```bash
locust -f locustfile.py --csv=report --csv-full-history
```
3. Open a web browser and go to http://localhost:8089 to access the Locust web interface.
4. Enter the total number of users to simulate (in our case 50), the spawn rate, and the host URL of the web service under test.
5. Start the load test using the web interface and monitor the results.
6. Upon completion, check the specified directory for report_stats.csv, report_stats_history.csv, report_failures.csv and report_exceptions.csv files containing the test results.

### File Description
`locustfile.py`: The main Python script containing the definition of the Locust user class. This class includes various tasks that simulate user actions, such as accessing different endpoints and submitting data for prediction.

## BetterUpTime

BetterUpTime is a tool designed to monitor and improve the uptime of web applications. It provides real-time alerts, detailed reporting, and analytics to help teams maintain high availability and performance of their web services.

### Features

- **Real-Time Monitoring**: Continuously monitors web applications and services for downtime.
- **Alert System**: Sends immediate notifications through email, SMS, or integrated chat applications when outages are detected.
- **Performance Analytics**: Tracks response times and availability trends over time.
- **Dashboard**: A user-friendly dashboard for an at-a-glance view of the system's health.
- **Multi-Service Support**: Capable of monitoring multiple services and endpoints simultaneously.
- **Customizable Checks**: Define the frequency and conditions for uptime checks.