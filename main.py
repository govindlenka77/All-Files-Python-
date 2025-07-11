import csv
import json
import os
import re
from typing import Any, Dict, List, Union, Optional

class JsonFileReader:
    """
    A class to read and parse JSON files.

    This class provides functionality to safely read a JSON file and load its content
    as a Python object, with proper exception handling for common errors.

    Example:
        >>> reader = JsonFileReader("data.json")
        >>> data = reader.read()
        >>> print(data)
    """

    def __init__(self, file_path: str):
        """
        Initialize the JsonFileReader with the path to the JSON file.

        Args:
            file_path (str): Path to the JSON file to be read.
        """
        self.file_path = file_path

    def read(self) -> Any:
        """
        Read and parse the JSON file.

        Returns:
            Any: The Python object representation of the JSON file content.

        Raises:
            FileNotFoundError: If the file does not exist.
            json.JSONDecodeError: If the file contains invalid JSON.
            IOError: If there's an issue opening or reading the file.

        Example:
            >>> reader = JsonFileReader("example.json")
            >>> try:
            ...     data = reader.read()
            ...     print(data)
            ... except Exception as e:
            ...     print(f"Error: {e}")
        """
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError as e:
            raise FileNotFoundError(f"File not found: {self.file_path}") from e
        except json.JSONDecodeError as e:
            raise json.JSONDecodeError(f"Invalid JSON in file: {self.file_path}", e.doc, e.pos)#Full JSON string:", e.doc,===>Position of error:", e.pos
        except IOError as e:
            raise IOError(f"Error reading file: {self.file_path}") from e

class JsonFileWriter:
    """
    A utility class for writing Python data structures to JSON files.

    This class provides a method to serialize Python objects (such as dictionaries or lists)
    and write them to a file in JSON format. It includes error handling for common issues 
    like permission errors, invalid data types, and write failures.

    Example:
        >>> writer = JsonFileWriter("output.json")
        >>> data = {"name": "Alice", "age": 30}
        >>> writer.write(data)
        >>> print("JSON data written successfully.")
    """

    def __init__(self, file_path: str):
        """
        Initialize the JsonFileWriter with a target file path.

        Args:
            file_path (str): The path where the JSON data should be written.
        """
        self.file_path = file_path

    def write(self, data: Any, indent: int = 4) -> None:
        """
        Write Python data to a JSON file.

        Args:
            data (Any): The Python object to be serialized (e.g., dict, list).
            indent (int, optional): Number of spaces for indentation in the JSON file. Default is 4.

        Raises:
            TypeError: If the data cannot be serialized to JSON.
            PermissionError: If the file cannot be written due to insufficient permissions.
            IOError: If an I/O error occurs during writing.

        Example:
            >>> writer = JsonFileWriter("data.json")
            >>> data = {"city": "New York", "temperature": 22}
            >>> try:
            ...     writer.write(data)
            ...     print("File written successfully.")
            ... except Exception as e:
            ...     print("Error writing file:", e)
        """
        try:
            with open(self.file_path, 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=indent)
        except TypeError as e:
            raise TypeError(f"Data provided is not JSON serializable: {e}") from e
        except PermissionError as e:
            raise PermissionError(f"Permission denied when writing to file: {self.file_path}") from e
        except IOError as e:
            raise IOError(f"Failed to write to file: {self.file_path}") from e

class LogFileReader:
    """
    A utility class to read contents from a log file.

    This class provides functionality to safely open and read a log file, line by line
    or all at once. It handles common errors such as file not found or permission denied.

    Example:
        >>> reader = LogFileReader("app.log")
        >>> lines = reader.read_lines()
        >>> for line in lines:
        ...     print(line.strip())
    """

    def __init__(self, file_path: str):
        """
        Initialize the LogFileReader with the path to the log file.

        Args:
            file_path (str): The path to the log file to be read.
        """
        self.file_path = file_path

    def read_lines(self) -> list[str]:
        """
        Reads all lines from the log file and returns them as a list of strings.

        Returns:
            list[str]: List of lines from the log file.

        Raises:
            FileNotFoundError: If the log file does not exist.
            PermissionError: If access to the log file is denied.
            IOError: If an I/O error occurs while reading the file.

        Example:
            >>> try:
            ...     reader = LogFileReader("server.log")
            ...     log_lines = reader.read_lines()
            ...     print("Total lines read:", len(log_lines))
            >>> except Exception as e:
            ...     print("Failed to read log file:", e)
        """
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                return file.readlines()
        except FileNotFoundError as e:
            raise FileNotFoundError(f"Log file not found: {self.file_path}") from e
        except PermissionError as e:
            raise PermissionError(f"Permission denied: Cannot access file {self.file_path}") from e
        except IOError as e:
            raise IOError(f"An error occurred while reading file: {self.file_path}") from e

    def read_all(self) -> str:
        """
        Reads the entire content of the log file as a single string.

        Returns:
            str: The full content of the log file.

        Raises:
            FileNotFoundError: If the log file does not exist.
            PermissionError: If access to the log file is denied.
            IOError: If an I/O error occurs while reading the file.

        Example:
            >>> try:
            ...     reader = LogFileReader("access.log")
            ...     content = reader.read_all()
            ...     print("First 200 characters:", content[:200])
            >>> except Exception as e:
            ...     print("Error reading full log:", e)
        """
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                return file.read()
        except FileNotFoundError as e:
            raise FileNotFoundError(f"Log file not found: {self.file_path}") from e
        except PermissionError as e:
            raise PermissionError(f"Permission denied: Cannot access file {self.file_path}") from e
        except IOError as e:
            raise IOError(f"An error occurred while reading file: {self.file_path}") from e


class CsvFileReader:
    """
    A utility class for reading CSV files.

    This class provides functionality to read a CSV file and return its contents
    either as a list of dictionaries (if headers exist) or a list of rows. It includes
    proper exception handling for common file and format issues.

    Example:
        >>> reader = CsvFileReader("data.csv")
        >>> rows = reader.read(as_dict=True)
        >>> for row in rows:
        ...     print(row)
    """

    def __init__(self, file_path: str):
        """
        Initialize the CsvFileReader with the path to the CSV file.

        Args:
            file_path (str): The path to the CSV file.
        """
        self.file_path = file_path

    def read(self, as_dict: bool = True, delimiter: str = ',') -> Union[List[Dict[str, str]], List[List[str]]]:
        """
        Read the CSV file.

        Args:
            as_dict (bool): If True, returns each row as a dictionary (uses the first row as header).
                            If False, returns each row as a list. Default is True.
            delimiter (str): The delimiter used in the CSV file. Default is ','.

        Returns:
            List[Dict[str, str]] or List[List[str]]: The contents of the CSV file.

        Raises:
            FileNotFoundError: If the CSV file does not exist.
            PermissionError: If access to the file is denied.
            csv.Error: If there's a parsing error in the CSV file.
            IOError: If an I/O error occurs during reading.

        Example:
            >>> try:
            ...     reader = CsvFileReader("employees.csv")
            ...     records = reader.read(as_dict=True)
            ...     print("First row:", records[0])
            ... except Exception as e:
            ...     print("Failed to read CSV file:", e)
        """
        try:
            with open(self.file_path, mode='r', encoding='utf-8') as file:
                if as_dict:
                    reader = csv.DictReader(file, delimiter=delimiter)
                    return [row for row in reader]
                else:
                    reader = csv.reader(file, delimiter=delimiter)
                    return [row for row in reader]
        except FileNotFoundError as e:
            raise FileNotFoundError(f"CSV file not found: {self.file_path}") from e
        except PermissionError as e:
            raise PermissionError(f"Permission denied: Cannot access file {self.file_path}") from e
        except csv.Error as e:
            raise csv.Error(f"Error parsing CSV file: {self.file_path}. Details: {str(e)}") from e
        except IOError as e:
            raise IOError(f"An I/O error occurred while reading file: {self.file_path}") from e

class CsvFileWriter:
    """
    A utility class to write data to a CSV file.

    This class supports writing lists of dictionaries or lists of lists to a CSV file,
    with options to include headers and customize the delimiter. It handles common
    exceptions like file access errors and invalid data formats.

    Example:
        >>> writer = CsvFileWriter("output.csv")
        >>> data = [{"Name": "Alice", "Age": 30}, {"Name": "Bob", "Age": 25}]
        >>> writer.write(data, include_header=True)
    """

    def __init__(self, file_path: str):
        """
        Initialize the CsvFileWriter with the path to the output CSV file.

        Args:
            file_path (str): The path where the CSV file will be written.
        """
        self.file_path = file_path

    def write(
        self,
        data: Union[List[Dict[str, Union[str, int, float]]], List[List[Union[str, int, float]]]],
        include_header: bool = True,
        fieldnames: List[str] = None,
        delimiter: str = ','
    ) -> None:
        """
        Write data to the CSV file.

        Args:
            data (list): A list of dictionaries (for key-value data) or a list of lists (for raw rows).
            include_header (bool): Whether to include the header row. Applies only to list of dicts.
            fieldnames (list): Optional list of fieldnames (keys) to define column order. Only used for list of dicts.
            delimiter (str): Character to separate fields. Default is ','.

        Raises:
            ValueError: If data is empty or of unsupported format.
            PermissionError: If the file cannot be accessed due to insufficient permissions.
            IOError: If there is an error writing the file.

        Example:
            >>> try:
            ...     writer = CsvFileWriter("people.csv")
            ...     rows = [
            ...         {"Name": "Alice", "Age": 30},
            ...         {"Name": "Bob", "Age": 25}
            ...     ]
            ...     writer.write(rows, include_header=True)
            ...     print("CSV written successfully.")
            >>> except Exception as e:
            ...     print("Failed to write CSV:", e)
        """
        if not data:
            raise ValueError("No data provided for CSV writing.")

        try:
            with open(self.file_path, mode='w', encoding='utf-8', newline='') as file:
                if isinstance(data[0], dict):
                    keys = fieldnames if fieldnames else list(data[0].keys())
                    writer = csv.DictWriter(file, fieldnames=keys, delimiter=delimiter)
                    if include_header:
                        writer.writeheader()
                    writer.writerows(data)
                elif isinstance(data[0], list):
                    writer = csv.writer(file, delimiter=delimiter)
                    writer.writerows(data)
                else:
                    raise ValueError("Unsupported data format. Must be list of dicts or list of lists.")
        except PermissionError as e:
            raise PermissionError(f"Permission denied: Cannot write to file {self.file_path}") from e
        except IOError as e:
            raise IOError(f"An I/O error occurred while writing to file: {self.file_path}") from e


class LogFileParser:
    """
    A utility class to parse log files and extract information.

    This class is designed to:
    1. Find lines containing test cases (e.g., "Starting testcase").
    2. Extract specific configurations using regex (e.g., build_id, suite_name, etc.).

    Attributes:
    -----------
    file_path : str
        The path to the log file to be processed.
    log_lines : List[str]
        The content of the log file as a list of lines (read once).

    Methods:
    --------
    __init__(file_path: str):
        Initializes the LogFileParser with the path to the log file.

    read_log_file() -> None:
        Reads the log file and stores its content in memory.

    extract_testcases() -> Dict[str, Dict[int, str]]:
        Extracts test case names and line numbers.

    extract_configurations() -> Dict[str, Dict[str, str]]:
        Extracts specific configurations from matching log lines.
    """

    def __init__(self, file_path: str):
        """
        Initializes the LogFileParser with the path to the log file.

        Parameters:
        -----------
        file_path : str
            The path to the log file to be processed.
        """
        self.file_path = file_path
        self.log_lines = []
        self.read_log_file()

    def read_log_file(self) -> None:
        """
        Reads the log file and stores its content in memory as a list of lines.

        Raises:
        -------
        FileNotFoundError:
            If the file does not exist at the specified path.
        PermissionError:
            If the file cannot be accessed due to insufficient permissions.
        Exception:
            For any other unexpected errors.
        """
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                self.log_lines = file.readlines()
        except FileNotFoundError as e:
            raise FileNotFoundError(f"File not found: {self.file_path}. Please check the path and try again.") from e
        except PermissionError as e:
            raise PermissionError(f"Permission denied: Unable to access file at {self.file_path}.") from e
        except Exception as e:
            raise Exception(f"An unexpected error occurred while reading the file: {str(e)}") from e

    def extract_testcases(self) -> Dict[str, Dict[int, str]]:
        """
        Searches for lines containing the pattern "Starting testcase",
        and extracts test case names and their respective line numbers.

        Returns:
        --------
        Dict[str, Dict[int, str]]:
            A dictionary in the format {"testcases": {line_number: testcase_name}}.
        """
        testcases = {}
        for line_number, line in enumerate(self.log_lines):
            # Match lines containing "Starting testcase" and extract the test case name
            match = re.search(r"Starting testcase\s+(\S+)", line)
            if match:
                testcase_name = match.group(1)
                testcases[line_number] = testcase_name

        return {"testcases": testcases}

    def extract_configurations(self) -> Dict[str, Dict[str, str]]:
        """
        Extracts specific configurations from log lines using regex.

        Configurations extracted:
        - build_id, suite_name, component, zalenium, uuid, security, snapshots.revert,
          testbed.value, testbed.cell.

        Returns:
        --------
        Dict[str, Dict[str, str]]:
            A dictionary in the format {"configurations": {key: value}}.
        """
        configurations = {}

        # Define regex patterns to extract the required configurations
        patterns = {
            "build_id": r"--build_id\s+([\w\.\-]+)",
            "suite_name": r"--suite_name\s+([\w\.\-]+)",
            "component": r"--component\s+([\w\.\-]+)",
            "zalenium": r"--zalenium\s+([\w]+)",
            "uuid": r"--uuid\s+([\w\-]+)",
            "security": r"--security\s+([\w]+)",
            "snapshots.revert": r"--snapshots\.revert\s+([\w]+)",
            "testbed.value": r"--testbed\.value\s+([\w\-]+)",
            "testbed.cell": r"--testbed\.cell\s+([\w\-]+)"
        }

        for line in self.log_lines:
            # Match and extract each configuration based on the defined patterns
            for key, pattern in patterns.items():
                match = re.search(pattern, line)
                if match:
                    configurations[key] = match.group(1)

        return {"configurations": configurations}

######## Checking the Failed patterns #################
class SlaChecker:
    """
    A utility class to check for failed record patterns from log files
    based on the configuration provided in a JSON file.

    This class:
    - Reads the configuration from a JSON file.
    - Searches for logs in the parent directory provided in the configuration.
    - Checks for the failed record patterns in log files.
    - Generates a report as a CSV file.

    Attributes:
    -----------
    config_file : str
        Path to the SLA configuration JSON file.
    config : Dict[str, str]
        Parsed configuration from the SLA JSON file.

    Methods:
    --------
    __init__(config_file: str):
        Initializes the SlaChecker with the path to the configuration JSON file.

    read_config() -> None:
        Reads and parses the SLA JSON configuration file.

    scan_logs_and_generate_report() -> None:
        Scans the log files, checks for failed record patterns, and generates a CSV report.
    """

    def __init__(self, config_file: str):
        """
        Initializes the SlaChecker with the path to the SLA configuration JSON file.

        Parameters:
        -----------
        config_file : str
            Path to the SLA JSON configuration file.
        """
        self.config_file = config_file
        self.config = {}
        self.read_config()

    def read_config(self) -> None:
        """
        Reads and parses the SLA JSON configuration file.

        Raises:
        -------
        FileNotFoundError:
            If the configuration file does not exist.
        json.JSONDecodeError:
            If the configuration file contains invalid JSON.
        """
        reader = JsonFileReader(self.config_file)
        self.config = reader.read()

    def scan_logs_and_generate_report(self) -> None:
        """
        Scans the log files under the parent directory, checks for failed record patterns,
        and generates a CSV report.

        Raises:
        -------
        FileNotFoundError:
            If the logs parent directory does not exist.
        ValueError:
            If required fields are missing in the configuration file.
        """
        # Validate required fields in the configuration
        required_fields = ["logs_parent_directory", "failed_record_pattern", "csv_report_fields"]
        for field in required_fields:
            if field not in self.config:
                raise ValueError(f"Missing required field '{field}' in the SLA configuration file.")

        logs_parent_directory = self.config["logs_parent_directory"]
        print("Logs Parent Directory:", logs_parent_directory)
        failed_record_pattern = self.config["failed_record_pattern"]
        csv_report_fields = self.config["csv_report_fields"].split("|")
        print("CSV Report Fields:", csv_report_fields)

        # Ensure the logs directory exists
        if not os.path.exists(logs_parent_directory):
            raise FileNotFoundError(f"The logs parent directory '{logs_parent_directory}' does not exist.")

        # Initialize the CSV writer
        csv_writer = CsvFileWriter("sla_report.csv")
        report_data = []

        # Compile the failed record pattern regex
        failed_record_regex = re.compile(failed_record_pattern, re.IGNORECASE)

        # Traverse the logs directory and process each log file
        for root, _, files in os.walk(logs_parent_directory):
            for file_name in files:
                if file_name.endswith(".log"):  # Process only .log files
                    log_file_path = os.path.join(root, file_name)
                    log_parser = LogFileParser(log_file_path)
                    testcases = log_parser.extract_testcases()["testcases"]

                    # Check for failed record patterns
                    for line_number, line in enumerate(log_parser.log_lines):
                        if failed_record_regex.search(line):  # Match the failed record pattern
                            failed_record = line.strip()
                            failed_pattern = failed_record_regex.search(line).group(0)

                            # Extract configurations from the log file
                            configurations = log_parser.extract_configurations()["configurations"]

                            # Build the CSV record
                            record = {
                                "log_file": log_file_path,
                                "build_id": configurations.get("build_id", "N/A"),
                                "suite_name": configurations.get("suite_name", "N/A"),
                                "component": configurations.get("component", "N/A"),
                                "job_url": configurations.get("job_url", "N/A"),  # Example field
                                "testcase_name": testcases.get(line_number, "N/A"),
                                "failed_record": failed_record,
                                "failed_pattern": failed_pattern,
                            }
                            print(record , "--------------")
                            report_data.append(record)

        print(report_data)
        # print(csv_report_fields)
        # Write the report to the CSV file
        csv_writer.write(report_data, include_header=True, fieldnames=csv_report_fields)


# Example Usage
if __name__ == "__main__":
    try:

        sla_checker = SlaChecker("C:\\Users\\rajkanam\\OneDrive - Cisco\\Documents\\SLA_ISE\\sla.json")
        
        sla_checker.scan_logs_and_generate_report()
        print("SLA report generated successfully as 'sla_report.csv'.")
    except Exception as e:
        print(f"Error: {e}")

