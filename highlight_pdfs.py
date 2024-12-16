import os
import re
import fitz  # PyMuPDF
import sys

def highlight_asset_names_in_pdfs(directory):
    """
    Scans the specified directory for PDFs named 'XYZ-Onboarding_Evidence_Package.pdf',
    highlights all instances of 'XYZ' within each PDF, and saves the changes.
    """
    # Define the regex pattern to match the filenames and extract XYZ
    pattern = re.compile(r'^(.+)-Onboarding_Evidence_Package\.pdf$', re.IGNORECASE)

    # Check if the directory exists
    if not os.path.isdir(directory):
        print(f"Error: The directory '{directory}' does not exist.")
        sys.exit(1)

    # List all files in the directory
    files = os.listdir(directory)

    # Filter files that match the pattern
    pdf_files = [f for f in files if pattern.match(f) and f.lower().endswith('.pdf')]

    if not pdf_files:
        print("No matching PDF files found in the specified directory.")
        return

    print(f"Found {len(pdf_files)} PDF file(s) to process.")

    for pdf_file in pdf_files:
        match = pattern.match(pdf_file)
        if not match:
            continue  # This should not happen due to the earlier filter

        asset_name = match.group(1)
        pdf_path = os.path.join(directory, pdf_file)

        print(f"\nProcessing '{pdf_file}' with asset name '{asset_name}'...")

        try:
            # Open the PDF
            doc = fitz.open(pdf_path)
            total_highlights = 0

            for page_num in range(len(doc)):
                page = doc[page_num]
                # Search for all instances of the asset name
                text_instances = page.search_for(asset_name)

                for inst in text_instances:
                    # Add a highlight annotation
                    highlight = page.add_highlight_annot(inst)
                    highlight.update()
                    total_highlights += 1

            if total_highlights > 0:
                # Save the changes to the original file incrementally
                doc.save(pdf_path, incremental=True, encryption=fitz.PDF_ENCRYPT_KEEP)
                print(f"Highlighted {total_highlights} instance(s) of '{asset_name}' in '{pdf_file}'.")
            else:
                print(f"No instances of '{asset_name}' found in '{pdf_file}'.")

            doc.close()

        except Exception as e:
            print(f"An error occurred while processing '{pdf_file}': {e}")

    print("\nProcessing completed.")

if __name__ == "__main__":
    # Check if the directory path is provided as a command-line argument
    if len(sys.argv) == 2:
        directory = sys.argv[1]
    else:
        # If not provided, use a default path (modify as needed)
        directory = "C:\\YourDirectory"

    # Print the 'fitz' module path for debugging
    import fitz
    print(f"Using 'fitz' module from: {fitz.__file__}")

    highlight_asset_names_in_pdfs(directory)
