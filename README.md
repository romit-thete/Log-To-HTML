# Code to read a log and generate HTML reports.

# Usage:

### Step 1: Navigate to the *"Log_to_Html"* directory which has the working code:
  ```
  cd Log_to_Html
  ```
### Step 2: Run the *"ticky_check.py"*. Make sure to provide the logfile as well.
  - Windows:
    ```
    python ticky_check.py syslog.log
    ```
  - Unix:
    ```
    ./ticky_check.py syslog.log
    ```
   This will simply create 2 CSV files, *"error_message.csv"* and *"user_statistics.csv"*.

### Step 3: Pass the two csv files generated in Step 2 to the *"csv_to_html.py"* file.
  - *error_message.csv*:

    - Windows:
    ```
    python csv_to_html.py error_message.csv <html_file_name>.html
    ```
    - Unix:
    ```
    ./csv_to_html.py error_message.csv <html_file_name>.html
    ```
  - *user_statistics.csv*:

    - Windows:
    ```
    python csv_to_html.py user_statistics.csv <html_file_name>.html
    ```
    - Unix:
    ```
    ./csv_to_html.py user_statistics.csv <html_file_name>.html
    ```
    The HTML files will be created in the current directory (unless an explicit path is specified).

### Step 4: Use your favourite browser to open the HTML files and BOOM!!.
