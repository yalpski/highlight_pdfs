# PDF Asset Name Highlighter

A Python script to automatically highlight asset names within specific PDF files. This tool scans a designated directory for PDFs following the naming convention `XYZ-Onboarding_Evidence_Package.pdf`, highlights all occurrences of `XYZ` within each PDF, and saves the changes seamlessly.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Example](#example)
- [Troubleshooting](#troubleshooting)

## Features

- **Automated Scanning:** Automatically scans a specified directory for PDF files matching the pattern `XYZ-Onboarding_Evidence_Package.pdf`.
- **Dynamic Asset Detection:** Extracts the asset name (`XYZ`) from the filename and searches for all instances within the PDF.
- **Highlight Annotations:** Adds highlight annotations to every occurrence of the asset name.
- **Incremental Saving:** Saves changes incrementally to preserve original PDF content and annotations.
- **Error Handling:** Provides informative messages for missing directories, processing errors, and cases with no matches.

## Prerequisites

- **Python 3.6 or higher**
- **PyMuPDF Library**

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/pdf-asset-name-highlighter.git
   cd pdf-asset-name-highlighter
   ```

2. **Create a Virtual Environment (Optional but Recommended)**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Required Dependencies**

   ```bash
   pip install PyMuPDF
   ```

## Usage
Run the script via the command line, providing the target directory as an argument. If no directory is specified, the script defaults to C:\YourDirectory (modify the default path in the script as needed).
   ```bash
   python highlight_pdfs.py /path/to/your/directory
   ```


**Example:**
   ```bash
   python highlight_pdfs.py "C:\Users\YourName\Documents\PDFs"
   ```

**Output:**
   ```javascript
   Using 'fitz' module from: /path/to/fitz/__init__.py
   
   Found 3 PDF file(s) to process.
   
   Processing 'ABC-Onboarding_Evidence_Package.pdf' with asset name 'ABC'...
   Highlighted 5 instance(s) of 'ABC' in 'ABC-Onboarding_Evidence_Package.pdf'.
   
   Processing 'DEF-Onboarding_Evidence_Package.pdf' with asset name 'DEF'...
   No instances of 'DEF' found in 'DEF-Onboarding_Evidence_Package.pdf'.
   
   Processing 'GHI-Onboarding_Evidence_Package.pdf' with asset name 'GHI'...
   Highlighted 2 instance(s) of 'GHI' in 'GHI-Onboarding_Evidence_Package.pdf'.
   
   Processing completed.
   ```

## Example
Suppose you have the following PDF files in C:\PDFs:

- Alpha-Onboarding_Evidence_Package.pdf
- Beta-Onboarding_Evidence_Package.pdf
- Gamma-Onboarding_Evidence_Package.pdf

Running the script:
   ```bash
   python highlight_pdfs.py "C:\PDFs"
   ```

The script will:
   1. Extract asset names Alpha, Beta, and Gamma from the filenames.
   2. Search each PDF for occurrences of these asset names.
   3. Highlight each found instance.
   4. Save the changes to the original PDF files.

## Troubleshooting
### Directory Not Found
```bash
Error: The directory 'path' does not exist.
```
**Solution:** Ensure the provided directory path is correct and accessible.

### No Matching PDF Files Found
```bash
No matching PDF files found in the specified directory.
```
**Solution:** Verify that the PDFs follow the naming convention XYZ-Onboarding_Evidence_Package.pdf.

### Module Import Error
```bash
ImportError: No module named 'fitz'
```
**Solution:** Install PyMuPDF using pip install PyMuPDF.

### Permission Issues When Saving PDFs
**Solution:** Ensure you have write permissions for the target directory and PDF files.
