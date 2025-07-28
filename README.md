Using influx 2.x because it is the last fully open source and free to use (even in commercial projects) version

## Requirements

- Python 3.8+
- Virtual environment (`python -m venv .venv`)
- Install dependencies with:
  ```powershell
  pip install -r requirements.txt
  ```

## Project Structure

- `src/insert_random_data.py`: Inserts random data into InfluxDB
- `src/plot_data.py`: Plots data from InfluxDB for a given time interval

## Start the virtual environment:
Linux/macOS:
```shell
source venv/bin/activate
```
Windows:
```powershell
.venv\Scripts\Activate.ps1
```

## Insert random data:
python src\insert_random_data.py

## Plot data:
python src\plot_data.py --start "2025-07-27T00:00:00Z" --stop "2025-07-29T23:59:59Z"
