# AWS Textract Tabular Data Parser

This script utilizes AWS Textract to extract and parse tabular data from a file to JSON format. Then it uses amazon-textract-prettyprinter library to convert it into CSV format.

## Prerequisites

The script has the following requirements:

- Python 3.x
- AWS credentials properly configured for Textract service access


## Usage

Follow the steps below to use the script:

1. Set up a virtual environment using `venv`:
   ```
   python3 -m venv venv
   ```
2. Activate the virtual environment:
- Linux/macOS:
  ```
  source venv/bin/activate
  ```
- Windows (Command Prompt):
  ```
  venv\Scripts\activate
  ```

3. Install the required dependencies by running the following command:
     ```
     pip3 install -r requirements.txt
     ```

4. Update the `input_document` variable in the `main.py` file with the path or filename of the document you want to process. Ensure that the document is supported by AWS Textract.

5. Run the script by executing the following command:
     ```
     python3 main.py
     ```
   

The script will call AWS Textract to extract tabular data from the input document. It will then parse the JSON response and convert the tabular data into CSV format. The result will be printed to the console.
