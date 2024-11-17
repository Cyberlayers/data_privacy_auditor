import os

def scan_directory(directory):
    sensitive_extensions = ['.txt', '.csv', '.docx', '.xlsx']
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(tuple(sensitive_extensions)):
                filepath = os.path.join(root, file)
                permissions = oct(os.stat(filepath).st_mode)[-3:]
                print(f"File: {filepath}, Permissions: {permissions}")

if __name__ == "__main__":
    target_directory = input("Enter the directory to scan: ")
    if os.path.exists(target_directory):
        print("Scanning for sensitive files...")
        scan_directory(target_directory)
    else:
        print("The directory does not exist. Please try again.")
