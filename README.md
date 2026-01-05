# Port Monitor

A simple Python tool to monitor the status of a specific port on a target host in real-time.

![Port Monitor Screenshot](https://imgur.com/a/Nnp5vJT)

*Created by Xinor.Sec*

## Description

This tool continuously checks if a specific port on a target host is open or closed, displaying the status every second until interrupted with Ctrl+C. It shows the timestamp, IP address, port number, and status in a clear, color-coded format.

## Features

- Real-time port status monitoring
- Color-coded output (green for OPEN, red for CLOSED)
- Shows timestamp, IP address, and port number
- Continuous monitoring until manually stopped
- Supports both IP addresses and hostnames

## Requirements

- Python 3.x
- colorama library

## Installation

1. Install the required library:
   ```
   pip install colorama
   ```

2. Save the `main.py` file to your local machine.

## Usage

Run the tool with a target host and port:
```
python main.py <target> [port]
```

- `target`: The hostname or IP address to monitor (required)
- `port`: The port number to monitor (optional, defaults to 80)

### Examples

Monitor port 80 on localhost:
```
python main.py 127.0.0.1 80
```

Monitor port 443 on a website:
```
python main.py google.com 443
```

Monitor default port 80 on a specific IP:
```
python main.py 192.168.1.1
```

## Output Format

The tool displays a table with the following columns:
- **Timestamp**: Current time in HH:MM:SS format
- **IP Address**: Resolved IP address of the target
- **Port**: Port number being monitored
- **Status**: OPEN (in green) or CLOSED (in red)

## Stopping the Tool

Press `Ctrl+C` to stop the monitoring process.

## License


This project is free to use and modify.
