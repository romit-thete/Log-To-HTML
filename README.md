# Code to read a log and generate HTML reports.

# Usage:

### Step 1: Run the ticky_check.py. Make sure to provide the logfile as well.
  - Windows:
    ```
    python ticky_check.py syslog.log
    ```
  - Unix:
    ```
    ./ticky_check.py syslog.log
    ```
   This will simply create 2 CSV files, "error_message.csv" and "user_statistics.csv".

### Step 2: Pass the two csv files generated in Step 1 to the "csv_to_html.py" file.
  - error_message.csv:

    - Windows:
    ```
    python csv_to_html.py error_message.csv <html_file_name>.html
    ```
    - Unix:
    ```
    ./csv_to_html.py error_message.csv <html_file_name>.html
    ```
  - user_statistics.csv:

    - Windows:
    ```
    python csv_to_html.py user_statistics.csv <html_file_name>.html
    ```
    - Unix:
    ```
    ./csv_to_html.py user_statistics.csv <html_file_name>.html
    ```
    The HTML files will be created in the current directory (unless a path is specified explicitly).

### Step 3: Use your favourite browser to open the files and BOOM!!.
